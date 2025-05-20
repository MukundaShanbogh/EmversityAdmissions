from selenium.webdriver.common.by import By


class landingPage():
    def __init__(self,driver):
        self.driver = driver
    
    enquire_now_btn = (By.XPATH,"//*[text()='Enquire Now']")
    schedule_started_txt = (By.XPATH,"(//*[contains(text(),'Schedule')])[2]")
    students_name = (By.XPATH,"(//*[@placeholder='Student Name'])[1]")
    phone_number = (By.XPATH,"(//*[@name='phoneNumber'])[1]")
    send_otp_btn = (By.XPATH,"(//*[text()='Send OTP'])[1]")
    otp_input = (By.XPATH,"//*[contains(@id,'myInput')]")
    University_campus_input = (By.XPATH,"(//*[@name='campuse'])[1]")
    campus_select = (By.XPATH,"//*[text()='BVoc at Emversity Centre, Vizag']")
    current_location  = (By.XPATH,"(//*[@name='currentLocation'])[1]")
    preferred_language = (By.XPATH,"(//*[text()='Select Preferred Language'])[1]")
    language_select = (By.XPATH,"//*[@data-value='Kannada']")
    request_callback_btn = (By.XPATH,"(//*[text()='Request Callback'])[1]")

    # 2nd page form locators
    choose_preferred_course_text = (By.XPATH,"//*[text()='Choose Preferred Course']")
    preferred_course_select = (By.XPATH,"//div[@id='preferredCourse']//div[contains(text(),'A&OTT')]")
    YOP = (By.ID,"passingYear")
    YOP_select = (By.XPATH,"//*[text()='2024']")
    subject_select = (By.XPATH,"//*[text()='Science (Bio)']")
    Board_select = (By.XPATH,"//*[text()='CBSE']")
    gender_select = (By.XPATH,"//*[text()='Male']")
    percentage_select = (By.XPATH,"//*[text()='Above 85%']")
    family_income = (By.XPATH,"//*[text()='Less than 25,000 per month']")
    check_scholarship_btn = (By.XPATH,"//*[text()='Check Scholarship']")
    congrats_text = (By.XPATH,"//*[text()='Congratulations!']")


    def get_enquire_now_btn(self):
        return self.driver.find_element(*landingPage.enquire_now_btn)
    
    def get_schedule_started_txt(self):
        return self.driver.find_element(*landingPage.schedule_started_txt)
    
    def get_students_name(self):
        return self.driver.find_element(*landingPage.students_name)
    
    def get_phone_number(self):
        return self.driver.find_element(*landingPage.phone_number)
    
    def get_send_otp_btn(self):
        return self.driver.find_element(*landingPage.send_otp_btn)
    
    def get_otp_input(self):
        return self.driver.find_elements(*landingPage.otp_input)
    
    def get_University_campus_input(self):
        return self.driver.find_element(*landingPage.University_campus_input)
    
    def get_campus_select(self):
        return self.driver.find_element(*landingPage.campus_select)
    
    def get_current_location(self):
        return self.driver.find_element(*landingPage.current_location)
    
    def get_preferred_language(self):
        return self.driver.find_element(*landingPage.preferred_language)
    
    def get_language_select(self):
        return self.driver.find_element(*landingPage.language_select)
    
    def get_request_callback_btn(self):
        return self.driver.find_element(*landingPage.request_callback_btn)
    
    # 2nd page elements unpacking

    def get_choose_preferred_course_text(self):
        return self.driver.find_element(*landingPage.choose_preferred_course_text)
    
    def get_preferred_course_select(self):
        return self.driver.find_element(*landingPage.preferred_course_select)
    
    def get_YOP(self):
        return self.driver.find_element(*landingPage.YOP)
    
    def get_YOP_select(self):
        return self.driver.find_element(*landingPage.YOP_select)
    
    def get_subject_select(self):
        return self.driver.find_element(*landingPage.subject_select)
    
    def get_Board_select(self):
        return self.driver.find_element(*landingPage.Board_select)
    
    def get_gender_select(self):
        return self.driver.find_element(*landingPage.gender_select)
    
    def get_percentage_select(self):
        return self.driver.find_element(*landingPage.percentage_select)
    
    def get_family_income(self):
        return self.driver.find_element(*landingPage.family_income)
    
    def get_check_scholarship_btn(self):
        return self.driver.find_element(*landingPage.check_scholarship_btn)
    
    def get_congrats_text(self):
        return self.driver.find_element(*landingPage.congrats_text)