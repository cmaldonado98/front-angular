#librerias
#import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from openpyxl import load_workbook
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
filesheet="../excel/test_respaldo.xlsx"
wb=load_workbook(filesheet)
hojas= wb.get_sheet_names()
print(hojas)
nombres = wb.get_sheet_by_name("test")
wb.close()
time.sleep(2)
for i in range(2,3):
    ci, password = nombres[f'E{i}:F{i}'][0]
    print(ci.value, password.value)
    #time.sleep(3)
    #LLENAR CEDULA
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                        'login')))\
        .send_keys(ci.value)
    except NoSuchElementException:
            time.sleep(1)
    #LLENAR PASSWORD
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'password')))\
        .send_keys(password.value)
    except NoSuchElementException:
            time.sleep(1)

    #CLICK BOTON INICIAR SESION
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'btn-login')))\
        .click()
    except NoSuchElementException:
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
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'cantidad1')))\
        .send_keys("1")
    except NoSuchElementException:
            time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                    'cantidad2')))\
        .send_keys("1")
    except NoSuchElementException:
            time.sleep(1)
    #CLICK BOTONES PARA AGREGAR AL CARRITO
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="btn0"]')))\
        .click()
    except NoSuchElementException:
            time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="btn1"]')))\
        .click()
    except NoSuchElementException:
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
    #LLENAR DIRECCION Y NUMERO DE CONTACTO
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                        'numeroContacto')))\
        .send_keys("0992606306")
    except NoSuchElementException:
            time.sleep(1)
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                        'direccionEnvio')))\
        .send_keys("Av. Loja")
    except NoSuchElementException:
            time.sleep(1)
    #LLENAR NUMERO DE CUENTA
    try:
        link=WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.ID,
                                        'cuenta')))\
        .send_keys("5555555555")
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

