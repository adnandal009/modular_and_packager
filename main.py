from package import date_time
from package import math_op
from package import uu_id
from package import file_op
from package import explore_module
from package import random_op


def main():
    while True:
        print()
        print("=="*20)
        print("Welcome to Multi-Utility Toolkit ")
        print("=="*20)
        print()
        print("Choose an Option:")
        print("1.Datetime and Time Operattions")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit ")
        print("=="*20)
        print("=="*20)
        print()

        choice=int(input("Enter your choice : "))

        if choice==1:
            print("=="*20)
            date_time()
            print("=="*20)
        elif choice==2:
            math_op()
        elif choice==3:
            random_op()
        elif choice==4:
            uu_id()
        elif choice==5:
            file_op()
        elif choice==6:
            explore_module()
        elif choice==7:
            print("="*10)
            print("Thank You for using the Multi-utility Toolkit!")
            print("="*10)
            
            break
        else:
            print("Invalid Choice !!")



if __name__ == "__main__":
    main()