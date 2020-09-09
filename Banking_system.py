import sqlite3
import random
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

conn.execute('select number, pin, balance from card')
conn.commit()

cust = dict()
while True:
    print("""1. Create an account
2. Log into account
0. Exit""")
    ch = input()
    if ch == '0':
        print('Bye!')
        break
    elif ch == '1':
        num = 400000 * 10000000000
        while True:
            a = random.randint(100000, 1000000)
            a *= 10
            s = num + a
            n = list(str(s))
            m = []
            for i in range(16):
                digit = int(n[i-1])
                if i % 2 == 1:
                    digit *= 2
                    if digit > 9:
                        digit = digit - 9
                m.append(digit) 
                
            k = (10 - sum(m) % 10) % 10
            s += k
            cas = conn.execute('select number from card where number = {}'.format(s))
            if s in cas:
                continue
            else:
                break
        num += a + k
        pin = random.randint(1000, 10000)
        cust[num] = pin
        conn.execute('insert into card( number, pin) values ({}, {})'.format(num, pin))
        conn.commit()
        print("""Your card has been created
Your card number:
{}
Your card PIN:
{}""".format(num, pin))
    elif ch == '2':
        print('Enter your card number:')
        num = int(input())
        print('Enter your PIN:')
        pin = int(input())
        if num in cust:
            if cust[num] == pin:
                print('''You have successfully logged in!
    
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit''')
                while True:
                    ch = input()
                    if ch == '0':
                        print('Buy!')
                        break
                    elif ch == '1':
                        bal = conn.execute('select balance as bal from card where number = {}'.format(num))
                        print('Balance: {}'.format(bal))
                    elif ch == '5':
                        print('You have successfully logged out!')
                        break
                    elif ch == '2':
                        print('Enter income:')
                        inc = int(input())
                        print('Income was added!')
                        conn.execute('update card set balance = balance + {} where number = {}'.format(inc, num))
                        conn.commit()
                    elif ch == '3':
                        print('''Transfer
Enter card number:''')
                        numb = input()
                        m = []
                        for i in range(16):
                            digit = int(numb[i - 1])
                            if i % 2 == 1:
                                digit *= 2
                                if digit > 9:
                                    digit = digit - 9
                            m.append(digit)
                        suc = conn.execute('select number from card where number = {}'.format(numb))
                        suc = str(list(suc))
                        if sum(m) % 10 != 0:
                            print('Probably you made mistake in card number. Please try again!')
                        elif str(numb) not in suc:
                            print('Such a card does not exist.')
                        elif numb == num:
                            print("You can't transfer money to the same account!")
                        else:
                            print('Enter how much money you want to transfer:')
                            tra = int(input())
                            bal = conn.execute('select balance as bal from card where number = {}'.format(num))
                            bal = str(list(bal))
                            bal = int(bal[2:-3])
                            if tra > bal:
                                print('Not enough money!')
                            else:
                                print('Success!')
                                conn.execute('update card set balance = balance + {} where number = {}'.format(tra, numb))
                                conn.commit()
                                conn.execute('update card set balance = balance - {} where number = {}'.format(tra, num))
                                conn.commit()
                    elif ch == '4':
                        conn.execute('DELETE FROM card WHERE number = {}'.format(num))
                        conn.commit()
                        print('The account has been closed!')
                        break
            else:
                print('Wrong card number or PIN!')
        else:
            print('Wrong card number or PIN!')
    if ch == '0':
        break
