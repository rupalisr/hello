import smtplib , webbrowser
def get_mail():
    services=['gmail','yahoo','rediffmail','outlook','hotmail']
    while True:
         email_id=input("enter your email-id:")
         if '@' in email_id and '.com' in email_id:
             sym_pos=email_id.find('@')
             com_pos=email_id.find('.')
             sp=email_id[sym_pos+1:com_pos]
             if sp in services:
                 return email_id,sp
                 break
             else:
                 print("services are valid only for yahhoo,gmail,outlook,rediffmail and hotmail")
                 print("we not provide servies for"+" "+sp)
                 continue
                 
             
         else:
             print("please enter a valid email address")
             continue

def smtp_domain(serviceProvider):
    if serviceProvider=='gmail':
        return 'smtp.gmail.com'
    elif serviceProvider=='yahoo':
        return 'smtp.mail.yahoo.com'
    elif serviceProvider=='hotmail' or 'outllook':
        return 'smtp-mail.outlook.com'
print("welcome in python program\n\n you can send mail by using this program.")
print("please enter your email-id and password")
email,serviceProvider=get_mail()
password=input('password: ')
while True:
    try:
       smtpDomain=smtp_domain(serviceProvider)
       print("your service provider is:",smtpDomain)
       connection=smtplib.SMTP(smtpDomain,587)
       connection.ehlo()
       connection.starttls()
       connection.login(email,password)
    except:
         if serviceProvider=='gmail':
            print("login is unsucessfully:")
            print("then there is two type of error:")
            print("1.user enter wrong username and password")
            print("2.when user login with gmail then error occur due to allow less secure apps")
            print("do you want to allow less secure apps:yes\\no?")
            x=input()
            if(x=='yes'):
                webbrowser.open("https:\\myaccount.google.com\lesssecureapps")
            else:
                print("gmail cannot send this mail")
            print("again enter email-id and password:")
            email,serviceProvider=get_mail()
            password=input("password: ")
            continue
         else:
            print("login unsucessfully")
            print("again enter emailid and password:")
            email,serviceProvider=get_mail()
            password=input("password: ")
            continue
    else:
       print("login  sucessfully")
       break
print("please enter receiver  email-id:")
receiver_email,receiver_sp=get_mail()
print("enter the subject and message:")
subject=input("subject: ")
message=input("message: ")
connection.sendmail(email,receiver_email,("Subject: "+str(subject)+  "\n\n" +str(message)))
print("your mail is send sucessfully")
connection.quit()
