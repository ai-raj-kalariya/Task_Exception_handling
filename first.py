#psuedo code

#start
#show 4 option (add,update,delete,exit())
#select any one option
#if add 
#adding country,state and city
#if update
#updating country or state or city
#if delete 
#delete country or state or city
#if exit()
#end

country_dic = {}
empty = {}
info = {}
state_dic = {}
country = []
states = []
cities = []


def about():
    print("you can select one option")
    print("Enter 1 for Add")
    print("Enter 2 for Update")
    print("Enter 3 for Delete")
    print("Enter 4 for Exit()")

    value=int(input("\nChoose option : "))
    
    def add():
        global country
        country = [i for i in(input("\nEnter the country name : ").split(","))]

        reply1_state = input("\nAre you want to add state type 'yes' or 'no' : ")
        if reply1_state == 'yes':
            global states
            states = [i for i in(input("Enter the state name : ").split(","))]
            reply1_city = input("\nAre you want to add city type 'yes' or 'no' : ")
            if reply1_city == 'yes':
                print(states)
                repl = input("select the state name : ")
                if repl in states:
                    global cities
                    cities = [i for i in(input("Enter the city name :").split(","))]
                    for i in states:
                        state_dic[i] = empty
                        if i == repl:
                            state_dic[i] = cities
                else:
                    print("invalid state name")
        for i in country:
            country_dic[i] = state_dic
            print('\n',country_dic)
            print()
            about()

#  updation part starting.......

    def updt():
        ask_update = input("\nwhat you want to change (country, state, city) ? : ")

        if ask_update == 'country':
            print(country)
            select_country = input("\nselect country which you want to update : ")
            if select_country in country_dic.keys():
                updated_country = input("write the updated country name : ")
                country_dic[updated_country] = country_dic.pop(select_country)
                print('\n',country_dic)
            else:
                print("Invalid Country name")

        if ask_update == 'state':
            print(state_dic)
            select_state = input("\nselect state which you want to update : ")
            if select_state in state_dic.keys():
                updated_state = input("write the updated state name : ")
                state_dic[updated_state] = state_dic.pop(select_state)
                print('\n',country_dic)
            else:
                print("Invalid state name")

        if ask_update == 'city':
            print(cities)
            select_city = input("\nselect city which you want to update : ")
            if select_city in cities:
                updated_city = input("update city name : ")
                cities.append(updated_city)
                cities.remove(select_city)
                print('\n',country_dic)
            else:
                print("Invalid city name")
        
        print()
        about()
        
# deletion part started.....

    def delete():
        ask_delete = input("\nwhat you want to delete (country, state, city) ? : ")

        if ask_delete == 'country':
            print(country)
            select_country = input("\nselect country which you want to delete : ")
            if select_country in country_dic.keys():
                del country_dic[select_country]
                print('\n',country_dic)
            else:
                print("Invalid Country name")

        if ask_delete == 'state':
            print(state_dic)
            select_state = input("\nselect state which you want to delete : ")
            if select_state in state_dic.keys():
                del state_dic[select_state]
                print('\n',country_dic)
            else:
                print("Invalid state name")

        if ask_delete == 'city':
            print(cities)
            select_city = input("\nselect city which you want to delete : ")
            if select_city in cities:
                cities.remove(select_city)
                print('\n',country_dic)
            else:
                print("Invalid city name")
        
        print()
        about()
     
#Quit....

    def Exit():
    	print('\n',country_dic)
    	quit()
    	
    if value == 1:
        add()
    if value == 2:
        updt()
    if value == 3:
        delete()
    if value == 4:
        Exit()

about()
