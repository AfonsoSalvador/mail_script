import os
import sys
import smtplib
import email.message
from dotenv import load_dotenv

load_dotenv()
APP_PASSWORD = os.getenv("APP_PASSWORD")
SENDER = os.getenv("SENDER")
SUBJECT = os.getenv("SUBJECT")

def send_email(body, receiver):  
    
    msg = email.message.Message()
    msg['Subject'] = SUBJECT
    msg['From'] = SENDER
    msg['To'] = receiver
    password = APP_PASSWORD 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print(f'Email enviado para {receiver}')


def main():
  # Validating args
  if len(sys.argv) < 3:
    print("You need to insert all files at command line!")
    exit(1)

  # Opening text file
  fileWay = sys.argv[1]
  with open(fileWay, "r") as file:
    text = file.read()

  # Open params file
  params_file_way = sys.argv[2]
  with open(params_file_way,"r") as params_file:
    params = params_file.readlines()

  # Removing '\n' from string last character
  for x in range(len(params)):
    params[x] = params[x][:-1]

  # Calculating amounts
  emails_amount = len(params)
  pack0 = params[0].split(",")
  params_amount = len(pack0) - 1

  # Creating formated texts to send
  for i in range(emails_amount):
    text_to_send = text
    params_package = params[i].split(',')
    receiver = params_package[0]

    for j in range(params_amount):
      text_to_send = text_to_send.replace(f'<{j+1}>', params_package[j+1])

    send_email(body=text_to_send, receiver=receiver)

# Running application
if __name__ == '__main__':
  main()
