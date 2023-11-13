'''
Created on 12 nov. 2023

@author: M&P
'''
import unittest
import os
import pytest
import pytest_html
import allure_pytest
import time 
from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException 
from selenium.common.exceptions import NoAlertPresentException 
from selenium.common.exceptions import NoSuchWindowException 
from selenium.common.exceptions import TimeoutException
from PIL import Image

class Test(unittest.TestCase):


     def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://bensimon.com.ar")

    

     def testName_003(self):
        #TEST_CASE_003: CAMPO EMAIL
        
        #BUSCAR EL ELEMENTO POP UP Y CERRARLO
        pop_up = self.driver.find_element(By.ID, "closeBtn").click()
        time.sleep(3)
        
        #HACER CLICK EN BOTON DE USUARIO
        self.driver.find_element(By.ID, "boton-usr").click()
        time.sleep(3)
        
        #INGRESAR A LA OPCION CREAR CUENTA
        crear_cuenta_button = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, "CREAR CUENTA")))
        crear_cuenta_button.click()
        
        #BUSCAR EL ELEMENTO NOMBRE, COMPLETAR Y VALIDAR
        nombre = self.driver.find_element(By.ID, "firstname").send_keys("PRUEBAS QA")
        time.sleep(3)
        
        #VALIDAR LA EXISTENCIA Y VISIBILIDAD DEL LABEL APELLIDO (manual)
        label_Apellido = self.driver.find_element(By.XPATH, "//span[contains(text(),'Apellido')]")
        print("El texto Apellido de la label es válido")
        self.assertTrue(label_Apellido.is_displayed(), "La etiqueta Apellido no es visible")
         
         
        #VALIDAR QUE EL INPUT APELLIDO EXISTA 
        apellido = self.driver.find_element(By.ID, "lastname")
        is_apellido_input= self.driver.find_element(By.ID, "lastname").is_displayed()
        print(is_apellido_input, "El input Apellido es válido y es visible")
        apellido.send_keys("QUALITY TESTING")
        time.sleep(3)
        
       
        #BUSCAR EL ELEMENTO EMAIL, COMPLETAR EL CAMPO Y VALIDAR EN FORMA MANUAL
        email = self.driver.find_element(By.ID, "email_address")
        is_email_valido = self.driver.find_element(By.ID, "email_address").is_displayed()
        print(is_email_valido, "El email ingresado es válido")
        email.send_keys("pruebas_quality003@gmail.com")
        time.sleep(3)
        try:
            error_email_presente = self.driver.find_element(By.ID, "email_address").is_displayed()
            if error_email_presente:
                error_email_msg = self.driver.find_element(By.ID, "email_address").text
                assert error_email_msg != "Email ingresado válido", "Email ingresado no es válido"
        except NoSuchElementException:
            print("Email ingresado válido")
        
       
        #BUSCAR EL ELEMENTO CONTRASEÑA, COMPLETAR EL CAMPO Y VALIDAR.
        contraseña = self.driver.find_element(By.ID, "password").send_keys("pruebas2000*")
        time.sleep(3)
        
        #BUSCAR EL ELEMENTO CONFIRMAR CONTRASEÑA, COMPLETAR EL CAMPO Y VALIDAR
        confirmar_contraseña = self.driver.find_element(By.ID, "password-confirmation").send_keys("pruebas2000*")
        time.sleep(3)
        
        #PRESIONAR EL BOTON REGISTRARSE Y VALIDAR
        registrate = self.driver.find_element(By.ID, "send2").click()
        time.sleep(3)
        
  
    
     def tearDown(self):
        unittest.TestCase.tearDown(self)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()