#!/usr/bin/python3

db = {}

def newuser():
    prompt = 'login desired:'
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name taben,try another:'
        else:
            break
    pwd = input('passwd:')
    if len(pwd) == 0:
        print("passwd can't null")
    else:
        db[name] = pwd

def olduser():
    name = input('login:')
    if name not in db:
        print('name :%s not exists!' % name)
    else:
       pwd = input('passwd:')
       passwd = db.get(name)
       if passwd == pwd:
           print ('welcome back',name)
       else:
           print ('login incorrect')

def showmenu():
    prompt = """
           (N)ew User Login
           (E)xisting User Login
           (Q)uit
           
           Enter choice:"""
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
                print(choice)
            except (EOFError,KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked:[%s]' % choice)
            if choice not in 'neq':
                print ('invalid option,try again')
            else:
                chosen = True
                if choice == 'q':done = True
                if choice == 'n':newuser()
                if choice == 'e':olduser()

if __name__ == '__main__':
    showmenu()
