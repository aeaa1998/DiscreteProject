from Utils import Utils


class Crypt:
    def __init__(self):
        utils = Utils()
        coprimesArray = []
        pN = 0
        invalid = True
        while invalid:
            primeQ = 11
                # utils.primeInput("Ingrese el valor del numero primo q", 11, 1000)
            primeP = 13
                # utils.primeInput("Ingrese el valor del numero primo p", 13,1000)
            # MOD N
            self.n = primeP * primeQ
            # MOD N2
            pN = (primeQ - 1) * (primeP - 1)
            coprimesArray = utils.coprimes(pN)
            for coprime in coprimesArray:
                if coprime >= self.n or coprime == 1:
                    coprimesArray.remove(coprime)
            if len(coprimesArray) > 0:
                invalid = not invalid

        # PUBLIC KEY CRYPT
        print("Escoja el public key")
        self.publicKey = utils.chooseIntList(coprimesArray)
        # PRIVATE KEY DECRYPT
        self.privateKey = utils.inverseMod(self.publicKey, pN)

    def cryptMessage(self, text: str):
        cryptedMessage = ''.join(chr(pow(ord(char), self.publicKey, self.n)) for char in text)


        cryptedMessages = ''.join(chr(pow(ord(char), self.privateKey, self.n)) for char in cryptedMessage)
        print("El mensaje encriptado es: \n" + cryptedMessage)
        print("El mensaje normal es: \n" + cryptedMessages)

    def showPublicKey(self):
        print("Public Key:\n" + str(self.publicKey))


    def showPrivateKey(self):
        print("Private Key:\n" + str(self.privateKey))