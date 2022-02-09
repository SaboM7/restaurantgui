
from tkinter import *
#creating main menu frame
class Glavni_meni(Frame):

    def __init__(self, master,controler):
        Frame.__init__(self, master)

        Label(self,text= "Izaberite šta želite da poručite").grid(row=0,
                                                                  column=0,
                                                                  columnspan= 2,
                                                                  sticky="W")

        Button(self, text="Hrana", command= lambda :controler.show_frame(Hrana)).grid(row=1,
                                                                                      column=0,
                                                                                      sticky="W")
        Button(self, text="Piće", command= lambda: controler.show_frame(Pice)).grid(row=2,
                                                                                    column=0,
                                                                                    sticky="W")

        Button(self, text="Račun", command= lambda: controler.suma()).grid(row=3,
                                                                           column=0,
                                                                           sticky="W")

        Label(self, text="Vas racun je ").grid(row=3,
                                               column=1,
                                               sticky="W")

        self.text=Text(self, width = 5, height = 1, wrap = WORD)
        self.text.grid(row=3, column=2,sticky="W")
#the food frame
class Hrana(Frame):
    def __init__(self, master,controler):
        Frame.__init__(self, master)
        Label(self, text= "Koje jelo želite da poručite").grid(row=0, column=0, columnspan= 2, sticky="W")

        self.cevapi=BooleanVar()
        Checkbutton(self,
                    text="Cevapi(200g)  300din",
                    variable=self.cevapi).grid(row=1, column=0, sticky="W")

        self.pljeskavica = BooleanVar()
        Checkbutton(self,
                    text="Pljeskavica(250g) 350din",
                    variable=self.pljeskavica).grid(row=2, column=0, sticky="W")

        self.belo_m = BooleanVar()
        Checkbutton(self,
                    text="Belo Meso(250g)   350din",
                    variable=self.belo_m).grid(row=3, column=0, sticky="W")

        self.svinjski_gulas = BooleanVar()
        Checkbutton(self,
                    text="Svinjski Gulaš(porcija)   250din",
                    variable=self.svinjski_gulas).grid(row=1, column=1, sticky="E")

        self.batak = BooleanVar()
        Checkbutton(self,
                    text="Pileći Batak(200g)    300din",
                    variable=self.batak).grid(row=2, column=1, sticky="E")

        self.pica = BooleanVar()
        Checkbutton(self,
                    text="Pica(porodična)   720din",
                    variable=self.pica).grid(row=3, column=1, sticky="E")

        Button(self,text="Nazad", command=lambda :controler.show_frame(Glavni_meni)).grid(row=4,
                                                                                          column=1,
                                                                                          sticky="E")

        Button(self, text="Dezerti", command=lambda: controler.show_frame(Dezerti)).grid(row=4,
                                                                                         column=0,
                                                                                         sticky="W")

        self.lista_jela = [self.pljeskavica, self.cevapi, self.belo_m, self.svinjski_gulas, self.batak, self.pica]

    def suma(self):
        suma=0
        if self.pica.get():
            suma+=720
        if self.pljeskavica.get():
            suma+=350
        if self.cevapi.get():
            suma+=300
        if self.batak.get():
            suma+=300
        if self.belo_m.get():
            suma+=350
        if self.svinjski_gulas.get():
            suma+=250
        return suma

#drinks frame
class Pice(Frame):
    def __init__(self, master,controler):
        Frame.__init__(self, master)
        Label(self, text="Koje piće želite da poručite").grid(row=0, column=0, columnspan= 2, sticky="W")

        self.pivoJ = BooleanVar()
        Checkbutton(self,
                    text="Jelen pivo (0.5l) 210din",
                    variable=self.pivoJ).grid(row=1, column=0, sticky="W")

        self.pivoL = BooleanVar()
        Checkbutton(self,
                    text="Laško pivo (0.5l) 220din",
                    variable=self.pivoL).grid(row=2, column=0, sticky="W")

        self.pivoZ = BooleanVar()
        Checkbutton(self,
                    text="Zaječarko pivo (0.5l) 200din",
                    variable=self.pivoZ).grid(row=3, column=0, sticky="W")

        self.kola = BooleanVar()
        Checkbutton(self,
                    text="Koka kola (0.5l)  180din",
                    variable=self.kola).grid(row=1, column=1, sticky="E")

        self.jabuka_s = BooleanVar()
        Checkbutton(self,
                    text="Sok od jabuke (0.5l)  180din",
                    variable=self.jabuka_s).grid(row=2, column=1, sticky="E")

        self.fanta = BooleanVar()
        Checkbutton(self,
                    text="Fanta (0.5l)  180din",
                    variable=self.fanta).grid(row=3, column=1, sticky="E")

        Button(self,text= "Nazad", command=lambda :controler.show_frame(Glavni_meni)).grid(row=4, column=1, sticky="E")

    def suma(self):
        #calculates sum of prices ordered
        suma=0
        if self.pivoZ.get():
                suma += 200
        if self.pivoL.get():
                suma += 220
        if self.pivoJ.get():
                suma += 210
        if self.kola.get():
                suma += 180
        if self.jabuka_s.get():
                suma += 180
        if self.fanta.get():
                suma += 180
        return suma
class Dezerti(Frame):
    #deserts frame
    def __init__(self, master, controler):
        Frame.__init__(self, master)

        Label(self,text= "Koji dezert želite da poručite").grid(row=0, column=0, columnspan=2, sticky="W")

        self.palacinke = BooleanVar()
        Checkbutton(self,
                    text="Palačinke (porcija)   150din",
                    variable=self.palacinke).grid(row=1, column=0, sticky="W")

        self.torta = BooleanVar()
        Checkbutton(self,
                    text="Torta (parče) 180din",
                    variable=self.torta).grid(row=2, column=0, sticky="W")

        self.sladoled = BooleanVar()
        Checkbutton(self,
                    text="Sladoled (2 kugle 100din)",
                    variable=self.sladoled).grid(row=3, column=0, sticky="W")

        Button(self,text= "Nazad", command=lambda :controler.show_frame(Hrana)).grid(row=4, column=0, sticky="W")

    def suma(self):
        # calculates sum of prices ordered
        suma=0
        if self.torta.get():
            suma+=180
        if self.palacinke.get():
            suma+=150
        if self.sladoled.get():
            suma+=100
        return suma
class Prozor(Tk):

    def __init__(self):
        Tk.__init__( self)
        container= Frame(self)
        container.pack(side="top", fill="both", expand=True)
        #container.grid_rowconfigure(0, weight=1)
        #container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Glavni_meni, Hrana, Pice, Dezerti):
            #creating frames and asigning their master
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Glavni_meni)


    def show_frame(self,ime):
        frame= self.frames[ime]
        frame.tkraise()
    def suma(self):
        #calculating sum of all frames
        self.racun = 0
        for F in ( Hrana, Pice, Dezerti):

            frame=self.frames[F]
            self.racun+=frame.suma()
        #self.frames[Glavni_meni].lbl.text("Vas Racun je: ")
        self.frames[Glavni_meni].text.delete(0.0, END)
        self.frames[Glavni_meni].text.insert(0.0, str(self.racun))
def main():
    Gl_meni= Prozor()
    Gl_meni.title("Jelovnik")
    Gl_meni.geometry("400x150")
    Gl_meni.mainloop()

main()





