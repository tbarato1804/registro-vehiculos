import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta del ChromeDriver
chrome_driver_path = "C:/chromedriver/chromedriver.exe"

# Ruta del archivo CSV
csv_path = "vehiculos.csv"

# Configuración del navegador
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Leer archivo CSV y recorrer vehículos
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            print(f"🚗 Procesando vehículo: {row['placa']}")

            driver = webdriver.Chrome(service=service, options=options)
            wait = WebDriverWait(driver, 15)

            # Ingresar a la página
            driver.get("https://www.register2park.com/register")

            # Esperar unos segundos para que cargue la siguiente página del formulario (información del vehículo)
            time.sleep(2)

            # Llenar campos usando datos del CSV
            wait.until(EC.presence_of_element_located((By.ID, "propertyName"))).send_keys(row['propiedad'])

            # Esperar unos segundos para que cargue la siguiente página del formulario (información del vehículo)
            time.sleep(2)

            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))).click()

            # Esperar unos segundos para que cargue la siguiente página del formulario (información del vehículo)
            time.sleep(2)

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.select-property"))).click()

            # Esperar unos segundos para que cargue la siguiente página del formulario (información del vehículo)
            time.sleep(2)
            
            wait.until(EC.element_to_be_clickable((By.ID, "registrationTypeVisitor"))).click()

            # Esperar unos segundos para que cargue la siguiente página del formulario (información del vehículo)
            time.sleep(2)

            wait.until(EC.presence_of_element_located((By.ID, "vehicleApt"))).send_keys(row['apartamento'])           
            wait.until(EC.element_to_be_clickable((By.ID, "vehicleMake"))).send_keys(row['marca'])
            wait.until(EC.element_to_be_clickable((By.ID, "vehicleModel"))).send_keys(row['modelo'])
            wait.until(EC.element_to_be_clickable((By.ID, "vehicleLicensePlate"))).send_keys(row['placa'])
            wait.until(EC.element_to_be_clickable((By.ID, "vehicleLicensePlateConfirm"))).send_keys(row['placa'])

            # Esperar unos segundos para que cargue la siguiente página del formulario (información del vehículo)
            time.sleep(2)
            
            wait.until(EC.element_to_be_clickable((By.ID, "vehicleInformation"))).click()

            # Enviar por email
            wait.until(EC.element_to_be_clickable((By.ID, "email-confirmation"))).click()
            
            # Esperar unos segundos para que cargue la siguiente página del formulario (información del vehículo)
            time.sleep(2)
            
            wait.until(EC.presence_of_element_located((By.ID, "emailConfirmationEmailView"))).send_keys(row['email'])

            # Esperar unos segundos para que cargue la siguiente página del formulario (información del vehículo)
            time.sleep(2)
            
            wait.until(EC.element_to_be_clickable((By.ID, "email-confirmation-send-view"))).click()

            print(f"✅ Registro completado y enviado para: {row['placa']}")
            time.sleep(3)  # Espera antes de cerrar

        except Exception as e:
            print(f"❌ Error con el vehículo {row['placa']}: {e}")
        finally:
            driver.quit()
            time.sleep(2)  # Pausa entre vehículos
