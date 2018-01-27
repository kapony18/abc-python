
cats = ['Gryffindor','Hufflepuff','Ravenclaw','Slytherin']
file = 'houseFile.txt'
house =''
for line in open(file, 'r'):
    if line.rstrip() in cats:
    	house=line.rstrip()
    else:
    	name = line.split()
    	if len(name) > 1 :
    		firstName = name[0]
    		lastName = name[1]
    		fh = open('characters/'+firstName+'_'+lastName+'.json','w')
    		fh.write('{\n\t"firstName": "'+firstName+'",\n\t"lastName": "'+lastName+'",\n\t"house": "'+house+'"\n}')
    		fh.close()

