import pyautogui
import string
import random



def pesquisas():
    
    pyautogui.PAUSE = 1.5 # pausa de 1.5 segundos entre comandos
    pyautogui.press("win")
    pyautogui.write("microsoft edge")
    pyautogui.press("enter")
    pyautogui.write(random.choice(string.ascii_letters))

    """
        Repete 34 pesquisas respectivamente para, Edge e PC: 0/12p e 0/90p; com vpn 0/20p e 0/150p.
        Cada pesquisa vale 3 pontos e 5 com vpn
        Total: 262
    """

    for i in range(34):

        pyautogui.press("enter") # pressiona enter
        
        if i == 33:
            break
        else:
            pyautogui.click(x=348, y=105) # clica no espaço de pesquisa
            pyautogui.write(random.choice(string.ascii_letters)) # escreve 


    #pyautogui.hotkey("ctrl", "tab") # proxima página
    pyautogui.hotkey("ctrl","shift", "c") # ativa inspecionar elemento
    pyautogui.hotkey("ctrl","shift", "m") # ativa modo mobile
    pyautogui.hotkey("ctrl","shift", "c") # desativa inspecionar elemento
    pyautogui.click(x=281, y=160) # clica no espaço de pesquisa
    pyautogui.write(random.choice(string.ascii_letters)) # escreve na barra de pesquisa

    """
        Repete Mobile 20 pesquisas 0/60; com vpn 0/100 
        Cada pesquisa vale 3 pontos e 5 com vpn
        Total: 160
    """
    for i in range(20):

        pyautogui.press("enter")
        
        if i == 19:
            break
        else:
            pyautogui.click(x=364, y=182)
            pyautogui.write(random.choice(string.ascii_letters))
        


    pyautogui.hotkey("ctrl","shift", "c") # ativa inspecionar elemento
    pyautogui.hotkey("ctrl","shift", "m") # desativa modo mobile
    pyautogui.hotkey("ctrl","shift", "c") # desativa inspecionar elemento
    pyautogui.hotkey("alt","f4") #fecha todas as janelas do edge


    """
        Total de pesquisas por dia: 422p
        Total de pesquisas por dia: 12.660p
        Gamepass(12.000p) todo mês :-)
        Obs.: com vpn
    """

"""
def vpn():
    
    pyautogui.press("win") # tecla windows
    pyautogui.write("TunnelBear") # pesquisa o vpn
    pyautogui.press("enter") # tecla enter
    pyautogui.click(x=392, y=96) # ativa vpn
    pyautogui.hotkey("alt","tab") # alterna a aba anterior 
    
# Chama funções e realiza o código normalmente mas se alguma tecla for ativada pelo usuário para o código
"""    


pesquisas()
