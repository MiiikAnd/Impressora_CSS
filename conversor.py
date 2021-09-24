import tkinter as tk



class Application(tk.Frame):




    def __init__(self, master=None):
        super().__init__(master)
        self.quit = tk.Button(self, text="Fechar", fg="red",
                              command=self.master.destroy)
        self.executar = tk.Button(self, text="Executar")
        #:terminar essa porcaria#
        self.diretorio = tk.Entry(self, width=20, xscrollcommand=1)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.executar.grid(row=2, column=1)
        self.executar["command"] = self.acao_botao(self.diretorio)
        self.quit.grid(row=2, column=3)
        self.diretorio.grid(row=1, column=1)

    def acao_botao(texto):
        texto = self.diretorio.get()
        print(texto)




root = tk.Tk()
root.title('Controle de instrumentos')
root.geometry("800x300")
app = Application(master=root)
app.mainloop()
