import requests
import smtplib
import logging
import random
import os
from email.message import EmailMessage
from datetime import datetime
from squirrel_data import SQUIRREL_FACTS

from config import *


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

now = lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S')



def get_unique_squirrel():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            sent_ids = f.read().splitlines()
    else:
        sent_ids = []

    for _ in range(5):
        url = f"https://api.unsplash.com/photos/random?query=squirrel&client_id={UNSPLASH_ACCESS_KEY}&sig={os.urandom(8).hex()}"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data['id'] not in sent_ids:
                    with open(HISTORY_FILE, 'a') as f:
                        f.write(data['id'] + '\n')
                    return data['urls']['regular']
        except Exception as e:
            logging.error(f"API Error: {e}")
    return None

def send_email(image_url,email):
    fact = random.choice(SQUIRREL_FACTS)
    msg = EmailMessage()
    msg['Subject'] = f"Daily Squirrel: {datetime.now().strftime('%B %d')}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = email
    
    msg.set_content(f"Daily Fact: {fact}\nView Image: {image_url}")
    msg.add_alternative(f"""\
    <html>
      <body style="font-family: Arial, sans-serif; color: #333;">
        <h2 style="color: #8B4513;">🐿️ Your Daily Squirrel Dispatch</h2>
        <div style="background-color: #f4f4f4; padding: 15px; border-radius: 8px; border-left: 5px solid #8B4513;">
            <strong>Did you know?</strong> {fact}
        </div>
        <br>
        <img src="{image_url}" style="width:100%; max-width:500px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
        <p style="font-size: 0.8em; color: #777;">Stay bright and bushy-tailed!</p>
      </body>
    </html>
    """, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        logging.info(f"SUCCESS: Sent squirrel and fact: '{fact[:30]}...'")
        logging.info(f"SUCCESS: Email sent to [{email}]")
        logging.info(f"IMAGE URL: {image_url}")
    except Exception as e:
        logging.error(f"FAILED to send email: {e}")
        raise e

if __name__ == "__main__":
    logging.info("--- Squirrel Script Started ---")
    img = get_unique_squirrel()
    if img:
        for person in RECIPIENTS:
            send_email(img,person)
        print(f"[{now()}] Squirrel dispatched successfully!")
    else:
        print(f"[{now()}] Failed to find a squirrel. They must be hiding.")
        logging.warning("Script ended early because no image was found.")
    logging.info("--- Squirrel Script Finished ---")