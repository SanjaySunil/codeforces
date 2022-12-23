import glob
import os

difficulties = list(sorted([int(x[:-1]) for x in glob.glob("*/")]))

string = ''
solved = 0
for i in difficulties:
    arr = [os.path.basename(x)[:-3] for x in glob.glob(str(i) + "/*.py")]
    string += (f"\n## Difficulty: {str(i)}\n")
    string += ("\n| Problem | Solution |\n|---|---|\n")
    solved += len(arr)
    for j in arr:
        if j == 'tempCodeRunnerFile': pass
        else: string += f"| [{j}](https://codeforces.com/problemset/problem/{j[:-1]}/{j[-1]}) | [{j}.py](./{i}/{j}.py)|\n"

f = open('README.md', 'w')
f.writelines(f"""
<br />
<h1 align="center">
  <a href='https://codeforces.com/profile/sanjaysunil' target="_blank">
  <img width="400px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Codeforces_logo.svg/2560px-Codeforces_logo.svg.png" />
  </a>
</div>

<h3 align='center'>Solutions to problems from the <a href="https://codeforces.com/problemset">problem set</a> on <a href="https://www.codeforces.com/">CodeForces</a></h3>

<p align="center">
	<img src="https://img.shields.io/badge/Problems%20Solved-{str(solved)}-brightgreen.svg">
	<img src="https://img.shields.io/badge/Language-Python-blue.svg">
</p>
<br/>

This repository contains my solutions to problems from the CodeForces problem set.
""")
f.writelines(string)
f.close()
