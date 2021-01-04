global f
f = 0
global Inox
Inox=20
global Inon
Icon=20
global pvp
pvp=20
t_book1=[]
t_book2=[]
t_book3=[]

#this t_movie function is used to select movie name
def t_movie():

    global f
    f = f+1
    print("which movie do you want to watch?")
    print("1,movie 1 ")
    print("2,movie 2 ")
    print("3,movie 3")
    print("4,back")
    movie = int(input("choose your movie: "))
    if movie == 4:
         center()
         theater()
         return 0
    if f == 1:
         theater()

# this theater function used to select screen
def theater():
    print("which screen do you want to watch movie: ")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a = int(input("chosse your screen: "))
    if a>3 and a<1:
        print("Please make valid choice")

    timing(a)

# this timing function used to select timing for movie
def timing(a):
    time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.25-4.25",
        "3": "4.35-7.35",
        "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.00-10.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("successfull!, enjoy movie at "+x)
        print("Do you want book more tickets??")
        print("Press 1 for 'Yes' and Press 2 for 'No'")
        c = int(input())
        if c == 1:
            city()
        else:
            exit()
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("successfull!, enjoy movie at "+x)
        print("Do you want book more tickets??")
        print("Press 1 for 'Yes' and Press 2 for 'No'")
        c = int(input())
        if c == 1:
            city()
        else:
            exit()
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("successfull!, enjoy movie at "+x)
        print("Do you want book more tickets??")
        print("Press 1 for 'Yes' and Press 2 for 'No'")
        c=int(input())
        if c==1:
            city()
        else:
            exit()

    return 0


def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")


def center():
    print("which theater do you wish to see movie? ")
    print("1,Inox")
    print("2,Icon")
    print("3,pvp")
    print("4,back")

    a = int(input("choose your option: "))
    ticket(a,Inox,Icon,pvp)

    return 0

def ticket(a,Inox,Icon,pvp):
    tk = int(input("number of ticket do you want?: "))
    if tk > 5:
        print("Sorry!! You can only book 5 tickets at once")
        ticket(a,Inox,Icon,pvp)
    if Inox== 0 or Icon == 0 or pvp == 0 or Inox < tk or Icon < tk or pvp < tk:
        print("Sorry!! House Full")
        center()
    else:
        if a == 1:
            print("Which seat do you want?? plz mention seperated with space")
            n1 = list(map(int, input().split()))
            for i in n1:
                if i <= 20 and i > 0:
                    if i not in t_book1:
                        t_book1.append(i)

                        Inox=Inox-1
                    else:
                        print("This seat is already booked")
                        ticket(a,Inox,Icon,pvp)
        elif a == 2:
            print("Which seat do you want?? plz mention seperated with space")
            n2 = list(map(int, input().split()))
            for i in n2:
                if i <= 20 and i > 0:
                    if i not in t_book2:
                        t_book2.append(i)
                        Icon=Icon-1
                    else:
                        print("This seat is already booked")
                        ticket(a,Inox,Icon,pvp)
        elif a == 3:
            print("Which seat do you want?? plz mention seperated with space")
            n3 = list(map(int, input().split()))
            for i in n3:
                if i <= 20 and i > 0:
                    if i not in t_book3:
                        t_book3.append(i)
                        pvp=pvp-1
                    else:
                        print("This seat is already booked")
                        ticket(a,Inox,Icon,pvp)
        elif a==4:
            center()
    movie(a)
    return 0

# this function is used to select city
def city():
    print("Hi welcome to movie ticket booking: ")
    print("where you want to watch movie?:")
    print("1,city 1")
    print("2,city 2")
    print("3,city 3")
    place=int(input("choose your option:"))
    if place==1:
        center()
    elif place==2:
        center()
    elif place==3:
        center()
    else:
        print("Wrong Choice")


city() # it calls the function city
