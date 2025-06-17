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
    whats_App_Num_text = (By.XPATH,"//*[contains(text(),'Is your Whatsapp')]")
    whats_App_Num_No = (By.XPATH,"//*[contains(text(),'Is your Whatsapp')]/parent::div/parent::div//h6[text()='No']")
    alternate_whats_app_num = (By.XPATH,"//*[text()='If Not, WhatsApp Number']")
    alternate_whats_app_num_input = (By.XPATH,"//*[@placeholder='Please enter whatsapp number']")
    whats_App_Num_Yes = (By.XPATH,"//*[contains(text(),'Is your Whatsapp')]/parent::div/parent::div//h6[text()='Yes']")
    Relegion_text = (By.XPATH,"//*[text()='Religion']")
    Relegion = (By.XPATH,"//*[@id='religion']//h6")
    caste_text = (By.XPATH,"//*[text()='Category']")
    caste = (By.XPATH,"//*[@id='caste']//h6")
    guardian_name_text = (By.XPATH, "//*[contains(text(),\"Guardian’s name\")]")
    guardian_name = (By.XPATH,"//*[@placeholder=\"Enter your Guardian’s name\"]")
    guardian_name_phone_num = (By.XPATH,"//*[@placeholder=\"Enter your Guardian’s Phone number\"]")
    
    relation_text = (By.XPATH,"//*[text()='Relation']")
    relation_option = (By.XPATH,"//*[text()='Father']")
    educational_qualification = (By.XPATH,"//*[text()='Graduate']")
    occupation = (By.XPATH,"//*[text()='Govt. Job']")
    annual_income = (By.XPATH,"//*[text()='Below 50,000']")
    assets = (By.XPATH,"//*[text()='4-Wheeler']")
    credit_card = (By.XPATH,"//*[@id='is_credit_card_used']//h6[text()='Yes']")
    bank_account = (By.XPATH,"//*[@id='is_family_used_bank_account']//h6[text()='Yes']")
    education = (By.XPATH,"//*[@id='is_own_fund']//*[text()='Self']")
    current_address = (By.XPATH,"//*[@placeholder='Enter your current address']")
    pin_code = (By.XPATH,"//*[@placeholder='Enter current address pincode']")
    town_city = (By.XPATH,"//*[@placeholder='Enter current address town/city']")
    same_current_address = (By.XPATH,"//*[@id='is_permanent_address_same_as_current_address']//*[text()='No']")
    permanent_address = (By.XPATH,"//*[@placeholder='Enter permanent address']")
    permanent_address_pincode = (By.XPATH,"//*[@placeholder='Enter permanent address pincode']")
    permanent_address_town_city = (By.XPATH,"//*[@placeholder='Enter permanent address town/city']")
    accommodation = (By.XPATH,"//*[text()='Rent']")
    hostel_facility = (By.XPATH,"//*[@id='hostel_need']//*[text()='Yes']")
    distance_to_centre = (By.XPATH,"//*[@placeholder='Enter how far you are from Emversity']")
    educational_qualification = (By.XPATH,"//*[text()='Bachelors']")
    YOP = (By.XPATH,"//*[@placeholder='Enter your 12th passing year']")
    percentage = (By.XPATH,"//*[@placeholder=' Enter 12th percentage']")
    board = (By.XPATH,"//*[text()='CBSE']")
    stream = (By.XPATH,"//*[text()='PCMB']")
    school_type = (By.XPATH,"//*[text()='Private']")
    school_name = (By.XPATH,"//*[@placeholder='Enter your school name']")
    school_address = (By.XPATH, "//*[@placeholder='Enter your school address']")
    school_pincode = (By.XPATH,"//*[@placeholder='Enter your  school pincode']")
    school_fee = (By.XPATH,"//*[@placeholder='Enter school fee (in ₹)']")
    entrance_exam = (By.XPATH,"//*[@id='is_appeared_entrance_exam']//h6[text()='Yes']")
    jee = (By.XPATH,"//*[text()='JEE']")
    neet = (By.XPATH,"//*[text()='NEET']")
    cuet = (By.XPATH,"//*[text()='CUET']")
    state_cet = (By.XPATH,"//*[text()='State-CET']")
    jee_rank_input = (By.XPATH,"//*[@placeholder='Please mention your Jee Rank']")
    neet_rank_input = (By.XPATH,"//*[@placeholder='Please mention your Neet Rank ']")
    cuet_rank_input = (By.XPATH,"//*[@placeholder='Please mention your CUET percentage']")
    state_cet_rank_input = (By.XPATH,"//*[@placeholder='Please mention CET Rank']")
    work_exp_yes = (By.XPATH,"//*[@id='self_work_experience_flag']//h6[text()='Yes']")

    work_exp_input = (By.XPATH,"//*[@placeholder='Enter your total year of work experience']")
    about_emversity = (By.XPATH,"//*[@id='heard_about_emversity_from']//h6[text()='Google Search']")
    course_considered = (By.XPATH,"//*[@placeholder='Enter interested course name']")
    college_considered = (By.XPATH,"//*[@placeholder='Enter interested college name ']")
    check_box = (By.XPATH,"//*[@type='checkbox']")


    ok_btn = (By.XPATH,"//*[text()='OK']")    


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
    
    def get_ok_btn(self):
        return self.driver.find_element(*AdmissionsPage.ok_btn)
    
    def get_yes_btn(self):
        return self.driver.find_element(*AdmissionsPage.yes_btn)
    
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
    
    def get_alternate_whats_app_num(self):
        return self.driver.find_element(*AdmissionsPage.alternate_whats_app_num)
    
    def get_alternate_whats_app_num_input(self):
        return self.driver.find_element(*AdmissionsPage.alternate_whats_app_num_input)
    
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
    
    def get_relation_text(self):
        return self.driver.find_element(*AdmissionsPage.relation_text)
    
    def get_relation_option(self):
        return self.driver.find_element(*AdmissionsPage.relation_option)
    
    def get_educational_qualification(self):
        return self.driver.find_element(*AdmissionsPage.educational_qualification)
    
    def get_occupation(self):
        return self.driver.find_element(*AdmissionsPage.occupation)
    
    def get_annual_income(self):
        return self.driver.find_element(*AdmissionsPage.annual_income)
    
    def get_assets(self):
        return self.driver.find_element(*AdmissionsPage.assets)
    
    def get_credit_card(self):
        return self.driver.find_element(*AdmissionsPage.credit_card)
    
    def get_bank_account(self):
        return self.driver.find_element(*AdmissionsPage.bank_account)
    
    def get_education(self):
        return self.driver.find_element(*AdmissionsPage.education)
    
    def get_current_address(self):
        return self.driver.find_element(*AdmissionsPage.current_address)
    
    def get_pin_code(self):
        return self.driver.find_element(*AdmissionsPage.pin_code)
    
    def get_town_city(self):
        return self.driver.find_element(*AdmissionsPage.town_city)
    
    def get_same_current_address(self):
        return self.driver.find_element(*AdmissionsPage.same_current_address)
    
    def get_permanent_address(self):
        return self.driver.find_element(*AdmissionsPage.permanent_address)
    
    def get_permanent_address_pincode(self):
        return self.driver.find_element(*AdmissionsPage.permanent_address_pincode)
    
    def get_permanent_address_town_city(self):
        return self.driver.find_element(*AdmissionsPage.permanent_address_town_city)
    
    def get_accommodation(self):
        return self.driver.find_element(*AdmissionsPage.accommodation)
    
    def get_hostel_facility(self):
        return self.driver.find_element(*AdmissionsPage.hostel_facility)
    
    def get_distance_to_centre(self):
        return self.driver.find_element(*AdmissionsPage.distance_to_centre)
    
    def get_educational_qualification(self):
        return self.driver.find_element(*AdmissionsPage.educational_qualification)
    
    def get_YOP(self):
        return self.driver.find_element(*AdmissionsPage.YOP)
    
    def get_percentage(self):
        return self.driver.find_element(*AdmissionsPage.percentage)
    
    def get_board(self):
        return self.driver.find_element(*AdmissionsPage.board)
    
    def get_stream(self):
        return self.driver.find_element(*AdmissionsPage.stream)
    
    def get_school_type(self):
        return self.driver.find_element(*AdmissionsPage.school_type)
    
    def get_school_name(self):
        return self.driver.find_element(*AdmissionsPage.school_name)
    
    def get_school_address(self):
        return self.driver.find_element(*AdmissionsPage.school_address)
    
    def get_school_pincode(self):
        return self.driver.find_element(*AdmissionsPage.school_pincode)
    
    def get_school_fee(self):
        return self.driver.find_element(*AdmissionsPage.school_fee)
    
    def get_entrance_exam(self):
        return self.driver.find_element(*AdmissionsPage.entrance_exam)
    
    def get_jee(self):
        return self.driver.find_element(*AdmissionsPage.jee)
    
    def get_neet(self):
        return self.driver.find_element(*AdmissionsPage.neet)
    
    def get_cuet(self):
        return self.driver.find_element(*AdmissionsPage.cuet)
    
    def get_state_cet(self):
        return self.driver.find_element(*AdmissionsPage.state_cet)
    
    def get_jee_rank_input(self):
        return self.driver.find_element(*AdmissionsPage.jee_rank_input)
    
    def get_neet_rank_input(self):
        return self.driver.find_element(*AdmissionsPage.neet_rank_input)
    
    def get_cuet_rank_input(self):
        return self.driver.find_element(*AdmissionsPage.cuet_rank_input)
    
    def get_state_cet_rank_input(self):
        return self.driver.find_element(*AdmissionsPage.state_cet_rank_input)
    
    def get_work_exp_yes(self):
        return self.driver.find_element(*AdmissionsPage.work_exp_yes)
    
    def get_work_exp_input(self):
        return self.driver.find_element(*AdmissionsPage.work_exp_input)
    
    def get_about_emversity(self):
        return self.driver.find_element(*AdmissionsPage.about_emversity)
    
    def get_course_considered(self):
        return self.driver.find_element(*AdmissionsPage.course_considered)
    
    def get_college_considered(self):
        return self.driver.find_element(*AdmissionsPage.college_considered)
    
    def get_check_box(self):
        return self.driver.find_elements(*AdmissionsPage.check_box)
    
    def get_ok_btn(self):
        return self.driver.find_element(*AdmissionsPage.ok_btn)
    
    
    
    

    

    
    
    
    
    
