import Job_Application_Tracker
import time

operations = Job_Application_Tracker.Operations()

def test_validate_company():

    try:    # Test valid company name
        assert operations.Validate_Company("Google") == True
    except AssertionError:
        print("FAILED: Valid company name failed")

    try:    # Test invalid company name
        assert operations.Validate_Company("") == False
    except AssertionError:
        print("FAILED: Should fail")

def test_validate_job_title():

    try:    # Test valid job title
        assert operations.Validate_Job_Title("Mechanical Engineer (Best Engineer)") == True
    except AssertionError:
        print("FAILED: Valid job title failed")

    try:    # Test invalid job title
        assert operations.Validate_Job_Title("") == False
    except AssertionError:
        print("FAILED: Should fail")

def test_validate_application_date():

    print("")

def test_validate_status():

    print("")

def test_validate_email():

    print("")

def main():

    for i in range(5):
        print("Running tests...")
        time.sleep(1)
        i += 1

    time.sleep(3)

    print("If there are no error messages, all valid input tests have passed successfully.")
    print("If there are error messages, they either come from the python file being tested, or are specified above")

    test_validate_company()
    test_validate_job_title()
    test_validate_application_date()
    test_validate_status()
    test_validate_email()

main()