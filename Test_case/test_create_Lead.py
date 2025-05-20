import time
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_object.Landing_page.landing_page import landingPage
from Utilities.BaseClass import BaseClass


class Test_landing_page(BaseClass):


    #  Base part of the URL
    BASE_URL = "https://dev2.emversity.com/programs/"

    # Link to Google Sheet (CSV format)
   
    CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQGMQ0ZZqgjxqpqUBvU4llpKYcdRuRJ5zknfyAeTCq5mPENb2Dp--3chhF9106PqePtWOJbTKS5iBJz/pub?output=csv"

    # Get full URLs
    urls = BaseClass.get_urls_from_gsheet(BASE_URL, CSV_URL)
    
    @pytest.mark.parametrize("setup", urls, indirect=True)
    def test_program_page(self,setup):


        spelling_mistake=BaseClass.check_page_spelling(self.driver)
        # these steps will click on the enquire Now button and fill the form 
        lp = landingPage(self.driver)
        lp.get_enquire_now_btn().click()
        schedule_text =lp.get_schedule_started_txt().text

        # assertion to check the form has opned or not   
        assert schedule_text == 'Schedule a Free Career Counseling Session & Get Expert Guidance'

        # from it will start filling the form 
        random_name = BaseClass.random_name()
        random_phone_number = BaseClass.random_phone_number()
        lp.get_students_name().send_keys(random_name)
        lp.get_phone_number().send_keys(random_phone_number)
        lp.get_send_otp_btn().click()
        otp_input = lp.get_otp_input()
        for i in otp_input :
            i.send_keys('1')
        
        # it will select the university campus
        university_campus = lp.get_University_campus_input()
        university_campus.click()
        lp.get_campus_select().click()

        #  it will select the current location
        current_location =  lp.get_current_location()
        current_location.click()
        current_location.send_keys(Keys.ARROW_DOWN)
        current_location.send_keys(Keys.ENTER)

        #  it will select the preferred language 
        lp.get_preferred_language().click()
        time.sleep(.5)
        lp.get_language_select().click()

        #  this step will click on the request call back button
        lp.get_request_callback_btn().click()
        # ---------------------------- end of first page form ------------------------------------------------

        #-----------------------  2nd page form starts-----------------------
        course_text = lp.get_choose_preferred_course_text().text
        assert course_text == 'Choose Preferred Course'

        lp.get_preferred_course_select().click()

        lp.get_YOP_select().click()

        lp.get_subject_select().click()

        lp.get_Board_select().click()

        lp.get_gender_select().click()

        lp.get_percentage_select().click()

        lp.get_family_income().click()

        lp.get_check_scholarship_btn().click()

        congrats_text = lp.get_congrats_text().text
        assert congrats_text == 'Congratulations!'

        self.driver.close()

