"""MIGUEL ANGEL CUENTAS BARRETO - T00067657
Código de prueba en verificación, es un sumario o una evidencia y claramente le hacen falta optimizaciones que lo hagan mucho más profundo, pero cumple los requerimientos en general
"""

from admin import Admin
from campus_platform import CampusPlatform
from bike import Bike
from equipment import Equipment
from student import Student
from library import Library

def main():
    campus = CampusPlatform()
    campus.bikes.append(Bike(1))
    campus.bikes.append(Bike(2, False))  # Agregar una bicicleta no disponible
    """Mini base de datos con diccionarios que validen los usuarios existentes"""
    campus.equipment.append(Equipment("Laptop"))
    campus.library.append(Library("The Great Gatsby", "F. Scott Fitzgerald"))
    campus.library.append(Library("To Kill a Mockingbird", "Harper Lee"))
    campus.library.append(Library("1984", "George Orwell"))
    campus.add_admin(Admin("admin1", "password123"))

    while True:
        print("\n--- Campus Platform Menu ---")
        print("1. Student")
        print("2. Admin")
        print("3. Exit")

        option = input("Select an option: ")

        if option == "1":
            while True:
                print("\n--- Student Menu ---")
                print("1. Register")
                print("2. Login")
                print("3. Go back to main menu")

                student_option = input("Select an option: ")

                if student_option == "1":
                    student_id = input("Enter student ID: ")
                    student_name = input("Enter student name: ")
                    user = input("Enter the new student user: ")
                    password = input("Enter the new student password: ")
                    campus.register_student(student_id, student_name, user, password)
                elif student_option == "2":
                    user = input("Enter student user: ")
                    password = input("Enter student password: ")
                    student = campus.student_login(user, password)
                    if student:
                        while True:
                            print("\n--- Student Actions ---")
                            print("1. Reserve a bike")
                            print("2. Request equipment")
                            print("3. Buy stationery")
                            print("4. Access Library")
                            print("5. Go back to student menu")

                            student_action = input("Select an action: ")
                            if student_action == "1":
                                campus.reserve_bike(student.student_id)
                            elif student_action == "2":
                                campus.request_equipment(student.student_id)
                            elif student_action == "3":
                                campus.buy_stationery(student.student_id)
                            elif student_action == "4":
                                campus.access_library()
                            elif student_action == "5":
                                break
                            else:
                                print("Invalid option. Please try again.")
                elif student_option == "3":
                    break
                else:
                    print("Invalid option. Please try again.")

        elif option == "2":
            while True:
                print("\n--- Admin Menu ---")
                print("1. Login")
                print("2. Go back to main menu")

                admin_option = input("Select an option: ")

                if admin_option == "1":
                    admin_username = input("Enter admin username: ")
                    admin_password = input("Enter admin password: ")
                    if campus.admin_login(admin_username, admin_password):
                        print("Admin logged in successfully.")
                        campus.admin_menu(admin_username)
                    else:
                        print("Admin login failed.")
                elif admin_option == "2":
                    break
                else:
                    print("Invalid option. Please try again.")

        elif option == "3":
            print("Exiting the Campus Platform. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()