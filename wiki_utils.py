import os
import subprocess

def get_wiki_text():
    if not os.path.exists("GAM.wiki"):
        subprocess.run(["git", "clone", "https://github.com/GAM-team/GAM.wiki.git"])
    
    text = ""
    for root, _, files in os.walk("GAM.wiki"):
        for f in files:
            if f.endswith(".md"):
                with open(os.path.join(root, f), encoding="utf-8") as file:
                    text += file.read() + "\n"
    return text[:12000]  # Limite token per GPT
