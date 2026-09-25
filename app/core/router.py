class CommandRouter:
    def __init__(self,memory,approval,skills,ai,tools): self.memory=memory; self.approval=approval; self.skills=skills; self.ai=ai; self.tools=tools
    def handle(self,c):
        t=c.strip(); l=t.lower()
        if l=='help': return 'help | remember <text> | memory | skills | open <url> | list files <folder> | create folder <folder> | delete <path> | press <key> | exit'
        if l=='memory': return '\n'.join('- '+x for x in self.memory.all()) or 'Memory is empty.'
        if l.startswith('remember '): self.memory.add(t[9:].strip()); return 'Saved to local memory.'
        if l=='skills': return 'Skills: '+(', '.join(self.skills.names()) or 'none')
        if l.startswith('open '): return self.tools.open_url(t[5:].strip())
        if l.startswith('list files '): return self.tools.list_files(t[11:].strip())
        if l.startswith('create folder '): return self.tools.create_folder(t[14:].strip())
        if l.startswith('delete '):
            if not self.approval.check(t).approved:return 'Action cancelled.'
            return self.tools.delete_path(t[7:].strip())
        if l.startswith('press '):
            if not self.approval.check(t).approved:return 'Action cancelled.'
            return self.tools.computer_press(t[6:].strip())
        if self.ai.available(): return self.ai.ask(t)
        return 'AI is not configured. Set OPENAI_API_KEY locally.'
