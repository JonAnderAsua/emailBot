import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



def getHelblideak(s):
    helbideak = []
    file = open(s)
    lines = file.readlines()
    for line in lines:
        helbideBakarra = {}
        helbideBakarra['email'] = str(line)
        helbideak.append(helbideBakarra)
    return helbideak


def mezuaBidali(smtpserver, login, password, msg):
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()



def getMessage(s):
    file = open(s).readlines()
    message = ""
    for l in file:
        message += l + "\n"
    return message


def main():
    helbideak = getHelblideak('helbideak.txt')
    smtpserver = 'smtp.gmail.com:587'
    login = 'jasuamiranda1998@gmail.com'
    password = ''

    mensaje = getMessage('message.txt')
    msg = MIMEMultipart(mensaje)
    msg['Subject'] = "Pierda hasta el 19% de su peso. Un nuevo sistema para adelgazar está aquí."
    msg['From'] = 'jasuamiranda1998@gmail.com'

    # Adjuntamos Imagen
    file = open("image.png", "rb")
    attach_image = MIMEImage(file.read())
    attach_image.add_header('Content-Disposition', 'attachment; filename = "avatar.png"')
    msg.attach(attach_image)


    for helbide in helbideak:
        msg = MIMEMultipart(mensaje)
        msg['Subject'] = "Pierda hasta el 19% de su peso. Un nuevo sistema para adelgazar está aquí."
        msg['From'] = 'jasuamiranda1998@gmail.com'
        msg['To'] = helbide['email']

        # Adjuntamos Imagen
        file = open("image.png", "rb")
        attach_image = MIMEImage(file.read())
        attach_image.add_header('Content-Disposition', 'attachment; filename = "avatar.png"')
        msg.attach(attach_image)

        mezuaBidali(smtpserver, login, password, msg)
        print('Sent to ' + helbide['email'])


if __name__ == "__main__":
    main()
