import json
import random
import requests

class lead_create:

    base_url = "https://apidev.emversity.com/"
    

    def generate_random_phone_number(self):
        country_code = "91"
        start_digit = random.choice(['9', '8', '7'])  
        remaining_digits = ''.join(random.choices('0123456789', k=9))  
        phone_number = country_code + start_digit + remaining_digits  
        print(phone_number)
        return phone_number


    # sending the number to create lead
    def send_otp(self,number):
        url = "api/v1/auth/otp/send"
        complete_url = f"{self.base_url}{url}"
        data = {
            "phoneNumber":f"{number}"     
            }
        headers = {
            "Content-Type" : "application/json"
        }
        response = requests.post(url=complete_url ,headers= headers,json=data)
        assert response.status_code == 200
        response_data = response.json()["berry"]
        print("the berry is :",response_data)
        return response_data

    def verify_OTP(self,berry,number):
        url = "api/v1/auth/otp/verify"
        complete_url = f"{self.base_url}{url}"
        headers ={
            "Content-Type" : "application/json"
        }
        data = {
            "hash":f"{berry}",
            "otp":"1111",
            "phoneNumber":f"{number}",
            "isValidReq":0
        }
        response = requests.post(url= complete_url ,json=data,headers=headers)

        return response.json()['result']['token']
        

    def create_lead(self,number,token):
        phone_number = number[2:]
        url = "https://7v260ib1gf.execute-api.ap-south-1.amazonaws.com/v1/create-lead"
        headers = {
            "Content-type" : "application/json",
            "authorization" : f"Bearer {token}"
        }
        data = {
            "phone":f"{phone_number}",
            "country_code": "+91",
            "first_name": "test",
            "lead_form_step": 4,
            "url": "https://dev2.emversity.com/programs/bvoc-ott-course-nagpur",
            "campus": "Vizag",
            "city": "Adilabad",
            "state": "Andhra Pradesh",
            "preferred_language": "Kannada",
            "program_type": "BVoc",
            "utm_source": "website",
            "_fbc": 'null',
            "_fbp": "fb.1.1741857291219.775404687884638248",
            "slug": "bvoc-ott-course-nagpur"
        }
        response = requests.post(url=url, headers=headers,json=data)
        print(json.dumps(response.json(), indent = 4))
        assert response.status_code == 200

    def update_lead(self,number,token):
        url = "https://7v260ib1gf.execute-api.ap-south-1.amazonaws.com/v1/update-lead-details"
        phone_number = number[2:]
        data = {
            "phone":f"{phone_number}",
            "country_code":"+91",
            "lead_form_step":5,
            "course_enquired":"3-Year_Degree_Program_in_Medical_Laboratory_Technology_(MLT)",
            "class_12th_percentage":85,
            "class_12th_passout_year":"2024",
            "board":"CBSE",
            "gender":"male",
            "family_income":"less_25000_per_month",
            "class_12th_stream":"PCB",
            "utm_source":"website"
        }
        headers = {
            "Content-type" : "application/json",
            "authorization" : f"Bearer {token}"
        }
        response = requests.post(url=url, json=data, headers= headers)
        assert response.status_code == 200


lead = lead_create()
phone_num = lead.generate_random_phone_number()
res_data = lead.send_otp(phone_num)
token = lead.verify_OTP(res_data,phone_num)
lead.create_lead(phone_num,token)
lead.update_lead(phone_num,token)