import random
ONE_LIST_PRICE = 3

def menu():
    exit = "yes"

    while (exit == "yes"):
        print("Lotto menu: \n1. Manual\n2. Auto\n3. Double \n4. Check winning")
        win = random.sample(range(1, 10), 6)
        choose = int(input("Choose number: "))
        if choose == 1:
            results = manual()
            calculate_win(results, win)
        elif choose == 2:
            results = auto()
            calculate_win(results, win)
        elif choose == 3:
            print("3")
        # elif choose == 4:
        #     check_win(manu)
        else:
            print("Enter 1-4 only")
            continue
        choose2 = input("Are you want to quit? yes/no")
        if choose2 == "no":
            continue
        else:
            print("Bye bye")
            break
    print("winnig numbers: " + str(win))


def get_list_from_user():
    results = []

    print("Enter your 6 number in a row: ")
    for j in range(6):
        num = int(input("Enter number: "))
        while num < 1 or num > 37:
            print("Enter 1-37 only")
            num = int(input("Enter number: "))
        results.append(num)
    return results


def manual():
    money = int(input("Enter how many shekels you have: "))
    while (money < ONE_LIST_PRICE):
        print("minimum %s shekels" % ONE_LIST_PRICE)
        money = int(input("Enter how many shekels you have: "))

    num_of_lists = money // ONE_LIST_PRICE
    print("Please enter %s list" % num_of_lists)
    customer_lists = []
    for i in range(num_of_lists):
        print("Enter List #%s" % (i+1))
        current_results = get_list_from_user()
        print("List #%s completed" % i)
        customer_lists.append(current_results)
        print("list #%s: %s: " % (i, current_results))
    return customer_lists


def auto():
    money = int(input("Enter how many shekels you have: "))
    if money < ONE_LIST_PRICE:
        print("minimum %s shekels" % ONE_LIST_PRICE)
    num_of_lists = money // ONE_LIST_PRICE
    print("Please enter %s list" % num_of_lists)

    # print("You get " + str(int(money // 3)) + " auto list's")
    autolist = []
    for i in range(num_of_lists):
        auto = random.sample(range(1, 10), 6)
        autolist.append(auto)
    # print(autolist)
    return (autolist)
    # check_win(autolist)


def double():
    print("double")


# get a list in a and return the total prize
def check_win(qqq, win):
    guesses = 0

    # count the number of right guesses
    for num in qqq:
        if num in win:
            guesses += 1

    # calculate the reward
    reward = 0
    if guesses == 6:
        reward = 1000000
    elif guesses == 5:
        reward = 5000
    elif guesses == 4:
        reward = 250
    elif guesses == 3:
        reward = 10

    return reward


def calculate_win(lists, win):
    total_reward = 0
    for a_list in lists:
        reward = check_win(a_list, win)
        total_reward += reward
        print("List %s won: %s " % (a_list, reward))
    print ("Total Reward: %s" % total_reward)
    print("winning list: %s " % win)

################### main code ##############################

### winnig list ###
print(menu())
