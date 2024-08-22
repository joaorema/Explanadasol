import customtkinter
import sqlite3

#Settings da Windows
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Variaveis 
selected_cidade = ""
selected_horario = ""
selected_rating = ""

#Defeniçoes 

def escolha_cidade(value):
    global selected_cidade
    selected_cidade = value
    update_label()


def escolha_horario(value):
    global selected_horario
    if value == "Manha":
         selected_horario = "Manha"
    else:
         selected_horario = "Tarde"
    update_label()

def escolha_rating(value):
    global selected_rating
    if value == "1-3":
          selected_rating = "1.0-3.0"
    else:
          selected_rating = "4.0-5.0"
    
    update_label()
        

     
def update_label():
    display_rating = selected_rating.replace("1.0-3.0", "1-3").replace("4.0-5.0", "4-5")
    resposta_label.configure(text=f"{selected_cidade} / {selected_horario} / {display_rating}")
    
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
    conn = sqlite3.connect('/home/joaorema/Documents/Explanadasol/explanada.db')
    cursor = conn.cursor()
    
    query = """
    SELECT name.nome 
    FROM name 
    JOIN city ON name.id = city.idc 
    JOIN time ON name.id = time.idt 
    JOIN rating ON name.id = rating.idr
    WHERE city.cidade = ? 
    AND (time.horario = ? OR time.horario LIKE '%' || ? || '%')
    AND rating.cotacao BETWEEN ? AND ?
    """

    
    #para confirmar se esta a receber resultados
    print(f"Selected cidade: {selected_cidade}")
    print(f"Selected horario: {selected_horario}")
    print(f"Selected rating: {selected_rating}")
    lower_bound, upper_bound = selected_rating.split('-')
    print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")
    cursor.execute(query, (selected_cidade, selected_horario, selected_horario, lower_bound, upper_bound))
    
    
    results = cursor.fetchall()
    conn.close()
    
    
    result_text = "\n".join([result[0] for result in results])
    result_textbox.delete("1.0", customtkinter.END)
    result_textbox.insert(customtkinter.END, result_text)


#inicio do programada    
              
root = customtkinter.CTk()
root.geometry("900x600")
root.title("Explanda ao sol")
root.maxsize(900, 650)
root.minsize(900, 650)

#frame de cima
button_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
button_frame.pack(side="top", pady=30)

#Titulo
opcoes_label = customtkinter.CTkLabel(button_frame, text="Escolha as suas preferencias")
opcoes_label.grid(row=0, column=0, columnspan=3, pady=10)

#subtitulo
cidade_label = customtkinter.CTkLabel(button_frame, text = "Cidade")
cidade_label.grid(row=1, column=0, padx=5)

horario_label = customtkinter.CTkLabel(button_frame, text="Horario")
horario_label.grid(row=1, column=1, padx=5)

rating_label =customtkinter.CTkLabel(button_frame, text="Rating")
rating_label.grid(row=1, column=2, padx=5)

#Opcao 1
cidade = ["Maia", "Porto", "Matosinhos", "Gaia", "Paredes", "Guimaraes"]
my_combo1 = customtkinter.CTkComboBox(button_frame, values=cidade, command=escolha_cidade)
my_combo1.grid(row=2, column=0, padx=5)

#Opcao 2
horario = ["Manha", "Tarde"]
my_combo3 = customtkinter.CTkComboBox(button_frame, values=horario, command=escolha_horario)
my_combo3.grid(row=2, column=1, padx=5)

#Opcao 3
rating = ["1-3", "4-5"]
my_combo4 = customtkinter.CTkComboBox(button_frame, values=rating, command=escolha_rating)
my_combo4.grid(row=2, column=2, padx=5)

#label com as opcoes escolhidas -
resposta_label = customtkinter.CTkLabel(master=root, text="")
resposta_label.pack(pady=14, padx=12)

#caixa de texto com resultados
result_textbox = customtkinter.CTkTextbox(master=root, height=200, width=600, fg_color="transparent", font=('arial', 13))
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

