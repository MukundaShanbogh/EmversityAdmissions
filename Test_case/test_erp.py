import datetime
import pytest
from selenium.webdriver.support import expected_conditions as EC
import requests
from Utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class TestSchedule(BaseClass):
    dev_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozLCJlbWFpbCI6Im11a3VuZGEuc3JAZW12ZXJzaXR5LmNvbSIsImlhdCI6MTc1MDkzNTc5MCwiZXhwIjoxNzUzNTI3NzkwfQ.JP3cIsWdj-0F_XTUTjeCQNl9lGAKWJaSlcbInS9pk_g'
    domain = '.emversity.com'
    erp_tab_handle = None
    tv_app_tab_handle = None
    lms_tab_handle = None
    tabs_initialized = False

    @pytest.mark.smoke
    @pytest.mark.order(0)
    def test_setup_browser(self):
        if not TestSchedule.tabs_initialized:
            # Open ERP
            self.driver.get("https://erpdev.emversity.com/")
            TestSchedule.erp_tab_handle = self.driver.current_window_handle
            
            self.driver.add_cookie({'name': 'login_token',
                                    'value': self.dev_token,
                                    'domain': self.domain,
                                    'path': '/'})
            self.driver.get("https://erpdev.emversity.com/dashboard")

            # Open TV app in new tab
            self.driver.execute_script("window.open('https://tvtutordev.emversity.com/login', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[1])
            TestSchedule.tv_app_tab_handle = self.driver.current_window_handle

            # Open LMS in new tab
            self.driver.execute_script("window.open('https://emversedev.emversity.com/', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[2])
            TestSchedule.lms_tab_handle = self.driver.current_window_handle

            # Switch back to ERP tab
            self.driver.switch_to.window(TestSchedule.erp_tab_handle)
            TestSchedule.tabs_initialized = True

    @pytest.mark.smoke
    @pytest.mark.order(1)
    def test_schedule_creation(self):
        try:          
            # Get current date 
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")  # Changed to DD-MM-YYYY format
            
            # Get current day and calculate column
            current_day = BaseClass.get_day_name()
            if current_day == 6:  # Sunday
                pytest.skip("Today is Sunday, there are no classes")
            column = current_day - 1

            # Get current time and calculate row
            current_time = BaseClass.get_current_time()
            row = BaseClass.get_row_number(current_time)
            if row is None:
                pytest.skip("Schedule is not allowed at this time")

            # time range
            start_time, end_time = BaseClass.calculate_time_range()

            # payload
            payload = {
                "row": row,
                "col": column,
                "n": 0,
                "date": current_date,
                "batch": {'label': "Automation_section", 'value': 50},
                "i":{
                    "id": 34,
                    "name": "automation_class",
                    "centre_id": 33,
                    "active": True,
                    "created_at": "2025-04-14T06:29:22.000Z",
                    "created_by": 0,
                    "course_type": None,
                    "center": {
                        "id": 33,
                        "name": "Automation_center",
                        "state": "Karnataka",
                        "city": "Bengaluru",
                        "address": "bengaluru",
                        "teritory_manager": 32,
                        "active": True,
                        "created_at": "2025-04-14T06:27:38.000Z",
                        "created_by": 3,
                        "center_photo": "Center/photo/1744612058700.jpg",
                        "latitude": None,
                        "longitude": None,
                        "wifi_ip": [
                        "106.51.37.182:55349"
                        ],
                        }
                    },
                "subject": {"label": "communication skills", "value": "17"},
                "subject_type": {"label": "theory", "value": "theory"},
                "start_time": start_time,
                "end_time": end_time
            }

            url = 'https://apidev.emversity.com/api/v1/crm/university/program/batch/semester/subject/section/schedule'
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
                'authorization': f'Bearer {self.dev_token}',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://erpdev.emversity.com',
                'pragma': 'no-cache'
            }

            # API request
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 400 and "Cannot book the same section for multiple classes at the same time" in response.text:
                # print("Skipping test as section is already booked")
                pytest.skip("Section is already booked for this time slot")
            else:
                # assertion
                assert response.status_code == 201, f"API request failed with status code: {response.status_code}"
                response_data = response.json()
                assert response_data is not None, "API response is empty"
                # print("API Response:", response_data)

        except Exception as e:
            pytest.fail(f"Test failed due to: {e}")