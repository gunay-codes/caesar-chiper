class Caesar():
    def __init__(self, text, shift):
        self.text = text
        self.shift = shift

    def encrypt(self):
        cipher = ""

        for encrypt in self.text:
            print(encrypt, "==>", chr(ord(encrypt) + shift))
            cipher += chr(ord(encrypt) + shift)

        print(self.text, "Encrypted form ===>", cipher, '\n')

    def decrypting(self):
        decrypted = ""

        for decrypt in self.text:
            print(decrypt, "==>", chr(ord(decrypt) - shift))
            decrypted += chr(ord(decrypt) - shift)

        print(self.text, "Decrypted form ===>", decrypted, "\n")


while True:
    choice = input("1- Encrypt \n2- Decrypt \n3- Exit \nSelect the action you want to do: ")

    if choice == "1":
        text = input("Enter text: ")
        shift = int(input("Enter the number value you want to shift: "))
        caesar = Caesar(text, shift)
        caesar.encrypt()
    elif choice == "2":
        text = input("Enter text: ")
        shift = int(input("Enter the number value you want to shift: "))
        caesar = Caesar(text, shift)
        caesar.decrypting()
    elif choice == "3":
        break
    else:
        print("Incorrect choice.")
