from Crypt import Crypt
from Decrypt import Decrypt
from Utils import Utils
utils = Utils()
running = True
mainMenu = ["Encryptar", "Decryptar", "Salir"]
cryptMenu = ["Encryptar mensaje", "Mostrar public key", "Mostrar private key", "Mostrar mod n", "Salir"]
decryptMenu = ["Dencryptar mensaje", "Setear nuevo mod n", "Setear nuevo private key", "Salir"]

while running:
    mainKey = utils.chooseKey(mainMenu)
    if mainKey == 1:
        cm = True
        crypt = Crypt()
        while cm:
            cryptKey = utils.chooseKey(cryptMenu)
            if cryptKey == 1:
                crypt.cryptMessage(input("Ingrese el mensaje que desea encryptar:\n"))
            elif cryptKey == 2:
                crypt.showPublicKey()
            elif cryptKey == 3:
                crypt.showPrivateKey()
            elif cryptKey == 4:
                crypt.showModN()
            else:
                print("Ha salido del menu")
                cm = False
    elif mainKey == 2:
        cm = True
        decrypt = Decrypt()
        while cm:
            decryptKey = utils.chooseKey(decryptMenu)
            if decryptKey == 1:
                decrypt.decryptMessage(input("Ingrese el mensaje que desea decryptar:\n"))
            elif decryptKey == 2:
                decrypt.setModN()
            elif decryptKey == 3:
                decrypt.setPrivateKey()
            else:
                print("Ha salido del menu")
                cm = False
    else:
        print("Gracias por usar el programa")
        running = False