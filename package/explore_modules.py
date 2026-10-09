def explore_module():
    while True:
        print("="*10)
        print("Explore Module Attributes :")
        print("1. Math's Module")
        print("2. Datetime's Module ")
        print("3. Time's Module ")
        print("4. UUID's Module ")
        print("5. Random's Module ")
        print("6. String's Module ")
        print("7. Back To Main Menu ")

        print("="*10)

        choice=int(input("Enter your  Choice : "))

        if choice==1:
            import math
            print(f"Math Module :  {dir(math)}")
        elif choice==2:
            from datetime import datetime
            print(f"Datetime Module : {dir(datetime)}")
        elif choice==3:
            import time
            print(f"Time Module : {dir(time)}")
        elif choice==4:
            from uuid import uuid4
            print(f" UUID Module : {dir(uuid4)}")
        elif choice==5:
            import random
            print(f" Random Module : {dir(random)}")
        elif choice==6:
            import string
            print(f" String Module : {dir(string)}")
        elif choice==7:
            print("Going Back to Main Menu..........")
            break
        else:
            print("Invalid Choice (1-7)")


