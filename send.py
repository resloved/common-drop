import smtplib

def send(links):

    # [Change secrets to be opened in main and then pass to each]
    with open('secret.json') as data_file:
        secret = json.load(data_file)

    username = secret['email_user']
    password = secret['email_pass']

    content = '\n'.join(links)

    mail = smtplib.SMTP ('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()

    mail.login(username, password)

    # @Scale: Loop through DB
    mail.sendmail (username, username, content)

    mail.close()
