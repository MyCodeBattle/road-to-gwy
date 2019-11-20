import os
os.system('gitbook build 冰熊手册/')
os.system('cp -r 冰熊手册/_book/* .')
os.system('git add .')
os.system('git commit -m commit')
os.system('git push')
