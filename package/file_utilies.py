



def create_file():
    try:
        file=input("Enter File Name (example.txt) :")
        with open(file,"x") as file:
            print("File created sucessfully")
            print("===================================")
    except:
        print("There was an Error Creating File !!!")

def write_into_file():
    try:
        file=input("Enter File Name (example.txt) :")
        data=input("Enter data to Write :")
        with open(file,"a") as file:
            file.write(data + "\n")
            print("Data written Sucessfully")
            print("===================================")
    except:
        print("There Was An Error on Reading File ")

def read_file():
    try:
            file=input("Enter File Name :")
            with open(file,"r") as file:
                print("File Content :")
                print(file.read())
                print("===================================")
    except:
        print("There is no file To Read Please Create a File First")

def append_file():
    try:
             file=input("Enter File Name :")
             content=input("Enter Data to Append :")
             with open(file,"a") as file:
                 file.write(content + "\n")
                 print("Data Append Sucessfully!!")
                 print("===================================")
    except:
         print("There was an Error on appending a File !!")

# def update_entry():
#         try:
#             with open("data.txt","r") as file :
                
#                 entry=input("Enter your word you want to  replace : ")
#                 a=file.readlines()
#                 for x in a:
#                     if entry.lower() in x.lower() :
#                         with open(file,"w") as file :
#                             update=input(f"Enter your word to replace it with {entry} =  ")
#                             file.write(update)
#                             print("File Updated Sucessfully!")

                        
#                         break
#                 else:
#                     print(f"No entries were found for the keyword : {entry}. ")

#         except:
#                     print("Something Went Wrong in Search Function !!")


        

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
        print("5. Update to a File ")
        print("6. Back to Main Menu")
        print("===================================")

        ch=int(input("Enter Your Choice : "))

        if ch==1:
                create_file()


        elif ch==2:
            write_into_file()
             
            
        elif ch==3:
            read_file()
            
        elif ch==4:
             append_file()

        elif ch==5:
            update_entry()
             
        elif ch==6:
            print("Going Back to Main Menu....")
            break
        else:
            print("Invalid Choice (1-5)")

file_op()