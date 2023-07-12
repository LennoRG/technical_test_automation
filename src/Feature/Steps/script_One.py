import json
import os
import time
from behave import *
from httpcore import TimeoutException
from src.Functions.functions import Functions as Test
from selenium.webdriver.common.by import *
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

use_step_matcher("re")

class Saucedemo_prueba(Test):
    @given(('Open the application'))
    def open_the_application(self):
        Test.abrir_navegador(self)

    @when(('Load the data json'))
    def load_the_data_json(self):
        Test.get_json_file(self, "login")
        
    @then(('Clinc Informacion de viaje'))
    def step_function(self):
        Test.get_elements(self, "info_viaje").click()
        time.sleep(1)
        
    @then(('Clik Estado Vuelo'))
    def step_function(self):
        Test.get_elements(self, "estado_vuelo").click()
    
    @then(('Click Numero de vuelo'))
    def step_function(self):
        Test.get_elements(self, "numero_vuelo").click()
 
        
    @then(('Ingresa nuemero de vuelo'))
    def step_function(self):
        numVuelo = "123456789"
        Test.get_elements(self, "enter_numero_vuelo").click()
        Test.get_elements(self, "enter_numero_vuelo").send_keys(numVuelo)
    
        
    @then(('Click en buscar vuelos'))
    def step_function(self):
          Test.get_elements(self,  "btn_buscar").click()
          
        
    @then(('Validar resultados de vuelo')) 
    def step_function(self):
        erroCopy = "Vuelo no encontrado. Intente con otro número o haga la búsqueda por ciudadesss."
        #assert  Test.get_text(self, "copy_Error") == erroCopy
        
        titleError = Test.get_text(self, "copy_Error")
        
        if titleError == erroCopy:
            assert titleError == erroCopy

        else:
            self.driver.save_screenshot('ImagenError.png')
            screenshot = Image.open('ImagenError.png')
            screenshot.show()
            assert titleError == erroCopy
            self.driver.quit()
            
            
            '''copy_field_vacio = "//*[@id='flighjjtNuesmber.errors']"
            
            
            try:
                element = WebDriverWait(self.driver, 1)
                element.until(EC.presence_of_element_located((By.XPATH, copy_field_vacio)))
                assert  Test.get_text(self, "copy_vacio") == copyVacio
            
            except TimeoutError:
                print("NO SE ENCONTRO EL ELEMENTO" )
                self.driver.save_screenshot('ImagenError.png')
                screenshot = Image.open('ImagenError.png')
                screenshot.show()
                self.driver.quit()'''
    
        
   
        
        
        
        
            
            
        
    '''@then(('Tap on the login button'))
    def tap_on_the_login(self):
        Test.get_elements(self, "login_btn").click()
        self.driver.implicitly_wait(10)
        #assert Test.get_text(self, "title") == "PRODUCTS"
        
        titlePage = Test.get_text(self, "title")

        if titlePage == "PRODUCTS":
            assert titlePage == "PRODUCTS"
        else:
            assert titlePage == "Products"'''
            
