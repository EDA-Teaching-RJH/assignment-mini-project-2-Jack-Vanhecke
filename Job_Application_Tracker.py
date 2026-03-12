import csv # for handling CSV files
from operator import index
import re  # for REGEX
from datetime import datetime # for handling dates

class Application_Format:
    def __init__(self, index, company, title, date, status, email, notes):
        self.index = index
        self.company = company
        self.title = title
        self.date = date
        self.status = status
        self.email = email
        self.notes = notes

    def format(self):
        return[self.index, self.company, self.title, self.date, self.status, self.email, self.notes]

class Opperations:

    application = [] # List to store the volitile application data, stored in terminal temporarily not in csv file

    def Validate_Company(self, company):                                    #Ensures the company name is not empty
        if company == "":
            print("Company name cannot be empty. Enter a valid company name.")
            return company
        return True
    
    def Validate_Job_Title(self, title):                                    #Ensures the job title is not empty
        if title == "":
            print("Job title cannot be empty. Enter a valid job title.")
            return title
        return True
    
    def Validate_Application_Date(self, date):                              #Ensures the application date is not empty and in a valid format
        try:
            datetime.strptime(date, "%d-%m-%Y") # Checks if the date is in the correct format (DD-MM-YYYY)
        except ValueError:
            print("Invalid date format. Use the format DD-MM-YYYY.")
            return False
        if date == "":
            print("Application date cannot be empty. Enter a valid date in the format DD-MM-YYYY.")
            return False
        return True

    def Validate_Status(self, status):                                      #Ensures the application Status is deemed as a valid status (Applied, Interview, Offer, Rejected)
        if re.search(r'^(Applied|Interview|Accepted|Rejected)$', status):
            return status
        elif status == "":
            print("Status cannot be empty. Enter a valid status (Applied / Interview / Offer / Rejected).")
            return status
        return True
    
    def Validate_Email(self, email):                                        # Ensures the email is a valid email
        if re.search(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return email
        elif email == "":
            print("Email cannot be empty. Enter a valid email address.")
            return email
        return True
    
    def add_app(self):                                                      # Adds a job application to the application list, with all the required data points, and validates each input to ensure it is acceptable and makes logical sense
        while True:
            company = input("Company Name: ")
            if self.Validate_Company(company):
                break

        while True:
            title = input("Job Title: ")
            if self.Validate_Job_Title(title):
                break

        while True:
            date = input("Did you apply today or another date? (Enter 'today' or a date in the format DD-MM-YYYY) ")
            if date == "today":
                date = datetime.now().strftime("%d-%m-%Y")              # datetime.now() gets the current date and time, .strftime() formats it to the specified format (DD-MM-YYYY in this case)
                break
            elif self.Validate_Application_Date(date):
                date = self.Validate_Application_Date(date)
                break

        while True:
            status = input("Status (Applied / Interview / Offer / Rejected): ")
            if self.Validate_Status(status):
                break
        
        while True:
            email = input("Email Contact: ")
            if self.Validate_Email(email):
                break
        
        notes = input("Notes: ")

        index = len(self.application) + 1
        appended_app = Application_Format(index, company, title, date, status, email, notes)
        self.application.append(appended_app)
        print("Application added successfully.")

    def view_app(self):
        if len(self.application) == 0:
            print("No unsaved applications to view.")
            return
        else:
            for app in self.application:
                print(f"[{app.index}] {app.company} | {app.title} | {app.status} | {app.date} | {app.email} | {app.notes}")

    def search_app(self):
        if len(self.application) == 0:
            print("No unsaved applications to search.")
            return
        search = input("Enter a search term (Company, Job Title, Status, etc.): ").lower()
        found = [app for app in self.application if search in app.company.lower() or search in app.title.lower() or search in app.status.lower() or search in app.date.lower() or search in app.email.lower() or search in app.notes.lower()]
        
        if found:
            for app in found:
                print(f"[{app.index}] {app.company} | {app.title} | {app.status} | {app.date} | {app.email} | {app.notes}")
        else:
            print("No applications found matching the search term.")

    def update_app(self):
        self.view_app()
        if len(self.application) == 0:
            print("No unsaved applications to update.")
            return
        try:
            index = int(input("Enter the number of the job application you want to update: "))
            if index < 1 or index > len(self.application):
                print("Invalid number. Please enter a valid number from the list.")
                return
            elif index > 0 and index <= len(self.application):
                new_status = input("Enter the new status (Applied / Interview / Offer / Rejected): ")
                if self.Validate_Status(new_status):
                    self.application[index - 1].status = new_status
                    print("Status updated successfully.")
                else:
                    print("Invalid status. Status not updated.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        new_status = input("Enter the new status (Applied / Interview / Offer / Rejected): ")
        if self.Validate_Status(new_status):
            app.status = new_status
            print("Status updated successfully.")
        else:
            print("Invalid status. Status not updated.")

    def save_app(self):
        if len(self.application) == 0:
            print("No unsaved applications to save.")
            return
        with open("Job_Applications.csv", "a", newline= "") as file:
            writer = csv.writer(file)
            for app in self.application:
                writer.writerow(app.format())
        print("Applications saved successfully.")

    def load_app(self):
        try:
            with open("Job_Applications.csv", "r") as file:
                reader = csv.reader(file)
                self.application = []
                [index, company, title, date, status, email, notes] = row
                for row in reader:
                    loaded_app = Application_Format(index, company, title, date, status, email, notes)
                    self.application.append(loaded_app)
            print("Applications loaded successfully.")
        except FileNotFoundError:
            print("No saved applications found. Please save applications before trying to load.")

def main():

    Changes = Opperations()

    while True:                              # Loops the code indefinitely, unless exit option is entered

        print("---MENU---")                  # Menu options
        print("1. Add Job Application ")
        print("2. View Unsaved Job Application(s) ")
        print("3. Search For Job Application(s) ")
        print("4. Update Job Application ")
        print("5. Save Job Applications to file ")
        print("6. Download Job Applications from file ")
        print("7. Exit ")
        option = input("Please enter your option. ")

        if option == "1":                    # Chooses the definition within the Tracker class to run dependant on the option chosen
            Changes.add_app()
        elif option == "2":
            Changes.view_app()
        elif option == "3":
            Changes.search_app()
        elif option == "4":
            Changes.update_app()
        elif option == "5":
            Changes.save_app()
        elif option == "6":
            Changes.load_app()
        elif option == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

'''
NOTE: Program idea was generated by ChatGPT, but all code is "hand" written.
      ChatGPT prompt: "What is a possble useful application for Regex, Testing, Libraries, File I/O, and OOP functions?"

Step by step process:
    Create / find Job_Applications.csv for storing data
    Have a menu system for each option:
        Add Job Application
            Company Name
            Job Title
            Application Date
            Status (Applied / Interview / Offer / Rejected)
            Email Contact
            Notes
        View Job Applications (All data)
        Search Job Applications (Ideally by any data point, however by Status at minimum)
        Update Job Applications
        Save (Upload to CSV file) Job Applications
        Load (Extract from CSV file) Job Applications
        Exit
    
    The code must also be able to Validate inputs to ensure they are acceptable and make logical sense'''