@echo off
python3 -c "import sys; sys.stdout.reconfigure(encoding='utf-8'); f=open(r'D:\Users\雾盛华\Documents\Obsidian Vault\.obsidian\plugins\obsidian-kanban\main.js','r+',encoding='utf-8'); c=f.read(); f.seek(0); f.write(c.replace('getItem(\"language\")','getItem(\"language\")===\"zh-CN\"?\"zh\":getItem(\"language\")',1)); f.truncate()"
