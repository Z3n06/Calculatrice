import packaging 
import customtkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk, messagebox

app=customtkinter.CTk()
app.title("Calculatrice")
app.geometry("250x350")
app.config(bg="#000000")

font1=('Arial',20,'bold')

# Initialise des variables globales pour l'équation et le suivi de l'index d'insertion dans le champ de résultat
i=0
equation=""

# Fonction appelée lorsque les boutons numériques ou opérationnels sont cliqués
def show(value):
    global i 
    global equation
    # Si le bouton cliqué est "%", remplace par "/100"
    if(value=="%"):
        value="/100"
    # Ajoute la valeur à l'équation et à l'entrée du résultat
    equation+=value
    result_entry.insert(i,value)
    i=i+1

def clear():
    result_entry.delete(0,END)

def calculate():
    try: 
        global equation
        result=""
        result=eval(equation)
        clear()
        result_entry.insert(0,result)
    except:
        messagebox.showerror(title="Pas bon chef",message="Entrer un nombre valide")#affiche un pop up message error si la syntaxe n'est pas bonne

#création des bnoutons
ButtonScientifique = Button(app, text="Scientifique", command=lambda: messagebox.showinfo("Scientifique Mode", "Mode scientifique activé"))
ButtonScientifique.place(x=10, y=30)


result_entry=customtkinter.CTkEntry(app,width=250,fg_color="#000000",border_color="#000000")
result_entry.place(x=0,y=10)

Button1=customtkinter.CTkButton(app,command=clear,text="C",width=50,height=2,fg_color="#003366",hover_color="#003366")
Button1.place(x=10,y=60)

Button2=customtkinter.CTkButton(app,command=lambda:show("%"),text="%",width=50,height=2,fg_color="#003366",hover_color="#003366")
Button2.place(x=70,y=60)

Button3=customtkinter.CTkButton(app,command=lambda:show("/"),text="/",width=50,height=2,fg_color="#003366",hover_color="#003366")
Button3.place(x=130,y=60)

Button4=customtkinter.CTkButton(app,command=lambda:show("*"),text="*",width=50,height=2,fg_color="#003366",hover_color="#003366")
Button4.place(x=190,y=60)

Button5=customtkinter.CTkButton(app,command=lambda:show("7"),text="7",width=50,height=2,fg_color="#b5520b",hover_color="#b5520b")
Button5.place(x=10,y=120)

Button6=customtkinter.CTkButton(app,command=lambda:show("8"),text="8",width=50,height=2,fg_color="#b5520b",hover_color="#b5520b")
Button6.place(x=70,y=120)

Button7=customtkinter.CTkButton(app,command=lambda:show("9"),text="9",width=50,height=2,fg_color="#b5520b",hover_color="#b5520b")
Button7.place(x=130,y=120)

Button8=customtkinter.CTkButton(app,command=lambda:show("+"),text="+",width=50,height=2,fg_color="#003366",hover_color="#003366")
Button8.place(x=190,y=120)

Button9=customtkinter.CTkButton(app,command=lambda:show("4"),text="4",width=50,height=2,fg_color="#b5520b",hover_color="#b5520b")
Button9.place(x=10,y=180)

Button10=customtkinter.CTkButton(app,command=lambda:show("5"),text="5",width=50,height=2,fg_color="#b5520b",hover_color="#b5520b")
Button10.place(x=70,y=180)

Button11=customtkinter.CTkButton(app,command=lambda:show("6"),text="6",width=50,height=2,fg_color="#b5520b",hover_color="#b5520b")
Button11.place(x=130,y=180)

Button12=customtkinter.CTkButton(app,command=lambda:show("-"),text="-",width=50,height=2,fg_color="#003366",hover_color="#003366")
Button12.place(x=190,y=180)

Button13=customtkinter.CTkButton(app,command=lambda:show("0"),text="0",width=50,height=2,fg_color="#b5520b",hover_color="#b5520b")
Button13.place(x=10,y=240)

Button14=customtkinter.CTkButton(app,command=lambda:show("1"),text="1",width=50,height=2,fg_color="#b5520b",hover_color="#b5520b")
Button14.place(x=70,y=240)

Button15=customtkinter.CTkButton(app,command=lambda:show("2"),text="2",width=50,height=2,fg_color="#b5520b",hover_color="#b5520b")
Button15.place(x=130,y=240)

Button16=customtkinter.CTkButton(app,command=lambda:show("3"),text="3",width=50,height=2,fg_color="#b5520b",hover_color="#b5520b")
Button16.place(x=190,y=240)

Button17=customtkinter.CTkButton(app,command=lambda:show("."),text=".",width=50,height=2,fg_color="#003366",hover_color="#003366")
Button17.place(x=10,y=300)

Button18=customtkinter.CTkButton(app,command=calculate,text="=",width=170,height=2,fg_color="#003366",hover_color="#003366")
Button18.place(x=70,y=300)

app.mainloop()





#Zeno/Ilyes