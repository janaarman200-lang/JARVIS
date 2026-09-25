import tkinter as tk

class JarvisUI:
    def __init__(self, assistant):
        self.assistant=assistant
        self.root=tk.Tk(); self.root.title('JARVIS'); self.root.geometry('800x600')
        self.output=tk.Text(self.root); self.output.pack(fill='both',expand=True)
        self.entry=tk.Entry(self.root); self.entry.pack(fill='x')
        self.entry.bind('<Return>',self.send)
    def send(self,event=None):
        c=self.entry.get().strip()
        if not c:return
        self.output.insert('end','You: '+c+'\n')
        self.output.insert('end','JARVIS: '+self.assistant.router.handle(c)+'\n')
        self.entry.delete(0,'end')
    def run(self): self.root.mainloop()
