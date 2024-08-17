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
    resposta_label.configure(text=f"{selected_cidade} / {selected_explanada} / {selected_horario}")

def clear():
        resposta_label.configure(text="") 
        result_textbox.delete("1.0", customtkinter.END)

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
    result_textbox.delete("1.0", customtkinter.END)  # Clear existing text
    result_textbox.insert(customtkinter.END, result_text)
              
root = customtkinter.CTk()
root.geometry("900x600")
root.title("Explanda ao sol")

button_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
button_frame.pack(side="top", pady=30)

opcoes_label = customtkinter.CTkLabel(button_frame, text="Escolha as suas preferencias")
opcoes_label.pack(side="top", pady=10)

cidade = ["maia", "porto", "paredes"]
my_combo1 = customtkinter.CTkComboBox(button_frame, values=cidade, command=escolha_cidade)
my_combo1.pack(side="left", padx=5)


explanada = ["sol", "sombra"]
my_combo2 = customtkinter.CTkComboBox(button_frame, values=explanada, command=escolha_explanada)
my_combo2.pack(side="left", padx=5)


horario = ["manha", "tarde"]
my_combo3 = customtkinter.CTkComboBox(button_frame, values=horario, command=escolha_horario)
my_combo3.pack(side="left", padx=5)

resposta_label = customtkinter.CTkLabel(master=root, text="")
resposta_label.pack(pady=14, padx=12)

result_textbox = customtkinter.CTkTextbox(master=root)
result_textbox.pack(pady=16, padx=14)


button_frame2 = customtkinter.CTkFrame(master=root, fg_color="transparent")
button_frame2.pack(side="bottom", pady=30)

button_pesquisar= customtkinter.CTkButton(button_frame2,
        text="Pesquisar",
        command=pesquisar,
        state="normal")
button_pesquisar.pack(side="top", pady=10)


clearbtn = customtkinter.CTkButton(button_frame2, text="Limpar", command=clear)
clearbtn.pack(side="bottom", pady=10)

root.mainloop()

