import random

while True:

    print("Press y or yes to roll the dice and n or no to exit")
    user = input("What you want to do\n")

    if user=="n" or user=="no":
        break

    if user=="y" or user=="yes":
        no = random.randint(1,6)

        if no ==1:
            print("[-----]")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print("[-----]")
            
        if no ==2:
            print("[-----]")
            print("[ 0    ]")
            print("[     ]")
            print("[   0 ]")
            print("[-----]")
        
        if no ==3:
            print("[-----]")
            print("[     ]")
            print("[ 000 ]")
            print("[     ]")
            print("[-----]")

        if no ==4:
            print("[-----]")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print("[-----]")

        if no ==5:
            print("[-----]")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print("[-----]")

        if no ==6:
            print("[-----]")
            print("[0 0 0]")
            print("[     ]")
            print("[0 0 0]")
            print("[-----]")