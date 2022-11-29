main menu:
    print("********************************************")
    print("*                   Hello!                 *")
    print("*                                          *")
    print("*             (1)   admin?                 *")
    print("*             (2) captain?                 *")
    print("*             (3)   guest?                 *")
    print("*             (q)    quit?                 *")
    print("*                                          *")
    print("********************************************")


admin login
    print("********************************************")
    print("*             Hello admin!                 *")
    print("*                                          *")
    print("*                                          *")
    print("*     Please input password for admin      *")
    print("*             (b) to go back               *")
    print("*                                          *")
    print("*                                          *")
    print("********************************************")

captain login
    print("********************************************")
    print("*           Hello captain!                 *")
    print("*                                          *")
    print("*                                          *")
    print("*    Please input password for captain     *")
    print("*             (b) to go back               *")
    print("*                                          *")
    print("*                                          *")
    print("********************************************")

admin login
    print("********************************************")
    print("*             Hello admin!                 *")
    print("*                                          *")
    print("*                                          *")
    print("*     (1) Tournament standings             *")
    print("*     (b) to go back to main menu          *")
    print("*                                          *")
    print("*                                          *")
    print("********************************************")

inputprompt():
    admin_login()
    password = input("Please input password for admin")
    valid = validate_password(password)
    if password == "b":
        break
    while valid == False:
        print("Password incorrect")
    