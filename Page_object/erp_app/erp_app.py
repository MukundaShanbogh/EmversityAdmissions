from selenium.webdriver.common.by import By


class erp_elements:
    def __init__(self,driver):
        self.driver = driver

    support_btn = (By.XPATH,"//*[text()='Support']")
    ticketID_input = (By.XPATH,"//*[contains(@placeholder,'Ticket ID')]")
    erp_ticket_ID = (By.XPATH,"(//*[text()='Ticket ID']/parent::th/parent::tr/parent::thead/parent::table//p)[1]")
    resolved_status = (By.XPATH,"//*[@type='checkbox']")
    confirm_btn = (By.XPATH,"//*[text()='Confirm']")
    


    tutor_management = (By.XPATH,"//*[text()='Tutor Management']")
    tutor_schedule_btn = (By.XPATH,"//span[text()='Tutor Schedule']")
    select_center = (By.XPATH,"//label[text()='Please Select Centre']")
    select_section = (By.XPATH,"//label[text()='Please Select Section']")
    


    def get_support_btn(self):
        return self.driver.find_element(*erp_elements.support_btn)
    
    def get_ticketID_input(self):
        return self.driver.find_element(*erp_elements.ticketID_input)
    
    def get_erp_ticket_ID(self):
        return self.driver.find_element(*erp_elements.erp_ticket_ID)
    
    def get_resolved_status(self):
        return self.driver.find_element(*erp_elements.resolved_status)
    
    def get_confirm_btn(self):
        return self.driver.find_element(*erp_elements.confirm_btn)
    
    
    
    