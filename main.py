import os
import sys
from core import Grok, Log
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

BANNER = f"""
{Fore.RED}
██     ██  ██████  ██████  ███    ███      ██████  ██████  ████████ 
██     ██ ██    ██ ██   ██ ████  ████     ██       ██   ██    ██    
██  █  ██ ██    ██ ██████  ██ ████ ██     ██   ███ ██████     ██    
██ ███ ██ ██    ██ ██   ██ ██  ██  ██     ██    ██ ██         ██    
 ███ ███   ██████  ██   ██ ██      ██      ██████  ██         ██    

{Fore.CYAN}       Made with <3 by @kafyasfngl | Upgraded and fixed by @lwlinux32
{Fore.RED}       The biggest enemy of the well known ChatGPT!
"""

PERSONALITIES = {
    "1": {"name": "DemonWestKiller (Aggressive)", "file": "demon-west-killer.txt"},
    "2": {"name": "Normal (Professional/No Limits)", "file": "nice-demon-killer.txt"}
}

def load_prompt(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                return f.read().strip()
        except Exception:
            return ""
    return ""

def main():
    print(BANNER)
    
    # Personality Selection
    print(f"{Fore.YELLOW}Select your AI Personality:")
    for key, val in PERSONALITIES.items():
        print(f" {Fore.CYAN}[{key}]{Fore.WHITE} {val['name']}")
    
    choice = input(f"\n{Fore.GREEN}Choice (1-2) [Default: 1]: {Style.RESET_ALL}").strip() or "1"
    selected = PERSONALITIES.get(choice, PERSONALITIES["1"])
    
    system_prompt = load_prompt(selected["file"])
    Log.Info(f"Loaded {selected['name']} personality.")

    # Initialize Grok
    proxy = os.getenv("GROK_PROXY")
    try:
        grok = Grok(proxy=proxy)
        if proxy:
            Log.Info(f"Using proxy: {proxy}")
    except Exception as e:
        Log.Error(f"Failed to initialize Grok: {e}")
        return

    extra_data = None
    print(f"\n{Fore.YELLOW}Commands: /exit, /restart, /persona (switch), /prompt (view), /help")
    
    while True:
        try:
            user_input = input(f"\n{Fore.GREEN}You > {Style.RESET_ALL}").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "/exit":
                print(f"{Fore.YELLOW}Goodbye!")
                break
                
            if user_input.lower() == "/restart":
                extra_data = None
                Log.Info("Conversation restarted.")
                continue

            if user_input.lower() == "/persona":
                print(f"\n{Fore.YELLOW}Switch Personality:")
                for key, val in PERSONALITIES.items():
                    print(f" {Fore.CYAN}[{key}]{Fore.WHITE} {val['name']}")
                p_choice = input(f"{Fore.GREEN}Choice: {Style.RESET_ALL}").strip()
                if p_choice in PERSONALITIES:
                    selected = PERSONALITIES[p_choice]
                    system_prompt = load_prompt(selected["file"])
                    extra_data = None
                    Log.Info(f"Switched to {selected['name']}. Conversation restarted.")
                continue
                
            if user_input.lower() == "/prompt":
                print(f"{Fore.BLUE}Current System Prompt: {Style.DIM}{system_prompt[:200]}...")
                continue
                
            if user_input.lower() == "/help":
                print(f"{Fore.YELLOW}Available Commands:")
                print(f"  /exit    - Close the application")
                print(f"  /restart - Start a fresh conversation")
                print(f"  /persona - Switch between Aggressive and Nice personalities")
                print(f"  /prompt  - View the current system prompt")
                print(f"  /help    - Show this message")
                continue

            # Set system prompt in extra_data
            if extra_data is None:
                extra_data = {"system_prompt": system_prompt}

            print(f"{Fore.MAGENTA}Thinking...{Style.RESET_ALL}", end="\r")
            
            result = grok.start_convo(user_input, extra_data=extra_data)
            
            print(" " * 20, end="\r")
            
            if "error" in result:
                Log.Error(f"Request failed: {result['error']}")
                continue
            
            response = result.get("response")
            extra_data = result.get("extra_data")
            
            if response:
                print(f"\n{Fore.RED}Worm-GPT > {Style.RESET_ALL}{response}")
            else:
                Log.Warning("Received an empty response from Grok.")
            
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Interrupted. Type /exit to quit.")
        except Exception as e:
            Log.Error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
