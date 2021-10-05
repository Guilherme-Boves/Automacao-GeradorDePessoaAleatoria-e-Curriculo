from math import e
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
idade_pessoa = str(random.randrange(18, 80))
idade = Select(driver.find_element_by_xpath("//select[@id='idade']"))
idade.select_by_visible_text(idade_pessoa)

# Vetor com todos os estados do Brasil
estados = ["AC","AL","AM","AP","BA","CE","DF","ES","GO","MA","MG","MS","MT","PA","PB","PE","PI","PR","RJ","RN","RO","RR","RS","SE","SP","TO"]

# Quantidade de municípios de cada estado. 
# Cada valor dos indices do vetor "qtd_de_Municipios" é respectivo ao indices do vetor "estados"
qtd_de_municipios = [23, 102, 64, 16, 417, 184, 1, 78, 246, 79, 141, 217, 853, 144, 
339, 185, 223, 224, 92, 167, 52, 15, 497, 75, 645, 139]

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='cep_estado']")))
estado_aleatorio = random.randrange(0, 25)

estado_selecionado = Select(driver.find_element_by_xpath("//select[@id='cep_estado']"))
for i in range(estado_aleatorio):        
    estado_selecionado.select_by_visible_text(estados[estado_aleatorio])

cidade_aleatoria = random.randrange(qtd_de_municipios[estado_aleatorio])
driver.find_element_by_xpath("//select[@id='cep_cidade']").click()
for i in range(cidade_aleatoria):
    driver.find_element_by_xpath("//select[@id='cep_cidade']").send_keys(Keys.ARROW_DOWN)
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

xpath_nome = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[6]/div[1]/div[2]/div[1]/span[1]"
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath_nome)))
nome = driver.find_element_by_xpath(xpath_nome).text 

xpath_genero = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[6]/div[5]/div[2]/div[1]/span[1]"
genero = driver.find_element_by_xpath(xpath_genero).text

xpath_email = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[6]/div[10]/div[2]/div[1]/span[1]"
email = driver.find_element_by_xpath(xpath_email).text

xpath_cep = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[6]/div[12]/div[2]/div[1]/span[1]"
cep = driver.find_element_by_xpath(xpath_cep).text

xpath_endereco = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[6]/div[13]/div[2]/div[1]/span[1]"
endereco = driver.find_element_by_xpath(xpath_endereco).text

xpath_cidade = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[6]/div[16]/div[2]/div[1]/span[1]"
cidade = driver.find_element_by_xpath(xpath_cidade).text

xpath_telefone = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[6]/div[19]/div[2]/div[1]/span[1]"
telefone = driver.find_element_by_xpath(xpath_telefone).text

xpath_celular = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[6]/div[20]/div[2]/div[1]/span[1]"
celular = driver.find_element_by_xpath(xpath_celular).text

driver.get("https://www.4devs.com.br/gerador-de-curriculo")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']")))

# input nome
driver.find_element_by_xpath("//input[@id='name']").send_keys(nome)

#input email
driver.find_element_by_xpath("//input[@id='email']").send_keys(email)

#input idade
driver.find_element_by_xpath("//input[@id='age']").send_keys(idade_pessoa)

#select gênero
genero_pessoa = Select(driver.find_element_by_xpath("//select[@id='gender']"))
genero_pessoa.select_by_visible_text(genero)

#select estado civil
estado_civil_aleatorio = random.randrange(0, 5)
for i in range(estado_civil_aleatorio):
    driver.find_element_by_xpath("//select[@id='marital']").send_keys(Keys.ARROW_DOWN)
driver.find_element_by_xpath("//select[@id='marital']").send_keys(Keys.ENTER)

#input telefone
driver.find_element_by_xpath("//input[@id='telephone']").send_keys(telefone)

#input celular
driver.find_element_by_xpath("//input[@id='mobile']").send_keys(celular)

#input endereço
driver.find_element_by_xpath("//input[@id='address']").send_keys(endereco)

#input cidade
driver.find_element_by_xpath("//input[@id='city']").send_keys(cidade)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='state']")))
#input estado
for i in range(len(estados)):
    if(estados[estado_aleatorio] == estados[0]):
        estado_para_curriculo = "Acre"
    elif(estados[estado_aleatorio] == estados[1]):
        estado_para_curriculo = "Alagoas"
    elif(estados[estado_aleatorio] == estados[2]):
        estado_para_curriculo = "Amazonas"
    elif(estados[estado_aleatorio] == estados[3]):
        estado_para_curriculo = "Amapá"
    elif(estados[estado_aleatorio] == estados[4]):
        estado_para_curriculo = "Bahia"
    elif(estados[estado_aleatorio] == estados[5]):
        estado_para_curriculo = "Ceara"
    elif(estados[estado_aleatorio] == estados[6]):
        estado_para_curriculo = "Distrito Federal"
    elif(estados[estado_aleatorio] == estados[7]):
        estado_para_curriculo = "Espírito Santo"
    elif(estados[estado_aleatorio] == estados[8]):
        estado_para_curriculo = "Goiás"
    elif(estados[estado_aleatorio] == estados[9]):
        estado_para_curriculo = "Maranhão"
    elif(estados[estado_aleatorio] == estados[10]):
        estado_para_curriculo = "Minas Gerais"
    elif(estados[estado_aleatorio] == estados[11]):
        estado_para_curriculo = "Mato Grosso do Sul"
    elif(estados[estado_aleatorio] == estados[12]):
        estado_para_curriculo = "Mato Grosso"
    elif(estados[estado_aleatorio] == estados[13]):
        estado_para_curriculo = "Pará"
    elif(estados[estado_aleatorio] == estados[14]):
        estado_para_curriculo = "Paraíba"
    elif(estados[estado_aleatorio] == estados[15]):
        estado_para_curriculo = "Pernambuco"
    elif(estados[estado_aleatorio] == estados[16]):
        estado_para_curriculo = "Piauí"
    elif(estados[estado_aleatorio] == estados[17]):
        estado_para_curriculo = "Paraná"
    elif(estados[estado_aleatorio] == estados[18]):
        estado_para_curriculo = "Rio de Janeiro"
    elif(estados[estado_aleatorio] == estados[19]):
        estado_para_curriculo = "Rio Grande do Norte"
    elif(estados[estado_aleatorio] == estados[20]):
        estado_para_curriculo = "Rondônia"
    elif(estados[estado_aleatorio] == estados[21]):
        estado_para_curriculo = "Roraima"
    elif(estados[estado_aleatorio] == estados[22]):
        estado_para_curriculo = "Rio Grande do Sul"
    elif(estados[estado_aleatorio] == estados[23]):
        estado_para_curriculo = "Sergipe"
    elif(estados[estado_aleatorio] == estados[24]):
        estado_para_curriculo = "São Paulo"
    elif(estados[estado_aleatorio] == estados[25]):
        estado_para_curriculo = "Tocantins"
    
driver.find_element_by_xpath("//input[@id='state']").send_keys(estado_para_curriculo)

#input cep
driver.find_element_by_xpath("//input[@id='cep']").send_keys(cep)

#textarea Objetivo
driver.find_element_by_xpath("//textarea[@id='career-goal']").send_keys("Busco oportunidade como gerente de loja, para desenvolver minha vasta experiência no setor de vendas.")

#botão seguinte
driver.find_element_by_xpath("//input[@id='btnNext']").click()

#input curso
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]").send_keys("Análise e Desenvolvimento de Sistemas")

#input instituição
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("Fatec Itu")

#input ano de conclusão
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("2021")

#textarea Qualificações e cursos complementares
driver.find_element_by_xpath("//textarea[@id='other_courses']").send_keys("Informática Básica, Pacote Office e Inglês")

#botão seguinte
driver.find_element_by_xpath("//input[@id='btnNext']").click()

#input Empresa
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input[1]")))
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input[1]").send_keys("4R Tecnologia")

#input Inicio
ano_aleatorio = random.randrange(1960, 2021)
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys(ano_aleatorio)

#checkbox Trabalho atualmente na empresa
checkbox_trabalho = random.randrange(0, 2)
if(checkbox_trabalho == 1):
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/input[1]").click()
else:
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("2020")
#input cargo
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[3]/input[1]").send_keys("Analista de QA")

#textarea Descrição das suas principais funções na empresa
if(checkbox_trabalho == 1):
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[4]/textarea[1]").send_keys("Realizo testes para diversos sistemas")
else:
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[4]/textarea[1]").send_keys("Realizava testes para diversos sistemas")
#textarea Atividades Complementares
driver.find_element_by_xpath("//textarea[@id='other_activity']").send_keys("Professor de Inglês na Escola CNA Porto Feliz")

#botão pré-visualizar currículo
driver.find_element_by_xpath("//input[@id='btnPreview']").click()

time.sleep(20)