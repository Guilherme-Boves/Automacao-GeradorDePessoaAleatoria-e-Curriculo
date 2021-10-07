from math import e
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
from os.path import dirname, realpath


path = dirname(realpath(__file__))+"/"
options = webdriver.ChromeOptions()
prefs = {"download.default_directory" : path}
options.add_experimental_option("prefs",prefs)

# options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

print("\n\n*************** Iniciando a impressão do currículo ***************\n\n")

driver.get("https://www.4devs.com.br/gerador_de_pessoas")

# Escolhe o Gênero da pessoa
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'1. Qual sexo?')]")))
genero = random.randrange(0, 2)
if(genero == 1):
    driver.find_element_by_xpath("//body/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/label[1]/span[1]").click()
else:
    driver.find_element_by_xpath("//body/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/label[1]/span[1]").click()

# Sorteia um número entre 18 e 80 e escolhe a idade da pessoa
idade_pessoa = str(random.randrange(18, 80))
idade = Select(driver.find_element_by_xpath("//select[@id='idade']"))
idade.select_by_visible_text(idade_pessoa)

# Escolhendo um estado aleatório
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='cep_estado']")))
estado_aleatorio = Select(driver.find_element_by_xpath("//select[@id='cep_estado']"))
while len(estado_aleatorio.options) == 1:
    estado_aleatorio = Select(driver.find_element_by_xpath("//select[@id='cep_estado']"))
estado_aleatorio.select_by_index(random.randrange(1, len(estado_aleatorio.options)))

# Escolhendo uma cidade aleatória
cidade_aleatoria = Select(driver.find_element_by_xpath("//select[@id='cep_cidade']"))
while len(cidade_aleatoria.options) == 1:
    cidade_aleatoria = Select(driver.find_element_by_xpath("//select[@id='cep_cidade']"))
cidade_aleatoria.select_by_index(random.randrange(1, len(cidade_aleatoria.options)))

# Definindo aleatoriamente se o usuário possui pontuação ou não
pontuacao = random.randrange(0, 2)
if(pontuacao == 1):
    driver.find_element_by_xpath("//body/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/label[1]/span[1]").click()
else:
    driver.find_element_by_xpath("//body/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[2]/div[2]/div[4]/div[1]/div[3]/label[1]/span[1]").click()

# Definindo a quantidade de pessoas geradas
qtd_de_pessoas_geradas = 1
driver.find_element_by_xpath("//input[@id='txt_qtde']").clear()
driver.find_element_by_xpath("//input[@id='txt_qtde']").send_keys(qtd_de_pessoas_geradas)

# Aciona o botão "Gerar pessoa"
driver.find_element_by_xpath("//input[@id='bt_gerar_pessoa']").click()

# Copia as informações pessoais da pessoa, como nome, genero, email, cep, endereço...
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

estado = driver.find_element_by_xpath("//div[@id='estado']").text

xpath_telefone = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[6]/div[19]/div[2]/div[1]/span[1]"
telefone = driver.find_element_by_xpath(xpath_telefone).text

xpath_celular = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/div[6]/div[20]/div[2]/div[1]/span[1]"
celular = driver.find_element_by_xpath(xpath_celular).text

driver.get("https://www.4devs.com.br/gerador-de-curriculo")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']")))
# input nome
driver.find_element_by_xpath("//input[@id='name']").send_keys(nome)

# input email
driver.find_element_by_xpath("//input[@id='email']").send_keys(email)

# input idade
driver.find_element_by_xpath("//input[@id='age']").send_keys(idade_pessoa)

# select gênero
genero_pessoa = Select(driver.find_element_by_xpath("//select[@id='gender']"))
genero_pessoa.select_by_visible_text(genero)

# select estado civil
estado_civil_aleatorio = Select(driver.find_element_by_xpath("//select[@id='marital']"))
while len(estado_civil_aleatorio.options) == 1:
    estado_civil_aleatorio = Select(driver.find_element_by_xpath("//select[@id='marital']"))
estado_civil_aleatorio.select_by_index(random.randrange(1, len(estado_civil_aleatorio.options)))

# input telefone
driver.find_element_by_xpath("//input[@id='telephone']").send_keys(telefone)

# input celular
driver.find_element_by_xpath("//input[@id='mobile']").send_keys(celular)

# input endereço
driver.find_element_by_xpath("//input[@id='address']").send_keys(endereco)

# input cidade
driver.find_element_by_xpath("//input[@id='city']").send_keys(cidade)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='state']")))
#input estado
if(estado == "AC"):
    estado_para_curriculo = "Acre"
elif(estado == "AL"):
    estado_para_curriculo = "Alagoas"
elif(estado == "AM"):
    estado_para_curriculo = "Amazonas"
elif(estado == "AP"):
    estado_para_curriculo = "Amapá"
elif(estado == "BA"):
    estado_para_curriculo = "Bahia"
elif(estado == "CE"):
    estado_para_curriculo = "Ceara"
elif(estado == "DF"):
    estado_para_curriculo = "Distrito Federal"
elif(estado == "ES"):
    estado_para_curriculo = "Espírito Santo"
elif(estado == "GO"):
    estado_para_curriculo = "Goiás"
elif(estado == "MA"):
    estado_para_curriculo = "Maranhão"
elif(estado == "MG"):
    estado_para_curriculo = "Minas Gerais"
elif(estado == "MS"):
    estado_para_curriculo = "Mato Grosso do Sul"
elif(estado == "MT"):
    estado_para_curriculo = "Mato Grosso"
elif(estado == "PA"):
    estado_para_curriculo = "Pará"
elif(estado == "PB"):
    estado_para_curriculo = "Paraíba"
elif(estado == "PE"):
    estado_para_curriculo = "Pernambuco"
elif(estado == "PI"):
    estado_para_curriculo = "Piauí"
elif(estado == "PR"):
    estado_para_curriculo = "Paraná"
elif(estado == "RJ"):
    estado_para_curriculo = "Rio de Janeiro"
elif(estado == "RN"):
    estado_para_curriculo = "Rio Grande do Norte"
elif(estado == "RO"):
    estado_para_curriculo = "Rondônia"
elif(estado == "RR"):
    estado_para_curriculo = "Roraima"
elif(estado == "RS"):
    estado_para_curriculo = "Rio Grande do Sul"
elif(estado == "SE"):
    estado_para_curriculo = "Sergipe"
elif(estado == "SP"):
    estado_para_curriculo = "São Paulo"
elif(estado == "TO"):
    estado_para_curriculo = "Tocantins"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='state']")))    
driver.find_element_by_xpath("//input[@id='state']").send_keys(estado_para_curriculo)

# input cep
driver.find_element_by_xpath("//input[@id='cep']").send_keys(cep)

# textarea Objetivo
driver.find_element_by_xpath("//textarea[@id='career-goal']").send_keys("Busco oportunidade como gerente de loja, para desenvolver minha vasta experiência no setor de vendas.")

# botão seguinte
driver.find_element_by_xpath("//input[@id='btnNext']").click()

# input curso
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[1]/input[1]").send_keys("Análise e Desenvolvimento de Sistemas")

# input instituição
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("Fatec Itu")

# input ano de conclusão
ano_conclusao = (2021 - int(idade_pessoa)) + 18
ano_conclusao_aux = random.randrange(ano_conclusao, 2021)
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys(ano_conclusao_aux)

# textarea Qualificações e cursos complementares
driver.find_element_by_xpath("//textarea[@id='other_courses']").send_keys("Informática Básica\n Pacote Office\n Inglês avançado")

# botão seguinte
driver.find_element_by_xpath("//input[@id='btnNext']").click()

# input Empresa
xpath_empresa = "/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input[1]"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_empresa)))
driver.find_element_by_xpath(xpath_empresa).send_keys("Empresa X")

# input "Inicio em"
ano_trabalho = (2021 - int(idade_pessoa)) + 18
ano_aleatorio = random.randrange(ano_trabalho, 2021)
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys(ano_aleatorio)

# checkbox Trabalho atualmente na empresa
checkbox_trabalho = random.randrange(0, 2)
if(checkbox_trabalho == 1):
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[2]/input[1]").click() 
else:
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("2021")

# input cargo
driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[3]/input[1]").send_keys("Analista de QA")

# textarea Descrição das suas principais funções na empresa
if(checkbox_trabalho == 1):
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[4]/textarea[1]").send_keys("Realizo testes para diversos sistemas")
else:
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[4]/textarea[1]").send_keys("Realizava testes para diversos sistemas")
# textarea Atividades Complementares
driver.find_element_by_xpath("//textarea[@id='other_activity']").send_keys("Professor de Inglês")

# botão pré-visualizar currículo
driver.find_element_by_xpath("//input[@id='btnPreview']").click()

# botão para baixar o pdf
xpath_botão_pdf = "//body/main[1]/div[1]/div[2]/div[1]/div[4]/div[1]/article[1]/div[1]/div[3]/div[1]/div[1]/input[1]"
time.sleep(1)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_botão_pdf)))
driver.find_element_by_xpath(xpath_botão_pdf).click()   

print("\n\n*************** Impressão concluída ***************\n\n")

time.sleep(2)