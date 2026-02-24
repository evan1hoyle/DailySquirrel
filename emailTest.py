import smtplib

from config import UNSPLASH_ACCESS_KEY
from config import SENDER_EMAIL
from config import SENDER_PASSWORD



try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        print("✅ Login Successful! Your App Password is working.")
except Exception as e:
    print(f"❌ Still failing: {e}")