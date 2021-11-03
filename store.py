

PRODUCT = []

def loadFile():

    print('laoding...')

    f = open('database.csv' , 'r')
    textFile = f.read()
    rows = textFile.split('\n')
    
    for row in rows:
        info = row.split(',')
        new_dictianory = { 'id':info[0] , 'name':info[1] , 'price':info[2] , 'count':info[3] }
        PRODUCT.append(new_dictianory)
    print('OK.')


def show():
    i = 1
    for pro in PRODUCT:
        print(i , "-" , pro)
        i += 1
         

def add():
   
    counter = int(input('How many products do you want to add? '))
    f = open('database.csv' , 'a')

    for i in range(counter):
        print('Product',i+1,':')
        id = int(input('Product ID: '))
        name = input('Product Name: ')
        price = int(input('Product Price: '))
        count = int(input('Number of products available: '))

        addFile = [id , ',' , name , ',' , price ,',' , count]
        f.write('\n')
        for x in addFile:
            f.write(str(x))
        i+=1
    
    print('Added.')


def edit():
    NAME = input('Enter the NAME of the product you want to edit: ')
    for x in PRODUCT:
        if NAME == x['name']:
            x['id'] = input('Enter new ID: ')
            x['price'] = input('Enter new Price: ')
            x['count'] = input('Enter new Count: ')

            print('Edited')
            break
        

def delete():
    NAME = input('Enter the NAME of the product you want to delete: ')
    
    f = open('database.csv', 'r')
    lineFile = f.readlines()
    f = open('database.csv', 'w')

    for line in lineFile:
        if NAME not in line:
            f.write(line)
    print('Deleted.')
    f.close()

    for x in PRODUCT:
        if NAME == x['name']:
            PRODUCT.remove(x)
    

def search():
    NAME = input('Which product do you want to search for? ')
    flag = 0
    for x in PRODUCT:
        if  NAME == x['name']:
            print('Found:')
            print(x)
            flag = 1
    if flag == 0:
        print('not found..!')
             

def buy():
    NAME = input('Enter the product name: ')
    flag = 0
    for x in PRODUCT:
        if  NAME == x['name']:
            C = int(x['count'])
            if C == 0 :
                print('Sorry . this product is not available')
                flag = 1
            
            else :
                flag = 1
                C -= 1
                x['count'] = str(C)
                print('Ok. Please pay the cost : ', x['price'] , '$')
    
    if flag == 0:
        print('not found..!')



loadFile()

def showMenu():
    print('''
    ... Welcome ...
    
    1- Show products
    2- Add
    3- Edit
    4- Delete
    5- Search
    6- Buy & Print invoice
    7- Exit
    ''')



while True:
    showMenu()
    select = int(input('Choose an option : '))
    
    if select == 1:
        show()

    elif select == 2:
        add()

    elif select == 3:
        edit()

    elif select == 4:
        delete()

    elif select == 5:
        search()

    elif select == 6:
        buy()

    elif select == 7:
        print('saved , bye')
        exit()