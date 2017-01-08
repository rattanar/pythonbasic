a=2
b=2
while(a<=12):
	print(str(a)+"x"+str(b)+"="+str(a*b))
	b=b+1
	if(b>12):
		a=a+1
		b=2

#break
a=2
b=2
while(True):
	print(str(a)+"x"+str(b)+"="+str(a*b))
	b=b+1
	if(b>12):
		a=a+1
		b=2
	if(a>12):
		break

text = "Today is Sunday. I stay at home and keep coding. Today is Monday. I stay at office and keep cleaning but still keep coding."
def find_all(text, word):
	start_pos = 0
	while (start_pos!=-1):
		text, start_pos = find_next_word(text, word, start_pos)
		
	
