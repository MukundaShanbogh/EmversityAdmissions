import random
import re
import time
import pytest
from Page_object.erp_app.erp_app import erp_elements
from Page_object.lms_app.lms import lms_elements
from Page_object.tv_app.tv_app import tv_app
from Test_case.test_erp import TestSchedule
from Utilities.BaseClass import BaseClass
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException




@pytest.mark.usefixtures("setup")
class Test_lms_accessibility(BaseClass):
    lms_obj = None
    tv_app_obj = None

    @pytest.mark.smoke
    @pytest.mark.order(4)
    def test_lms_login(self):
        try:
            # Switch to LMS tab
            self.driver.switch_to.window(TestSchedule.lms_tab_handle)
            Test_lms_accessibility.lms_obj = lms_elements(self.driver)
            Test_lms_accessibility.tv_app_obj = tv_app(self.driver)
            
            getstarted = Test_lms_accessibility.lms_obj.get_login_text().text
            if getstarted == "Log in":
                # Need to login
                phone_number = "9930769654"
                Test_lms_accessibility.lms_obj.get_mobile_num_input().send_keys(phone_number)
                Test_lms_accessibility.tv_app_obj.get_start_session_btn().click()
                
                # Wait for OTP verification text
                # BaseClass.wait_for_element_visibility(self.driver, Test_lms_accessibility.lms_obj.get_verify_otp_text())
                # verify_otp_text = Test_lms_accessibility.lms_obj.get_verify_otp_text().text
                # assert verify_otp_text == f"We have sent an OTP to +91{phone_number}"
                time.sleep(2)
                # Enter OTP
                otp_input = Test_lms_accessibility.lms_obj.get_otp_input()
                for i in range(len(otp_input)):
                    otp_input[i].send_keys("1")
                
                # Click verify OTP
                Test_lms_accessibility.lms_obj.get_verify_otp_btn().click()
        except Exception as e:
            raise


    @pytest.mark.smoke
    @pytest.mark.order(7)
    def test_student_quiz_Logic(self):
        try:
            # Switch to LMS tab for answering questions
            self.driver.switch_to.window(TestSchedule.lms_tab_handle)
            while True:
                try:    
                    # Check if leaderboard is visible
                    leaderboard = Test_lms_accessibility.lms_obj.get_quiz_leader_board()    
                    print("Leaderboard found, ending quiz.")
                    self.driver.switch_to.window(TestSchedule.tv_app_tab_handle)
                    Test_lms_accessibility.tv_app_obj.get_start_session_btn().click()
                    self.driver.switch_to.window(TestSchedule.lms_tab_handle)
                    break
                except NoSuchElementException:
                    # No leaderboard yet, keep answering
                    options = Test_lms_accessibility.lms_obj.get_quiz_options()
                    random_options = random.choice(options)   
                    random_options.click() 

        except Exception as e:
           raise
    

class Test_lms_Dashboard(BaseClass):
    erplocators = None
    ticket_id = None
    @pytest.mark.smoke
    @pytest.mark.order(8)
    def test_help_support(self):
        time.sleep(2)
        Test_lms_Dashboard.erplocators = erp_elements(self.driver)
        actions = ActionChains(self.driver)
        # assertion to check the student is in the 'discribe issue page'
        Test_lms_accessibility.lms_obj.get_help_assistance_btn().click()
        Test_lms_accessibility.lms_obj.get_new_ticket_btn().click()
       
        # enter the issue subject
        Test_lms_accessibility.lms_obj.get_issue_subject().send_keys('Testing the feature')
        Test_lms_accessibility.lms_obj.get_issue_details().send_keys('Testing the feature')
        Test_lms_accessibility.lms_obj.get_issue_submit_btn().click()
        # assert the thank you page
        thank_you_text = Test_lms_accessibility.lms_obj.get_issue_thank_you_text().text
        assert thank_you_text == 'Thank you for raising your concern.'
        # get the ID of the ticket 
        Test_lms_Dashboard.ticket_id = Test_lms_accessibility.lms_obj.get_issue_ticket_ID().text
        Test_lms_Dashboard.ticket_id = re.search(r'\d+', Test_lms_Dashboard.ticket_id).group()
        self.driver.switch_to.window(TestSchedule.erp_tab_handle)
        Test_lms_Dashboard.erplocators.get_support_btn().click()
        Test_lms_Dashboard.erplocators.get_ticketID_input().send_keys(Test_lms_Dashboard.ticket_id)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(.5)
        erp_ticket_ID = Test_lms_Dashboard.erplocators.get_erp_ticket_ID().text
        assert erp_ticket_ID == Test_lms_Dashboard.ticket_id ,"did not get the ticket-ID in erp"
        
    
    #  this method will update the status of the ticket to resolved and it will verify in the lms.
    @pytest.mark.smoke
    @pytest.mark.order(9)
    def test_resolved_status(self):
        try:
            Test_lms_Dashboard.erplocators.get_resolved_status().click()
            time.sleep(1)
            Test_lms_Dashboard.erplocators.get_confirm_btn().click()
            self.driver.switch_to.window(TestSchedule.lms_tab_handle)
            Test_lms_accessibility.lms_obj.get_go_back_btn().click()
            Test_lms_accessibility.lms_obj.get_return_to_dashboard().click()
            # ADD the assertion step here
        except Exception as e :   
            raise e

    # this method will book one on one meeting with the mentor
    @pytest.mark.smoke
    @pytest.mark.order(10)
    def test_book_session(self):
        # self.driver.switch_to.window(TestSchedule.lms_tab_handle)
        time.sleep(1)
        Test_lms_accessibility.lms_obj.get_book_session_home_btn().click()
        # select_teacher_page = Test_lms_accessibility.lms_obj.get_select_teacher_text().text
        try:
            # Test_lms_accessibility.lms_obj.get_book_session_home_btn().click()
            tutor_name_elements  = Test_lms_accessibility.lms_obj.get_tutor_name_text()
            for tutor_element in tutor_name_elements:
                tutor_name = tutor_element.text
                if tutor_name == "Dr Nikhil New":
                    print(f"the tutor name for the session booked is: {tutor_name}")
                    time_slot = Test_lms_accessibility.lms_obj.get_time_slots()
                    time_slot = random.choice(time_slot)
                    time_slot.click()
                    # check if the time is selected
                    Test_lms_accessibility.lms_obj.get_book_session_home_btn().click()
                    successful_msg = Test_lms_accessibility.lms_obj.get_session_booked_successful().text
                    assert successful_msg == 'Session Booked Successfully!'
                    Test_lms_accessibility.lms_obj.get_return_to_dashboard().click()

        except:
            pytest.fail("tutor has not been assigned to this centre or class")
            raise


    @pytest.mark.smoke
    @pytest.mark.order(11)
    def test_practice_quiz(self):
        Test_lms_accessibility.lms_obj.get_practice_btn().click()

        inner_page_quiz = Test_lms_accessibility.lms_obj.get_subject_quiz()
        random_quiz = random.choice(inner_page_quiz)
        random_quiz.click()

        quiz_questions = Test_lms_accessibility.lms_obj.get_number_of_quiz_questions().text
        print(f"the number of quiz questions is: {quiz_questions}")
        quiz_questions = quiz_questions.strip().split("/")[-1].strip()
        quiz_questions = int(quiz_questions)

        for i in range(quiz_questions):
            quiz_options = Test_lms_accessibility.lms_obj.get_practice_quiz_options()
            random_option = random.choice(quiz_options)
            random_option.click()
            time.sleep(3)
        Test_lms_accessibility.lms_obj.get_return_to_dashboard().click()

 
