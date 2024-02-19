import customtkinter as ctk
import time

def formato_fecha(): #Paraun formato 01/Ene/24
    fecha = time.strftime("%d/%m/%y")
    fecha = fecha.split("/")
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    fecha[1] = meses[int(fecha[1])-1]
    fecha = fecha[0]+"/"+fecha[1]+"/"+fecha[2]
    return fecha



class App(ctk.CTk):
    def __init__(self, nombre="default", Emessage=None, screen_size=(800, 600)):
        super().__init__()
        self.nombre = nombre
        self.title(nombre)
        self.screen_size = screen_size
        self.geometry(f"{self.screen_size[0]}x{self.screen_size[1]}")
        self.barra_superior_color_azul = "#1E90FF"
        self.cuerpo_color_oscuro = "#252525"
        self.cuerpo_color_dark = "#161616"
        self.boton_color_azul = "#0159AF"
        self.hora = time.strftime("%H:%M")
        self.fecha = formato_fecha()
        self.Emessage = Emessage
        
        if self.Emessage != None:
            self.error = ctk.CTkLabel(master=self, text="Error: " +self.Emessage, height=32, width=120, font=("Arial", 20), fg_color="#FF0000")
            self.error.pack(padx=0, pady=0, side="top")
            
            self.barra_superior = ctk.CTkFrame(master=self, fg_color=self.barra_superior_color_azul, width=self.screen_size[0], height=30)
            self.barra_superior.pack(padx=0, pady=0, side="top")
        else:
        
            self.barra_superior = ctk.CTkFrame(master=self, fg_color=self.barra_superior_color_azul, width=self.screen_size[0], height=50)
            self.barra_superior.pack(padx=0, pady=0, side="top")

        self.Hora = ctk.CTkLabel(master=self.barra_superior, text=self.hora, height=32, width=120, font=("Arial", 20))
        self.Hora.place(relx=0.1, rely=0.5, anchor="center")

        self.Encabezado = ctk.CTkLabel(master=self.barra_superior, text=nombre, height=32, width=120, font=("Arial", 20))
        self.Encabezado.place(relx=0.5, rely=0.5, anchor="center")

        self.Fecha = ctk.CTkLabel(master=self.barra_superior, text=self.fecha, height=32, width=120, font=("Arial", 20))
        self.Fecha.place(relx=0.9, rely=0.5, anchor="center")

        ###
        # Barra de errores
        ###
        


        ###
        # Creación del cuerpo
        ###
        self.cuerpo = ctk.CTkFrame(master=self, fg_color=self.cuerpo_color_oscuro, width=(self.screen_size[0]), height=500)
        self.cuerpo.pack(padx=2, pady=0, side="top")
        self.aside = ctk.CTkFrame(master=self.cuerpo, fg_color=self.cuerpo_color_dark, width=((self.screen_size[0])*(1/6)), height=self.screen_size[1]-80)
        self.aside.pack(padx=0, pady=0, side="left")
        self.workbench = ctk.CTkFrame(master=self.cuerpo, fg_color=self.cuerpo_color_oscuro, width=((self.screen_size[0])*(5/6)), height=self.screen_size[1]-80)
        self.workbench.pack(padx=0, pady=0, side="right")
        self.workbenchtop = ctk.CTkFrame(master=self.workbench, fg_color=self.cuerpo_color_oscuro, width=(self.screen_size[0]), height=(self.screen_size[1]-80)/2)
        self.workbenchtop.pack(padx=1, pady=0, side="top")
        self.workbenchbottom = ctk.CTkFrame(master=self.workbench, fg_color=self.cuerpo_color_oscuro, width=(self.screen_size[0]), height=(self.screen_size[1]-80)/2)
        self.workbenchbottom.pack(padx=1, pady=0, side="bottom")
        
        

        


        ###
        # Creación de la barra inferior
        ###

        self.barra_inferior = ctk.CTkFrame(master=self, fg_color=self.barra_superior_color_azul, width=self.screen_size[0], height=50)
        self.barra_inferior.pack(padx=0, pady=0, side="bottom")

        self.adios = ctk.CTkButton(master=self.barra_inferior, text="Salir", height=32, width=120, font=("Arial", 20), fg_color="#FF0000", command=self.quit)
        self.adios.place(relx=0.05, rely=0.5, anchor="center")

