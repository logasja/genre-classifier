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

    def run(self):
        self.get_attribs()
        run_all(rule_list=self.rules,
            defined_variables=SongVariables(self.song),
            defined_actions=SongActions(self.song),
            stop_on_first_trigger=False
            )

    def createWidgets(self):
        # Instrument Select
        inst_var = tk.StringVar()
        inst_var.set(instruments)
        self.INST               = tk.Listbox(self, listvariable=inst_var, selectmode=tk.MULTIPLE, width=20, height=10)
        self.INST.configure(exportselection=False)
        self.INST.pack(side=tk.LEFT)
        
        # Descriptor Select
        desc_var = tk.StringVar()
        desc_var.set(descriptors)
        self.DESCR              = tk.Listbox(self, listvariable=desc_var, selectmode=tk.MULTIPLE, width=20, height=10)
        self.DESCR.configure(exportselection=False)
        self.DESCR.pack(side=tk.LEFT)

        # Intended Emotion
        emot_var = tk.StringVar()
        emot_var.set(emotions)
        self.INTNDEMOT          = tk.Listbox(self, listvariable=emot_var, selectmode=tk.MULTIPLE, width=20, height=10)
        self.INTNDEMOT.configure(exportselection=False)
        self.INTNDEMOT.pack(side=tk.LEFT)

        # Felt Emotion
        self.FLTEMOT            = tk.Listbox(self, listvariable=emot_var, selectmode=tk.MULTIPLE, width=20, height=10)
        self.FLTEMOT.configure(exportselection=False)
        self.FLTEMOT.pack(side=tk.LEFT)

        self.INSTBTN            = ttk.Button(self, text="Choices", command=self.get_attribs)
        self.INSTBTN.pack(side=tk.LEFT)

        # Quit button
        self.QUIT               = tk.Button(self)
        self.QUIT["text"]       = "QUIT"
        self.QUIT["fg"]         = "red"
        self.QUIT["command"]    = self.quit
        self.QUIT.pack(side=tk.LEFT)

        # Run Button
        self.run_rules = tk.Button(self)
        self.run_rules["text"] = "Run"
        self.run_rules["command"] = self.run

        self.run_rules.pack(side=tk.LEFT)

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