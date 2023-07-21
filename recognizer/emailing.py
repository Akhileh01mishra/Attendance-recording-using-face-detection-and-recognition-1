import smtplib, ssl,datetime

sender= 'grp1facerecognitionatt@gmail.com'     #senders email id
password='anlzquejdqwbeymc'                #password



def email_rollno(email,roll_no):
    port = 465
    now=datetime.datetime.now()
    date=now.strftime('%m/%d/%Y').replace('/0','/')
    if(date[0]=='0'):
        date=date[1:]
    subject="your roll no for the class"
    text="\nYour roll no for attendance app is "+str(roll_no)

    message ='Subject: {}\n\n{}'.format(subject, text)
    

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, email, message)

    print("sent email!")



def send_email(receiver_mail,attendance):
    port = 465
    now=datetime.datetime.now()
    date=now.strftime('%m/%d/%Y').replace('/0','/')
    subject="Attendance on "+str(date)
    text="\nYour attendance is marked "+attendance

    message ='Subject: {}\n\n{}'.format(subject, text)
    

    context = ssl.create_default_context()

    print("Starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver_mail , message)

    print("sent email!")