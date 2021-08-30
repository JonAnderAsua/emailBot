import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

helbideak = []
mezua = ""
smtpserver = 'smtp.gmail.com:587'  # Zein mezu protokoloa erabiliko da, kasu honetan gmailaren smtp protokoloa
login = 'jasuamiranda1998@gmail.com'  # Zein mezu helbidetik bidaliko da
password = ''  # Korreoaren pasahitza'

# Bidali nahi diren helbideak eskuratzeko metodoa
def getHelbideak(s):
    global helbideak

    helbideak = []
    file = open(s)
    lines = file.readlines()
    i = 1

    #Lerro bakoitzean email bakarra dagoenez lerro osoa hartuko da
    for line in lines:
        helbideak.append(str(line))
        i += 1

# Mezua bidaltzeko metodoa
def mezuaBidali(msg):
    global smtpserver,login,password

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login, password)
    problems = server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

#Mezuaren mamia kargatzeko metodoa
def getMessage(s):
    global mezua

    file = open(s).readlines()

    #Mezua lerroz lerro gehituko da
    for l in file:
        mezua += l + "\n"


def bucle():
    i = 0
    while(True):
        main()
        i += 1
        print(str(i) +  ". iterazioa")
        time.sleep(5) #5 segundu geldirik


# Metodo nagusia
def main():
    for helbide in helbideak:
        #Mezua sortu eta konfigurazio nagusia ezarri
        msg = MIMEMultipart()
        msg['Subject'] = "SPAM mezua"
        msg['From'] = login
        msg['To'] = helbide

        # Testua eraiki
        testua = MIMEText(mezua)

        # Irudia eraiki
        file = open("image.png", "rb")
        attach_image = MIMEImage(file.read())

        # Irudia eta mezua atxitu
        msg.attach(testua)
        msg.attach(attach_image)

        mezuaBidali(msg)
        print('Sent to ' + helbide)

def getDatuak():
    getHelbideak('helbideak.txt') #Helbideen fitxategia
    getMessage("message.txt") #Mezua dagoen fitxategia


if __name__ == "__main__":
    aukera = str(input("Aukeratu normal (n) ala buklea (b)"))

    getDatuak()
    print("Datuak hartzen...")


    if(aukera == "b"):
        print("Bukle infinitoa egingo da")
        bucle() #Con bucle
    else:
        print("Bidalketa normala egingo da")
        main() #Sin bucle

