'''
author : ferdivdb
date : 19/12/2021

'''
from tkinter import *
from random import randint, choice
import string

def generate_password():
	password_min = 24
	password_max = 26
	all_chars = string.ascii_letters + string.punctuation + string.digits
	password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
	password_entry.delete(0, END)
	password_entry.insert(0, password)


# creer fenetre
window = Tk()
window.title("Password generator")
window.geometry("1080x720")
window.iconbitmap("logo.ico")
window.config(background='#41B77F')

# creation de frame principale
frame = Frame(window, bg='#41B77F')

# création d'image
width = 300
height = 300
image = PhotoImage(file='password_little.png')
canvas = Canvas(frame, width=width, height=height, bg='#41B77F', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creer une sous boite
right_frame = Frame(frame, bg='#41B77F')

# creer un titre
label_title = Label(right_frame, text='Mot de passe', font=('Roboto', 36), bg='#41B77F', fg='black')
label_title.pack()

# creer un input
password_entry = Entry(right_frame, font=('Roboto', 36), bg='#41B77F', fg='black')
password_entry.pack()

# creer un boutton
generate_password_button= Button(right_frame, text='Générer', font=('Roboto', 18), bg='#41B77F', fg='black', command=generate_password)
generate_password_button.pack(fill=X)

# place la sous boite a droite de la frame principale
right_frame.grid(row=0, column=1, sticky=W)



# afficher la frame
frame.pack(expand=YES)

# creation barre de menu
menu_bar = Menu(window)

# creer premier menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer fenetre pour ajouter menu bar
window.config(menu=menu_bar)

# afficher la fenetre
window.mainloop()