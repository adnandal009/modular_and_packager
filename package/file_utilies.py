
def create_file():
    try:
        file=input("Enter File Name (example.txt) :")
        with open(file,"x") as file:
            print("File created sucessfully")
            print("=="*20)
    except:
        print("There was an Error Creating File !!!")

def write_into_file():
    try:
        file=input("Enter File Name (example.txt) :")
        data=input("Enter data to Write :")
        with open(file,"a") as file:
            file.write(data + "\n")
            print("Data written Sucessfully")
            print("=="*20)
    except:
        print("There Was An Error on Reading File ")

def read_file():
    try:
            file=input("Enter File Name :")
            with open(file,"r") as file:
                print("File Content :")
                print(file.read())
                print("=="*20)
    except:
        print("There is no file To Read Please Create a File First")

def append_file():
    try:
             file=input("Enter File Name :")
             content=input("Enter Data to Append :")
             with open(file,"a") as file:
                 file.write(content + "\n")
                 print("Data Append Sucessfully!!")
                 print("=="*20)
    except:
         print("There was an Error on appending a File !!")


def update_entry():
    try:

        entry = input("Enter the word you want to replace: ")
        update = input(f"Enter the word to replace '{entry}' with: ")

        with open("data.txt", "r") as f:
            text = f.read()


        if entry in text:
            text = text.replace(entry, update)

            with open("data.txt", "w") as file:
                file.write(text)
        else:
            print(f"No entries were found for: {entry}")
            return


        print("File Updated Successfully!")
    except:
         print("There Was An Error in Updating The File !!")



def file_op():
    while True:
        print()
        print("=="*20)
        print("File Operations :")
        print("=="*20)
        print("1. Create a New File ")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File ")
        print("5. Update to a File ")
        print("6. Back to Main Menu")
        print("=="*20)

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
