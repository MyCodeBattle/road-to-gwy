import os
os.system('gitbook build')
os.system('cp -r _books/* .')
os.system('git add .')
os.system('git commit -m commit')
os.system('git push')
print('finish task')
