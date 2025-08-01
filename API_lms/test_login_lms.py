import requests
import json
from datetime import date


class Test_login_lms:
    base_url = "https://apidev.emversity.com/"
    current_day = date.today()

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
            assert response.status_code == 200
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
        centre_id = response.json()["data"]["centre_id"]
        student_id = response.json()["data"]["student_id"]
        return centre_id,student_id

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

    def doubt_slot(self,token,center_id,student_id):
        end_point = "/api/v1/lms/doubt-session"
        url = f"{self.base_url}{end_point}"
        payload = {
            "student_id": f"{student_id}",
            "tutor_id": "2",
            "centre_id": f"{center_id}",
            "date": f"{self.current_day}",
            "start_time": "T15:30:00.000Z",
            "end_time": "T16:00:00.000Z"
        }
        headers = {
            "authorization" : f"Bearer {token}",
            "content-type"  :  "application/json",
            "centre-id" : f"{center_id}"
        }

        response = requests.post(url= url , headers=headers,json=payload)
        print(json.dumps(response.json(),indent=4))



login = Test_login_lms()
berry = login.enter_number()
token = login.verify_otp(berry)
centre_id,student_id = login.student_login(token)
login.tutor_details(token,centre_id)
login.doubt_slot(token,centre_id,student_id)