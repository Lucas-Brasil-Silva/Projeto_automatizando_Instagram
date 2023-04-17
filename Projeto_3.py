from selenium   import webdriver
from selenium.webdriver.chrome.service  import Service  as ChromeService
from webdriver_manager.chrome   import ChromeDriverManager
from selenium.webdriver.chrome.options  import Options
from selenium.webdriver.support.ui    import WebDriverWait
from selenium.common.exceptions   import *
from selenium.webdriver.support  import expected_conditions as CondicaoEsperada
from selenium.webdriver.common.by  import By
from time   import sleep
import random

def iniciar_driver():
    chromeoptions = Options()
    arguments = ['--lang=pt-BR', 'window-size=800,800']
    for argument in arguments:
        chromeoptions.add_argument(argument)
    
    chromeoptions.add_experimental_option(
        'excludeSwitches', ['enable-logging'])

    chromeoptions.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()),options=chromeoptions)

    wait = WebDriverWait(
        driver,
        timeout=10,
        poll_frequency=1,
        ignored_exceptions=[
            ElementNotVisibleException,
            ElementNotInteractableException,
            NoSuchElementException,
        ]
        )


    return driver, wait

def digitando_humanamente(text, element):
    for letra in text:
        element.send_keys(letra)
        sleep(random.randint(1, 5)/30)

login_usuario = input('Digite seu E-mail de login: ')
senha_usuario = input('Digite sua senha de login: ')

driver, wait = iniciar_driver()
driver.get('https://www.instagram.com/')
sleep(5)

campo_usuario = wait.until(CondicaoEsperada.element_to_be_clickable((
    By.XPATH, '//input[@name="username"]')))
sleep(2)
digitando_humanamente(login_usuario, campo_usuario)

campo_senha = wait.until(CondicaoEsperada.element_to_be_clickable(
    (By.XPATH, '//input[@name="password"]')))
sleep(2)
digitando_humanamente(senha_usuario, campo_senha)

botao_entrar = wait.until(CondicaoEsperada.element_to_be_clickable(
    (By.XPATH, '//button[@class="_acan _acap _acas _aj1-"]')))
sleep(2)
botao_entrar.click()

wait.until(CondicaoEsperada.visibility_of_all_elements_located(
    (By.XPATH, '//div[@class="x2lah0s x1n2onr6 x1to3lk4 xh8yej3"]')))
sleep(2)

while True:
    driver.get(
        'https://www.instagram.com/style_singlle/')

    wait.until(CondicaoEsperada.visibility_of_all_elements_located(
        (By.XPATH, '//span[@class= "_aacl _aaco _aacw _aacx _aad7 _aade"]')))
    sleep(2)
    driver.execute_script('window.scrollTo(0, 500)')
    sleep(1)
    postagens = wait.until(CondicaoEsperada.visibility_of_all_elements_located(
        (By.XPATH, '//div[@class="_aagw"]')))
    sleep(1)
    postagens[0].click()

    botoes_arial = wait.until(CondicaoEsperada.visibility_of_all_elements_located(
        (By.XPATH, '//div[@class="_abm0 _abl_"]')))
    sleep(2)

    if len(botoes_arial) == 6:
        botoes_arial[1].click()
        sleep(86400)
    else:
        print('Postagem já foi Curtida')
        sleep(86400)

driver.close()