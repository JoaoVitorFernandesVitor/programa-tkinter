from tkinter import *
from fucoes import *



#Iniciando a tela principal
screen = Tk()

#Propriedades da tela
altura = 600
largura = 800
titulo = 'Login'
icone = ''

#Centralizando a Tela
tela_x = Centerx(screen, largura)
tela_y = Centery(screen, altura)

#Programação da Tela
screen.geometry('%dx%d+%d+%d'%(largura, altura, tela_x, tela_y))
screen.title(titulo)
#screen.icon= icone

#Adicionando Widgets
login = Login(screen)
screen.mainloop()