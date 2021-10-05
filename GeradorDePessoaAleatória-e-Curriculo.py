from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Chrome()

driver.get("https://www.4devs.com.br/gerador_de_pessoas")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'1. Qual sexo?')]")))
sexo = random.randrange(0, 2)
if(sexo == 1):
    driver.find_element_by_xpath("//body/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
else:
    driver.find_element_by_xpath("//body/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/label[1]/span[1]").click()

# Sorteia um número entre 18 e 80 e escolhe a idade da pessoa no site
idadePessoa = str(random.randrange(18, 80))
idade = Select(driver.find_element_by_xpath("//select[@id='idade']"))
idade.select_by_visible_text(idadePessoa)
time.sleep(3)

# Vetor com todos os estados do Brasil
estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES","GO","MA"," MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS"
"RO", "RR", "SP", "TO", "SE"]

# Quantidade de municípios de cada estado. 
# Cada valor dos indices do vetor "qtd_de_Municipios" é respectivo ao indices do vetor "estados"
qtd_de_Municipios = [23, 102, 16, 64, 417, 184, 1, 78, 246, 217, 141, 79, 853, 144, 
223, 339, 185, 224, 92, 167, 497, 52, 15, 645, 139, 75]

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='cep_estado']")))
estadoAleatorio = random.randrange(0, 26)
driver.find_element_by_xpath("//select[@id='cep_estado']").click()
i = 0
while(i < estadoAleatorio):
    driver.find_element_by_xpath("//select[@id='cep_estado']").send_keys(Keys.ARROW_DOWN)
    i += 1
driver.find_element_by_xpath("//select[@id='cep_estado']").send_keys(Keys.ENTER)

cidadeAleatoria = random.randrange(qtd_de_Municipios[estadoAleatorio])
driver.find_element_by_xpath("//select[@id='cep_cidade']").click()
y = 0
while (y < cidadeAleatoria):
    driver.find_element_by_xpath("//select[@id='cep_cidade']").send_keys(Keys.ARROW_DOWN)
    y += 1
driver.find_element_by_xpath("//select[@id='cep_cidade']").send_keys(Keys.ENTER)

pontuacao = random.randrange(0, 2)
if(pontuacao == 1):
    driver.find_element_by_xpath("//body/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/label[1]/span[1]").click()
else:
    driver.find_element_by_xpath("//body/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[4]/div[1]/div[3]/label[1]/span[1]").click()

qtd_de_pessoas_geradas = 1
driver.find_element_by_xpath("//input[@id='txt_qtde']").clear()
driver.find_element_by_xpath("//input[@id='txt_qtde']").send_keys(qtd_de_pessoas_geradas)

driver.find_element_by_xpath("//input[@id='bt_gerar_pessoa']").click()

time.sleep(20)


