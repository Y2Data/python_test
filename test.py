"""
このファイルに解答コードを書いてください
"""
import sys 
import collections

f = open('input.txt', 'r')
while f:
	lines = f.readlines()
	break

#clean the string
n_lines = []
for line in lines:
	line = line.strip("\n")
	n_lines.append(line)

#seperate m
m = n_lines[-1]
n_lines = n_lines[:-1]
#seperate i and s into two independent collection
i_s_dict = {}
for line in n_lines:
	i_s_dict[line[0]] = line[2:]
sorted_d = collections.OrderedDict(sorted(i_s_dict.items()))

output = ""
for i, s in sorted_d.items():
	if int(m) % int(i) == 0:
		output += s	

if output == "":
	print(m)
else:
	print(output)