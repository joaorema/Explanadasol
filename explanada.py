import customtkinter
import sqlite3

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


selected_cidade = ""
selected_explanada = ""
selected_horario = ""

def escolha_cidade(value):
    global selected_cidade
    selected_cidade = value
    update_label()

def escolha_explanada(value):
    global selected_explanada
    selected_explanada = value
    update_label()

def escolha_horario(value):
    global selected_horario
    selected_horario = value
    update_label()

def update_label():
    resposta_label.configure(text=f"{selected_cidade}, {selected_explanada}, {selected_horario}")

def pesquisar():
    pass

def clear():
        resposta_label.configure(text="") 
        result_label.configure(text="")

import sqlite3

def pesquisar():
    conn = sqlite3.connect('/home/joao-rema/Documents/joao/explanadasol/cafe.db')
    cursor = conn.cursor()
    
    query = """
    SELECT nome FROM name 
    WHERE cidade = ? 
    AND (sol = 'sim' OR sombra = 'sim') 
    AND (manha = 'sim' OR tarde = 'sim')
    """
    cursor.execute(query, (selected_cidade,))
    
    results = cursor.fetchall()
    conn.close()
    
    
    result_text = "\n".join([str(result) for result in results])
    result_label.configure(text=result_text)
              
root = customtkinter.CTk()
root.geometry("800x500")
root.title("Explanda ao sol")


cidade = ["maia", "porto", "paredes"]
my_combo1 = customtkinter.CTkComboBox(root, values=cidade, command=escolha_cidade)
my_combo1.pack(pady=20)


explanada = ["sol", "sombra"]
my_combo2 = customtkinter.CTkComboBox(root, values=explanada, command=escolha_explanada)
my_combo2.pack(pady=30)


horario = ["manha", "tarde"]
my_combo3 = customtkinter.CTkComboBox(root, values=horario, command=escolha_horario)
my_combo3.pack(pady=40)

button_pesquisar= customtkinter.CTkButton(master=root,
        text="Pesquisar",
        command=pesquisar,
        height=50,
        width=100,
        font=("Helvetica", 24),
        corner_radius=50,
        state="normal")
button_pesquisar.pack(pady=12, padx=10)

resposta_label = customtkinter.CTkLabel(master=root, text="")
resposta_label.pack(pady=14, padx=12)

result_label = customtkinter.CTkLabel(master=root, text="")
result_label.pack(pady=16, padx=14)

clearbtn = customtkinter.CTkButton(master=root, text="Clear", command=clear)
clearbtn.pack(padx=18, pady=16)

root.mainloop()

