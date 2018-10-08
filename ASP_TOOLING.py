tool_met = [500,250,250,100,100,100,80,55,50,45,40,35,30,30,25]
sae = True
b_length = 60
b_length_met = b_length*25.4

start = 0
for i in range(0, len(tool_met)):
	if tool_met[i] > b_length_met:
		continue
	else:
		start = i
		break

best_num = tool_met[start]
best = [best_num]
for i in range(start,len(tool_met)-start):
	for j in range(i+1,len(tool_met)-i):
		if best_num < best_num+tool_met[j] < b_length_met:
			best_num += tool_met[j]
			best.append(tool_met[j])
			tool_met[j] = 0
		else:
			continue

if ((b_length_met - best_num)/2) < 12.7:
	print('TOOLING COMBINATION FOUND')
else:
	print('NO TOOLING COMBINATION FOUND')
print('Bend Length:', b_length_met, 'mm')
print('ASP Total Length:', best_num, 'mm')
print('ASP Tools Used:', best)
print('Bend Overhang:', (b_length_met - best_num)/2, 'mm')