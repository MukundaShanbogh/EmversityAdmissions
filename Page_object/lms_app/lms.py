from selenium.webdriver.common.by import By


class lms_elements:
    def __init__(self,driver):
        self.driver = driver


    lets_start_text = (By.XPATH,"//*[text()=\"Let's get started\"]")
    mobile_num_input = (By.XPATH,"//*[@placeholder='Mobile Number']")
    verify_otp_text = (By.XPATH,"//*[text()='We have sent an OTP to']")
    otp_input = (By.XPATH,"//*[contains(@aria-label,'Digit')]")
    verify_otp_btn = (By.XPATH,"//button//p[text()='Verify OTP']")
    resend_otp_btn = (By.XPATH,"//button//p[text()='Resend OTP']")
    upcoming_events_text = (By.XPATH,"//*[text()='Upcoming Events']")
    access_denied_text = (By.XPATH,"//*[text()='Access Denied']")
    performance_text = (By.XPATH,"//*[text()='Performance Overview']")
    quiz_options = (By.XPATH,"//*[@type='button']")
    number_of_quiz_questions_text = (By.XPATH,"(//p[text()])[3]")
    refer_student = (By.XPATH,"(//*[text()='Refer your friends to Emversity,'])")




    def get_lets_start_text(self):
        return self.driver.find_element(*lms_elements.lets_start_text)
    
    def get_mobile_num_input(self):
        return self.driver.find_element(*lms_elements.mobile_num_input)
    
    def get_verify_otp_text(self):
        return self.driver.find_element(*lms_elements.verify_otp_text)
    
    def get_otp_input(self):
        return self.driver.find_elements(*lms_elements.otp_input)
    
    def get_verify_otp_btn(self):
        return self.driver.find_element(*lms_elements.verify_otp_btn)
    
    def get_resend_otp_btn(self):
        return self.driver.find_element(*lms_elements.resend_otp_btn)
    
    def get_upcoming_events_text(self):
        return self.driver.find_element(*lms_elements.upcoming_events_text)
    
    def get_access_denied_text(self):
        return self.driver.find_element(*lms_elements.access_denied_text)
    
    def get_performance_text(self):
        return self.driver.find_element(*lms_elements.performance_text)
    
    def get_quiz_options(self):
        return self.driver.find_elements(*lms_elements.quiz_options)
    
    def get_number_of_quiz_questions_text(self):
        return self.driver.find_element(*lms_elements.number_of_quiz_questions_text)
    
    def get_refer_student(self):
        return self.driver.find_element(*lms_elements.refer_student)


