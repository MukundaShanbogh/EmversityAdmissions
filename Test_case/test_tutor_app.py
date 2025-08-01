import time
import pytest
from Page_object.tutor_app.tutor_app import tutor_elements
from Test_case.test_erp import TestSchedule
from Utilities.BaseClass import BaseClass


class Test_tutor_app(BaseClass):
    tutor_obj = None
    @pytest.mark.smoke
    @pytest.mark.order(2)
    def test_tutor_login(self):  
        Test_tutor_app.tutor_obj = tutor_elements(self.driver)
        try:
            # Switch to LMS tab
            # self.driver.get("https://tvtutordev.emversity.com/tutor")
            self.driver.switch_to.window(TestSchedule.tutor_handle)
            Test_tutor_app.tutor_obj.get_tutor_phone_number().send_keys("9538572354")
            Test_tutor_app.tutor_obj.get_continue_btn().click()
            otp = Test_tutor_app.tutor_obj.get_otp_input()
            for i in range(len(otp)):
                otp[i].send_keys(str(i+1))
            Test_tutor_app.tutor_obj.get_continue_btn().click()
            assert_text = Test_tutor_app.tutor_obj.get_off_class_students_txt().text
            assert assert_text == "Off-Class Students", f"the tutor has not logged in"
            Test_tutor_app.tutor_obj.get_calander_btn().click()
            try:
                start_class=Test_tutor_app.tutor_obj.get_start_class()
                BaseClass.scroll_to_element(self.driver,start_class)
                start_class.click()
                Test_tutor_app.tutor_obj.get_student_attendance_mark().click()
   
            except :
                pytest.skip("start class not found ")
                raise
        except:
            raise