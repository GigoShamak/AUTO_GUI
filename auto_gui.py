# Abrir arquivo
# identificar ângulo X e Y do arquivo
# Copiar nome do pagante
# fechar arquivo ctrl+w
# Renomear arquivo f2
# Apertar seta baixo
# repetir processo 
    
import pyautogui as py

def copia_texto():
    py.moveTo(x=posicao_texto_inicial_x,y=posicao_texto_inicial_y)
    py.PAUSE = tempo_de_delay
    py.mouseDown()
    py.PAUSE = tempo_de_delay
    py.moveTo(x=posicao_texto_final_x, y=posicao_texto_final_y)
    py.PAUSE = tempo_de_delay
    py.mouseUp()
    py.PAUSE = tempo_de_delay
    py.hotkey("ctrl","c")
    py.PAUSE = tempo_de_delay
    py.hotkey("ctrl","w")
    py.PAUSE = tempo_de_delay
    py.press("f2")
    py.PAUSE = tempo_de_delay
    py.hotkey("ctrl","v")
    py.PAUSE = tempo_de_delay

# Variáveis

tempo_de_delay = 1
tempo_de_abertura = 3
auxiliador = 1

import pyautogui as py
arquivo = input("Selecione o arquivo inicial: ")
arquivo = py.position()

posicao_do_arquivo_x = arquivo[0]
posicao_do_arquivo_y = arquivo[1]

# informa o eixo X
# print(posicao_do_arquivo[0])

# informa o eixo Y
# print(posicao_do_arquivo[1])

texto_inicial = input("Selecione o inicio do trecho a ser copiado: ")
texto_inicial = py.position()

posicao_texto_inicial_x = texto_inicial[0]
posicao_texto_inicial_y = texto_inicial[1]

texto_final = input("Posicione no final do trecho a ser copiado: ")
texto_final = py.position()

posicao_texto_final_x = texto_final[0]
posicao_texto_final_y = texto_final[1]

qtd_arquivos = int(input("Informe a quantidade de arquivos: "))

print(f"{qtd_arquivos} serão nomeados.")
aceite = input("Deseja continuar? (S/N)")

py.hotkey("alt","tab")
py.PAUSE = tempo_de_delay
py.press("enter")
py.PAUSE = tempo_de_abertura
    
while auxiliador <= qtd_arquivos: 
    # inicio do texto
    copia_texto()
    # fim do texto
    py.press("enter")
    py.PAUSE = tempo_de_delay
    py.press("down")
    py.PAUSE = tempo_de_delay
    py.press("enter")
    auxiliador = auxiliador + 1