import csv # for handleing CSV files
import re  # for REGEX
from datetime import datetime # for handling dates

class Application_Format:
    def __init__(self, company, title, date, status, email, notes):
        self.company = company
        self.title = title
        self.date = date
        self.status = status
        self.email = email
        self.notes = notes

    def format(self):
        return[self.company, self.title, self.date, self.status, self.email, self.notes]

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
        if date == "":
            print("Application date cannot be empty. Enter a valid date in the format DD-MM-YYYY.")
            return date
        elif datetime.strptime(date, "%d-%m-%Y"):
            return date
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
    
    def add_app(self):
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
                date = datetime.now().strftime("%d-%m-%Y")
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

        appended_app = Application_Format(company, title, date, status, email, notes)
        self.application.append(appended_app)
        print("Application added successfully.")

    def view_app(self):
        for _ in range(len(self.application)):
            print(self.application[_].format())

    def search_app(self):
        print("Search")

    def update_app(self):
        print("Update")

    def save_app(self):
        print("Save")

    def load_app(self):
        print("Load")

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