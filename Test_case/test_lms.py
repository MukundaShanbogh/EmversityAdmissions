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
            
            try:
                if Test_lms_accessibility.lms_obj.get_access_denied_text().text == "Access Denied":
                    self.driver.execute_script("window.localStorage.setItem('allow-me', '1')")
                    self.driver.refresh()
                    # time.sleep(2)  # Wait for refresh
            except:
                pass  # Continue with the test if Access Denied is not present
            
                getstarted = Test_lms_accessibility.lms_obj.get_lets_start_text().text
                if getstarted == "Let's get started":
                    # Need to login
                    phone_number = "9618788418"
                    Test_lms_accessibility.lms_obj.get_mobile_num_input().send_keys(phone_number)
                    Test_lms_accessibility.tv_app_obj.get_start_session_btn().click()
                    
                    # Wait for OTP verification text
                    BaseClass.wait_for_element_visibility(self.driver, Test_lms_accessibility.lms_obj.get_verify_otp_text())
                    verify_otp_text = Test_lms_accessibility.lms_obj.get_verify_otp_text().text
                    assert verify_otp_text == f"We have sent an OTP to +91{phone_number}"
                    
                    # Enter OTP
                    otp_input = Test_lms_accessibility.lms_obj.get_otp_input()
                    for i in range(len(otp_input)):
                        otp_input[i].send_keys("1")
                    
                    # Click verify OTP
                    Test_lms_accessibility.lms_obj.get_verify_otp_btn().click()
                    performance_text = Test_lms_accessibility.lms_obj.get_performance_text()
                    BaseClass.wait_for_element_visibility(self.driver,performance_text)
                    performance_text = performance_text.text
                    assert performance_text == "Performance Overview" 
                
        except Exception as e:
            pytest.fail(f"LMS login failed: {str(e)}")


    @pytest.mark.smoke
    @pytest.mark.order(6)
    def test_student_quiz_Logic(self):
        try:
            # Switch to LMS tab for answering questions
            self.driver.switch_to.window(TestSchedule.lms_tab_handle)
            
            try:
                total_number_of_questions = Test_lms_accessibility.lms_obj.get_number_of_quiz_questions_text().text
                number = total_number_of_questions.strip().split("/")[-1].strip()
                total_questions = int(number)
                if total_questions <= 0:
                    pytest.fail("No quiz questions found")
                print(f"Total questions found: {total_number_of_questions}")
            except:
                pytest.fail("Could not get number of quiz questions")

            # Answer each question
            for question_num in range(total_questions):
                    answer_options = Test_lms_accessibility.lms_obj.get_quiz_options() 
                    # Select a random option
                    selected_option = random.choice(answer_options)
                    selected_option.click()
                    # Wait between answers
                    time.sleep(3)  
        except Exception as e:
            pytest.fail(f"Quiz answering failed: {str(e)}")
    
@pytest.mark.parametrize("setup", ["https://lmsdev.emversity.com"], indirect=True, scope="class")
class Test_lms_Dashboard(BaseClass):
    erplocators = None
    ticket_id = None

    def test_student_login(self):
        Test_lms_accessibility.lms_obj = lms_elements(self.driver)
        Test_lms_accessibility.tv_app_obj = tv_app(self.driver)
            
        try:
            if Test_lms_accessibility.lms_obj.get_access_denied_text().text == "Access Denied":
                self.driver.execute_script("window.localStorage.setItem('allow-me', '1')")
                self.driver.refresh()
        except:
            pass

        getstarted = Test_lms_accessibility.lms_obj.get_lets_start_text().text
        if getstarted == "Let's get started":
            # Need to login
            phone_number = "9618788418"
            Test_lms_accessibility.lms_obj.get_mobile_num_input().send_keys(phone_number)
            Test_lms_accessibility.tv_app_obj.get_start_session_btn().click()
            
            # Wait for OTP verification text
            BaseClass.wait_for_element_visibility(self.driver, Test_lms_accessibility.lms_obj.get_verify_otp_text())
            verify_otp_text = Test_lms_accessibility.lms_obj.get_verify_otp_text().text
            assert verify_otp_text == f"We have sent an OTP to +91{phone_number}"
            
            # Enter OTP
            otp_input = Test_lms_accessibility.lms_obj.get_otp_input()
            for i in range(len(otp_input)):
                otp_input[i].send_keys("1")
            
            # Click verify OTP
            Test_lms_accessibility.lms_obj.get_verify_otp_btn().click()
    
    # it will create the ticket and verify it on the ERP
    def test_help_support(self):
        Test_lms_Dashboard.erplocators = erp_elements(self.driver)
        actions = ActionChains(self.driver)
        # assertion to check the student is in the dashboard
        upcoming_text = Test_lms_accessibility.lms_obj.get_upcoming_events_text().text
        assert upcoming_text == 'Upcoming Events'

        # assertion to check the student is in the 'discribe issue page'
        Test_lms_accessibility.lms_obj.get_help_assistance_btn().click()
        discribe_issue_text = Test_lms_accessibility.lms_obj.get_discribe_issue_text().text
        assert discribe_issue_text == 'Describe your issue'

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
        self.driver.get("https://erpdev.emversity.com")
        domain = '.emversity.com'
        dev_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozLCJlbWFpbCI6Im11a3VuZGEuc3JAZW12ZXJzaXR5LmNvbSIsImlhdCI6MTc0ODM0MjM3MywiZXhwIjoxNzUwOTM0MzczfQ.O8Tca9srY8gSyqwTXbs486p1FVUvoYjmyzXLJjMRFJ8'
        self.driver.add_cookie({'name': 'login_token',
                                    'value': dev_token,
                                    'domain': domain,
                                    'path': '/'})
        self.driver.get("https://erpdev.emversity.com/dashboard")
        Test_lms_Dashboard.erplocators.get_support_btn().click()
        Test_lms_Dashboard.erplocators.get_ticketID_input().send_keys(Test_lms_Dashboard.ticket_id)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(.5)
        erp_ticket_ID = Test_lms_Dashboard.erplocators.get_erp_ticket_ID().text
        assert erp_ticket_ID == Test_lms_Dashboard.ticket_id ,"did not get the ticket-ID in erp"
    
    #  this method will update the status of the ticket to resolved and it will verify in the lms.
    def test_resolved_status(self):
        Test_lms_Dashboard.erplocators.get_resolved_status().click()
        time.sleep(.5)
        Test_lms_Dashboard.erplocators.get_confirm_btn().click()
        self.driver.get("https://lmsdev.emversity.com/home")
        Test_lms_accessibility.lms_obj.get_profile_section().click()
        raise_a_concern = Test_lms_accessibility.lms_obj.get_raise_concern()
        BaseClass.scroll_to_element(self.driver,raise_a_concern)
        raise_a_concern.click()
        old_tickets = Test_lms_accessibility.lms_obj.get_older_ticket_list()
        for i in old_tickets:
            old_Ticket_ID = i.text
            match = re.search(r'\d+', old_Ticket_ID)
            if match:
                if match.group() == Test_lms_Dashboard.ticket_id:
                    ticket_found = True
                    break  # No need to check further

        assert ticket_found, f"Ticket ID {Test_lms_Dashboard.ticket_id} not found in old tickets"



    def test_book_session(self):
        self.driver.get("https://lmsdev.emversity.com/home")
        time.sleep(1)
        Test_lms_accessibility.lms_obj.get_book_session_home_btn().click()
        select_teacher_page = Test_lms_accessibility.lms_obj.get_select_teacher_text().text
        assert select_teacher_page == 'Select a Teacher'
        try:
            Test_lms_accessibility.lms_obj.get_book_session_home_btn().click()
            tutor_name = Test_lms_accessibility.lms_obj.get_tutor_name_text().text
            print(f"the tutor name for the session booked is: {tutor_name}")
            time_slot = Test_lms_accessibility.lms_obj.get_time_slots()
            time_slot = random.choice(time_slot)
            time_slot.click()
            # check if the time is selected
            Test_lms_accessibility.lms_obj.get_book_session_home_btn().click()
            successful_msg = Test_lms_accessibility.lms_obj.get_session_booked_successful().text
            assert successful_msg == 'Session Booked Successfully!'

            Test_lms_accessibility.lms_obj.get_return_to_dashboard.click()

        except:
            pytest.fail("tutor has not been assigned to this centre or class")
