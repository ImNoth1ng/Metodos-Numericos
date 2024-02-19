from views.mainwindow import App
import customtkinter as ctk
import time




if __name__ == '__main__':
    
    app = App(nombre="Bisección", screen_size=(1920, 1050))
    app.attributes("-fullscreen", True)
    
    ###
    #Cuerpo
    def Ingresar_ecuacion():
                
        lblTitle = ctk.CTkLabel(master=app.workbenchtop, text="Ingresar ecuación", height=32, width=40, font=("Arial", 20))
        lblTitle.place(relx=0.5, rely=0.1, anchor="center")
        
        lblGrado = ctk.CTkLabel(master=app.workbenchtop, text="Grado", height=32, width=40, font=("Arial", 20))
        lblGrado.place(relx=0.1, rely=0.3, anchor="center")
        txtGrado = ctk.CTkEntry(master=app.workbenchtop, width=120, font=("Arial", 20), placeholder_text="ej. 2, 3, 4...")
        txtGrado.place(relx=0.2, rely=0.3, anchor="center")
        
       
        
        btnOk = ctk.CTkButton(master=app.workbench, text="Ok", height=32, width=120, font=("Arial", 20), fg_color=app.boton_color_azul, command="")
        btnOk.place(relx=0.5, rely=0.5, anchor="center")
        
        

        
    Ingresar_ecuacion()
        
    def insertar():
        Li = ctk.CTkLabel(master=app.workbench, text="Li", height=32, width=40, font=("Arial", 20))
        Li.place(relx=0.1, rely=0.1, anchor="center")
        LiValue = ctk.CTkEntry(master=app.workbench, width=120, font=("Arial", 20))
        LiValue.place(relx=0.2, rely=0.1, anchor="center")

        Ls = ctk.CTkLabel(master=app.workbench, text="Ls", height=32, width=40, font=("Arial", 20))
        Ls.place(relx=0.5, rely=0.1, anchor="center")
        LsValue = ctk.CTkEntry(master=app.workbench, width=120, font=("Arial", 20))
        LsValue.place(relx=0.65, rely=0.1, anchor="center")

        delta = ctk.CTkLabel(master=app.workbench, text="δ", height=32, width=40, font=("Arial", 20))
        delta.place(relx=0.1, rely=0.3, anchor="center")
        deltaValue = ctk.CTkEntry(master=app.workbench, width=120, font=("Arial", 20))
        deltaValue.place(relx=0.2, rely=0.3, anchor="center")

        grado = ctk.CTkLabel(master=app.workbench, text="Grado", height=32, width=40, font=("Arial", 20))
        grado.place(relx=0.5, rely=0.3, anchor="center")
        gradoValue = ctk.CTkEntry(master=app.cuerpo, width=120, font=("Arial", 20))
        gradoValue.place(relx=0.65, rely=0.3, anchor="center")


        Generar = ctk.CTkButton(master=app.workbench, text="Generar", height=32, width=120, font=("Arial", 20), fg_color=app.boton_color_azul)
        Generar.place(relx=0.85, rely=0.3, anchor="center")
    
    ################
    
    def limpiar_datos():
        pass
    ### Botones inferiores
    app.otros = ctk.CTkButton(master=app.barra_inferior, text="Otro", height=32, width=120, font=("Arial", 20), fg_color=app.boton_color_azul, command=limpiar_datos)
    app.otros.place(relx=0.12, rely=0.5, anchor="center")
    
    app.Graficar = ctk.CTkButton(master=app.barra_inferior, text="Graficar", height=32, width=120, font=("Arial", 20), fg_color=app.boton_color_azul, command=limpiar_datos)
    app.Graficar.place(relx=0.19, rely=0.5, anchor="center")
    
    def actualizar_hora():
        app.hora = time.strftime("%H:%M")
        app.Hora.configure(text=app.hora)
        app.after(1000, actualizar_hora)
    actualizar_hora()
    
    
    
    
    app.mainloop()



