import Job_Application_Tracker
import time

operations = Job_Application_Tracker.Operations()

def test_validate_company():

    try:    # Test valid company name
        assert operations.Validate_Company("Google") == True
    except AssertionError:
        print("TEST FAILED: Valid company name failed")

    try:    # Test invalid company name
        assert operations.Validate_Company("") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

def test_validate_job_title():

    try:    # Test valid job title
        assert operations.Validate_Job_Title("Mechanical Engineer (Best Engineer)") == True
    except AssertionError:
        print("TEST FAILED: Valid job title failed")

    try:    # Test invalid job title
        assert operations.Validate_Job_Title("") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

def test_validate_application_date():

    try:    # Test valid application date
        assert operations.Validate_Application_Date("01-05-2024") == True
    except AssertionError:
        print("TEST FAILED: Valid application date failed")

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("") == False
    except AssertionError:
        print("FAILED: Should fail")

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("2024-05-01") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("01/05/2024") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("yesterday") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("31-02-2029") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("29-02-2024") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("35-05-2024") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("123") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        
    try:    # Test invalid application date
        assert operations.Validate_Application_Date("12th March 2023") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

def test_validate_status():

    try:    # Test valid application status
        assert operations.Validate_Status("Applied") == True
    except AssertionError:
        print("TEST FAILED: Valid status failed")

    try:    # Test valid application status
        assert operations.Validate_Status("Interview") == True
    except AssertionError:
        print("TEST FAILED: Valid status failed")
    
    try:    # Test valid application status
        assert operations.Validate_Status("Offer") == True
    except AssertionError:
        print("TEST FAILED: Valid status failed")

    try:    # Test valid application status
        assert operations.Validate_Status("Rejected") == True
    except AssertionError:
        print("TEST FAILED: Valid status failed")

    try:    # Test invalid application status
        assert operations.Validate_Status("applied") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application status
        assert operations.Validate_Status("interview") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application status
        assert operations.Validate_Status("offer") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application status
        assert operations.Validate_Status("rejected") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application status
        assert operations.Validate_Status("Pending") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application status
        assert operations.Validate_Status("Waiting") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application status
        assert operations.Validate_Status("Ignored") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application status
        assert operations.Validate_Status("OFFER!!!!!") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

def test_validate_email():
    
    try:    # Test valid application email
        assert operations.Validate_Email("Name@Email.com") == True
    except AssertionError:
        print("TEST FAILED: Valid email failed")

    try:    # Test invalid application email
        assert operations.Validate_Email("email@email") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application email
        assert operations.Validate_Email("Hello@@Email.com") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application email
        assert operations.Validate_Email("im getting really really bored at writing these examples. AGHHHH") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application email
        assert operations.Validate_Email("email") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application email
        assert operations.Validate_Email("n/a") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application email
        assert operations.Validate_Email("email@email.") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application email
        assert operations.Validate_Email("@email.com") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application email
        assert operations.Validate_Email("email.com") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

    try:    # Test invalid application email
        assert operations.Validate_Email("@.") == False
    except AssertionError:
        print("TEST FAILED: Should fail")

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

    print("")
    print("")
    print("All tests completed.")
    print("If error message contains 'TEST FAILED', the test failed, other outputs are valid")

main()