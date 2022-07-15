# Nirmit Shah(A203)

opt = int(input("SELECT 1: ENCRYPTION & 2: DECRYPTION & 3: EXIT. \nYOUR CHOICE: "))

s = ""

if opt == 1:
    key = int(input("\nEnter key: "))
    txt = input("Enter your text to cipher: ")
    for i in txt:
        if 65 <= ord(i) <= 90:
            ct = ((((ord(i) - 65) + key) % 26) + 65)
            s = s + chr(ct)
        elif 97 <= ord(i) <= 122:
            ct = ((((ord(i) - 97) + key) % 26) + 97)
            s = s + chr(ct)
        else:
            s = s + i
    print("\n" + s)

elif opt == 2:
    key = int(input("\nEnter key: "))
    txt = input("Enter your text to decipher: ")
    for i in txt:
        if 65 <= ord(i) <= 90:
            dt = ((((ord(i) - 65) - key) % 26) + 65)
            s = s + chr(dt)
        elif 97 <= ord(i) <= 122:
            dt = ((((ord(i) - 97) - key) % 26) + 97)
            s = s + chr(dt)
        else:
            s = s + i
    print("\n" + s)

elif opt == 3:
    print("Exited.")

else:
    print("Invalid Input.")



