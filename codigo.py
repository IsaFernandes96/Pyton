from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
# Passo 1:
navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_videoselenium")

navegador.maximize_window()
navegador.find_element('xpath', 
                       '//*[@id="firstname"]').send_keys("Isabelle")
navegador.find_element('xpath', 
                       '//*[@id="email"]').send_keys("bebellefernandes96@gmail.com")
navegador.find_element('xpath', 
                       '//*[@id="phone"]').send_keys("11948849445")
navegador.find_element('xpath', '//*[@id="_form_1925_submit"]').click()
navegador.find_element('xpath', '//*[@id="botao-minicurso"]').click()
navegador.maximize_window()
input ()

