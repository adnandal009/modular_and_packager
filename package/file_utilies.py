def file_op():
    while True:
        print()
        print("===================================")
        print("File Operations :")
        print("===================================")
        print("1. Create a New File ")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File ")
        print("5. Back to Main Menu")
        print("===================================")

        ch=int(input("Enter Your Choice : "))

        if ch==1:
                file=input("Enter File Name (example.txt) :")
                with open(file,"x") as file:
                    print("File created sucessfully")
                    print("===================================")


        elif ch==2:
             file=input("Enter File Name (example.txt) :")
             data=input("Enter data to Write :")
             with open(file,"a") as file:
                file.write(data)
                print("Data written Sucessfully")
                print("===================================")

            
        elif ch==3:
            file=input("Enter File Name :")
            with open(file,"r") as file:
                print("File Content :")
                print(file.read())
                print("===================================")

            
        elif ch==4:
             file=input("Enter File Name :")
             content=input("Enter Data to Append :")
             with open(file,"a") as file:
                 file.write(content)
                 print("Data Append Sucessfully!!")
                 print("===================================")

            
        elif ch==5:
            print("Going Back to Main Menu....")
            break
        else:
            print("Invalid Choice (1-5)")

file_op()
