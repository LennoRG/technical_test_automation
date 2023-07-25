import json
import os
import time
from behave import *
from src.Functions.functions import Functions as Test
from selenium.webdriver.common.by import *
from PIL import Image
use_step_matcher("re")

class Scrip_Two(Test):
    @then(('Numero de vuelo vacio'))
    def numero_vuelo_vacio(self):  
        Test.get_elements(self, "enter_numero_vuelo").click()
        
    @then(('Validar resultados de vuelo vacio'))
    def resultado_vuelo_vacio(self):
        copyVacio = "Debe ingresar el número del vuelo."
        titleVacio = Test.get_text(self, "copy_vacio")
        
        if titleVacio == copyVacio:
            assert titleVacio== copyVacio

        else:
            self.driver.save_screenshot('ImagenError.png')
            #screenshot = Image.open('ImagenError.png')
            #screenshot.show()
            assert titleVacio == copyVacio
            self.driver.quit()
        
