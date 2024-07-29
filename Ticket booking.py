#login page
print("___________Welcome To Fast&Safe Bus__________")
print("__________Bus Ticket Booking__________")
print("Sign up")
username=input("username:")
age=int(input("userage:"))
gender=input("male/female/other:")
email=input("email:")
number_=int(input("Enter Your Mobile Number:"))
while True:
    password=input("password:")
    re_password=input("re_enter password:")
    if password==re_password:
         print("SUCCESSESFULLY REGISTER")
         break
    else:
        print("Both Password Or Not Same")    
print("Sign in")
while True:
    login=input("username:")
    login_pass=input("password:")
    if (username==login and password==login_pass):
         print("SIGN IN SUCCESSFULLY")
         break
    else:
         print("username or password is wrong")
#booking page
print("!!!!!BOOK NOW!!!!!")
class route1():
    def chennai_to_trichy(self):
        print("!!!!!BOOK NOW!!!!!")
        print("chennai,kilambakkam,chengalpet,melmaruvathur,thindivanam,villuppuram,ulundurpet,trichy...")
        while True:
            from_=input("From:")      
            to_=input("to:")
            if(from_=="chennai" and to_=="trichy"):
                details21={"bus_no":"301",
                        "pickuptime":"8.30",
                        "amount":"700"}
                print(details21)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==700:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="ulundurpet"):
                details22={"bus_no":"301",
                        "pickuptime":"8.30",
                        "amount":"550"}
                print(details22)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==550:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="villuppuram"):
                details23={"bus_no":"301",
                        "pickuptime":"8.30",
                        "amount":"450"}
                print(details23)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==450:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="thindivanam"):
                details24={"bus_no":"301",
                        "pickuptime":"8.30",
                        "amount":"400"}
                print(details24)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==400:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="melmaruvathur"):
                details25={"bus_no":"301",
                        "pickuptime":"8.30",
                        "amount":"350"}
                print(details25)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==350:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="chengalpet"):
                details26={"bus_no":"301",
                        "pickuptime":"8.30",
                        "amount":"300"}
                print(details26)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==300:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="kilambakkam"):
                details27={"bus_no":"301",
                        "pickuptime":"8.30",
                        "amount":"200"}
                print(details27)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==200:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
                break
            else:
                print("enter your correct route")
class route2(route1):
    def chennai_to_pudhuchery(self):
        print("!!!!!BOOK NOW!!!!!")
        print("stops:chennai,navalur,mamallalapuram,kalpakkam,kuvathur,marakkanam,pudhuchery...")
        while True:
            from_=input("From:")      
            to_=input("to:")
            if(from_=="chennai" and to_=="pudhuchery"):
                details11={"bus_no":"302",
                        "pickuptime":"8.30",
                        "amount":"1000"}
                print(details11)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==1000:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="marakkanam"):
                details12={"bus_no":"302",
                        "pickuptime":"8.30",
                        "amount":"800"}
                print(details12)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==800:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="kuvathur"):
                details13={"bus_no":"302",
                        "pickuptime":"8.30",
                        "amount":"700"}
                print(details13)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==700:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="kalpakkam"):
                details14={"bus_no":"302",
                        "pickuptime":"8.30",
                        "amount":"550"}
                print(details14)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==550:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="mamallalapuram"):
                details15={"bus_no":"302",
                        "pickuptime":"8.30",
                        "amount":"350"}
                print(details15)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==350:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="navalur"):
                details16={"bus_no":"302",
                        "pickuptime":"8.30",
                        "amount":"250"}
                print(details16)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==250:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
                break
            else:
                print("enter your correct route")
                break
class route3(route2):
    def chennai_to_madurai(self):
        print("!!!!!BOOK NOW!!!!!")
        print("stops:chennai,villupuram,ulundurpet,perambalur,trichy,madurai...")
        while True:
            from_=input("From:")      
            to_=input("to:")
            if(from_=="chennai" and to_=="madurai"):
                details1={"bus_no":"303",
                        "pickuptime":"8.30",
                        "amount":"1500"}
                print(details1)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==1500:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="trichy"):
                details2={"bus_no":"303",
                        "pickuptime":"8.30",
                        "amount":"900"}
                print(details2)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==900:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="perambalur"):
                details3={"bus_no":"303",
                        "pickuptime":"8.30",
                        "amount":"600"}
                print(details3)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==600:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="ulundurpet"):
                details4={"bus_no":"303",
                        "pickuptime":"8.30",
                        "amount":"500"}
                print(details4)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==500:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="dindukkal"):
                details5={"bus_no":"303",
                        "pickuptime":"8.30",
                        "amount":"1200"}
                print(details5)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==1200:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
            elif(from_=="chennai" and to_=="villupuram"):
                details6={"bus_no":"303",
                        "pickuptime":"8.30",
                        "amount":"450"}
                print(details6)
                while True:
                    amount=int(input("pay the amount for ticket booking:"))
                    if amount==450:
                        print("payment succesfully!")
                        print("your ticket is booked")
                        break
                    else:
                        print("@ payment amount was wroung @","pay the correct amount and confirm your ticket",",")
                break
            else:
                print("enter your correct route")
                break
obj=route3()
print("1)chennai to trichy")
print("2)chennai to pudhuchery")
print("3)chennai_to_madurai")
while True:
    route=int(input("enter the root:"))
    if route==1:
        obj.chennai_to_trichy()
        break
    elif route==2:
        obj.chennai_to_pudhuchery()
        break
    elif route==3:
        obj.chennai_to_madurai()
        break
    else:
        print("enter your correct route")
