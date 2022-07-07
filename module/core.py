def encrypt():
    print(cipher)

while 1:
    e_or_d = input("(e)ncryption, (d)ecryption, or (q)uit: ")
    if e_or_d == "e":
        while 1:
            cipher = input("\n(r)everse\n(c)easar\n\nCipher or (q)uit: ")
            break
        break
    elif e_or_d == "d":
        print("waiting")
        break
    elif e_or_d == "q":
        break

if e_or_d == "e":
    encrypt()