import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
print("El texto analizado es: ",text)
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Encontrado "%s" entre la posicion %d y %d' % (text[s:e], s, e-1))