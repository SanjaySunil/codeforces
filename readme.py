import glob
import os
import json
import requests
import re

problems_file = open('problems.json', 'r')
problems = json.loads(problems_file.read())
difficulties = list(sorted([int(x[:-1]) for x in glob.glob("*/")]))
problems_file.close()
string = ''
solved = 0
problems_file = open('problems.json', 'w')
for i in difficulties:
    arr = [os.path.basename(x)[:-3] for x in glob.glob(str(i) + "/*.py")]
    string += (f"\n## Difficulty: {str(i)}\n")
    string += ("\n| Problem | Solution |\n|---|---|\n")
    solved += len(arr)
    for j in sorted(arr):
        if j == 'tempCodeRunnerFile': pass
        else:
          if j in problems:
            string += f"| [{j} - {problems[j]}](https://codeforces.com/problemset/problem/{j[:-1]}/{j[-1]}) | [{j}.py](./{i}/{j}.py)|\n"
          else:
            r = requests.get(f'https://codeforces.com/problemset/problem/{j[:-1]}/{j[-1]}')
            sub1 = '<div class="title">'
            sub2 = '</div>'
            result = re.search('<div class="title">(.*)</div><div class="time-limit">', r.text)
            problems[j] = result.group(1)[3:]
            string += f"| [{j} - {problems[j]}](https://codeforces.com/problemset/problem/{j[:-1]}/{j[-1]}) | [{j}.py](./{i}/{j}.py)|\n"
            print(f'Added new problem: {j}')

problems_file.write(json.dumps({key: value for key, value in sorted(problems.items())}, sort_keys=True, indent=2, separators=(',', ': ')))
problems_file.close()

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
