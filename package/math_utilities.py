from uuid import uuid4
from datetime import datetime
import time
import math



def date_time():
        while True:
            print("Date and Time Operations :")
            print("1. Display Current Date and Time :")
            print("2. Calculate Differnce Between Two Dates/Times : ")
            print("3. Format data into Customs Format: ")
            print("4. Stopwatch: ")
            print("5. Countdown Timer:")
            print("6. Back to Menu :")

            ch=int(input("Enter Your Choice :"))

            if ch==1:
                  dt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                  print("===========================")
                  print("Current Date and Time :",dt)
            elif ch==2:
                  print("===========================")
                  first=str(input("Enter First Date (YYYY-MM-DD) : "))
                  second=str(input("Enter Second Date (YYYY-MM-DD) : "))
              
                  
                  a=datetime.strptime(first,"%Y-%m-%d")
                  b=datetime.strptime(second,"%Y-%m-%d")
                  c=abs(a-b)
                  print(f" Diffrence :{c}")
            elif ch==3:
                while True:
                    print("========================")
                    print("Choose an Option :")
                    print("1.Date ")
                    print("2. Time ")
                    print("3. Date and Time")
                    print("4. Back to Date and Time Operations")
                    ch=int(input("Enter your Choice : "))

                    if ch==1:
                        print(f"Date :{datetime.now().strftime("%Y-%m-%d")}")
                    elif ch==2:
                        print(f"Time : {datetime.now().strftime("%H:%M:%S")}")
                    elif ch==3:
                        print(f" Date and Time : {datetime.now()}")
                    elif ch==4:
                        print("Going Back to  Date and Time Operations....")
                        print("========================")
                        break
                    else:
                        print("Invalid Choice (1-4)")
                        print("========================")

            elif ch==4:
                 start=time.time()
                 input("Press Enter for Stop ")
                 end=time.time()
                 print(f"Time : {end-start}")
                 print("========================")

            elif ch==5:
                 count=int(input("Enter a Number for Countdown :"))
                 print("========================")

                 while count>0:
                      print(f"\t Countdown :  {count}")
                      time.sleep(1)
                      count=count-1
                      

            elif ch==6:
                 print("Going Back To Main Menu......")
                 print("========================")
                 break

                
                  
def math_op():
     while True:
        print()
        print("======================================")
        print("Mathematical Operations :")                  
        print("======================================")    
        print("1. Calculate Factorial")              
        print("2. Solve Compound Interest")              
        print("3. Trigonmetric Calculation")              
        print("4. Area of Geometric Shapes")              
        print("5. Back to Main Menu ")
        print("=================================================")


        choice=int(input("Enter your Choice :"))

        if choice==1:
             fact=int(input("Enter a Number For Factorial :"))
             print(f"Factorial of {fact} is : {math.factorial(fact)}")
             print("=================================================")

        elif choice==2:
             money=int(input("Enter Principle Amount :"))
             interest=int(input("Enter Rate of interest (in %) :"))
             year=int(input("Enter time (in years)"))
             cp=money*(1+interest/100)**year
             print(f"Compound Interest : {cp}")
             print("=================================================")
        elif choice==3:
             pass
             print("=================================================")
        
        elif choice==4:
             pass
             print("=================================================")
        
        elif choice==5:
             print("Going Back To Main Menu......")
             break
        else:
             print("Invalid Choice (1-5)")


def uu_id():
     while True:
        print()
        print("=================================")
        print("Unique Identifiers ")
        print("=================================")
        print("Select an Option")
        print("1. Generate a Unique ID")
        print("2. Back to Menu")
        ch=int(input("Enter Your Choice :"))
        if ch==1:
            a=uuid4()
            print(f"Unique ID : {a}")
        elif ch==2:
             print("Going Back to Main Menu")
             break
        else:
             print("Invalid Choice (1-2)!!")
     
     



                  
