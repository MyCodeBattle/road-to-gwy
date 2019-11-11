import os
os.system('gitbook build')
os.system('cp -r _book/* .')
os.system('git add .')
os.system('git commit -m commit')
os.system('git push')
print('finish task')
