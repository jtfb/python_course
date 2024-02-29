import smtplib
import getpass
import imaplib
import email

def send_email():
    
    '''Sending emails in python'''
    
    #SMTP settings for gmail below. Check for other servers
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)

    smtp_object.ehlo()

    smtp_object.starttls()

    email = getpass.getpass('Email: ')
    password = getpass.getpass('Password: ')

    smtp_object.login(email,password)

    from_address = email
    to_address = input('Enter a to address: ')
    subject = input('Enter a subject: ')
    message = input('Enter a message: ')
    msg = "Subject: "+subject+'\n'+message

    smtp_object.sendmail(from_address,to_address,msg)
    
def receive_email():

    '''Receiving emails in Python'''
    
    # Check IMAP settings for other servers
    M = imaplib.IMAP4_SSL('imap.gmail.com')
    
    email = getpass.getpass("Email: ")
    password = getpass.getpass("Password: ")
    
    M.login(email,password)
    
    M.list()
    
    M.select('inbox')
    typ,data = M.search(None, 'SUBJECT "test2"')
    
    email_id = data[0]
    result,email_data = M.fetch(email_id, '(EMAIL ID)')
    raw_email = email_data[0][1]
    
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    
    for part in email_message.walk():
        if part.get_content_type() == 'text/plain':
            body = part.get_playload(decode=True)
            print(body)
    
    

# send_email()
# receive_email()