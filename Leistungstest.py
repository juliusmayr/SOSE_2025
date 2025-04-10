First Projekt

first_experiment = {'date':'13.03.2025', 'supervisor':'JM', 'distance':'3000m'}

x : str = first_experiment['date']
y : str = first_experiment['supervisor']
z : str = first_experiment['distance']
print(x)
print(y)
print(z)

print()
print()

for i in range(10):
  try:
    i += 1
    print(i,first_experiment)
  except ZeroDivisionError:
    print('error')

print()
print()

for i in range(5):
  i += 1
  print(i,first_experiment)

print()
print()

print('letze aufgabestellung schaff ich nicht')
