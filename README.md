
# set up cron 
<https://crontab.guru/>

runs every day at 8 am `0 8 * * * /usr/bin/python3 /path/to/your/squirrel_sender.py`

# set up config.py 

```
UNSPLASH_ACCESS_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
SENDER_EMAIL = 'example@example.com'
SENDER_PASSWORD = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
HISTORY_FILE = 'sent_squirrels.txt'
LOG_FILE = 'squirrel_log.txt'
RECIPIENTS = [
    'example@example.com',
    'example@example.com'
]

```

