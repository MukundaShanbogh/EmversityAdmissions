from selenium.webdriver.common.by import By

class AdmissionsPage:
    def __init__(self,driver):
        self.driver = driver
    
    number_text_field = (By.ID, "outlined-basic")
    signIn_btn = (By.XPATH,"//*[text()='Sign in']")
    otp_field = (By.XPATH,"//*[@type='tel']")
    submit_btn = (By.XPATH,"//*[text() = 'Submit']")
    choose_Centre = (By.XPATH,"//*[text() = 'Please choose a']")
    centre_name = (By.XPATH,"//div[contains(@class,'MuiGrid-root MuiGrid-item')]//p[text()]")
    choose_program = (By.XPATH,"//h3")
    enroll_now = (By.XPATH,"(//*[text()='Enroll now'])[1]")
    last_name_input = (By.XPATH,"//*[text()='Last Name']/parent::div//input")
    email_address_input=(By.XPATH,"//*[text()='Email Address']/parent::div//input")
    DOB = (By.XPATH,"//*[text()='Date of Birth']/parent::div/parent::div//input")
    gender = (By.XPATH,"//*[text()='Male']")
    next_btn = (By.XPATH,"//*[text()='Next']")


    def get_number_field(self):
        return self.driver.find_element(*AdmissionsPage.number_text_field)
    
    def get_SignIn_btn(self):
        return self.driver.find_element(*AdmissionsPage.signIn_btn)
    
    def get_otp_field(self):
        return self.driver.find_elements(*AdmissionsPage.otp_field)
    
    def get_submit_btn(self):
        return self.driver.find_element(*AdmissionsPage.submit_btn)
    
    def get_chooseCentreTXT(self):
        return self.driver.find_element(*AdmissionsPage.choose_Centre)
    
    def get_centre_name(self):
        return self.driver.find_elements(*AdmissionsPage.centre_name)
    
    def get_choose_program(self):
        return self.driver.find_element(*AdmissionsPage.choose_program)
    
    def get_enroll_now(self):
        return self.driver.find_element(*AdmissionsPage.enroll_now)
    
    def get_last_name_input(self):
        return self.driver.find_element(*AdmissionsPage.last_name_input)
    
    def get_email_address_input(self):
        return self.driver.find_element(*AdmissionsPage.email_address_input)
    
    def get_DOB(self):
        return self.driver.find_element(*AdmissionsPage.DOB)
    
    def get_gender(self):
        return self.driver.find_element(*AdmissionsPage.gender)
    
    def get_next_btn(self):
        return self.driver.find_element (*AdmissionsPage.next_btn)
    
    

    
    
    
    
    
