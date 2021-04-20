class Cipher:
    def __init__(self,message):
        self.message = message 
    encrypted_message = ""
    original_message = ""
    def encrypt(self,key):
        for i in self.message:
            if i.isupper():
                if (ord(i) + key > ord("Z")):
                    self.encrypted_message += chr(ord(i) + key - 26)
                else:
                    self.encrypted_message += chr(ord(i) + key)
            elif i.islower():
                if (ord(i) + key > ord("z")):
                    self.encrypted_message += chr(ord(i) + key - 26)
                else:
                    self.encrypted_message += chr(ord(i) + key)
            elif (i == "." or i == "!" or i == "," or i == " " or i == "?"):
                self.encrypted_message += i

        return self.encrypted_message

    def decrypt(self,key):
        for i in self.encrypted_message:
            if i.isupper():
                if (ord(i) - key < ord("A")):
                    self.original_message += chr(ord(i) - key + 26)
                else:
                    self.original_message += chr(ord(i) - key)
            elif i.islower():
                if (ord(i) - key < ord("a")):
                    self.original_message += chr(ord(i) - key + 26)
                else:
                    self.original_message += chr(ord(i) - key)
            elif (i == "." or i == "!" or i == "," or i == " "):
                self.original_message += i
        return self.original_message


mes = "I am Talfao."
shift = 5

first = Cipher(mes)
print("Original: " + mes) 
print("Cipher: " + first.encrypt(shift))
print("Original: " + first.decrypt(shift)) 
