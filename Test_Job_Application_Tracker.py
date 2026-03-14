import Job_Application_Tracker

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

test_validate_company()