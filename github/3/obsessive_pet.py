import re

txt = input()
txt = re.sub(r' +', ' ', txt.strip())
txt = re.sub(r"\\n", "\n", txt)

text = []
text = list(txt)
text2 = []
atcounter = 0
for c in text:
    if c == '@':
        text2.append(c)
        atcounter += 1
    elif c == '#' and atcounter > 0:
        atcounter -= 1
    else:
        text2.append(c)       
result = ''
for c in text2:
    result += c

print("Formatted Text: " + result)
