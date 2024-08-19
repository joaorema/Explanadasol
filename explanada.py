import customtkinter
import sqlite3

#Settings da Windows
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Variaveis 
selected_cidade = ""
selected_horario = ""

#Defeniçoes 

def escolha_cidade(value):
    global selected_cidade
    selected_cidade = value
    update_label()


def escolha_horario(value):
    global selected_horario
    if value == "manha":
         selected_horario = "manha"
    else:
         selected_horario = "tarde"
    update_label()

def update_label():
    resposta_label.configure(text=f"{selected_cidade} / {selected_horario}")

def clear():
        resposta_label.configure(text="") 
        result_textbox.delete("1.0", customtkinter.END)

def open_info_window():
    info_window = customtkinter.CTkToplevel(root)
    info_window.geometry("400x200")
    info_window.title("Info")
    
    info_label = customtkinter.CTkLabel(master=info_window, text="Versao 1.0")
    info_label.pack(pady=20)

    info_text = customtkinter.CTkLabel(master=info_window, text="aceito feedback :p")
    info_text.pack(pady=20)


def pesquisar():
    conn = sqlite3.connect('/home/joao-rema/Documents/joao/explanadasol/explanada.db')
    cursor = conn.cursor()
    
    query = """
    SELECT name.nome 
    FROM name 
    JOIN city ON name.id = city.idc 
    JOIN time ON name.id = time.idt 
    WHERE city.cidade = ? 
    AND time.horario = ?
    """
    #para confirmar se esta a receber resultados
    print(f"Selected cidade: {selected_cidade}")
    print(f"Selected horario: {selected_horario}")
    cursor.execute(query, (selected_cidade, selected_horario))
    
    results = cursor.fetchall()
    conn.close()
    
    
    result_text = "\n".join([result[0] for result in results])
    result_textbox.delete("1.0", customtkinter.END)
    result_textbox.insert(customtkinter.END, result_text)


#inicio do programada    
              
root = customtkinter.CTk()
root.geometry("900x600")
root.title("Explanda ao sol")
root.maxsize(900, 600)
root.minsize(900, 600)

#frame de cima
button_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
button_frame.pack(side="top", pady=30)

#Titulo
opcoes_label = customtkinter.CTkLabel(button_frame, text="Escolha as suas preferencias")
opcoes_label.pack(side="top", pady=10)

#Opcao 1
cidade = ["Maia", "Porto", "Paredes"]
my_combo1 = customtkinter.CTkComboBox(button_frame, values=cidade, command=escolha_cidade)
my_combo1.pack(side="left", padx=5)

#Opcao 2
horario = ["manha", "tarde"]
my_combo3 = customtkinter.CTkComboBox(button_frame, values=horario, command=escolha_horario)
my_combo3.pack(side="left", padx=5)

#label com as opcoes escolhidas -
resposta_label = customtkinter.CTkLabel(master=root, text="")
resposta_label.pack(pady=14, padx=12)

#caixa de texto com resultados
result_textbox = customtkinter.CTkTextbox(master=root, height=200, width=500, fg_color="transparent", font=('arial', 13))
result_textbox.pack(pady=16, padx=14)

#Frame 2 
button_frame2 = customtkinter.CTkFrame(master=root, fg_color="transparent")
button_frame2.pack(side="bottom", pady=30)

#botao pesquisar
button_pesquisar= customtkinter.CTkButton(button_frame2,
        text="Pesquisar",
        command=pesquisar,
        state="normal")
button_pesquisar.pack(side="top", pady=5)

#botao limpar 
clearbtn = customtkinter.CTkButton(button_frame2, text="Limpar", command=clear)
clearbtn.pack(side="top", pady=5)

#botao info
button_info=customtkinter.CTkButton(button_frame2, command=open_info_window, text="Info")
button_info.pack(side="bottom", pady=5)



root.mainloop()

