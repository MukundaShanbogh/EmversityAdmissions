import requests
import json
import pytest



class Test_login_lms:
    base_url = "https://apidev.emversity.com/"

    def enter_number(self):
        end_point = "api/v1/auth/otp/send?mode=lms"
        url = f'{self.base_url}{end_point}'
        payload = {
            "phoneNumber": "919618788418"
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url= url, headers=headers, json = payload)
        return response.json()['berry']

    def verify_otp(self,berry):
        try:

            end_point="api/v1/auth/otp/verify?mode=lms"
            url = f"{self.base_url}{end_point}"
            
            print(f"i am the berry : {berry}")
            headers = {
                "content-type" : "application/json"
            }
            payload={
                "hash" : berry,
                "isValidReq" : "1",
                "otp" : "1111",
                "phoneNumber" : "919618788418"
            }
            response = requests.post(url= url ,headers = headers, json = payload )
            print("I am the response:",response)
            return response.json()['result']['token']
        except Exception as e:
            # pytest.fail(e)
            raise

    
    def student_login(self,token):           
        end_point = "api/v1/lms/student/get"
        url = f"{self.base_url}{end_point}"
        headers = {
            "authorization" :f"Bearer {token}",
            "content-type"  : "application/json"
        }
        response = requests.get(url = url , headers = headers )
        print(f"Student_details: {json.dumps(response.json(), indent = 4)}")
        return response.json()["data"]["centre_id"]

    def tutor_details(self,token,center_id):
        end_point = "/api/v1/lms/tutors"
        url = f"{self.base_url}{end_point}"
        headers = {
            "authorization" : f"Bearer {token}",
            "content-type"  :  "application/json",
            "centre-id" : f"{center_id}"
        }
        reponse = requests.get(url= url,headers=headers)
        print(f"tutor_details: {json.dumps(reponse.json(),indent=4)}")

login = Test_login_lms()
berry = login.enter_number()
token = login.verify_otp(berry)
centre_id = login.student_login(token)
login.tutor_details(token,centre_id)