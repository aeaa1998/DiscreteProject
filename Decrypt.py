
from Utils import Utils
class Decrypt:
    def __init__(self):
        self.utils = Utils()
        self.privatekey = self.utils.intInputMin("Ingrese un private key", 1)
        self.n = self.utils.intInputMin("Ingrese un mod n", 1)

    def decryptMessage(self, text: str):
        dec = ''.join(chr(pow(ord(char), self.privatekey, self.n)) for char in text)
        print("El mensaje normal es: \n" + dec)

    def setPrivateKey(self):
        self.privatekey = self.utils.intInputMin("Ingrese un private key", 1)

    def setModN(self):
        self.n = self.utils.intInputMin("Ingrese un mod n", 1)

