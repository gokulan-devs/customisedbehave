from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locators 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from urls import urls
from gokuls_data_loader import data_table

class HelperFunc(object):
    __TIMEOUT = 10
 
    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver
 
    def open(self, page):
        page=page.replace(" page","")
        url=urls[page]
        self._driver.get(url)
 
    def maximize(self):
        self._driver.maximize_window()        
        
    def close(self):
        self._driver.quit()
        
    # Helper functions that are used to identify the web locators in Selenium Python tutorial  
 
    def find_element(self, elementname):
        xpath=locators[elementname]
        print(xpath)
        element=None
        for i in range(4):
            try:
                element= self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
                break
            except:
                actions = ActionChains(self._driver)
                actions.send_keys(Keys.PAGE_DOWN)
                actions.perform()
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

 
    # def find_by_name(self, name):
    #     return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))
 
    # def find_by_id(self, id):
    #     return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id))) 
    #Actions
    def click(self,element):
        self._driver.click(element)

    def get_data(self,scenario,datalist):
        datalist=[x.strip() for x in datalist.split(',')]
        data_vals={}
        for item in datalist:
           data_vals[item]=(data_table[scenario]['data'][0][item])
        print(data_vals)
        return data_vals.copy()
    
    def fill_data(self,field_value_set):
        for loc,data in field_value_set.items():
            self.find_element(loc).click()
            self.find_element(loc).send_keys(data)
    

