# EMAIL SENDER WORKING !!!

# Import smtplib for the actual sending function
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

email_sender = ""
email_password = ""

def send_email (email, subject, message):
        
    #body
    msg = MIMEText(message)

    #headers
    msg["Subject"] = subject
    msg['From'] = email_sender
    msg['To'] = email

    #server connection
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(email_sender, email_password)
    # print(msg.as_string())
    server.sendmail(email_sender, email, msg.as_string())
    server.close()
    print("[+] Email sent!")

def send_email_10 (email, subject, message):

    #body
    msg = MIMEText(message)

    #headers
    msg["Subject"] = subject
    msg['From'] = email_sender
    msg['To'] = email

    #server connection
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email, msg.as_string())
    server.sendmail(email_sender, email, msg.as_string())
    server.sendmail(email_sender, email, msg.as_string())
    server.sendmail(email_sender, email, msg.as_string())
    server.sendmail(email_sender, email, msg.as_string())
    server.sendmail(email_sender, email, msg.as_string())
    server.sendmail(email_sender, email, msg.as_string())
    server.sendmail(email_sender, email, msg.as_string())
    server.sendmail(email_sender, email, msg.as_string())
    server.sendmail(email_sender, email, msg.as_string())
    server.close()
    print("[+] 10 emails sent!")

def bomber(seconds, subject, message, email):
    
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg['From'] = email_sender
    msg['To'] = email
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(email_sender, email_password)
    start_time = time.time()
    email_counter = 0
    while int(time.time() - start_time) <= seconds:
        server.sendmail(email_sender, email, msg.as_string())
        email_counter += 1
        print("[+] Email sent!")
        time.sleep(3)
    print("[+] Finished sending emails!")
    print(f"[+] Time elapsed: {time.time()-start_time},\n[+] Emails number: {email_counter}")
    server.close()

def main(): 
    
    subject = input("[+] Subject: ")
    email = input("[+] Email: ")
    message = input("[+] Message: ")
    sendtype = str(input("[+] Type (bomber/1/10): "))
    
    if sendtype == "bomber":
        time_bomber = int(input("[+] Time: "))
        bomber(time_bomber, subject, message, email)
    
    elif sendtype == "1":
        for j in range (int(input("[+] Number of emails: "))):
            send_email(email, subject, message)
    
    elif sendtype == "10":
        for k in range (int(input("[+] Number of emails (*10): "))):
            send_email_10(email, subject, message)
    

if __name__ == "__main__":
    main()