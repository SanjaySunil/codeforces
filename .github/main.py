import os
# Used `alias` command on mac to run globally
problem = input('Problem: ')
os.system('git add .')
os.system(f'git commit -m "feat({problem[-1]}): solved \`{problem[:-1]}{problem[-1]}\`"')