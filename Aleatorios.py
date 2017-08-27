import smtplib
from email.mime.text  import  MIMEText
from email.mime.image import MIMEImage 
from  email.mime.multipart  import  MIMEMultipart
import sys

if (len(sys.argv) == 2):
    port = int(sys.argv[1])
else:
    sys.exit("Escreva a porta teste.py 587 no terminal")

my_smtp = smtplib.SMTP('smtp.gmail.com',port)
my_smtp.ehlo()
my_smtp.starttls()

msg = MIMEMultipart()
msg['Subject'] = "teste1" #aqui vc escolhe o assunto!

my_email = str(input("Informe seu email: " ))
my_pass = input("Informe sua senha: ")
qtd_msg = int(input("Informe a Quantidade de msg: "))
my_msg = input("Digite a msg: ")

lista = ['sesk16@gmail.com','tardelesa@gmail.com'] #pode por uma lista infinita de emails

msg.attach(MIMEText(my_msg)) 

try:

    my_smtp.login(my_email,my_pass)
    print("conectado com sucesso!!")
except Exception as msg:
    print(msg)

my_file = "zelda.jpg" #aqui vc nforma o nome do arquivo e a extensão .png ou .jpg

with open(my_file,"rb") as msg_data:
    img = (MIMEImage(msg_data.read()))
    msg.attach(img)

x = 0
while x < qtd_msg:
    my_smtp.sendmail(my_email,lista,msg.as_string())
    x = x + 1 
    print("Foram Enviados",x,"Emails")


