import sqlite3
import time
con = sqlite3.connect('todo.db')
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS todolist(unix DOUBLE,period TEXT,time TEXT,action VAR_CHAR(50))")
def read_all():
    print('read all')
    data = c.execute('SELECT*FROM todolist')
    data = c.fetchall()    
    print("\tunix\t|\x20\x20\x20\x20period\x20\x20\x20\x20|  time\t\x20\x20\x20\x20\x20| action")
    for row in data:
           row = str(row)
           print(row.replace('(',' ').replace(')',' ').replace(',' ,'   | ' ))
def read_some():
    print('read some')
    while True:
        period = input('Enter period:')
        c.execute('SELECT time,action FROM todolist WHERE period={}'.format(period))
        data = c.fetchall()
        print("\tunix\t|\x20\x20\x20\x20period\x20\x20\x20\x20|  time\t\x20\x20\x20\x20\x20| action")
        for row in data:
           row = str(row)
           print(row.replace('(',' ').replace(')',' ').replace(',' ,'   | ' ))
        cont = input('continue? (y/n):')
        if cont == 'n':
            break
        else:
            continue
        
def insert():
    print('insert')
    while True:
        unix = int(time.time())
        period = input('enter the period:')
        action = input('enter the thing to do in this period :')
        t = input('Enter the time:')
        cont = input('continue? (y/n):')
        c.execute("INSERT INTO todolist(unix,period,time,action) VALUES(?,?,?,?)",(unix,period,t,action))
        if cont == 'n':
            break
        else:
            continue
    con.commit()
    time.sleep(1)
def help():
    print('help')
    
        
    return 'helped'

    
def main():
    actions = { 'read all': read_all,'read some' : read_some,'insert' : insert,'help' : help,'quit':quit}
    keys = []
    while True:
        command = input('Enter your command : ')
        for key,action in actions.items():
            if command == key:
                action()
                keys.append(key)
        if command not in keys:
            print('command {} not found'.format(command))
        if command == 'quit':
            print('byeee!!!')
            break   
main()
