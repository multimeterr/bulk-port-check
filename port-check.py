import socket
import ipaddress
import smtplib
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tabulate import tabulate
  
def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.settimeout(1)
   try:
      s.connect((ip, int(port)))
      s.shutdown(1)
      return True
   except:
      return False


#device_file = open("devices.txt", "r")
#device_content = device_file.read()
#nets = device_content.split(",")
#device_file.close()

openlist = []
nets = ['10.0.15.0/30']
for super1 in nets:
    for ip in ipaddress.IPv4Network(super1):
        if isOpen(str(ip), 80):
            print(str(ip)+":80 is open!")
            openlist.append((str(ip)+':80'))
        if isOpen(str(ip), 23):
            print(str(ip)+":23 is open!")
            openlist.append((str(ip)+':23'))

#print(openlist)

html = """\
<html>
  <body>
    <p style="font-family:'Courier New'"><font size=10><b>Port Scanner</b> </font><br></p>
    <p>
       {0}
       </p>
  </body>
</html>
""".format(tabulate(list(map(lambda x:[x], openlist)), tablefmt='html', headers=['Address'], showindex=False))


#print(html)
def send_email(sender = 'sernder@send.com',
               recipient = 'recipient@send.com',
               subj = '80-23 Port Scan'):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subj
    msg['From'] = sender
    msg['To'] = recipient
    part = MIMEText(html, "html")
    msg.attach(part)
    print("Sending mail...")
    try:
        s = smtplib.SMTP('1.1.1.1')
        s.sendmail(sender, recipient, msg.as_string())
        s.quit()
        return True
    except Exception as e:
        print("Error: {0}".format(e))
        return False
    #try:
    #    session = smtplib.SMTP('smtp.gmail.com', 587)
    #    session.starttls()
    #    session.login(sender, 'password') 
    #    session.sendmail(sender, recipient, msg.asString())
    #    session.quit()
    #    return True
    #except Exception as e:
    #    print("Error: {0}".format(e))
    #    return False
      
      
send_email()
