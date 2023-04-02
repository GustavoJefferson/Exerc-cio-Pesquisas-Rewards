import pyautogui
import random
import time
#import sys
import os 
import requests


    
def mousepos():
    
    time.sleep(5) #5 segundos para ativar próximo comando
    print(pyautogui.position()) # captura posição do mouse (x,y)        

def abrirnav():
    
    pyautogui.PAUSE = 1.5 # pausa de 1.5 segundos entre comandos
    pyautogui.press("win") # tecla windows
    pyautogui.write("microsoft edge") # escreve na barra de pesquisas
    pyautogui.press("enter") # entra navegador
    pyautogui.getWindowsWithTitle("edge")[0].maximize() # maximiza janela 
    
def pesquisas():
    
    letra = "abcdefgijklmnopqstuvwxyzABCDEFGIJKLMNOPQrSTUVWXYZ"
    pyautogui.PAUSE = 1.5 # pausa de 1.5 segundos entre comandos
    # escreve uma letra aleatória entre 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pyautogui.write(random.choice(letra)) 

    """
        Repete 34 pesquisas respectivamente para, Edge e PC: 0/12p e 0/90p; com vpn 0/20p e 0/150p.
        Cada pesquisa vale 3 pontos e 5 com vpn
        Total: 262
    """

    for i in range(34):

        pyautogui.press("enter") # pressiona enter
        pyautogui.click(x=348, y=105) # clica no espaço de pesquisa
        pyautogui.write(random.choice(letra)) # escreve 


    
    pyautogui.hotkey("ctrl","shift", "c") # ativa inspecionar elemento
    pyautogui.hotkey("ctrl","shift", "m") # ativa modo mobile
    pyautogui.hotkey("ctrl","shift", "c") # desativa inspecionar elemento
    pyautogui.click(x=281, y=160) # clica no espaço de pesquisa
    pyautogui.write(random.choice(letra)) # escreve na barra de pesquisa

    """
        Repete Mobile 20 pesquisas 0/60; com vpn 0/100 
        Cada pesquisa vale 3 pontos e 5 com vpn
        Total: 160
    """
    
    for i in range(20):
        
        pyautogui.press("enter")
        pyautogui.click(x=364, y=182)
        pyautogui.write(random.choice(letra))
        


    pyautogui.hotkey("ctrl","shift", "c") # ativa inspecionar elemento
    pyautogui.hotkey("ctrl","shift", "m") # desativa modo mobile
    pyautogui.hotkey("ctrl","shift", "c") # desativa inspecionar elemento
    pyautogui.hotkey("alt","f4") #fecha todas as janelas do edge

    
"""
        Total de pesquisas por dia: 422p
        Total de pesquisas por mês: 12.660p
        Gamepass(12.000p) todo mês :-)
        Obs.: com vpn
"""

# Chama funções e realiza o código normalmente mas se alguma tecla for ativada pelo usuário para o código

def vpn():
    
    pyautogui.PAUSE = 2
    pyautogui.press("win") # tecla windows
    pyautogui.write("TunnelBear") # pesquisa o vpn
    pyautogui.press("enter") # tecla enter
    pyautogui.click(x=392, y=96) # ativa vpn
    time.sleep(10)



def delay_print(text, delay):
    
    for i in text:
        time.sleep(delay)
        print(i, end='', flush = True) #end='' não pula a linha
        #sys.stdout.flush()
    print()
    
def check_internet():
    
    # checar conexão de internet 
    
    delay_print("Checando internet .............", 0.1)
    
    url = 'https://www.google.com'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        return False

def checar_internet():
    
    if not check_internet():
        print("Internet fora do ar!")
        print("Deseja testar novamente?(S/N)")   
        ans = input().upper()
        
        if ans == "S":
            checar_internet()
    
        elif ans == 'N':
            delay_print("Desativando .............", 0.1)
            os._exit(0)
    
        else:
            delay_print("Desativando .............", 0.1)
            os._exit(0)
    else:
        print("Internet OK!(ό‿ὸ)ﾉ")   
        
    
    
def getpesquisas():       
    
    print("Você deseja começar as pesquisas do rewards?(S/N)")
    ans = input().upper()
    
    if ans == "S":
        print("Caso deseje parar a execução mova o mouse até o canto superior esquerdo")
        delay_print("Ativando .............", 0.1)
        checar_internet()
        abrirnav()
        pesquisas()
        
            
    elif ans == 'N':
        delay_print("Desativando .............", 0.1)
        time.sleep(2)
        os._exit(0)
        #sys.exit()
    else:
        getpesquisas()

getpesquisas()
vpn()
abrirnav()
pesquisas()