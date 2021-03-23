class TestData:
    CHROME_EXECUTABLE_PATH = r"C:\mygit-hub_projects\ruttl_QA\driver\chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = r"C:\Users\aditya\PycharmProjects\pythonProject\driver\geckodriver.exe"

    BASEURL = "https://staging.ruttl.com/"
    ExpectedTitle = "ruttl"
    UserName = 'Adit'
    EmailAddress = 'dokaniaadi08+01@gmail.com'
    Password = 'QWERTY1'
    ProjectName = 'Test'
    WebsiteURL = "https://material-ui.com/"
    ForgetPasswordPageText = 'Forgot your password?'
    EmailMessage = 'A password reset email has been sent to your email address.'


"""command to run test cases"""
""" behave --no-capture Features/login.feature """
#behave --no-capture Features/forgetPassword.feature
