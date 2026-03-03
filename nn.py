print("       Solo Conor Restorantiga xush kelibsiz      ")
print("1 Bar")
print("2 Shirinliklar")
print("3")

tanlov = int(input(">>> "))

if tanlov == 1:
    print("1 Kaxva")
    print("2 Limonad")

    btanlov = int(input(">>> "))

    if btanlov == 1:
        print("1 Capuchino")
        print("2 Amerikano")

        ktanlov = int(input(">>> "))

        if ktanlov == 1:
            print("Kapuchino narxi 25 000 som")
            print("Qancha kerak: ")

            soni = int(input(">>> "))
            print("Sizdan", (soni * 25000), "som bo`ldi")

        atanlov = int(input(">>> "))

        if atanlov == 2:
            print("Americano narxi 30 000 som")
            print("Qancha kerak")

            soni = int(input(">>> "))
            print("Sizdan", (soni * 30000), "som bo'ldi")

    ltanlov = int(input(">>> "))

    if ltanlov ==2:
        print("1 Mango")
        print("2 Estragon")

        mtanlov = int(input(">>> "))

        if mtanlov == 1:
            print("Mangoning narxi 30 000 som")
            print("Qancha kerak: ")

            soni = int(input(">>> "))
            print("Sizdan", (soni*30000), "som bo'ldi hurmatli mijoz")

        etanlov =int(input(">>> "))

        if etanlov ==2:
            print("Estragonning narxi 60 000 som")
            print("Qancha olmoqchsiz")

            soni = int(input(">>> "))
            print("Sizdan", (soni*60000), "som bo'ldi hurmatli mijoz")

if tanlov == 2:
    print("1 Napoleon")
    print("2 Praga")

    ntanlov = int(input(">>> "))

    if ntanlov==1:
        print("1 Pista")

        ptanlov = int(input(">>> "))

        if ptanlov == 1:
            print("Pista narxi 29 000 som")
            print("Qancha kerak")

            soni = int(input(">>> "))
            print("Sizdan", (soni * 29000), "som bo'ldi hurmatli mijoz")

if ntanlov == 2:
    print("1 Pragaa")

    qtanlov = int(input(">>> "))

    if qtanlov == 1:
        print("Pragaa narxi 27 000 som")
        print("Qancha kerak")

        soni = int(input(">>> "))
        print("Sizdan", (soni * 27000), "som bo'ldi hurmatli mijoz")
