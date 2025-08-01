from selenium.webdriver.common.by import By



class tv_app:
    def __init__(self,driver):
        self.driver = driver
    

    login_input = (By.XPATH,"//*[@placeholder='Login Id']")
    password_input = (By.XPATH,"//*[@placeholder='Password']")
    # login_input = (By.CSS_SELECTOR, "[placeholder='Login Id']")
    # password_input = (By.CSS_SELECTOR, "[placeholder='Password']")
    login_button = (By.XPATH,"//button[text()='Login']")
    todays_class_text = (By.XPATH,"//*[text()=\"Today's Classes\"]")
    todays_schedule = (By.XPATH,"//div[text()]/parent::div")
    schedule_time_text = (By.XPATH,"//div[text()]/parent::div//div[text()]")
    start_session_btn = (By.XPATH,"//button")
    quiz_btn = (By.XPATH,"//div[text()='Next Topic' or  text()='Quiz']")
    ready_for_quiz_txt = (By.XPATH,"//*[text()='Ready for the Quiz?']")
    


    def get_login_input(self):
        return self.driver.find_element(*tv_app.login_input)

    def get_password_input(self):
        return self.driver.find_element(*tv_app.password_input)

    def get_login_button(self):
        return self.driver.find_element(*tv_app.login_button)

    def get_todays_class_text(self):
        return self.driver.find_element(*tv_app.todays_class_text)

    def get_todays_schedule(self):
        return self.driver.find_element(*tv_app.todays_schedule)

    def get_schedule_time_text(self):
        return self.driver.find_elements(*tv_app.schedule_time_text)
    
    def get_start_session_btn(self):
        return self.driver.find_element(*tv_app.start_session_btn)
    
    def get_quiz_btn(self):
        return self.driver.find_element(*tv_app.quiz_btn)
    
    def get_ready_for_quiz_txt(self):
        return self.driver.find_element(*tv_app.ready_for_quiz_txt)
