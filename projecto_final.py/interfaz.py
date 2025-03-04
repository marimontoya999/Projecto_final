import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")
label = ctk.CTkLabel(app, text="It works!", font=("Arial", 20))
label.pack(pady=20)
app.mainloop()

