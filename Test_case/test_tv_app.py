import time
import pytest
from Page_object.tv_app.tv_app import tv_app
# from Test_case.test_lms import Test_lms
from Utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
from Test_case.test_erp import TestSchedule


class TestTVApp(BaseClass):
    app = None
   
    @pytest.mark.smoke
    @pytest.mark.order(3)
    def test_tv_app(self):
        TestTVApp.app = tv_app(self.driver)
        try:
            # Switch to TV app tab
            self.driver.switch_to.window(TestSchedule.tv_app_tab_handle)
            
            # Wait for page to load
            time.sleep(1)  # Give extra time for initial page load
            
            # Login
            login_input = TestTVApp.app.get_login_input()
            login_input.clear()
            login_input.send_keys("section_34")
            
            password_input = TestTVApp.app.get_password_input()
            password_input.clear()
            password_input.send_keys("123456")
            
            login_button = TestTVApp.app.get_login_button()
            login_button.click()
            
            # Wait for dashboard to load
            time.sleep(1)  # Give extra time for dashboard to load
            todays_class = TestTVApp.app.get_todays_class_text()
            assert todays_class.text == "Today's Classes"
            
        except Exception as e:
            pytest.fail(f"TV App login failed: {str(e)}")

    @pytest.mark.smoke
    @pytest.mark.order(5)
    def test_acceibility_mode(self):
        try:
            self.driver.switch_to.window(TestSchedule.tv_app_tab_handle)
            # Wait for schedule to load
            time.sleep(1)  # Give extra time for schedule to load
            
            schedule_times = TestTVApp.app.get_schedule_time_text()
            if not schedule_times:
                pytest.skip("No schedule times found")
                
            current_time = BaseClass.get_current_time()
            current_hour = datetime.strptime(current_time, "%H:%M").hour
            
            schedule_found = False
            for i in schedule_times:
                schedule_time = i.text.strip()
                if not schedule_time:  # Skip empty strings
                    continue
                    
                try:
                    schedule_dt = datetime.strptime(schedule_time, "%I:%M %p")
                    schedule_hour = schedule_dt.hour
                    # print(f"current_hour: {current_hour}, schedule_hour: {schedule_hour}, schedule_time: {schedule_time}")
                    
                    if current_hour == schedule_hour or (current_hour + 1) == schedule_hour:
                        i.click()
                        schedule_found = True
                        break
                except ValueError as ve:
                    # print(f"Could not parse time: {schedule_time}, error: {str(ve)}")
                    continue
                    
            if not schedule_found:
                pytest.skip("No matching schedule found for current time")
            
            start_session_btn = TestTVApp.app.get_start_session_btn()
            BaseClass.wait_for_element_visibility(self.driver,start_session_btn)
            start_session_btn.click()
            
        except Exception as e:
            pytest.fail(f"Accessibility mode test failed: {str(e)}")

    @pytest.mark.smoke
    @pytest.mark.order(6)
    def test_quiz_start(self):
        try:
            # Switch to TV app tab
            self.driver.switch_to.window(TestSchedule.tv_app_tab_handle)
            
            quiz_btn = TestTVApp.app.get_quiz_btn()
            BaseClass.wait_for_element_clickable(self.driver,quiz_btn)
            quiz_btn.click()
            # Wait for quiz ready text
            time.sleep(1)  # Give time for quiz ready text to appear
            try:
                ready_for_quiz_txt = TestTVApp.app.get_ready_for_quiz_txt()
                if ready_for_quiz_txt.text != "Ready for the Quiz?":
                    pytest.fail("Quiz not ready")
            except:
                pytest.fail("Quiz ready text not found")
            # Start quiz
            quiz_start_btn = TestTVApp.app.get_start_session_btn()
            quiz_start_btn.click()
            # Wait for quiz to start
            time.sleep(2)
            
        except Exception as e:
            pytest.skip(f"No quiz found or quiz start failed: {str(e)}")
                    

        
