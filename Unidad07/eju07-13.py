import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print(f'Encontrado "{match.re.pattern}" en "{match.string}" desde {s} a {e-1}')
      