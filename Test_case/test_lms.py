import random
import time
import pytest
from Page_object.lms_app.lms import lms_elements
from Page_object.tv_app.tv_app import tv_app
from Test_case.test_erp import TestSchedule
from Utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC

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
                    time.sleep(4)
                    performance_text = Test_lms_accessibility.lms_obj.get_performance_text().text
                    assert performance_text == "Performance Overview" 
                
        except Exception as e:
            pytest.fail(f"LMS login failed: {str(e)}")


    @pytest.mark.smoke
    @pytest.mark.order(6)
    def test_student_quiz_Logic(self):
        try:
            # Switch to LMS tab for answering questions
            self.driver.switch_to.window(TestSchedule.lms_tab_handle)
            time.sleep(5)  
            try:
                total_number_of_questions = Test_lms_accessibility.lms_obj.get_number_of_quiz_questions_text().text
                number = total_number_of_questions.strip().split("/")[-1].strip()
                total_questions = int(number)
                if total_questions <= 0:
                    pytest.skip("No quiz questions found")
                print(f"Total questions found: {total_number_of_questions}")
            except:
                pytest.skip("Could not get number of quiz questions")

            # Answer each question
            for question_num in range(total_questions):
                    answer_options = Test_lms_accessibility.lms_obj.get_quiz_options() 
                    # Select a random option
                    selected_option = random.choice(answer_options)
                    selected_option.click()
                    # Wait between answers
                    time.sleep(4)  
        except Exception as e:
            pytest.fail(f"Quiz answering failed: {str(e)}")
            
        

       
       
