import json
import time
from behave import *
from src.Functions.functions import Functions as Test
from selenium.webdriver.common.by import *
use_step_matcher("re")

class Saucedemo_prueba(Test):
    @given(('Open the application'))
    def open_the_application(self):
        Test.abrir_navegador(self)

    @when(('Load the data json'))
    def load_the_data_json(self):
        Test.get_json_file(self, "login")
    
    @then(('Enter user credentials'))
    def enter_user_credentials(self):
        user = "standard_user"
        pwd = "secret_sauce"

        Test.get_elements(self, "name_user").send_keys(user)
        Test.get_elements(self, "pwd_user").send_keys(pwd)
       
    @then(('Tap on the login button'))
    def tap_on_the_login(self):
        Test.get_elements(self, "login_btn").click()
        self.driver.implicitly_wait(10)
        #assert Test.get_text(self, "title") == "PRODUCTS"
        
        titlePage = Test.get_text(self, "title")

        if titlePage == "PRODUCTS":
            assert titlePage == "PRODUCTS"
        else:
            assert titlePage == "PRskmODUCTS"

        
    @then(('Add products to cart'))
    def step_function(self):
        print("OK ✅")