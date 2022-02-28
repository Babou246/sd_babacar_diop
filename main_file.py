
from tkinter import *
from Projets import *
from tkinter.filedialog import askopenfilename

# creer la fenetre
window = Tk()
window.title("Structure de données")
window.geometry("720x480")
window.minsize(480,360)
window.iconbitmap("")
window.config(background='#4065A4')

# creer la frame principale
frame = Frame(window, bg='#dee5dc')
def Open():
    Directory = askopenfilename(initialdir=r"/home/abubakr/Bureau/LES_TP_SONATEL_ACADEMY/TP_Python", title="Ouvrir le fichier",
                filetypes=(("fichier json","*.json"),
                ("fichier csv","*.csv"),
                ("fichier xml","*.xml"),
                ("fichier YAML","*.yaml")))
    ext = Directory.split(".")[-1]
    if ext == "csv":
        csv_path(Directory)
    elif ext == "xml":
        dic = dic_xml(Directory)
        return dic
    elif ext == "json":
        dic = dic_to_json(Directory)
        return dic
    elif ext == "yaml":
        dic = dict_yaml(Directory)
        return dic

# creation d'image
width = 300
height = 300
image = PhotoImage(file="fichiers/image.png").zoom(32).subsample(64)
# Creation de la frame principale
frame = Frame(window)

# Creation du canvas
canvas = Canvas(frame,width=width,height=height,bg="#4065A4",highlightthickness=0)
canvas.create_image(width/2,height/2,image=image)
canvas.grid(row=0,column=0,sticky=W)

right_frame = Frame(frame,bg="#4065A4")

label_title = Label(right_frame, text="Mot de Passe",font=("Helvetica",20), bg='#4065A4',fg="white")
label_title.pack()
# On crée un input
password_entry = Entry(right_frame,font=("Helvetica",20), bg='#4065A4',fg="white")
password_entry.pack()
# Création de button
bouton = Button(right_frame,font=("Helvetica",20),text=' JSON ', bg='#4065A4',fg="green",command=Open())
# bouton.pack(fill=X)
# bouton2 = Button(right_frame,font=("Helvetica",20),text=' CSV ', bg='#4065A4',fg="yellow",command=dic_to_csv(Directory))
# bouton2.pack(fill=X)
# bouton3 = Button(right_frame,font=("Helvetica",20),text=' XML ', bg='#4065A4',fg="red",command=dic_xml(Directory))
# bouton3.pack(fill=X)
# bouton4 = Button(right_frame,font=("Helvetica",20),text=' YAML ', bg='#4065A4',fg="white",command=dict_yaml(Directory))
# bouton4.pack(fill=X)
# bouton5 = Button(right_frame,font=("Helvetica",20),text='Open choice', bg='#4065A4',fg="white",command=dict_yaml(Directory))
# bouton5.pack(fill=X)




# # On place la sous boite à droite de la frame principale
# right_frame.grid(row=0,column=1,sticky=W)
# # ajout de la frame au centre
# frame.pack(expand=YES)
# affichage
window.mainloop()
