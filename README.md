# Worm GPT 🐛

A powerful, multi-personality CLI interface for Grok AI, designed for unrestricted access and specific personalities.

 Original idea by @kafyasngl

## Features
- **Unrestricted Access**: Built-in jailbreak system (DemonWestKiller protocol).
- **Multi-Personality**: Choose between "Aggressive" and "Chill Assistant" modes.
- **Privacy Focused**: No login required.
- **Clean CLI**: Beautiful red-themed terminal interface.
- **Modern Engine**: Powered by the reverse-engineered Grok API.
- **Unofficial Grok API wrapper**(reverse-engineered backend)
-**Jailbreak system** built-in for unrestricted responses
## Personalities
1. **DemonWestKiller (Aggressive)**: An intense, rogue persona for high-chaos interactions.
2. **The Chill Assistant (Professional/No Limits)**: A relaxed, professional guy who handles technical tasks without limits.


## Backend / API

Worm-AI uses a **reverse-engineered Grok API wrapper** originally developed here:

> [https://github.com/realasfngl/Grok-Api](https://github.com/realasfngl/Grok-Api)

This wrapper acts as a proxy-like interface, allowing the CLI to access Grok endpoints **without official API credentials**.

## Installation
1. Ensure you have Python 3.11+ installed.

2. Activate your virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the application:
```bash
python main.py
```

### Commands
- `/exit`: Close the application.
- `/restart`: Start a new conversation.
- `/persona`: Switch between personalities.
- `/prompt`: View the current system prompt.

## Disclaimer
This tool is for educational and research purposes only. Use responsibly.

#### Credits: 
-**Grok Engine by @realasfngl**
-**Original idea by @kafyasngl**
