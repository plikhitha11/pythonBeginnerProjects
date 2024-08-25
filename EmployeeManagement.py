class EmployeeManagementSystem:
    def __init__(self):
        self.employees = {}
        self.next_id = 1

    def add_employee(self, name, position, salary):
        emp_id = self.next_id
        self.employees[emp_id] = {'Name': name, 'Position': position, 'Salary': salary}
        self.next_id += 1
        print(f"Employee added with ID: {emp_id}")

    def view_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        for emp_id, details in self.employees.items():
            print(f"ID: {emp_id}, Name: {details['Name']}, Position: {details['Position']}, Salary: ${details['Salary']}")

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee with ID {emp_id} deleted.")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def total_employees(self):
        print(f"Total number of employees: {len(self.employees)}")

    def menu(self):
        while True:
            print("\nEmployee Management System")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Delete Employee")
            print("4. Total Employees")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter employee name: ")
                position = input("Enter employee position: ")
                salary = float(input("Enter employee salary: "))
                self.add_employee(name, position, salary)
            elif choice == '2':
                self.view_employees()
            elif choice == '3':
                emp_id = int(input("Enter employee ID to delete: "))
                self.delete_employee(emp_id)
            elif choice == '4':
                self.total_employees()
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    system = EmployeeManagementSystem()
    system.menu()
