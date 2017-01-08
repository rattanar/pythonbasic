#########if##############
if (<Condition>):
	<Block 1>
else:
	<Block 2>

#################

if (<Condition 1>):
	<Block 1>
elif (<Condition 2>):
	<Block 2>
else:
	<Block 3>

#################

if (<Condition 1>):
	<Block 1>
elif (<Condition 2>):
	<Block 2>
elif (<Condition 3>):
	<Block 3>
else:
	<Block 4>

next_word = text[:text.find(" ")]

if (text.find(" ") != -1):
	next_word = text[:text.find(" ")]
else:
	next_word = text

if (a >= 5 and a <= 10):
if (a == 5 or a == 10):
if (a == 5 or a == 10 or a == 15):
if((a ==5) or (a >= 10 and a <= 15)):

#########nestedif##############
if (<Condition 1>):
	if(Condition 2>):
		<Block 1>
	else(<Condition 3>):
		<Block 2>

###############hw##############
#pattern1 
score = 80
if (score >= 80) :
	print("A")
elif (score >= 70 and score < 80) :
	print("B")
elif (score >= 60 and score < 70) :
	print("C")
elif (score >= 50 and score < 60) :
	print("D")
else : 
	print("F")	

#pattern2 can write pattern2 in python
score = 80
if (score >= 80) :
	print("A")
elif ( 70 <= score < 80) :
	print("B")
elif ( 60 <= score < 70) :
	print("C")
elif ( 50 <= score < 60) :
	print("D")
else : 
	print("F")	

#pattern3
score = 80
if (score >= 80) :
	print("A")
elif ( score >= 70) :
	print("B")
elif ( score >= 60 ) :
	print("C")
elif ( score >= 50) :
	print("D")
else : 
	print("F")		