def swapData():
    file1=input('1st file name: ')
    file2=input('2nd file name: ')
    with open(file1,'r') as a:
        data_a=a.read()
    with open(file2,'r') as b:
        data_b=b.read()    
    with open(file1,'w') as a:
        a.write(data_b)
    with open(file2,'w') as a:
        b.write(data_a)

swapData()