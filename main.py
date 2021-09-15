import time, sys
if len(sys.argv) < 2:
	print("Please give a ARG with the name of file, syntax:\"python main.py <file>\".")
	exit()
file = open(sys.argv[1], 'r+')
html = open('index.html', 'w+')
print('Reading your program...')
for c in range(10):
	print('#'*c)
	time.sleep(0.5)

print('.')
time.sleep(0.5)
print('..')
time.sleep(0.5)
print('...')

time.sleep(0.5)
print('Done!')
time.sleep(0.5)
print('A file (index.html) was created in this path.')
print('Tags found:')

lines_file = file.readlines()
tagsOpen = []
for line in lines_file:
	if '%' in line:
		line = line[:line.index('%')]
	line = line.replace("\t", "")
	if 'DOCTYPE' in line:
		#DOCTYPE: type;
		doctype = line[line.index(':')+1:line.index('!')].replace(" ", "")
		html.write(f'<!doctype {doctype}>')
	if '{' in line and '$' not in line:
		#tag{
		tag = line[:line.index('{')].replace(" ", "")
		print(f"<{tag}>")
		time.sleep(0.5)
		tagsOpen.append(f'{tag}')
		html.write(f'<{tag}')
		try:
			linhe = line
			while linhe != "":
				attr = linhe[linhe.index('<')+1:linhe.index(':')]
				value = linhe[linhe.index(':')+1:linhe.index('>')]
				html.write(f' {attr}={value}')
				linhe = linhe[linhe.index('>')+1:]
		except:
			pass
			#html.write(f'<{tag}>')
		html.write('>')
	if '$' in line and '{' in line:
		styleset = line[line.index('$')+1:line.index("{")]
		html.write(styleset + '{')
	elif '$' in line and '}' in line:
		html.write('}')
	if len(tagsOpen) > 1 and '{' not in line and '}' not in line:
		html.write(line)
	if '}' in line and '$' not in line:
		#}tag
		tag = line[line.index('}')+1:].replace(" ", "")
		tagsOpen.pop()
		html.write(f'</{tag}>')
print('\nSize of file:')
print(sys.getsizeof(lines_file), 'Bytes')
print('\nYour site is created.')
html.close()
file.close()