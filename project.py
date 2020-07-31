"""
MUST READ !!!
This is a project where user can perform crud operations with binary file.

This is a long project and therefore contains many user-defined functions.

I am providing docstring to each function to, understand it better.

Here I am classifying all user-defined functions into two categories..

1> These function are all main functions such as create, delete, change, main, etc....

2> These function are not main functions, they are created to reduce code needed to create main functions,.. You can call it as supporting functions, as they support main functions.

To clarify which function is supporting, I am defining all supporting function with prefix "supporting_"

## Originally created by : KUNWAR YUVRAJ

###########################################################
    Previously I made this project using python classes, which made this project very simple, but I shifted to this one because classes are not in  our syllabus

"""
import pickle

""" ##### STARTING OF MAIN FUNCTIONS ##### """

#file_name = input("Enter binary file's name with you want to work in this session : ")

def create():
    print("You can enter details now !\n")
    while True:
        code = input('Enter code : ')
        name = input('Enter name : ')
        salary = input('Enter salary : ')
        department = input('Enter department : ')
        details = [name, salary, department]
        data[code] = details
        ask = input('Enter any to continue or enter "q" to exit : ')
        print()
        if ask in 'qQ':
            break
    with open(file_name, 'ab') as file:
        pickle.dump(data, file)
    print("\nDetails have been created !")

def add_data():
    try:
        print("You can enter details now !\n")
        with open(file_name, 'rb+') as file:
            data = pickle.load(file)
            while True:
                code = input('Enter code : ')
                name = input('Enter name : ')
                salary = input('Enter salary : ')
                department = input('Enter department : ')
                details = [name, salary, department]
                data[code] = details
                ask = input('Enter any to continue or enter "q" to exit : ')
                print()
                if ask in 'qQ':
                    break
            file.seek(0)
            pickle.dump(data, file)
            print("\nDetails have been added !")
    except FileNotFoundError:
        print("This file does not exists ! (First create this file by going to STORE-->CREATE )")

def display():
    """
    Data inside file is displayed in tabular form.
    Supporting functions of this function are :-
        supporting_heading,
        supporting_display_table,
        supporting_display_table_last_row
    """
    try:
        with open(file_name, 'rb') as file:
            read = pickle.load(file)
        supporting_heading()
        for i in read:
            supporting_display_table(i,read)
        supporting_display_table_last_row()
    except FileNotFoundError:
        print("This file does not exists ! (First create this file by going to STORE-->CREATE )")

def search():
    """
    You can search any employee by their name, code, salary or department.
    Supporting function of this function is :-
        supporting_search
    """
    try:
        with open(file_name, 'rb') as file:
            read = pickle.load(file)

        ques = ['code', 'name', 'salary', 'department']
        for i in ques:
            print("Enter", ques.index(i)+1, "to search with",i)

        choice = input("\nEnter want you want to search with : ")            
        ask = input("Enter employee's detail : ")
        exists = False
        if choice == '1':
            for i in read:
                if i == ask:
                    supporting_search(i, read)
                    exists = True

        elif choice == '2':
            for i in read :
                if read[i][0] == ask:
                    supporting_search(i, read)
                    exists = True

        elif choice == '3':
            for i in read :
                if read[i][1] == ask:
                    supporting_search(i, read)
                    exists = True

        elif choice == '4':
            for i in read :
                if read[i][2] == ask:
                    supporting_search(i, read)
                    exists = True
        else:
            print("Invalid choice ! \n")
        if not exists:
            print("Employee's detail not found ! :(")

    except FileNotFoundError:
        print("This file does not exists ! (First create this file by going to STORE-->CREATE )")
def modify():
    """
    You can change name, salary or department of any employee.
    Supporting function of this function is :-
        supporting_change
    """
    try:
        with open(file_name, 'rb') as file:
            read = pickle.load(file)

        ques = ['name', 'salary', 'department']
        for i in ques:
            print('Enter', ques.index(i)+1,"to modify",i)
        print()
        choice = input("Enter your choice : ")
        ask_code = input("Enter employee's code : ")
        exists = False
        if choice == '1':        
            for i in read:
                if i == ask_code:
                    supporting_change(0, i, read,"name")
                    exists = True 
                    break
        elif choice == '2':        
            for i in read:
                if i == ask_code:
                    supporting_change(1, i, read, "salary")
                    exists = True 
                    break
        elif choice == '3':        
            for i in read:
                if i == ask_code:
                    supporting_change(2, i, read, "department")
                    exists = True 
                    break

        with open(file_name, 'wb') as file:
            pickle.dump(read, file)

        if exists:
            print("\nData have been modified !\n")

        if not exists:
            print("Employee does not exists ! :(")
    except FileNotFoundError:
        print("This file does not exist ! (First create this file by going to STORE-->CREATE )")

def delete():
    """
    You can delete all data of any employee. As this is irrevesible task to have to confirm it by entering employee's name.
    This function has no supporting function.

    """
    try:
        with open(file_name, 'rb') as file:
            read = pickle.load(file)
        ask = input("Enter employee's code you want to delete : ")
        exists = False
        for i in read:
            if i == ask:
                confirm = input("This will erase all data of this employee, enter employee's name to continue : ")
                if confirm == read[i][0]:
                    del read[i]
                    print("Employee is deleted !")
                    exists = True 
                    break
                elif confirm != read[i][0]:
                    exists = True
                    print("Wrong name employee is not deleted !")
                    break
        with open(file_name, 'wb') as file:
            pickle.dump(read, file)
        if not exists:
            print("Employee does not exists")
    except FileNotFoundError:
        print("This file does not exists ! (First create this file by going to STORE-->CREATE )")

def main():
    """
    This is the main function of this program. It calls every other function when needed.
    Supporting function of this function is :-
        supporting_my_name
    """
    ques = ['store', 'display', 'search', 'modify','delete', 'change file']
    supporting_my_name()
    global file_name
    global data
    data = dict()
    file_name = input("Enter file's name you want to work with (you can change it later) : ")
    while True:
        print()
        print('#'*100)
        print('='*100)
        supporting_print_mainmenu()
        for i in ques:
            print("Enter",ques.index(i)+1,"to",i)
        print("Enter ANY other key to exit !!!")
        print()

        choice = input("Enter your choice : ")
        print('='*100)
        print('#'*100)
        print()
        if choice == '1':
            supporting_print_store()
            print("Enter 1 to create a file by entering data or to erase all data and add new")
            print("Enter 2 to add more data to existing file")
            ask = input("Enter your choice : ")
            if ask == '1':
                print("\n\tS T O R E ---> Create \n")
                create()
            elif ask == '2':
                print("\n\tS T O R E ---> Add \n")
                add_data()
            else:
                print("Invalid choice !\n")
        elif choice == '2':
            supporting_print_display()
            display()
        elif choice == '3':
            supporting_print_search()
            search()
        elif choice == '4':
            supporting_print_modify()
            modify()
        elif choice == '5':
            supporting_print_delete()
            delete()

        elif choice == '6':
            supporting_print_changefile()
            file_name = input("Enter file's name you want to open  : ")
            data = dict()
        else:
            break


""" ##### END OF MAIN FUNCTIONS ##### """

""" ========================================================= """

""" ##### STARTING OF SUPPORTING FUNCTIONS ##### """


def supporting_heading():    
    """
    Just displays heading in tabular form whenever needed.
    """
    print()
    print('-'*100)
    print("|  E M P L O Y E E  C O D E  |  E M P L O Y E E  N A M E  |   S A L A R Y  |   D E P A R T M E N T |")
    print("-"*100)

def supporting_display_table(i,read):
    """
    This displays data inside dictionary in tabular form.
    """
    d = '|'
    print(d,i," "*(25-len(i)),d,read[i][0], " "*(25-len(read[i][0])),d,read[i][1]," "*(13-len(read[i][1])),d,read[i][2]," "*(20-len(read[i][2])),d)

def supporting_display_table_last_row():
    """
    This just prints last line of table ,i.e,. "-------".
    """
    print('-'*100)

def supporting_search(i, read):
    """
    This helps search function in printing data when an employee is searched.
    This just calls three different supporting function in special sequence.
    Supporting function are :-
        supporting_heading,
        supporting_display_table,
        supporting_display_table_last_row
    """
    supporting_heading()
    supporting_display_table(i, read)
    supporting_display_table_last_row()

def supporting_change(num, i, read, ques):
    """
    Just supports change function.
    """
    ask = input("Enter new "+ques+"  : ")
    read[i][num] = ask

def supporting_print_store():
    print('''
█▀ ▀█▀ █▀█ █▀█ █▀▀
▄█ ░█░ █▄█ █▀▄ ██▄
    ''')

def supporting_print_display():
    print('''
█▀▄ █ █▀ █▀█ █░░ ▄▀█ █▄█
█▄▀ █ ▄█ █▀▀ █▄▄ █▀█ ░█░
    ''')

def supporting_print_search():
    print('''
█▀ █▀▀ ▄▀█ █▀█ █▀▀ █░█
▄█ ██▄ █▀█ █▀▄ █▄▄ █▀█
    ''')

def supporting_print_modify():
    print('''
█▀▄▀█ █▀█ █▀▄ █ █▀▀ █▄█
█░▀░█ █▄█ █▄▀ █ █▀░ ░█░
    ''')

def supporting_print_delete():
    print('''
█▀▄ █▀▀ █░░ █▀▀ ▀█▀ █▀▀
█▄▀ ██▄ █▄▄ ██▄ ░█░ ██▄
    ''')

def supporting_print_mainmenu():
    print('''
█▀▄▀█ ▄▀█ █ █▄░█   █▀▄▀█ █▀▀ █▄░█ █░█
█░▀░█ █▀█ █ █░▀█   █░▀░█ ██▄ █░▀█ █▄█
    ''')

def supporting_print_changefile():
    print('''
█▀▀ █░█ ▄▀█ █▄░█ █▀▀ █▀▀   █▀▀ █ █░░ █▀▀
█▄▄ █▀█ █▀█ █░▀█ █▄█ ██▄   █▀░ █ █▄▄ ██▄
    ''')


def supporting_my_name():
    """
    This function shows heading of the program ,i.e, my name
    This supports main function
    """


    print("\nBINARY FILE PROJECT BY :",end='')

    print('''
        
██╗░░██╗██╗░░░██╗███╗░░██╗░██╗░░░░░░░██╗░█████╗░██████╗░  ██╗░░░██╗██╗░░░██╗██╗░░░██╗██████╗░░█████╗░░░░░░██╗
██║░██╔╝██║░░░██║████╗░██║░██║░░██╗░░██║██╔══██╗██╔══██╗  ╚██╗░██╔╝██║░░░██║██║░░░██║██╔══██╗██╔══██╗░░░░░██║
█████═╝░██║░░░██║██╔██╗██║░╚██╗████╗██╔╝███████║██████╔╝  ░╚████╔╝░██║░░░██║╚██╗░██╔╝██████╔╝███████║░░░░░██║
██╔═██╗░██║░░░██║██║╚████║░░████╔═████║░██╔══██║██╔══██╗  ░░╚██╔╝░░██║░░░██║░╚████╔╝░██╔══██╗██╔══██║██╗░░██║
██║░╚██╗╚██████╔╝██║░╚███║░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║  ░░░██║░░░╚██████╔╝░░╚██╔╝░░██║░░██║██║░░██║╚█████╔╝
╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░
    ''')
""" ##### END OF SUPPORTING FUNCTIONS ##### """

""" ========================================================= """

"""##### Finally, calling main function, without this nothing will work!!  #####"""
main()
