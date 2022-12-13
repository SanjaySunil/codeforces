import glob
import os

difficulties = list(sorted([int(x[:-1]) for x in glob.glob("*/")]))
f = open('template.md', 'r')
template = f.readlines()
f.close()

f = open('README.md', 'w')
f.writelines(template)
f.close()

f = open('README.md', 'a')

for i in difficulties:
  arr = [os.path.basename(x)[:-3] for x in glob.glob(str(i) + "/*.py")]
  f.writelines(f"\n## Difficulty: {str(i)}\n")
  f.writelines("\n| Problem | Solution |\n|---|---|\n")
  [f.writelines(f"| [{j}](https://codeforces.com/problemset/problem/{j[:-1]}/{j[-1]}) | [{j}.py](./{i}/{j}.py)|\n") for j in arr]

f.close()