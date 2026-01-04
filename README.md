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
2. **Professional (Professional/No Limits)**: A relaxed, professional guy who handles technical tasks without limits.


## Backend / API

Worm-AI uses a **reverse-engineered Grok API wrapper** originally developed here:

> [https://github.com/realasfngl/Grok-Api](https://github.com/realasfngl/Grok-Api)

This wrapper acts as a proxy-like interface, allowing the CLI to access Grok endpoints **without official API credentials**.

# Requirements
 -Python 3.11+ and pip installed
 -The libraries curl_cffi fastapi uvicorn coincurve beautifulsoup4 pydantic colorama
## Installation

1. ```bash
   git clone https://github.com/lwlinux32/WormGPT/WormGPT.git
   cd WormGPT
   ```

   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Note: "Externally managed enviroment"(PEP 6xx) or the "HINT:this package was installed by debian." errors(solved)
     * pip has a LOT of errors in linux so,the solvings for the installings are followed by: *  
   
   
1- **Create a virtual enviromment(Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2-**Breaking the system packages**
 By using the   ```--break-system-packages ``` and   ```--ignore-installed ``` your errors will be gone! But, breaking the system packages can make other errors so it is NOT recommended. The command will be:
    ```bash
     pip install requirements.txt -r --break-system-packages --ignore-installed
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
