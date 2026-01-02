FILENAME="employees.txt"

#read 
def read_employees():
    employees = []
    try:
        with open(FILENAME ,"r") as file :
            for line in file:
                name, time , salary =line.strip().split(",")
                employees.append({
                    "name" : name,
                    "time" : time,
                    "salary": salary
                })
    except FileNotFoundError:
        pass
    return employees

#write 
def wirte_employees(emplyoees):
    with open(FILENAME,"w") as file :
        for emp in emplyoees:
            file.write(f"{emp["name"]},{emp["time"]},{emp["salary"]}\n")

#add 
def add_employees():
    name = input("Enter name :-")
    time = input("Enter time :-")
    salary = input("Enter salary :-")

    employees= read_employees()
    employees.append({
        "name": name,
        "time" : time,
        "salary": salary
    })
    wirte_employees(employees)
    print("--Employees add successfully--")

#update
def update_employees():
    employees = read_employees()

    if not employees:
        print("--No employees found--")

    print("\nEmployees:")
    for  i , emp in enumerate(employees):
        print(i + 1 , emp["name"])

    choice =int(input("select your numer to update :"))-1
    if choice < 0 or choice >= len(employees):
        print("Invalid choice")
        return
    print("1 Update name")
    print("2 Update time")
    print("3 Update salary")

    option = int(input("Enter Your Option:- "))

    if option == 1:
        employees [choice]["name"] = input("Enter new name: ")
    elif option ==2:
        employees [choice]["time"] = input("Enter new time: ")
    elif option ==3:
        employees [choice]["salary"]= input("Enter new salary: ")
    else :
        print("Invalid Option ")
        return
    
    wirte_employees(employees)
    print("Employees Update successfully")

#show data
def show_all_employees():
    employees = read_employees()

    if not employees:
        print("not data employess")
        return
    
    print("\n---All Employess Data---")
    for i, emp in enumerate(employees):
        print(print(f"""
Employee {i + 1}
Name : {emp['name']}
Time : {emp['time']}
Salary : {emp['salary']}
-------------------------
"""))

#Delete employee         

def delete_empolyee():
    empolyee =read_employees()

    if not empolyee:
        print("no empolyees found")
        return
    print("\n empolyees found")
    for i,emp in enumerate(empolyee):
        print(i+1 , emp["name"])

    choice =int(input("select employee number to delete: "))-1
    if choice <0 or choice>=len(empolyee):
        print("Invalid chocie")
        return
    delete_emp =empolyee.pop(choice)
    wirte_employees(empolyee)
    print(f"Empolyees'{delete_emp['name']}' deleted successfully  ")


#main menu
while True:
    print("\n-- Employees Mangement --")
    print("1. Add Employee")
    print("2 Update Employee")
    print("3 Exit")
    print("4 Show All Employee")
    print("5 Delete Employee")

    menu = input("Enter your choice: ")

    if menu == "1":
        add_employees()
    elif menu =="2":
        update_employees()
    elif menu =="3":
        print("Goodbye")
        break
    elif menu =="4":
        show_all_employees()
    elif menu =="5":
        delete_empolyee()
    
    else:
        print("Invalid Choice ")

