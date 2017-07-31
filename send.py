from emails.template import JinjaTemplate as T
import emails
import json
import time

# [Change secrets to be opened in main and then pass to each]
with open('secret.json') as data_file:
    secret = json.load(data_file)

MAIL_USERNAME = secret['email_user']
MAIL_PASSWORD = secret['email_pass']

# [might add to config]
MAIL_SERVER  = 'smtp.googlemail.com'
MAIL_PORT    = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True

ADMINS = secret['admins']

def send(posts):

    print("==> SENDING")

    message = emails.html(text="BODY OF MSG",
                          html=T(open('templates/common.html').read()),
                          subject='New deals found on r/frugalmalefashion!',
                          mail_from=('COMMON', MAIL_USERNAME))

    # @Hack: adding attribute for created at format, should probably instead
    #        find way to do it in template
    for post in posts:
        # @Hack: something off with clock
        ago = time.time() - post.created_utc + 25220
        post.created_formatted = time.strftime("%M", time.gmtime(ago))

    current = time.strftime("%Y-%m-%d / %H:%M:%S", time.gmtime())
    response = message.send(to=ADMINS,
                            render={"posts":   posts,
                                    "time":    current},
                            smtp=  {"host":    MAIL_SERVER,
                                    "port":    MAIL_PORT,
                                    "user":    MAIL_USERNAME,
                                    "password":MAIL_PASSWORD,
                                    "ssl":     MAIL_USE_SSL})

    print(" -> SENT {} EMAILS".format(len(ADMINS)))

    return response
