import Job_Application_Tracker
import time

operations = Job_Application_Tracker.Operations()

def test_validate_company(counter):

    try:    # Test valid company name
        assert operations.Validate_Company("Google") == True
    except AssertionError:
        print("TEST FAILED: Valid company name failed")
        counter += 1

    try:    # Test invalid company name
        assert operations.Validate_Company("") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    return counter

def test_validate_job_title(counter):

    try:    # Test valid job title
        assert operations.Validate_Job_Title("Mechanical Engineer (Best Engineer)") == True
    except AssertionError:
        print("TEST FAILED: Valid job title failed")
        counter += 1

    try:    # Test invalid job title
        assert operations.Validate_Job_Title("") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    return counter

def test_validate_application_date(counter):

    try:    # Test valid application date
        assert operations.Validate_Application_Date("01-05-2024") == True
    except AssertionError:
        print("TEST FAILED: Valid application date failed")
        counter += 1

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("") == False
    except AssertionError:
        print("FAILED: Should fail")
        counter += 1

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("2024-05-01") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("01/05/2024") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("yesterday") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application date - Not Leap Year
        assert operations.Validate_Application_Date("31-02-2029") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test valid application date - Leap Year
        assert operations.Validate_Application_Date("29-02-2024") == True
    except AssertionError:
        print("TEST FAILED: Valid application date failed")
        counter += 1

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("35-05-2024") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application date
        assert operations.Validate_Application_Date("123") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1
        
    try:    # Test invalid application date
        assert operations.Validate_Application_Date("12th March 2023") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    return counter

def test_validate_status(counter):

    try:    # Test valid application status
        assert operations.Validate_Status("Applied") == True
    except AssertionError:
        print("TEST FAILED: Valid status failed")
        counter += 1

    try:    # Test valid application status
        assert operations.Validate_Status("Interview") == True
    except AssertionError:
        print("TEST FAILED: Valid status failed")
        counter += 1
    
    try:    # Test valid application status
        assert operations.Validate_Status("Offer") == True
    except AssertionError:
        print("TEST FAILED: Valid status failed")
        counter += 1

    try:    # Test valid application status
        assert operations.Validate_Status("Rejected") == True
    except AssertionError:
        print("TEST FAILED: Valid status failed")
        counter += 1

    try:    # Test invalid application status
        assert operations.Validate_Status("applied") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application status
        assert operations.Validate_Status("interview") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application status
        assert operations.Validate_Status("offer") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application status
        assert operations.Validate_Status("rejected") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application status
        assert operations.Validate_Status("Pending") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application status
        assert operations.Validate_Status("Waiting") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application status
        assert operations.Validate_Status("Ignored") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application status
        assert operations.Validate_Status("OFFER!!!!!") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    return counter

def test_validate_email(counter):
    
    try:    # Test valid application email
        assert operations.Validate_Email("Name@Email.com") == True
    except AssertionError:
        print("TEST FAILED: Valid email failed")
        counter += 1

    try:    # Test invalid application email
        assert operations.Validate_Email("email@email") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application email
        assert operations.Validate_Email("Hello@@Email.com") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application email
        assert operations.Validate_Email("im getting really really bored at writing these examples. AGHHHH") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application email
        assert operations.Validate_Email("email") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application email
        assert operations.Validate_Email("n/a") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application email
        assert operations.Validate_Email("email@email.") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application email
        assert operations.Validate_Email("@email.com") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application email
        assert operations.Validate_Email("email.com") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    try:    # Test invalid application email
        assert operations.Validate_Email("@.") == False
    except AssertionError:
        print("TEST FAILED: Should fail")
        counter += 1

    return counter

def main():

    counter = 0

    wait = input("How much patience do you have? ")

    for i in range(int(wait)):
        print("Running tests...")
        time.sleep(1)
        i += 1

    print("If there are no error messages, all valid input tests have passed successfully.")
    print("If there are error messages, they either come from the python file being tested, or are specified above")

    test_validate_company(counter)
    test_validate_job_title(counter)
    test_validate_application_date(counter)
    test_validate_status(counter)
    test_validate_email(counter)

    print("")
    print("All tests completed.")

    if counter == 0:
        print("All tests passed successfully!")
    else:
        print(str(counter) + " Errors found. Fix 'em bucko!") # Can you tell I'm slowly losing it....
        print("If error message contains 'TEST FAILED', the test failed, other outputs are valid")

main()