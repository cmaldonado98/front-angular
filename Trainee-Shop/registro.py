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
#import xmlrunner
import unittest
from selenium.common.exceptions import NoSuchElementException

#Opciones de navegacion
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver_path = './Drivers/chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)
#Iniciar en la pantalla 2
driver.set_window_position(2000,0)
driver.maximize_window()
time.sleep(1)

#Iniciamos el navegador
driver.get("http://a1a17f2828c0f4d7f83ff926804b9a74-1091942866.us-west-1.elb.amazonaws.com")
#driver.get('http://localhost:4200')

#Apertura a Excel
filesheet="../excel/registro.xlsx"
wb=load_workbook(filesheet)
hojas= wb.get_sheet_names()
print(hojas)
nombres = wb.get_sheet_by_name("registro")
wb.close()
#time.sleep(3)
for i in range(2,3):
    namelast, phone,email, direc, user,password,confirmpass = nombres[f'A{i}:G{i}'][0]
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
    time.sleep(1)
    #LLENA NOMBRE Y APELLIDO
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'nombre')))\
        .send_keys(namelast.value)
    except NoSuchElementException:
            time.sleep(1)
    #LLENA TELEFONO
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'celular')))\
        .send_keys(phone.value)
    except NoSuchElementException:
            time.sleep(1)
    #LLENA EMAIL
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'email')))\
        .send_keys(email.value)
    except NoSuchElementException:
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
    #LLENA CONTRASEÑA
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'contrasena')))\
        .send_keys(password.value)
    except NoSuchElementException:
            time.sleep(1)
    #CONFIRMA CONTRASEÑA
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'confirmContrasena')))\
        .send_keys(confirmpass.value)
    except NoSuchElementException:
            time.sleep(2)
    #CLICK BOTON REGISTRAR
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.NAME,
                                    'addButton')))\
        .click()
    except NoSuchElementException:
            time.sleep(1)
    time.sleep(3)
    #LOG OUT
    #WebDriverWait(driver, 5)\
    #.until(EC.element_to_be_clickable((By.ID,
    #                                'navbarDropdownMenuLink')))\
    #.click()
    #time.sleep(4)

    driver.close()

if __name__ == '__main__':
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='PRUEBAS DE REGISTRO'))
