from selenium.webdriver.common.by import By


class tutor_elements:
    def __init__(self,driver):
        self.driver = driver
    

    tutor_phone_number = (By.XPATH,"//input[@placeholder='Type your number']")
    otp_input = (By.XPATH,"//*[contains(@aria-label,'Digit')]")
    continue_btn = (By.XPATH,"//button")
    off_class_students_txt = (By.XPATH,"//p[text()='Off-Class Students']")
    calander_btn = (By.XPATH,"//*[text()='Calendar']")
    start_class = (By.XPATH,"//*[text()='Start Class']")
    student_attendance_mark = (By.XPATH,"//*[text()='ldfhbd test']/parent::div/parent::div//div[text()='Not Marked']")

    def get_tutor_phone_number(self):
        return self.driver.find_element(*tutor_elements.tutor_phone_number)
    
    def get_otp_input(self):
        return self.driver.find_elements(*tutor_elements.otp_input)
    
    def get_continue_btn(self):
        return self.driver.find_element(*tutor_elements.continue_btn)
    
    def get_off_class_students_txt(self):
        return self.driver.find_element(*tutor_elements.off_class_students_txt)

    def get_calander_btn(self):
        return self.driver.find_element(*tutor_elements.calander_btn)
    
    def get_start_class(self):
        return self.driver.find_element(*tutor_elements.start_class)
    
    def get_student_attendance_mark(self):
        return self.driver.find_element(*tutor_elements.student_attendance_mark)