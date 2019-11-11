import os
with open('dict.en','r', encoding='utf-8') as f, open('new_dict.en','a') as n:
	for line in f.readlines(): 
		new_line = line.strip(',').strip(' ').replace('"','').replace(':', ' ').replace(',',' ')
		n.write(new_line)


