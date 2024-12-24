filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']

results = []

for file in filenames:
    extention = file.split('.')[-1]
    if extention == 'h' or extention == 'c':
        results.append(file)

print(results)