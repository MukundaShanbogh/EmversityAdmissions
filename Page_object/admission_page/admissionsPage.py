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
    last_name_input = (By.XPATH,"//*[@placeholder='Type your Last Name']")
    email_address_input=(By.XPATH,"//*[@placeholder='Type your Email']")
    DOB = (By.XPATH,"//*[text()='Date of Birth']/parent::div/parent::div//input")
    gender = (By.XPATH,"//*[text()='Male']")
    # next_btn = (By.XPATH,"//*[text()='Next']")
    year_btn = (By.XPATH,"(//*[@role='presentation'])[3]//button")
    select_year = (By.XPATH,"//*[text()='1997']")

    # new xpaths have to  unpack these.
    whats_App_Num_text = (By.XPATH,"//*[contains(text(),'Is your Whatsapp')]")
    whats_App_Num_No = (By.XPATH,"//*[contains(text(),'Is your Whatsapp')]/parent::div/parent::div//h6[text()='No']")
    whats_App_Num_Yes = (By.XPATH,"//*[contains(text(),'Is your Whatsapp')]/parent::div/parent::div//h6[text()='Yes']")
    Relegion_text = (By.XPATH,"//*[text()='Religion']")
    Relegion = (By.XPATH,"//*[@id='religion']//h6")
    caste_text = (By.XPATH,"//*[text()='Category']")
    caste = (By.XPATH,"//*[@id='caste']//h6")
    guardian_name_text = (By.XPATH, "//*[contains(text(),\"Guardian’s name\")]")
    guardian_name = (By.XPATH,"//*[@placeholder=\"Enter your Guardian’s name\"]")
    guardian_name_phone_num = (By.XPATH,"//*[@placeholder=\"Enter your Guardian’s Phone number\"]")
    
    relation_text = (By.XPATH,"//*[text()='Relation']")
    relation_option = (By.XPATH,"//h6[text()='Relation']/ancestor::div[2]/div[position()>1]//h6/text()")


    # ok_btn = (By.XPATH,"//*[text()='OK']")
    # yes_btn = (By.XPATH,"//*[text()='Yes']")
    # no_btn = (By.XPATH,"//*[text()='No']")
    # work_exp = (By.XPATH,"//*[text()='Please specify your work experience']")
    # years_select = (By.XPATH,"//*[text()='1-2 Years']")
    # relegion = (By.XPATH,"//*[text()='Please choose your religion']")


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
    
    def get_year_btn(self):
        return self.driver.find_element(*AdmissionsPage.year_btn)
    
    def get_select_year(self):
        return self.driver.find_element(*AdmissionsPage.select_year)
    
    # def get_ok_btn(self):
    #     return self.driver.find_element(*AdmissionsPage.ok_btn)
    
    # def get_yes_btn(self):
    #     return self.driver.find_element(*AdmissionsPage.yes_btn)
    
    # def get_no_btn(self):
    #     return self.driver.find_element(*AdmissionsPage.no_btn)
    
    # def get_work_exp(self):
    #     return self.driver.find_element(*AdmissionsPage.work_exp)
    
    # def get_years_select(self):
    #     return self.driver.find_element(*AdmissionsPage.years_select)
    
    # def get_relegion(self):
    #     return self.driver.find_element(*AdmissionsPage.relegion)

    def get_whats_App_Num_text(self):
        return self.driver.find_element(*AdmissionsPage.whats_App_Num_text)
    
    def get_whats_App_Num_No(self):
        return self.driver.find_element(*AdmissionsPage.whats_App_Num_No)
    
    def get_whats_App_Num_Yes(self):
        return self.driver.find_element(*AdmissionsPage.whats_App_Num_Yes)
    
    def get_Relegion_text(self):
        return self.driver.find_element(*AdmissionsPage.Relegion_text)
    
    def get_Relegion(self):
        return self.driver.find_element(*AdmissionsPage.Relegion)
    
    def get_caste_text(self):
        return self.driver.find_element(*AdmissionsPage.caste_text)
    
    def get_caste(self):
        return self.driver.find_element(*AdmissionsPage.caste)
    
    def get_guardian_name_text(self):
        return self.driver.find_element(*AdmissionsPage.guardian_name_text)
    
    def get_guardian_name(self):
        return self.driver.find_element(*AdmissionsPage.guardian_name)
    
    def get_guardian_name_phone_num(self):
        return self.driver.find_element(*AdmissionsPage.guardian_name_phone_num)
    

    
    
    

    

    
    
    
    
    
