import time
from behave import *
from src.Functions.functions import Functions as buy
from selenium.webdriver.common.by import *
use_step_matcher("re")

class Saucedemo_Buy(buy):
    
    '''def load_json(self):
        buy.get_json_file(self, "products")'''

    @then(('Add products to cart'))
    def add_products_to_cart(self):
        buy.get_json_file(self, "Products")
        buy.get_elements(self, "backpack").click()
        buy.get_elements(self, "ultimoProdutc").click()
        buy.get_elements(self, "jacket").click()
        
        time.sleep(1)

        
    @then(('Delete products'))
    def delete_products(self):
        '''buy.get_json_file(self, "jacketRemove").click()'''

        numCart = buy.get_text(self, "numCart")

        if numCart == "3":
            assert numCart == "3"
        else:
            assert numCart == "4"