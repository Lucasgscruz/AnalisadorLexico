a = ['lucas,ffsf,asda', 'fdsf,sfdsdf.sfsfsd=sdfsf', 'sfsdf=sfsf']
cont = 0
for i in a :
    a[cont] = i.split(',')
    cont+=1

print a
