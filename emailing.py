import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "xyqjaouxnefmoylj"
SENDER = "copycatpresentsir@gmail.com"
RECEIVER = "copycatpresentsir@gmail.com"

def send_mail(image_path):
    print("mailing function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, a new customer is spotted.")
    
    with open(image_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))
    
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("mailing function ended")
    
if __name__ == "__main__":
    send_mail("images/18.png")