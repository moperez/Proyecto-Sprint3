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


    def testName_002(self):
        #TEST_CASE_002: CAMPO CONTRASEÑA
        
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
        nombre = self.driver.find_element(By.ID, "firstname").send_keys("PRUEBASTESTER")
        time.sleep(3)
        
        #VALIDAR LA EXISTENCIA Y VISIBILIDAD DEL LABEL APELLIDO (manual)
        label_Apellido = self.driver.find_element(By.XPATH, "//span[contains(text(),'Apellido')]")
        print("El texto Apellido de la label es válido")
        self.assertTrue(label_Apellido.is_displayed(), "La etiqueta Apellido no es visible")
         
         
        #VALIDAR QUE EL INPUT APELLIDO EXISTA 
        apellido = self.driver.find_element(By.ID, "lastname")
        is_apellido_input= self.driver.find_element(By.ID, "lastname").is_displayed()
        print(is_apellido_input, "El input Apellido es válido y es visible")
        apellido.send_keys("QUALITY")
        time.sleep(3)
    
        
        #BUSCAR EL ELEMENTO EMAIL, COMPLETAR EL CAMPO Y VALIDAR EN FORMA MANUAL
        email = self.driver.find_element(By.ID, "email_address").send_keys("pruebas_quality002@gmail.com")
        time.sleep(3)
        
        
        #BUSCAR EL ELEMENTO CONTRASEÑA, COMPLETAR EL CAMPO Y VALIDAR VISIBILIDAD DEL INPUT CONTRASEÑA
        contraseña1 = self.driver.find_element(By.ID, "password")
        is_password_input = contraseña1.is_displayed()
        print(is_password_input, "El campo de input Contraseña1 es visible y se valida")
        contraseña1.send_keys("pruebas2023A*")
        time.sleep(3)
        
        
        #BORRAR EL TEXTO QUE COMPLETAMOS EN CONTRASEÑA
        contraseña1.clear()
        time.sleep(3)
        
        
        #VALIDAR QUE EL CAMPO INPUT CONTRASEÑA, LA CANTIDAD MINIMA DEBE SER AL MENOS 8 CARACTERES
        contraseña2 = self.driver.find_element(By. ID, "password").send_keys("yo")
      
        requisito1_contraseña_obligatoria = self.driver.find_element(By.ID, "password-error")
        texto_requisito1 = requisito1_contraseña_obligatoria.text
        print(f"Texto de la etiqueta: {texto_requisito1}")
        time.sleep(5)
        
        contraseña2 = self.driver.find_element(By. ID, "password")
        contraseña2.clear()
        time.sleep(5)
        
       
        #VALIDAR QUE EL CAMPO INPUT CONTRASEÑA, no admite solo caracteres numericos
        contraseña3 = self.driver.find_element(By. ID, "password").send_keys("123456789")
        time.sleep(3)
        
       
        #BUSCAR EL ELEMENTO CONFIRMAR CONTRASEÑA, COMPLETAR EL CAMPO Y VALIDAR
        confirmar_contraseña = self.driver.find_element(By.ID, "password-confirmation").send_keys("123456789")
        time.sleep(5)
        
        #VALIDAR QUE EL CAMPO INPUT CONTRASEÑA, DEBE CONTENER MAYUSCULA, MINUSCULA, CARACTERES ESPECIALES.
        requisito2_contraseña_obligatoria = self.driver.find_element(By.ID, "password-error")
        texto_requisito2 = requisito2_contraseña_obligatoria.text
        print(f"Texto de la etiqueta: {texto_requisito2}")
        time.sleep(5)
        
        
        contraseña3 = self.driver.find_element(By. ID, "password")
        contraseña3.clear()
        confirmar_contraseña = self.driver.find_element(By.ID, "password-confirmation")
        confirmar_contraseña.clear()
        
        
        #INGRESAR NUEVAMENTE UNA CONTRASEÑA 
        contraseña3 = self.driver.find_element(By. ID, "password").send_keys("Pruebas002*")
        time.sleep(3)
        
       
        #BUSCAR EL ELEMENTO CONFIRMAR CONTRASEÑA, COMPLETAR EL CAMPO Y VALIDAR
        confirmar_contraseña = self.driver.find_element(By.ID, "password-confirmation").send_keys("Pruebas002*")
        time.sleep(5)
        
        
        
        #PRESIONAR EL BOTON REGISTRARSE Y VALIDAR
        registrate = self.driver.find_element(By.ID, "send2").click()
        time.sleep(10)
        
         
    
    
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()