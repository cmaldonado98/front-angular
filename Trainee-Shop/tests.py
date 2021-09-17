#LIBRERIAS
#import pandas as pd
#from typing_extensions import ParamSpecArgs
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
import HtmlTestRunner
from selenium.common.exceptions import NoSuchElementException
#import xmlrunner
import unittest

#Opciones de navegacion
# options = webdriver.ChromeOptions()
# options.add_argument('--start-maximized')
# options.add_argument('--disable-extensions')
options = webdriver.FirefoxOptions()
options.headless = True

driver_path = './Drivers/geckodriver.exe'
driver = webdriver.Firefox(options=options)
#Iniciar en la pantalla 2
driver.set_window_position(2000,0)
driver.maximize_window()
time.sleep(2)

#Iniciamos el navegador
driver.get('http://a1a17f2828c0f4d7f83ff926804b9a74-1091942866.us-west-1.elb.amazonaws.com')
#driver.get('http://localhost:4200')

#Apertura a Excel
filesheet="/Trainee-Shop/excel/test.xlsx"
wb=load_workbook(filesheet)
hojas= wb.get_sheet_names()
print(hojas)
nombres2 = wb.get_sheet_by_name("test")
wb.close()
#time.sleep(1)
#a = '''
for i in range(2,3):
    namelast, phone,email, direc, user,password,confirmpass = nombres2[f'A{i}:G{i}'][0]
    print(namelast.value, phone.value,email.value,direc.value, user.value,password.value,confirmpass.value)
    #scroll
    time.sleep(1)
    try:
        driver.execute_script("window.scrollTo(0, 1000);")
    except NoSuchElementException:
                time.sleep(1)
    #CLICK BOTON REGISTRO
    time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'btnRegistro')))\
        .click()
    except NoSuchElementException:
            time.sleep(1)
    #scroll
    time.sleep(1)
    try:
        driver.execute_script("window.scrollTo(1000, 0);")
    except NoSuchElementException:
                time.sleep(1)
    #LLENA NOMBRE Y
    time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'nombre')))\
        .send_keys(namelast.value)
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #LLENA TELEFONO
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'celular')))\
        .send_keys(phone.value)
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #LLENA EMAIL
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'email')))\
        .send_keys(email.value)
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #LLENA DIRECCION
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'direccion')))\
        .send_keys(direc.value)
    except NoSuchElementException:
            time.sleep(1)
    #scroll
    time.sleep(1)
    try:
            driver.execute_script("window.scrollTo(0, 1000);")
    except NoSuchElementException:
            time.sleep(1)
    #LLENA USUARIO CEDULA
    time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'cedula')))\
        .send_keys(user.value)
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #LLENA CONTRASEÑA
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'contrasena')))\
        .send_keys(password.value)
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #CONFIRMA CONTRASEÑA
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'confirmContrasena')))\
        .send_keys(confirmpass.value)
    except NoSuchElementException:
            time.sleep(2)
    time.sleep(1)
    #CLICK BOTON REGISTRAR
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'addButton')))\
        .click()
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(2)
#'''
driver.get('http://a1a17f2828c0f4d7f83ff926804b9a74-1091942866.us-west-1.elb.amazonaws.com')
nombres = wb.get_sheet_by_name("test")
wb.close()
for i in range(2,3):
    ci, password,confirmpass,numContacto,dirEnvio,nCuenta = nombres[f'E{i}:J{i}'][0]
    print(ci.value, password.value)
    time.sleep(2)
    #LLENAR CEDULA
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                        'login')))\
        .send_keys(ci.value)
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #LLENAR PASSWORD
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'password')))\
        .send_keys(password.value)
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #CLICK BOTON INICIAR SESION
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'btn-login')))\
        .click()
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #CLICK BOTON SUPERMERCADO SUPERMAXI
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'btn-Supermaxi')))\
        .click()
    except NoSuchElementException:
            time.sleep(2)
    #scroll
    time.sleep(2)
    try:
            driver.execute_script("window.scrollTo(0, 1000);")
    except NoSuchElementException:
            time.sleep(1)
    #RELLENAR CANTIDAD DE COMPRAS
    time.sleep(2)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'cantidad0')))\
        .send_keys("1")
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'cantidad1')))\
        .send_keys("1")
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'cantidad2')))\
        .send_keys("1")
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #CLICK BOTONES PARA AGREGAR AL CARRITO
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="btn0"]')))\
        .click()
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="btn1"]')))\
        .click()
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="btn2"]')))\
        .click()
    except NoSuchElementException:
            time.sleep(1)
    #scroll
    time.sleep(2)
    try:
            driver.execute_script("window.scrollTo(0, 1000);")
    except NoSuchElementException:
            time.sleep(1)
    #BOTON COMPRAR
    time.sleep(2)
    try:
        link= WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'btnComprar')))\
        .click()
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #LLENAR DIRECCION Y NUMERO DE CONTACTO
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                        'numeroContacto')))\
        .send_keys(numContacto.value)
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                        'direccionEnvio')))\
        .send_keys(dirEnvio.value)
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(1)
    #LLENAR NUMERO DE CUENTA
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                        'cuenta')))\
        .send_keys(nCuenta.value)
    except NoSuchElementException:
            time.sleep(1)
    #scroll
    time.sleep(2)
    try:
            driver.execute_script("window.scrollTo(0, 1000);")
    except NoSuchElementException:
            time.sleep(1)
    #CLICK bOTON PAGAR
    time.sleep(2)
    try:
        link= WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'btn-pagar')))\
        .click()
    except NoSuchElementException:
            time.sleep(1)

    time.sleep(2)
    #LOG OUT VOLVER AL LOGIN
    #WebDriverWait(driver, 5)\
    #.until(EC.element_to_be_clickable((By.ID,
    #                                'navbarDropdownMenuLink')))\
    #.click()
driver.close()

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='PRUEBAS DE REGISTRO'))


