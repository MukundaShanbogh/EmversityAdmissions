import random
import requests
from Utilities.BaseClass import BaseClass
from DB_connection.DB_connect import Database


class Test_fill_basic_details(BaseClass) :
    phone_number = None
    def test_get_berry(self):
        db = Database()
        self.phone_number = db.get_freash_lead_numbers()
        self.phone_number = random.choice(self.phone_number)["phone"]
        print(f"im the final phone number :{self.phone_number}")
        base_url = "https://apidev.emversity.com/api/v1/scholorship/test/auth/otp/send"
        payload = {
            "phone_number": f"{self.phone_number}",
            "country_code": "+91"
        }
        headers = {
            "Content-Type" : "application/json"
        }
        response = requests.post(url= base_url,json=payload,headers= headers)
        return response.json()["berry"]["hash"]
    
    def test_get_token(self,berry):
        base_url = "https://apidev.emversity.com/api/v1/scholorship/test/auth/otp/verify"
        payload = {
            "phone_number": f"{self.phone_number}",
            "country_code": "+91",
            "otp": "1111",
            "hash": f"{berry}"
        }
        headers = {
            "Content-Type" : "application/json"
        }

        response = requests.post(url=base_url, headers= headers, json=payload)
        return response.json()["token"]

    def test_basic_details_fill(self,token):
        base_url = "https://apidev.emversity.com/api/v1/scholorship/test/student/basic-details"
        headers = {
            "Content-Type" : "application/json",
            "authorization" : f"Bearer {token}"
        }
        random_name = BaseClass.random_name()
        
        payload= {
        "tenth_board": 'null',
        "student_title": "mr",
        "first_name": f"{random_name}",
        "last_name": "test",
        "email": f"{random_name}@gmail.com",
        "date_of_birth": "1998-8-6",
        "gender": "m",
        "phone_number": f"{self.phone_number}",
        "is_same_number_as_whats_app_number": 1,
        "whats_app_number": 'null',
        "religion": "1",
        "caste": "1",
        "father_title": "mr",
        "father_name": "test father",
        "father_mobile_numner": "9768776876",
        "mother_title": "mrs",
        "mother_name": "testMother",
        "mother_mobile_number": "7632246378",
        "guardian_qualification": "1",
        "guardian_occupation": "1",
        "family_annual_income": "1",
        "family_amenities": [
            "2W"
        ],
        "is_credit_card_used": 1,
        "is_family_used_bank_account": 1,
        "is_own_fund": "self",
        "current_address": "hjbjhbcusad",
        "current_address_pincode": "874365",
        "current_address_city_or_town": "jhshvdsa",
        "is_permanent_address_same_as_current_address": 1,
        "permanent_address": 'null',
        "permanent_address_pincode": 'null',
        "permanent_address_city_or_town": 'null',
        "home_type": "rent",
        "hostel_need": 1,
        "home_distance_from_centre": "7",
        "tenth_institue_name": "ajsbjdb",
        "tenth_year_of_passing": "2020",
        "tenth_marking_scheme": "cgpa_out_of_10",
        "tenth_percentage": "7.8",
        "qualification_after_tenth": "12th",
        "is_appeared_entrance_exam": 0,
        "highest_qualification": "3",
        "self_work_experience_flag": 0,
        "self_work_experience_in_years": 'null',
        "any_disability": 0,
        "student_aadhar_number": "837464238674",
        "heard_about_emversity_from": "1",
        "other_course_interested": "jhbcyh",
        "other_colleges_interested": "jhdsbchs",
        "is_allowed_to_analysis": 'true',
        "is_confirmed_data_accuracy": 'true',
        "country_code": "+91",
        "university_id": 37,
        "university_program_id": 47,
        "university_program_batch_id": 53,
        "nationality": 'null',
        "permanent_address_address_line_two": 'null',
        "guardian_name": 'null',
        "guardian_phone_number": 'null',
        "relation_with_guardian": 'null',
        "self_annual_income": 'null',
        "tweleth_board": "1",
        "tweleth_percentage": 'null',
        "core_subject_in_tweleth": "3",
        "selected_core_subjects": [],
        "selected_optional_subjects": [],
        "selected_languages_in_twelth": [],
        "selected_ranks_of_exams": [
            4
        ],
        "jee_rank": "",
        "neet_rank": "",
        "cuet_percentage": "",
        "other_text_from_heard_about_emversity": 'null',
        "created_at": "2025-08-06T12:00:07.000Z",
        "active": 1,
        "total_questions": 'null',
        "correct_answers": 'null',
        "quiz_questions": 'null',
        "is_EMSAT_online": 0,
        "test_start_time": 'null',
        "center_id": "33",
        "video_interview_status": 0,
        "video_interview_result": 0,
        "final_result": "pending",
        "twelve_year_of_passing": "2020",
        "test_manual_active": 0,
        "school_type": "1",
        "school_name": "jbsghva",
        "school_annual_fee": "56789",
        "school_address": "jasvcvxuyag",
        "school_pincode": "346873",
        "other_guardian_occupation": 'null',
        "other_school_type": 'null',
        "cet_rank": "",
        "emerge_online_test_status": 'null',
        "current_address_line_two": 'null',
        "university_year_of_passing": 'null',
        "university_aggregate_marks_or_cgpa": 'null',
        "student_university_name": 'null',
        "work_experience": [],
        "bachelor_year_of_passing": 'null',
        "bachelor_aggregate_marks_or_cgpa": 'null',
        "masters_year_of_passing": 'null',
        "masters_aggregate_marks_or_cgpa": 'null',
        "is_work_experience_mba_pg": 0,
        "twelfth_institue_name": "jasbdhb",
        "twelfth_marking_scheme": 'null',
        "twelfth_result_status": "awaited",
        "diploma_institue_name": 'null',
        "diploma_awarded_by": 'null',
        "diploma_year_of_passing": 'null',
        "diploma_result_status": 'null',
        "diploma_marking_scheme": 'null',
        "diploma_percentage_or_cgpa": 'null',
        "degree_understanding": 'null',
        "internship_schedule_acknowledgement": 'null',
        "internship_acknowledgement": 'null',
        "internship_policy_agree": 'null',
        "internship_location_notice": 'null',
        "exam_evaluation_acknowledgement": 'null',
        "attendance_requirement_acknowledgement": 'null',
        "passing_criteria_acknowledgement": 'null',
        "center_change_restrict_acknowledgement": 'null',
        "fee_policy_acknowledgement": 'null',
        "preferred_campus_location": 'null',
        "preferred_program_choice": 'null',
        "type_of_program": 'null',
        "max_program_fee": 'null',
        "credit_history": 'null',
        "bank_relation": 'null',
        "newspaper_subscription": 'null',
        "twelfth_school_type": 'null',
        "twelfth_school_medium": 'null',
        "twelfth_domicile_state": 'null',
        "mother_highest_qualification": 'null',
        "mother_highest_qualification_completion_year": 'null',
        "mother_occupation": 'null',
        "mother_monthly_income": 'null',
        "tenth_school_medium": 'null',
        "tenth_domicile_state": 'null',
        "father_highest_qualification": 'null',
        "father_highest_qualification_completion_year": 'null',
        "father_occupation": 'null',
        "father_monthly_income": 'null',
        "student_id_type": 'null',
        "student_id_number": 'null',
        "is_mobile_use": 'null',
        "is_laptop_use": 'null',
        "employer_name": 'null',
        "self_experience_working_role": 'null',
        "middle_name": 'null',
        "twelfth_domicile_pincode": 'null',
        "guardian_highest_qualification_completion_year": 'null',
        "blood_group": 'null',
        "student_comment": 'null',
        "university_name": "AutomationTestingUniversity",
        "lsq_mapping_university": 'null',
        "centre_name": "Automation_center",
        "lsq_mapping_center": 'null',
        "university_name_by_program": "AutomationTestingUniversity",
        "program_name": "AutomationProgramBVOC",
        "program_type": "bvc",
        "program_category": "aott",
        "program_duration": 36,
        "batch_name": "AutomationBvocAott",
        "batch_start_date": "2025-04-14",
        "program_category_name": "Anaesthesia Operation Theatre Technology",
        "is_student_available": 0,
        "student_id": 'null',
        "lead_id": 'null',
        "lead_additional_data": {
            "phone": "9790763457",
            "first_name": "guakwh",
            "country_code": "+91"
        },
        "lead_program_type": "",
        "utm_source": "",
        "event_id": 'null',
        "event_status": 'null',
        "config_id": 'null',
        "has_multiple_event_status": 0
    }
        response = requests.patch(url= base_url, headers= headers , json= payload)
        print(response.status_code)

class_obj = Test_fill_basic_details()
berry = class_obj.test_get_berry()
token = class_obj.test_get_token(berry)
class_obj.test_basic_details_fill(token)