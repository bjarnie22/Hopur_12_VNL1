def main():
    menu()
    answer = input()
    while answer != "q":
        while answer not in ["1", "2", "3"]:
            print("Please pick a ")
            answer = input()
        if answer == "1":
            admin_login()
            break
        elif answer == "2":
            captain_login()
            break
        elif answer == "3":
            guest()
            break
    
def admin_login():
    print("admin login deez nuts")

def captain_login():
    print("captian login deez nuts")

def guest():
    print("guest deez nuts")

def menu():
    print("********************************************")
    print("*                   Hello!                 *")
    print("*                                          *")
    print("*             (1)   admin?                 *")
    print("*             (2) captain?                 *")
    print("*             (3)   guest?                 *")
    print("*             (q)    quit?                 *")
    print("*                                          *")
    print("********************************************")


if __name__ == "__main__":
    main()