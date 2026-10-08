from package import date_time
from package import math_op
from package import uu_id


while True:

    print("=================================")
    print("Welcome to Multi-Utility Toolkit ")
    print("=================================")
    print()
    print("Choose an Option:")
    print("1.Datetime and Time Operattions")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit ")
    print("=================================")

    choice=int(input("Enter your choice : "))
    if choice==1:
        date_time()
    elif choice==2:
        math_op()
    elif choice==3:
        pass
    elif choice==4:
        uu_id()
    elif choice==5:
        pass
    elif choice==6:
        pass
    elif choice==7:
        break
    else:
        print("Invalid Choice !!")
