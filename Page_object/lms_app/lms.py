from selenium.webdriver.common.by import By


class lms_elements:
    def __init__(self,driver):
        self.driver = driver


    login_text = (By.XPATH,"//*[text()='Log in']")
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
    help_assistance_btn = (By.XPATH,"//*[text()='Get Assistance']")
    discribe_issue_text = (By.XPATH,"//*[text()='Describe your issue']")
    issue_subject = (By.XPATH,"//*[@placeholder='Subject']")
    issue_details = (By.XPATH,"//*[@placeholder='Details']")
    issue_submit_btn = (By.XPATH,"//*[text()='Submit']")
    issue_thank_you_text = (By.XPATH,"//*[contains(text(),'Thank you')]")
    issue_ticket_ID = (By.XPATH,"//*[contains(text(),'Your Ticket ID')]")
    profile_section = (By.XPATH,"//*[text()='Profile']")
    raise_concern = (By.XPATH,"//*[text()='Raise a concern']")
    older_ticket_list = (By.XPATH,"(//*[text()='Older Tickets']/parent::div/child::div)[2]//div[contains(text(),'Ticket ID')]")
    book_session_home_btn = (By.XPATH,"//*[contains(text(),'Session')]")
    select_teacher_text = (By.XPATH,"//*[text()='Select a Teacher']")
    tutor_name_text = (By.XPATH,"(//p[text()])[1]")
    time_slots = (By.XPATH,"//*[text()='Time Slot']/parent::div/parent::div//button")
    session_booked_successful = (By.XPATH,"//*[text()='Session Booked Successfully!']")
    return_to_dashboard = (By.XPATH,"//*[text()='Return to Dashboard']")
    practice_btn = (By.XPATH,"//*[text()='Practice']")
    number_of_practice_quiz_subject = (By.XPATH,"//div[@size='6']") #(this will get the subjects on the outer page)
    subject_quiz = (By.XPATH,"//p[text()]/parent::div") #(this will get quiz with in the selected subject add this as elements)
    practice_quiz_options = (By.XPATH,"((//div[text()])/parent::div)[4]/child::div")

    number_of_quiz_questions = (By.XPATH,"(//span[text()])[2]")







    def get_login_text(self):
        return self.driver.find_element(*lms_elements.login_text)
    
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

    def get_help_assistance_btn(self):
        return self.driver.find_element(*lms_elements.help_assistance_btn)
    
    def get_discribe_issue_text(self):
        return self.driver.find_element(*lms_elements.discribe_issue_text)
    
    def get_issue_subject(self):
        return self.driver.find_element(*lms_elements.issue_subject)
    
    def get_issue_details(self):
        return self.driver.find_element(*lms_elements.issue_details)
    
    def get_issue_submit_btn(self):
        return self.driver.find_element(*lms_elements.issue_submit_btn)
    
    def get_issue_thank_you_text(self):
        return self.driver.find_element(*lms_elements.issue_thank_you_text)
    
    def get_issue_ticket_ID(self):
        return self.driver.find_element(*lms_elements.issue_ticket_ID)
    
    def get_profile_section(self):
        return self.driver.find_element(*lms_elements.profile_section)
    
    def get_raise_concern(self):
        return self.driver.find_element(*lms_elements.raise_concern)
    
    def get_older_ticket_list(self):
        return self.driver.find_elements(*lms_elements.older_ticket_list)
    
    def get_book_session_home_btn(self):
        return self.driver.find_element(*lms_elements.book_session_home_btn)
    
    def get_select_teacher_text(self):
        return self.driver.find_element(*lms_elements.select_teacher_text)
    
    def get_tutor_name_text(self):
        return self.driver.find_element(*lms_elements.tutor_name_text)
    
    def get_time_slots(self):
        return self.driver.find_elements(*lms_elements.time_slots)
    
    def get_session_booked_successful(self):
        return self.driver.find_element(*lms_elements.session_booked_successful)
    
    def get_return_to_dashboard(self):
        return self.driver.find_element(*lms_elements.return_to_dashboard)
    
    def get_practice_btn(self):
        return self.driver.find_element(*lms_elements.practice_btn)
    
    def get_number_of_practice_quiz_subject(self):
        return self.driver.find_elements(*lms_elements.number_of_practice_quiz_subject)
    
    def get_subject_quiz(self):
        return self.driver.find_elements(*lms_elements.subject_quiz)
    
    def get_practice_quiz_options(self):
        return self.driver.find_elements(*lms_elements.practice_quiz_options)
    
    def get_number_of_quiz_questions(self):
        return self.driver.find_element(*lms_elements.number_of_quiz_questions)

    


