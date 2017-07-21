import smtplib, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send(links):

    # [Change secrets to be opened in main and then pass to each]
    with open('secret.json') as data_file:
        secret = json.load(data_file)

    username = secret['email_user']
    password = secret['email_pass']

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Rising Posts"
    msg['From'] = username
    msg['To'] = username

    text = "New rising links:\n"
    print("  * LINKS")
    for link in links:
        print(link)
        text += link + "\n"

    msg.attach(MIMEText(text, 'plain'))

    mail = smtplib.SMTP ('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()

    mail.login(username, password)

    # @Scale: Loop through DB
    mail.sendmail (username, username, msg.as_string())

    mail.close()
