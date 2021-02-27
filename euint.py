import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username1 = 'penhm01'
password1 = 'Summer01'
jobpostingtempalte = 'DE_ZÜP_Senior Facharbeiter'
startdate = "01/01/2021"
enddate = "28/02/2022"
manager = "Stephan Sulger (SULGERS)"

class JobPostingCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://euint13.fgvms.eu/?logOut")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()

    def test_001(self):
        driver = self.driver
        username_btn = driver.find_element_by_id('usernameId_new')
        username_btn.click()
        driver.find_element_by_id("usernameId_new").send_keys(username1)
        driver.find_element_by_id("passwordId_new").send_keys(password1)
        driver.find_element_by_class_name('formLoginButton_new').click()
        driver.find_element_by_id('createMenuTitle').click()
        driver.find_element_by_id("createMenu_1_jobpostingfortempworker_link").click()
        driver.find_element_by_id('job_template_by_person_list_title_sch').send_keys(jobpostingtempalte)
        driver.find_element_by_name("job_template_by_person_list_search").click()
        driver.find_element_by_link_text('DE_ZÜP_Senior Facharbeiter z.B. FA Metall (Ind), Chemie, Pharma, Fachkraft für Lagerlogistik_EUR').click()
        driver.find_element_by_id("startDate").clear()
        driver.find_element_by_id("startDate").send_keys(startdate)
        driver.find_element_by_id("endDate").clear()
        driver.find_element_by_id("endDate").send_keys(enddate)
        driver.execute_script("window.scrollTo(0, 1800)")
        driver.find_element_by_name("select_divisionCodeId").click()
        driver.find_element_by_xpath("//li[@data-index-id='z18082108391019296814901_select_divisionCodeId']").click()
        driver.find_element_by_name("select_site").click()
        driver.find_element_by_xpath("//li[@data-index-id='z18082109174819562589901_select_site']").click()
        driver.find_element_by_name("select_workLocation").click()
        driver.find_element_by_xpath("//li[@data-index-id='z18082211363452541983905_select_workLocation']").click()
        # organizations
        driver.find_element_by_name("select_label_z18082012484394167329905z18092107425235132415903__segment1").click()
        driver.find_element_by_name("select_label_z18082012484394167329905z18092107425235132415903__segment1").click()
        driver.find_element_by_name("select_label_z18082012484394167329905z18092107425235132415903__segment1").send_keys(manager)
        driver.find_element_by_xpath("//li[@data-index-id='Stephan Sulger (SULGERS)_select_label_z18082012484394167329905z18092107425235132415903__segment1']").click()
        driver.find_element_by_name("select_label_z18082012484394167329905z18092107425235132415903__segment2").click()
        driver.find_element_by_xpath("//li[@data-index-id='Insert Production (DOMALI | 25031124)_select_label_z18082012484394167329905z18092107425235132415903__segment2']").click()




        sleep(10)
if __name__ == "__euint__":
    unittest.main(verbosity=1)