month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
def get_month_name(order):
	return month[order-1]

#####################
name1 = ['aaa','bbb']
name2 = ['xxx','yyy']
name_list = [['aaa','bbb'],['xxx','yyy']]
name_list2 = [name1,name2]
print(name_list)
print(name_list[0])
print(name_list[1][1])

####################
people = [['Supasate','Choochaisri',30],
['Somchai','Python',22],['Thongchai','Java',42],
['Thana','C',15],['Nat','Ruby',20]]
print(people[3][1])
print(people[2][2]-people[1][2])

####################
l = [1,2]
p = l
l = l+[3,4]
print(p)
print(len(l))
print(len(p))

#l = [1,2]
#p = l
#l += [3,4]
#print(p)