from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Número de telefone e mensagem
contato = "5583987470126"
texto = "Oi, esta mensagem foi enviada usando Selenium"

# Inicializa o navegador
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

# Aguarde até que o usuário escaneie o código QR manualmente para iniciar a sessão

# Agora você pode obter o link diretamente para o envio da mensagem
link = f"https://web.whatsapp.com/send?phone={contato}&text={texto}"

time.sleep(20)
navegador.get(link)
time.sleep(10)  # Ajuste o tempo conforme necessário para garantir que a página carregue completamente
# Agora, você precisa encontrar o elemento de input de texto e enviar a mensagem
campo_mensagem = navegador.find_element("xpath", "//div[@contenteditable='true']")
campo_mensagem.send_keys(Keys.ENTER)

# Feche o navegador
# navegador.quit()
