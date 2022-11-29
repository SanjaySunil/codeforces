import os
category = input('Difficulty: ')
problem = input('Problem: ')
os.system('git add .')
os.system(f'git commit -m "feat({category}): solved \`{problem}\`"')