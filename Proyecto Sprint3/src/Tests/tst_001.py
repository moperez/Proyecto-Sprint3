'''
Created on 11 nov. 2023

@author: M&P
'''
import os
import unittest
import time 
import pytest
import pytest_html
import allure_pytest
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

    

    def testName_001(self):
        #TEST_CASE_001: CAMPO APELLIDO
        
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
        nombre = self.driver.find_element(By.ID, "firstname").send_keys("PRUEBA")
        time.sleep(3)
        
        #VALIDAR LA EXISTENCIA Y VISIBILIDAD DEL LABEL APELLIDO (manual)
        label_Apellido = self.driver.find_element(By.XPATH, "//span[contains(text(),'Apellido')]")
        print("El texto Apellido de la label es válido")
        self.assertTrue(label_Apellido.is_displayed(), "La etiqueta Apellido no es visible")
         
         
        #VALIDAR QUE EL INPUT APELLIDO EXISTA 
        apellido = self.driver.find_element(By.ID, "lastname")
        is_apellido_input= self.driver.find_element(By.ID, "lastname").is_displayed()
        print(is_apellido_input, "El input Apellido es válido y es visible")
        apellido.send_keys("QUALITY TEST")
        time.sleep(3)
        
        #VALIDAR QUE EL CAMPO INPUT APELLIDO SE HAYA COMPLETADO CORRECTAMENTE
        valor_ingresado = apellido.get_attribute("value")
        print("Valor ingresado en el campo: ", valor_ingresado)
        
                
        #BORRAR EL TEXTO QUE COMPLETAMOS EN APELLIDO 
        apellido.clear()
        time.sleep(3)
        
        #VALIDAR QUE EL CAMPO INPUT APELLIDO SE HAYA BORRADO CORRECTAMENTE
        valor_ingresado = apellido.get_attribute("value")
        print("Valor ingresado en el campo apellido es: ", valor_ingresado)
        assert valor_ingresado == "", "El campo no se borró correctamente"
        
        
        #BUSCAR EL ELEMENTO EMAIL, COMPLETAR EL CAMPO Y VALIDAR EN FORMA MANUAL
        email = self.driver.find_element(By.ID, "email_address").send_keys("pruebas_quality001@gmail.com")
        time.sleep(3)
        
        
        #BUSCAR EL ELEMENTO CONTRASEÑA, COMPLETAR EL CAMPO Y VALIDAR.
        contraseña = self.driver.find_element(By.ID, "password").send_keys("pruebas2023*")
        time.sleep(3)
        
        #BUSCAR EL ELEMENTO CONFIRMAR CONTRASEÑA, COMPLETAR EL CAMPO Y VALIDAR
        confirmar_contraseña = self.driver.find_element(By.ID, "password-confirmation").send_keys("pruebas2023*")
        time.sleep(3)
        
        #PRESIONAR EL BOTON REGISTRARSE Y VALIDAR
        registrate = self.driver.find_element(By.ID, "send2").click()
        time.sleep(3)
        
        #VALIDAR LA ETIQUETA QUE INDICA QUE EL CAMPO ES OBLIGATORIO Y ESTE PRESENTE EN LA PAGINA.
        text_apellido_obligatorio = self.driver.find_element(By.ID, "lastname-error")
        text_obligatorio = text_apellido_obligatorio.text
        print("Texto de la etiqueta: {text_obligatorio}")
        
        #VALIDAR QUE INDICA QUE EL CAMPO APELLIDO ES OBLIGATORIO
        if text_apellido_obligatorio.is_displayed():
            print("La etiqueta indica que el campo Apellido es obligatorio")
        else:
            print("No se muestra la etiqueta de campo obligatorio")
         
         
        #COMPLETAR EL FORMULARIO CON EL APELLIDO FALTANTE Y VALIDAR EL REGISTRO
        apellido = self.driver.find_element(By.ID, "lastname").send_keys("QUALITY TEST")
        time.sleep(3)  
        
        registrate = self.driver.find_element(By.ID, "send2").click()
        time.sleep(3)

    
    def tearDown(self):
        unittest.TestCase.tearDown(self)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()