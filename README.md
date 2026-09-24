# JARVIS

Personal AI assistant for Windows.

## Stage 1 — Core foundation

This first stage provides:
- Command-line chat interface
- Local JSON memory
- Safe vs consequential action classification
- Confirmation gate for consequential actions
- Skill registry foundation
- Clean project structure for future voice, browser, computer-control and integrations

## Safety

JARVIS must ask for confirmation before:
- payments or purchases
- publishing ads/content
- deleting important data
- sending sensitive messages
- changing account/security settings
- other irreversible consequential actions

Never put passwords, OTPs, recovery codes, API keys, or access tokens into source files or memory.

## Run

Windows PowerShell:

```powershell
python -m app.main
```

Type `help` for commands and `exit` to quit.
