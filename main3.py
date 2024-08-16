import customtkinter
import sqlite3

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())


def pesquisar():
    
    
    cidade = entry1.get()  
    sol = checkbox1.get()
    sombra = checkbox1.get()        
    manha = checkbox2.get()    
    tarde = checkbox2.get()
    
    conn = sqlite3.connect('/home/joao-rema/Documents/joao/explanadasol/cafe.db')
    cursor = conn.cursor()

    
    query = "SELECT * FROM name WHERE cidade = ? AND sol = ? AND manha =?"
    
    # Execute the query with the values
    cursor.execute(query, (cidade, sol, manha))

    # Fetch all matching rows
    results = cursor.fetchall()

    # Display the results (you can customize this part)
    for row in results:
        print(row)

    # Close the database connection
    conn.close()

root = customtkinter.CTk()
root.geometry("800x500")
root.title("Explanda ao sol")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=50, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Pesquisar")
label.pack(pady=12, padx=10)


entry1 =customtkinter.CTkEntry(master=frame, placeholder_text="Cidade",)
entry1.pack(pady=12, padx=10)

check_var = customtkinter.StringVar(value="on")
checkbox1 = customtkinter.CTkCheckBox(master=frame, text="Sol", command=checkbox_event, variable=check_var, onvalue="on", offvalue="off")
checkbox1.pack(pady=12, padx=10)

check_var = customtkinter.StringVar(value="on")
checkbox2 = customtkinter.CTkCheckBox(master=frame, text="Manha", command=checkbox_event, variable=check_var, onvalue="on", offvalue="off")
checkbox2.pack(pady=12, padx=10)


button_pesquisar= customtkinter.CTkButton(master=frame,
        text="Pesquisar",
        command=pesquisar,
        height=50,
        width=100,
        font=("Helvetica", 24),
        corner_radius=50,
        state="normal")
button_pesquisar.pack(pady=12, padx=10)

root.mainloop()

