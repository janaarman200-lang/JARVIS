import tkinter as tk

class JarvisUI:
    def __init__(self, assistant):
        self.assistant=assistant
        self.root=tk.Tk()
        self.root.title('JARVIS')
        self.entry=tk.Entry(self.root)
        self.entry.pack(fill='x')
        self.output=tk.Text(self.root)
        self.output.pack(fill='both',expand=True)
        tk.Button(self.root,text='Send',command=self.send).pack()
    def send(self):
        c=self.entry.get().strip()
        if c:
            self.output.insert('end','You: '+c+'\nJARVIS: '+self.assistant.handle(c)+'\n')
            self.entry.delete(0,'end')
    def run(self):
        self.root.mainloop()
