'''
author : ferdivdb
date : 19/12/2021

'''

from tkinter import *
import webbrowser

def open_ferdivdb_website():
	webbrowser.open_new("http://ferdivdb.be")

# création fenêtre
window = Tk()
# personnaliser la fenêtre
window.title("Ferduck")
window.geometry("1080x720")
window.minsize(480, 360)
window.iconbitmap("~/Documents/repo/perso/my_first_app/logo.ico")
window.config(background='#41B77F')


# création de frame
frame = Frame(window, bg='#41B77F')

# Image
img=PhotoImage(file='~/Documents/repo/perso/my_first_app/logo.png')
Label(frame, image=img, bg='#41B77F').pack()

# ajouter du texte
label_title = Label(frame, text='Welcome to Ferduck', font=("Roboto", 35), bg='#41B77F')
label_title.pack()

label_subtitle = Label(frame, text='Here you will find everything you want', font=("Roboto", 17), bg='#41B77F')
label_subtitle.pack()

# ajouter bouton
website_button = Button(frame, text="website", font=("Roboto", 25), bg='red', fg='#41B77F', command=open_ferdivdb_website)
website_button.pack(pady=25, fill=X)

# ajouter
frame.pack(expand='YES')

# affichage
window.mainloop()