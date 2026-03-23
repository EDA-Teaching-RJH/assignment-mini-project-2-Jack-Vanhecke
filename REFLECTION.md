Project Overview

    The Job_Application_Tracker.py file aims to read and write from a separate CSV file which contains the tracked applications.

    The main functions include:
        Import data from CSV file.
        Displaying a menu system for the user to input their option.
        Run specific code depending on the users chosen function.
        Take relevent inputs from the user depending on the function chosen.
        Validate any inputs.
        Save data to the CSV file.



Required Concepts and evidence:

    Regular Expressions (Regex): (Workshop 8)

        Regex functions search through given strings to check if specific criteria are met, giving a specific output if or if not met.
        Used to validate inputs before they get saved to the CSV file:

            if re.search(r'^(Applied|Interview|Offer|Rejected)$', status):
            Only allows the input Status if it is equal to one of the valid statuses.

            if re.search(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            Only allows the input Email if it follows this valid format.

                While not Regex, the Date, Title and Companies also need validation, however can be compared directly to either valid Date syntax or blank strings, using simple if statements, without regex.

        Evidence for regex: Lines 47 and 57.



    Testing: (Lecture 8)
        
        Testing is used to trial both valid and invalid inputs, whether logical or not given the valiable assigned, such as:
        Emails (email@company.com -Valid / $$@@@$. - Invalid)
        Dates (12/03/2024 - Valid / Yesterday - Invalid)

        The testing file works by asserting different inputs to each definition with an attached expected output. Where an assert is correct and the expected result is the same as that of what is returned, then the assert is valid. If this is not the case, the assert is invalid and therefore returns with an AssertError. When used with an if statement, I can print a line saying is the "test" came back valid or invalid. This allows for you to add multiple tests for all definitions and run them all at the same time, without needing to run the program over and over again.

        I also added a counter to the Test file under each assert, so that if any AssertErrors are returned, it will add 1 to the counter. At the end of the file, if the counter is not 0, then it is clear that something has not been asserted correctly, which is nice to have since the main code will also display messages if some inputs are invalid.

        Evidence for Testing is Test_Job_Application_Tracker.py file.



    Libraries: (Lecture 7)

        Libraries allow for common functions to be accessed quickly, without the need to write the code for it in each new file.

        My code uses the CSV, re (regex), and datetime Libraries, which contain the functions I used in the program to interact (load, save, edit) with the CSV file, use Regex functions, and check the formatting of the date inputs.

        Evidence for Libraries: Lines 1 to 3.



    File I/O: (Workshop 8)

        File I/O is used to load and save data to other files, such as .txt or .CSV files. This allows for data to be stored and accessed even once the program restarts / closes, where storing data in variables, lists or dictionaries is volitle (will be deleted once the program restarts).

        Here, I used a CSV file to store the applications, which are loaded when the user selects to either load or save the data to the CSV file. The save funtion also saves the data to the CSV file, once it is compiled with the current data in the CSV file, hence the load when saving.

            When save function is chosen:
                Data is loaded from the CSV file,
                Data is assigned to the temp_applications list,
                Current (new) data is appended to the temp_applications list,
                The CSV file is cleared,
                These temp_applications list (which now holds all saved and unsaved data) is saved to the CSV file,
                The temp_applications list is cleared.

        Evidence for File I/O: Lines 143 to 179.



    Object-Oriented Programming (OOP): (Lecture 9)

        OOP principles are used as a "standard" for good programming practices, allowing for code to be more legible and generally be separated into different functions or operations, often using classes.

        For my program I separated the Applications_Format class and Operations class, which separates the manipulation of data (Formatting) and Data manipulation (Functions).

        I also kept related definitions together such as the Validation definitions, and the File I/O definitions. This allows for other programers to find issues with the program, enter the code without any prior knowledge of it, and identify where the relevant code is quickly, allowing for the issue(s) to be reolved quickly. Using the OOP practices also allow for any mistakes to be easily found and fixed while being generally easier to manage and overal easier to read.

        OOP is also useful, not only to identify erroneious code due to its location in the program, but also so shorten code where some functions are used multiple times, such as with the Validation definitions. These definitions are due to the OOP principles, as writing the code out to validate each input every time would cause the code to probably be 100 - 200 lines longer than if called in a definition several times.

        Evidence for OOP: Thoughout Job_Application_Tracker.py file.