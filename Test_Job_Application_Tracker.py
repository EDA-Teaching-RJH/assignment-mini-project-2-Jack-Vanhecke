import Job_Application_Tracker
import time

operations = Job_Application_Tracker.Operations()

def test_validate_company():

    try:    # Test valid company name
        assert operations.Validate_Company("Google") == True
    except AssertionError:
        print("Valid company name failed")

    try:    # Test invalid company name
        assert operations.Validate_Company("") == False
    except AssertionError:
        print("Should fail")

def main():

    for i in range(5):
        print("Running tests...")
        time.sleep(1)
        i += 1

    time.sleep(3)
    test_validate_company()

main()