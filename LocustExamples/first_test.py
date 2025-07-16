from locust import HttpUser,task,between

class lms_users(HttpUser):
    wait_time = between(1,4)
    host = "https://apidev.emversity.com"
    payload = {
        "phoneNumber": "919618788418"
    }
    
    @task
    def lms_login(self):
        response = self.client.post("/api/v1/auth/otp/send?mode=lms", json=self.payload)
        print(response.status_code)
        hash=response.json().get("berry")
        print(hash)
        return hash
    
    @task
    def enter_otp(self):
        hash=self.lms_login()
        otp_payload = {
        "hash": hash,
        "isValidReq": "1",
        "otp": "1111",
        "phoneNumber": "919618788418"
    }
        response = self.client.post("/api/v1/auth/otp/verify?mode=lms",json=otp_payload)
        print(response.status_code)
        
