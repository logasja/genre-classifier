from business_rules import run_all
from rules import rules_json
from models import *
from tkinter import *

class Application(Frame):
    def app_run_all(self):
        run_all(rule_list=self.rules,
            defined_variables=SongVariables(self.song),
            defined_actions=SongActions(self.song),
            stop_on_first_trigger=False
            )

    def createWidgets(self):
        self.QUIT               = Button(self)
        self.QUIT["text"]       = "QUIT"
        self.QUIT["fg"]         = "red"
        self.QUIT["command"]    = self.quit

        self.QUIT.pack({"side": "left"})

        self.run_rules = Button(self)
        self.run_rules["text"] = "Run Rules"
        self.run_rules["command"] = self.app_run_all

        self.run_rules.pack({"side": "left"})

    def __init__(self, song, rules, master=None):
        Frame.__init__(self, master)
        self.song = song
        self.rules = rules
        self.pack()
        self.createWidgets()

example = {
    "descriptors": ["grounded", "melodic", "acoustical"],
    "instruments": ["vocals", "horns", "violin"],
    "distortion": False,
    "performers": 20,
    "age": 24,
    "perc_emot": ["content"],
    "felt_emot": ["inspired", "happy"],
    "genre": None,
}

root = Tk()
app = Application(master=root, song=example, rules=rules_json)
app.mainloop()
root.destroy()

print(example["genre"])