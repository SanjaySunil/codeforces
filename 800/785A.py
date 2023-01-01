n = int(input())
t = 0
for _ in range(n):
  string = input().lower()
  shapes = {
    'icosahedron': 20,
    'cube': 6,
    'tetrahedron': 4,
    'dodecahedron': 12,
    'octahedron': 8,
  }
  if string in shapes: t+=shapes[string]
print(t)