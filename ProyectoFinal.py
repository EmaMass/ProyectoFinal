import ctypes as c
import tkinter as tk
#import pygame

lib = c.CDLL(r"Debug\ProyectoFinal.dll")        

#def play_sound_effect():
 #   pygame.init()
  #  pygame.mixer.init()
   # pygame.mixer.music.load('towerSound.wav')
    #pygame.mixer.music.play()

def salir(): 
    root.quit()

def disable_take():
    take_buttons = [take_button1, take_button2, take_button3]

    for button in take_buttons:
        button.config(state=tk.DISABLED)

def disable_place():
    place_buttons = [place_button1, place_button2, place_button3]

    for button in place_buttons:
        button.config(state=tk.DISABLED)

def enable_take():
    take_buttons = [take_button1, take_button2, take_button3]

    for button in take_buttons:
        button.config(state=tk.NORMAL)

def enable_place():
    place_buttons = [place_button1, place_button2, place_button3]

    for button in place_buttons:
        button.config(state=tk.NORMAL)

def moverDisco(disco, horizontal, vertical):
    if disco == 1:
        label1.place(x=horizontal,y=vertical)
    elif disco == 2:
        label2.place(x=horizontal,y=vertical)
    elif disco == 3:
        label3.place(x=horizontal,y=vertical)
    else:
        label4.place(x=horizontal,y=vertical)

#Ventana principal
root = tk.Tk()
root.title("Torre de Hanoi")
root.geometry("700x500")
var = tk.IntVar(root, 0)
#importar foto
img = tk.PhotoImage(file="hanoibase2.png")
disc1 = tk.PhotoImage(file="hanoi1.png")
disc2 = tk.PhotoImage(file="hanoi2.png")
disc3 = tk.PhotoImage(file="hanoi3.png")
disc4 = tk.PhotoImage(file="hanoi4.png")
disc5 = tk.PhotoImage(file="hanoi5.png")
disc6 = tk.PhotoImage(file="hanoi6.png")
disc7 = tk.PhotoImage(file="hanoi7.png")

imglb = tk.Label(root,image=img)
label1 = tk.Label(root,image = disc1)
label2 = tk.Label(root,image = disc2)
label3 = tk.Label(root,image = disc3)
label4 = tk.Label(root,image = disc4)
label5 = tk.Label(root,image = disc5)
label6 = tk.Label(root,image = disc6)
label7 = tk.Label(root,image = disc7)
#colocar en su posicion inicial
imglb.place(x=70,y=50)
label4.place(x=70,y=215) #2 x=260 #3 x=450
label3.place(x=80,y=175) #2 x=270 #3 x=460
label2.place(x=90,y=140) #2 x=280 #3 x=470
label1.place(x=100,y=100) #2 x=290 #3 x=480

#Crear botones
take_button1 = tk.Button(root, text="Take",command=lambda: var.set(1))
take_button2 = tk.Button(root, text="Take",command=lambda: var.set(2))
take_button3 = tk.Button(root, text="Take",command=lambda: var.set(3))
place_button1 = tk.Button(root, text="Place",command=lambda: var.set(1))
place_button2 = tk.Button(root, text="Place",command=lambda: var.set(2))
place_button3 = tk.Button(root, text="Place",command=lambda: var.set(3))
exit_button = tk.Button(root, text="Exit",command=lambda: salir())

take_button1.grid(row=3, column=0)
take_button2.grid(row=3, column=1)
take_button3.grid(row=3, column=2)
place_button1.grid(row=4, column=0)
place_button2.grid(row=4, column=1)
place_button3.grid(row=4, column=2)
exit_button.grid(row=4, column=3)

exit_button.config(state="disabled")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(2, weight=5)
root.grid_rowconfigure(4, weight=1)

print("Bienvenido")
#discos = int(input("Ingrese numero de discos en juego: "))
discos = 4 
torres = [[] for x in range(3)]
for i in range(discos, 0, -1):
    torres[0].append(i)

print("Inicio del juego: ")
for torre in torres:
    print(torre)
print("\n")
n = 0

while n == 0:
    disable_place()
    root.wait_variable(var)
    disable_take()
    enable_place()
    inicio = var.get()
    root.wait_variable(var)
    enable_take()
    fin = var.get()
    if 0 <= inicio <= 3 and 0 <= fin-1 <= 3 and inicio-1 != fin-1 and torres[inicio-1]:
        disco = torres[inicio-1].pop()
        horizontal = lib.moverImagen(disco,fin)
        tlength = len(torres[fin-1])
        vertical = lib.moverVertical(tlength)
        if torres[fin-1] == []:
            moverDisco(disco, horizontal, vertical)
            #play_sound_effect()
            torres[fin-1].append(disco)
            for torre in torres:
                print(torre)
            print("\n")
        else: 
            if disco < torres[fin-1][len(torres[fin-1])-1]:
                moverDisco(disco, horizontal, vertical)
                #play_sound_effect()
                torres[fin-1].append(disco)
                for torre in torres:
                    print(torre)
                print("\n")
            else:
                torres[inicio-1].append(disco)
                print("Invalido. Intente otra vez.")
    else:
        print("Invalido. Intente otra vez.")
        for torre in torres:
            print(torre)
        print("\n")
    if len(torres[2]) == 4:
        n = lib.wincondition(torres[2][3])
        exit_button.config(state='normal')
        #pygame.mixer_music.load('winsound.wav')
root.mainloop()
print("Fin")
