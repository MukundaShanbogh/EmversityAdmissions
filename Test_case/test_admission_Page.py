import time

import pytest
from Page_object.admission_page.admissionsPage import AdmissionsPage
from Utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class TestAdmissionsPage(BaseClass):
    # the code below will login and assert the successful login of a user .
    @pytest.mark.parametrize("setup", ["https://testdev.emversity.com/"], indirect=True)
    def test_login(self,setup):
        try:
            number = "7975697137" #this is the number of the user
            global admission 
            admission =AdmissionsPage(self.driver,setup) #create the Object for the Page object
            admission.get_number_field().send_keys(number) 
            admission.get_SignIn_btn().click()
            otpField = admission.get_otp_field()
            for i in (otpField):
                i.send_keys('1')
            admission.get_submit_btn().click()
            choose_centre_text=admission.get_chooseCentreTXT().text
            assert choose_centre_text == "Please choose a Centre","text did not match"

        except Exception as e:
            f"Test failed due to: {e}"
            
    # the code below will be choosing the centre "Mukunda teaches testing centre".
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
            f"Test failed due to :{e}"

    #  the code below will be filling the complete form 
    def test_Complete_form_fill(self):
        try:
            last_name = admission.get_last_name_input()
            last_name.send_keys(Keys.CONTROL+"a")
            last_name.send_keys(Keys.BACKSPACE)
            last_name.send_keys("testing")
            input_filed = admission.get_email_address_input()
            input_filed.send_keys(Keys.CONTROL + "a")
            input_filed.send_keys(Keys.BACKSPACE)
            input_filed.send_keys("testing@gmail.com")
            admission.get_DOB().click()
            admission.get_year_btn().click()
            admission.get_select_year().click()
            admission.get_ok_btn().click()
            admission.get_gender().click()
            admission.get_next_btn().click()
            admission.get_next_btn().click()
            admission.get_yes_btn().click()
            admission.get_next_btn().click()
            work_exp_text = admission.get_work_exp().text
            if work_exp_text == "Please specify your work experience":
                admission.get_years_select().click()
            wait = WebDriverWait(self.driver,10)
            relegion_text = wait.until(EC.visibility_of_element_located((admission.get_relegion)))
            
        except Exception as e:
            f"Test failed due to :{e}"