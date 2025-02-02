class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_employee_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")


class Manager(Employee):
    def __init__(self, name, emp_id, post, no_of_employee):
        super().__init__(name, emp_id)  # Call the constructor of the Employee class
        self.post = post
        self.no_of_employee = no_of_employee

    def display_manager_info(self):
        self.display_employee_info()  # Call the method from the Employee class
        print(f"Post: {self.post}")
        print(f"Number of Employees Managed: {self.no_of_employee}")


# Example usage
if __name__ == "__main__":
    # Create a Manager object
    manager = Manager("Alice Smith", "M001", "Project Manager", 10)

    # Display Manager information
    manager.display_manager_info()