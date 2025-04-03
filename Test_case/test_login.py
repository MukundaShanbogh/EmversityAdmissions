import time
from Page_object.admissionsPage import AdmissionsPage
from Utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By

class TestAdmissionsPage(BaseClass):
    # will login and assert the successful login.
    def test_login(self):
        try:
            number = "7975697137"
            global admission 
            admission =AdmissionsPage(self.driver)
            admission.get_number_field().send_keys(number)
            admission.get_SignIn_btn().click()
            otpField = admission.get_otp_field()
            for i in (otpField):
                i.send_keys('1')
            admission.get_submit_btn().click()
            choose_centre_text=admission.get_chooseCentreTXT().text
            assert choose_centre_text == "Please choose a","text did not match"

        except Exception as e:
            print(f"Test failed due to: {e}") 
            
    # this will be choosing the centre "Mukunda teaches testing centre".
    def test_choose_centre_Program(self):
        try:
            centre = admission.get_centre_name()
            for i in centre:
                centre_name = i.text
                if centre_name== "Mukunda teaches testing center":
                    i.click()
            time.sleep(2)
            programText = admission.get_choose_program().text
            assert programText == "Please choose a Program", "text did not match"
            admission.get_enroll_now().click()

        except Exception as e:
            print(f"Test failed due to :{e}")