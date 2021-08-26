import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


# Bidali nahi diren helbideak eskuratzeko metodoa
def getHelbideak(s):
    helbideak = []
    file = open(s)
    lines = file.readlines()
    i = 0

    #Lerro bakoitzean email bakarra dagoenez lerro osoa hartuko da
    for line in lines:
        helbideak[i] = str(line)
        i += 1
    return helbideak

# Mezua bidaltzeko metodoa
def mezuaBidali(smtpserver, login, password, msg):
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

#Mezuaren mamia kargatzeko metodoa
def getMessage(s):
    file = open(s).readlines()
    message = ""

    #Mezua lerroz lerro gehituko da
    for l in file:
        message += l + "\n"
    return message

def bucle():
    i = 0
    while(True):
        main()
        i += 1
        print(i + ". iterazioa")
        time.sleep(5) #5 segundu geldirik


# Metodo nagusia
def main():
    helbideak = getHelbideak('helbideak.txt')
    smtpserver = 'smtp.gmail.com:587' #Zein mezu protokoloa erabiliko da, kasu honetan gmailaren smtp protokoloa
    login = 'jasuamiranda1998@gmail.com' #Zein mezu helbidetik bidaliko da
    password = '' #Korreoaren pasahitza


    for helbide in helbideak:

        #Mezua sortu eta konfigurazio nagusia ezarri
        msg = MIMEMultipart()
        msg['Subject'] = "Pierda hasta el 19% de su peso. Un nuevo sistema para adelgazar está aquí."
        msg['From'] = login
        msg['To'] = helbide['email']

        # Testua eraiki
        testua = MIMEText(getMessage("message.txt"))

        # Irudia eraiki
        file = open("image.png", "rb")
        attach_image = MIMEImage(file.read())

        # Irudia eta mezua atxitu
        msg.attach(testua)
        msg.attach(attach_image)

        mezuaBidali(smtpserver, login, password, msg)
        print('Sent to ' + helbide['email'])


if __name__ == "__main__":
    main() #Sin bucle
    #bucle() #Con bucle
