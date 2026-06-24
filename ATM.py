'''    #deposit
def Deposit():
    Balance=0
    c=int(input('Enter your Deposit Amount'))
    d=input('Enter your Passwod')
    if d=='4321':
        Balance+=c
        print('Your Doposit is successfully Completed')
        return Balance
    else:
        print('Your Password is Wrong')
        return Balance
Balance=Deposit()
z=Balance
#Withdraw
def Withdraw():
    w=input('Enter your Password')
    if w=='4321':
        r=int(input('Enter the Amount'))
        if r<=z:
            e=z-r
            print(e)
Withdraw()
def login():
        print('Welcome to HDFC bank')
        print('Please insert your atm card')
        s=input('if you inserted the card click <ok>')
        if s=='ok':
            a=10000
            b=int(input('Enter your 4 Digit Password'))
            if b==1212:
                print('your password is correct')
                log()
def deposit():
        a=10000
        n=int(input('Enter the amount'))
        b=int(input('Enter your 4 Digit Password'))
        if b==1212:
            print('your password is correct')
            if b>=n:
                m=a-n
                print('Your balance amount is',m)
                print('Your withdraw is successfully completed')
                log()
def log():
    print('select the 1,2,3,4,5 options')
    z=int(input('Withdraw  (1)=>
                Deposit  (2)=
                Balance  (3)=>
                Exit  (4)=>'))
    if z==1:
        deposit()
login()'''
#----------------log in------------
balance=10000
def login():
    print('Welcome to SBI Bank')
    print('Insert your ATM card')
    a=input('if you inserted enter ok=>')
    b=int(input('Enter your 6 Digit Password=>'))
    if b==102938:
        print('Your Password is correct')
        print('loading')
        option()
    else:
        print('your password is incorrect try again')
        login()
#------------option---------------
def option():
    print('select the option')
    print('Withdraw  <1>')
    print('Deposit   <2>')
    print('Balance   <3>')
    print('Exit      <4>')
    c=int(input('Type or select one Option=>'))
    if c==1:
        Withdraw()
    elif c==2:
        Deposit()
    elif c==3:
        Balance()
    elif c==4:
        Exit()
    else:
        print('incorrect Option')
        option()
        #---------------withdraw-----------
def Withdraw():
    print('Welcome to Withdraw')
    d=int(input('Enter your Amount=>'))
    if d<=balance:
        print('Your balance is=>',balance)
        b=int(input('Enter your 6 Digit Password=>'))
        if b==102938:
            print('Your password is correct')
            print('Withdraw is successfully Completed')
            print('Collect your Amount')
            print('Your remaining amount is=>',balance-d)
            option()
        else:
            print('Your Password is incorrect')
            Withdraw()
    else:
        print('In your Account That much Amount is not There')
        Withdraw()
#----------deposit-----------------
def Deposit():
    print('Welcome to Deposit')
    e=int(input('Enter your Deposit Amount=>'))
    if e<=50000:
        f=int(input('Enter your 6 Digit Password=>'))
        if f==102938:
            print('Your password is correct')
            print('Your Deposit is Successfully Completed')
            print('Your balance Amount is =>',balance+e)
            option()
        else:
            print('Your Password is incorrect')
            Deposit()
    else:
        print('In one Time You can Deposit only 50,000')
        Deposit()
#------------balance----------------
def Balance():
    print('Welcome to Balance Checking')
    f=int(input('Enter your 6 Digit Password=>'))
    if f==102938:
        print('Your password is correct')
        print('Your Balance is =>',balance)
        option()
    else:
        print('Your Password is incorrect')
        Balance()
#---------------exit--------------------
def Exit():
    print('Thank you for Visiting the SBI Bank')
    
login()
