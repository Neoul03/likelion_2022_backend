import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("cstim77@gmail.com","jepcjrsgpymmftdk")
smtp.send_message()
smtp.quit()