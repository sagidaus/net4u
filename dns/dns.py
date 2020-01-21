def menu():
    print("\n Menu: \n1. Add new url and ip \n2. Delete specific url \n3. Update ip to exits url \n4. Print to screen all url and ip's \n5. searching\n6. exit")
def add():
    c = input("Enter url : ")
    d = input("Enter ip :")
    dns.update({c: d})
def Delete():
    e = input("Enter url : ")
    if e in dns:
        del dns[e]
def update():
    f = input("Enter url : ")
    if f in dns:
        new = input("Enter new ip: ")
        dns[f] = new
    else:
        print("Url not exits")
def printscr():
    for key, value in dns.items():
        print('Url: {}, Ip: {}'.format(key, value))
def search():
    key = input("Enter url: ")
    if key in dns:
        print ("url exits")
    else:
        print("not exits")

dns = {}
print("Building the first DNS dictionary")
print("Enter 5 url's and ip's")
for i in range (2):
    a = input("Enter url : ")
    b = input("Enter ip :")
    dns.update({a: b})
x = "yes"
while x == "yes" or x == "y":
    menu()
    num = input("Enter your number: ")
    if num == "1":
        add()
    elif num == "2":
        Delete()
    elif num == "3":
        update()
    elif num == "4":
        printscr()
    elif num == "5":
        search()
    elif num == "6":
        exit()
    else:
        x = input("Type yes to continue or q to quit: ")