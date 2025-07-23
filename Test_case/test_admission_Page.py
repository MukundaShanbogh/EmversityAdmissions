import time
import pytest
from Page_object.admission_page.admissionsPage import AdmissionsPage
from Utilities.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from API_lms.test_lead_creat import lead_create


@pytest.mark.parametrize("setup", ["https://testdev.emversity.com/"], indirect=True, scope="class")
class TestAdmissionsPage(BaseClass):
    
    def scroll_into_view(self, element):
        """Scroll element into view using JavaScript executor"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)  # Small wait to ensure scroll completes

    # the code below will login and assert the successful login of a user .
    # @pytest.mark.parametrize("setup", ["https://testdev.emversity.com/"], indirect=True)
    def test_login(self):
        try:
            number = lead_create.generate_random_phone_number()
            print(number)
            global admission 
            admission =AdmissionsPage(self.driver) #create the Object for the Page object
            admission.get_number_field().send_keys(number) 
            admission.get_SignIn_btn().click()
            otpField = admission.get_otp_field()
            for i in (otpField):
                i.send_keys('1')
            admission.get_submit_btn().click()
            choose_centre_text=admission.get_chooseCentreTXT().text
            assert choose_centre_text == "Please choose a Centre","text did not match"

        except Exception as e:
            pytest.fail(f"Test failed due to: {e}")
            
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
            pytest.fail(f"Test failed due to :{e}") 

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
            
            # Scroll and click DOB
            dob_element = admission.get_DOB()
            self.scroll_into_view(dob_element)
            dob_element.click()
            
            # Scroll and click year button
            year_btn = admission.get_year_btn()
            self.scroll_into_view(year_btn)
            year_btn.click()
            
            # Scroll and click select year
            select_year = admission.get_select_year()
            self.scroll_into_view(select_year)
            select_year.click()
            
            # Scroll and click OK button
            ok_btn = admission.get_ok_btn()
            self.scroll_into_view(ok_btn)
            ok_btn.click()
            
            # Scroll and click gender
            gender = admission.get_gender()
            self.scroll_into_view(gender)
            gender.click()
            
            # Scroll and click WhatsApp number
            whatsapp_no = admission.get_whats_App_Num_No()
            self.scroll_into_view(whatsapp_no)
            whatsapp_no.click()
            
            admission.get_alternate_whats_app_num_input().send_keys("7973697173")
            
            # Scroll and click religion text
            religion_text = admission.get_Relegion_text()
            self.scroll_into_view(religion_text)
            
            # Scroll and click religion
            religion = admission.get_Relegion()
            religion.click()
            
            # Scroll and click caste text
            caste_text = admission.get_caste_text()
            self.scroll_into_view(caste_text)
            
            # Scroll and click caste
            caste = admission.get_caste()
            caste.click()
            
            # Scroll and click guardian name text
            guardian_text = admission.get_guardian_name_text()
            self.scroll_into_view(guardian_text)
            guardian_text.click()
            
            admission.get_guardian_name().send_keys(Keys.CONTROL+"a")
            admission.get_guardian_name().send_keys(Keys.BACKSPACE)
            admission.get_guardian_name().send_keys("testing")
            admission.get_guardian_name_phone_num().send_keys(Keys.CONTROL+"a")
            admission.get_guardian_name_phone_num().send_keys(Keys.BACKSPACE)
            admission.get_guardian_name_phone_num().send_keys("7975577173")
            admission.get_relation_option().click()
            admission.get_educational_qualification().click()
            admission.get_YOP().send_keys("2016")
            admission.get_percentage().send_keys(Keys.CONTROL+"a")
            admission.get_percentage().send_keys(Keys.BACKSPACE)
            admission.get_percentage().send_keys("90")
            admission.get_board().click()
            admission.get_stream().click()
            admission.get_occupation().click()
            admission.get_annual_income().click()
            admission.get_assets().click()
            admission.get_credit_card().click()
            admission.get_bank_account().click()
            admission.get_education().click()
            admission.get_current_address().send_keys(Keys.CONTROL+"a")
            admission.get_current_address().send_keys(Keys.BACKSPACE)
            admission.get_current_address().send_keys("indranagar bengaluru")
            admission.get_pin_code().send_keys(Keys.CONTROL+"a")
            admission.get_pin_code().send_keys(Keys.BACKSPACE)
            admission.get_pin_code().send_keys("560001")
            admission.get_town_city().send_keys(Keys.CONTROL+"a")
            admission.get_town_city().send_keys(Keys.BACKSPACE)
            admission.get_town_city().send_keys("bengaluru")
            admission.get_same_current_address().click()
            admission.get_permanent_address().send_keys(Keys.CONTROL+"a")
            admission.get_permanent_address().send_keys(Keys.BACKSPACE)
            admission.get_permanent_address().send_keys("indranagar bengaluru")
            admission.get_permanent_address_pincode().send_keys(Keys.CONTROL+"a")
            admission.get_permanent_address_pincode().send_keys(Keys.BACKSPACE)
            admission.get_permanent_address_pincode().send_keys("560001")
            admission.get_permanent_address_town_city().send_keys(Keys.CONTROL+"a")
            admission.get_permanent_address_town_city().send_keys(Keys.BACKSPACE)
            admission.get_permanent_address_town_city().send_keys("bengaluru")
            admission.get_accommodation().click()
            admission.get_hostel_facility().click()
            admission.get_distance_to_centre().send_keys(Keys.CONTROL+"a")
            admission.get_distance_to_centre().send_keys(Keys.BACKSPACE)
            admission.get_distance_to_centre().send_keys("10")
            admission.get_educational_qualification().click()
            admission.get_school_type().click()
            admission.get_school_name().send_keys(Keys.CONTROL+"a")
            admission.get_school_name().send_keys(Keys.BACKSPACE)
            admission.get_school_name().send_keys("emversity")
            admission.get_school_address().send_keys(Keys.CONTROL+"a")
            admission.get_school_address().send_keys(Keys.BACKSPACE)
            admission.get_school_address().send_keys("indranagar bengaluru")
            admission.get_school_pincode().send_keys(Keys.CONTROL+"a")
            admission.get_school_pincode().send_keys(Keys.BACKSPACE)
            admission.get_school_pincode().send_keys("560001")
            admission.get_school_fee().send_keys(Keys.CONTROL+"a")
            admission.get_school_fee().send_keys(Keys.BACKSPACE)
            admission.get_school_fee().send_keys("10000")
            admission.get_entrance_exam().click()
            admission.get_jee().click()
            admission.get_neet().click()
            admission.get_cuet().click()
            admission.get_state_cet().click()
           
            
            admission.get_jee_rank_input().send_keys(Keys.CONTROL+"a")
            admission.get_jee_rank_input().send_keys(Keys.BACKSPACE)
            admission.get_jee_rank_input().send_keys("100")
            admission.get_neet_rank_input().send_keys(Keys.CONTROL+"a")
            admission.get_neet_rank_input().send_keys(Keys.BACKSPACE)
            admission.get_neet_rank_input().send_keys("100")
            admission.get_cuet_rank_input().send_keys(Keys.CONTROL+"a")
            admission.get_cuet_rank_input().send_keys(Keys.BACKSPACE)
            admission.get_cuet_rank_input().send_keys("100")
            admission.get_state_cet_rank_input().send_keys(Keys.CONTROL+"a")
            admission.get_state_cet_rank_input().send_keys(Keys.BACKSPACE)
            admission.get_state_cet_rank_input().send_keys("100")
            admission.get_work_exp_yes().click()
            admission.get_work_exp_input().send_keys(Keys.CONTROL+"a")
            admission.get_work_exp_input().send_keys(Keys.BACKSPACE)
            admission.get_work_exp_input().send_keys("5")
            admission.get_about_emversity().click()
            admission.get_course_considered().send_keys(Keys.CONTROL+"a")
            admission.get_course_considered().send_keys(Keys.BACKSPACE)
            admission.get_course_considered().send_keys("BRIT")
            admission.get_college_considered().send_keys(Keys.CONTROL+"a")
            admission.get_college_considered().send_keys(Keys.BACKSPACE)
            admission.get_college_considered().send_keys("Jain college")
            check_box = admission.get_check_box()
            
            # Check each checkbox if not already checked
            for checkbox in check_box:
                if not checkbox.is_selected():
                    self.scroll_into_view(checkbox)
                    checkbox.click()
            
            # Scroll to submit button and click
            submit_btn = admission.get_submit_btn()
            self.scroll_into_view(submit_btn)
            submit_btn.click()
            
            time.sleep(10)
            
            
                
        except Exception as e:
            pytest.fail(f"Test failed due to :{e}")



