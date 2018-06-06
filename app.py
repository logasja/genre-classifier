from business_rules import run_all
from rules import rules_json
from models import *
import tkinter as tk
import tkinter.ttk as ttk

class Application(tk.Frame):
    def select_lstbx(self, lstbox):
        reslist = list()
        selection = lstbox.curselection()
        for i in selection:
            entry = lstbox.get(i)
            reslist.append(entry)
        print(reslist)
        return reslist

    def get_attribs(self):
        self.song.instruments = self.select_lstbx(self.INST)
        self.song.descriptors = self.select_lstbx(self.DESCR)
        self.song.perc_emot = self.select_lstbx(self.INTNDEMOT)
        self.song.felt_emot = self.select_lstbx(self.FLTEMOT)
        self.song.performers = int(self.PERFNUM.get())

    def run(self):
        self.get_attribs()
        run_all(rule_list=self.rules,
            defined_variables=SongVariables(self.song),
            defined_actions=SongActions(self.song),
            stop_on_first_trigger=False
            )
        self.genre_var.set(self.song.genre)
        self.update_idletasks()

    def createWidgets(self):
        # Instrument Select
        inst_title              = ttk.Label(self, text="Instruments")
        inst_title.grid(row=0, column=0)

        inst_var = tk.StringVar()
        instruments.sort()
        inst_var.set(instruments)
        self.INST               = tk.Listbox(self, listvariable=inst_var, selectmode=tk.MULTIPLE, width=20, height=10)
        self.INST.configure(exportselection=False)
        self.INST.grid(row=1, column=0)
        
        # Descriptor Select
        desc_title              = ttk.Label(self, text="Descriptor")
        desc_title.grid(row=0, column=1)

        desc_var = tk.StringVar()
        descriptors.sort()
        desc_var.set(descriptors)
        self.DESCR              = tk.Listbox(self, listvariable=desc_var, selectmode=tk.MULTIPLE, width=20, height=10)
        self.DESCR.configure(exportselection=False)
        self.DESCR.grid(row=1, column=1)

        # Intended Emotion
        intnemot_title          = ttk.Label(self, text="Intended Emotion")
        intnemot_title.grid(row=0, column=2)

        emot_var = tk.StringVar()
        emot_var.set(emotions)
        self.INTNDEMOT          = tk.Listbox(self, listvariable=emot_var, selectmode=tk.MULTIPLE, width=20, height=10)
        self.INTNDEMOT.configure(exportselection=False)
        self.INTNDEMOT.grid(row=1, column=2)

        # Felt Emotion
        fltemot_title           = ttk.Label(self, text="Felt Emotion")
        fltemot_title.grid(row=0, column=3)

        self.FLTEMOT            = tk.Listbox(self, listvariable=emot_var, selectmode=tk.MULTIPLE, width=20, height=10)
        self.FLTEMOT.configure(exportselection=False)
        self.FLTEMOT.grid(row=1, column=3)

        # Number of Performers
        perfnum_title           = ttk.Label(self, text="Number of Performers")
        perfnum_title.grid(row=2, column=0)

        self.PERFNUM            = tk.Spinbox(self, from_=0, to=20)
        self.PERFNUM.grid(row=2, column=1)

        INSTBTN            = ttk.Button(self, text="Choices", command=self.get_attribs)
        INSTBTN.grid(row=3, column=0)

        # Quit button
        QUIT               = tk.Button(self, text="QUIT", fg="red", command=self.quit)
        QUIT.grid(row=3, column=1)

        # Run Button
        run_rules          = tk.Button(self, text="RUN", command=self.run)
        run_rules.grid(row=3, column=2)

        # Result Text
        self.genre_var = tk.StringVar()
        self.genre_var.set('Not Run Yet')
        Result              = ttk.Label(self, textvariable=self.genre_var)
        Result.grid(row=3, column=3)
        

    def __init__(self, song, rules, master=None):
        tk.Frame.__init__(self, master)
        self.song = song
        self.rules = rules
        self.pack()
        self.createWidgets()

example = Song()
example.descriptors = ["grounded", "melodic", "acoustical"]
example.instruments = ["vocals", "horns", "violin"]
example.performers = 20
example.perc_emot = ["content"]
example.felt_emot = ["inspired", "happy"]

root = tk.Tk()
root.title("Genre Classifier")
# root.geometry("400x500")
app = Application(master=root, song=example, rules=rules_json)
app.mainloop()
root.destroy()