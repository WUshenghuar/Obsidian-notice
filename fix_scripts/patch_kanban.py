import os

path = r'D:\Users\雾盛华\Documents\Obsidian Vault\.obsidian\plugins\obsidian-kanban\main.js'
print(f'Reading {path}...')
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

old = 'getItem("language")'
new = 'getItem("language")==="zh-CN"?"zh":getItem("language")'

count = content.count(old)
print(f'Found {count} occurrences')

if count > 0:
    content = content.replace(old, new, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Replacement done!')
else:
    print('Not found!')
