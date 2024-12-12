# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 19:21:40 2022

@author: anany
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def display_menu():
    print("----------------------------------------------------")
    print(" ")
    print("Welcome to Courier Management System")
    print(" ")
    print("----------------------------------------------------")
    print(" ")
    print("1. Signup")
    print(" ")
    print("2. Login")
    print(" ")
    print("3. Quit")
    print(" ")
    print("----------------------------------------------------")

def add_user():
    print("-------------------------")
    print(" ")
    print("Registration ...")
    print(" ")
    print("-------------------------")
n = input('Name:')
print(" ")
mobile=int(input('MobileNo:'))
print(" ")
email=input('Email_IC:')
print(" ")
pas=input('Password:')
print(" ")
df=pd.read_csv("C:\\Downloads\\userlogin.csv")
df = df.append({'Name':'n','mob':'mobile',&#39;email&#39;:&#39;email&#39;,&#39;password&#39;:&#39;pas&#39;},ignore_index=True)
df.to_csv(&quot;C:\\Downloads\\userlogin.csv&quot;,index=False)
print(&#39;User Created&#39;)
print(&quot; &quot;)
input(&quot;Press any key to continue&quot;)
display_menu()

def login_user():
print(&quot;-------------------------&quot;)
print(&quot; &quot;)
print(&quot;-------- Login ---------&quot;)
print(&quot; &quot;)
print(&quot;-------------------------&quot;)
df=pd.read_csv(&quot;C:\\Downloads\\userlogin.csv&quot;)
a=int(input(&quot;Enter Mobile Number:- &quot;))
x=df[df[&quot;mob&quot;]==a]
if x.empty==False:
print(&quot;----- Login Successful -----&quot;)
loginmenu()
o=input(&quot;Enter your choice:- &quot;)
if o==&#39;1&#39;:

order()
elif o==&#39;2&#39;:
delete()
elif o==&#39;3&#39;:
service_track()
elif o==&#39;4&#39;:
net()
elif o==&#39;5&#39;:
input(&quot;PRESS ANY KEY TO CONTINUE&quot;)
else:
print(&quot;There is no such option&quot;)
print(&quot;Do you want to return to main menu?&quot;)
print(&quot; &quot;)
input(&quot;If yes,PRESS ANY KEY TO CONTINUE&quot;)
print(&quot; &quot;)
if a==123456:
adminmenu()
print(&quot; &quot;)
input(&quot;RETURN TO MAIN MENU(ADMIN PANEL)?&quot;)
print(&quot; &quot;)
adminmenu()
else:
print(&quot;----------------------------&quot;)
print(&quot; &quot;)
print(&quot;-------Invalid Number-------&quot;)
print(&quot; &quot;)
print(&quot;----------------------------&quot;)
display_menu()
def adminmenu():
print(&quot;----------------------------------------------------&quot;)
print(&quot; &quot;)

print(&quot; Courier Management System(ADMIN PANEL)&quot;)
print(&quot; &quot;)
print(&quot;----------------------------------------------------&quot;)
print(&quot;1. Customer Details&quot;)
print(&quot; &quot;)
print(&quot;2. Employee Details&quot;)
print(&quot; &quot;)
print(&quot;3. Add Employee&quot;)
print(&quot; &quot;)
print(&quot;4. Customers and Orders&quot;)
print(&quot; &quot;)
print(&quot;5. Return to Login Window&quot;)
print(&quot; &quot;)
print(&quot;----------------------------------------------------&quot;)
i=input(&quot;Enter your Choice:- &quot;)
if i==&#39;1&#39;:
print(&quot;-------------------------&quot;)
print(&quot; &quot;)
print(&quot;Customer Details&quot;)
print(&quot; &quot;)
print(&quot;-------------------------&quot;)
dfr=pd.read_csv(&quot;C:\\Downloads\\orderdet.csv&quot;)
print(dfr)
elif i==&#39;2&#39;:
print(&quot;-------------------------&quot;)
print(&quot; &quot;)
print(&quot;Employee Details&quot;)
print(&quot; &quot;)
print(&quot;-------------------------&quot;)
emp=pd.read_csv(&quot;C:\\Downloads\\empdet.csv&quot;)
print(emp)

elif i==&#39;3&#39;:
print(&quot;-------------------------&quot;)
print(&quot; &quot;)
print(&quot;Add Employee&quot;)
print(&quot; &quot;)
print(&quot;-------------------------&quot;)
nam=input(&quot;Enter Full Name:- &quot;)
numb=int(input(&quot;Enter Mobile Number:- &quot;))
em=input(&quot;Enter Employee Email:- &quot;)
iD=int(input(&quot;Enter ID Number:- &quot;))
sal=int(input(&quot;Enter Salary:- &quot;))
emp=pd.read_csv(&quot;C:\\Downloads\\empdet.csv&quot;)
emp=emp.append({&#39;Name&#39;:nam,&#39;MobileNumber&#39;:numb,&#39;Email&#39;:em,&#39;EmployeeID&#39;:iD,&#39;Salary&#39;:sal},ignor
e_index=True)
emp.to_csv(&quot;C:\\Downloads\\empdet.csv&quot;,index=False)
print(&quot;---------------------------&quot;)
print(&quot;Employee Successfully Added&quot;)
print(&quot;---------------------------&quot;)
elif i==&#39;4&#39;:
print(&quot;================================================&quot;)
print(&quot;================== SERVICES ================&quot;)
print(&quot;================================================&quot;)
service()
elif i==&#39;5&#39;:
display_menu()
def delete():
print(&quot;&quot;),
de=pd.read_csv(&quot;C:\\Downloads\\orderdet.csv&quot;)
bid=int(input(&quot;Please confirm your Mobile Number:- &quot;))
if bid in de[&#39;mob&#39;].values:
print(&quot;Are you sure you want to cancel your order?&quot;)

response=input(&quot;Enter &#39;Y&#39; for Yes and &#39;N&#39; for no:- &quot;)
if response==&#39;Y&#39; or response==&#39;y&#39;:
de.drop(de[de[&#39;mob&#39;]==bid].index,inplace=True)
print(&quot; &quot;)
print(&quot;YOUR ORDER HAS BEEN CANCELLED&quot;)
print(&quot; &quot;)
input(&quot;PRESS ANY KEY TO RETURN TO MAIN MENU&quot;)
else:
print(&quot; &quot;)
input(&quot;PRESS ANY KEY TO RETURN TO MAIN MENU&quot;)
print(&quot; &quot;)
else:
print(&quot; &quot;)
print(&quot;Order does not exist&quot;)
print(&quot; &quot;)
input(&quot;PRESS ANY KEY TO RETURN TO MAIN MENU&quot;)
print(&quot; &quot;)
def net():
print(&quot;=============================================================================
==================================================================================
=============================================================================&quot;)
print(&quot; &quot;)
print(&quot;1:National&quot;)
print(&quot; &quot;)
print(&quot;2:International&quot;)
print(&quot; &quot;)
print(&quot;3:Return to main menu&quot;)
print(&quot; &quot;)
print(&quot;=============================================================================
==================================================================================
=============================================================================&quot;)
me=int(input(&quot;INPUT ONE OPTION FROM ABOVE:-&quot;))

if me==1:
dfr=pd.read_csv(&#39;C:\\Downloads\\pct.csv&#39;)
print(dfr)
print(&quot; &quot;)
input(&quot;PRESS ANY KEY TO CONTINUE&quot;)
print(&quot; &quot;)
loginmenu()
elif me==2:
db=pd.read_csv(&#39;C:\\Downloads\\int.csv&#39;)
print(db)
print(&quot; &quot;)
input(&quot;PRESS ANY KEY TO CONTINUE&quot;)
print(&quot; &quot;)
loginmenu()
elif me==3:
print(&quot;Do you want to return to main menu?&quot;)
print(&quot; &quot;)
input(&quot;If yes,PRESS ANY KEY TO CONTINUE&quot;)
print(&quot; &quot;)
def service():
print(&quot;=============================================================================
==================================================================================
=============================================================================&quot;)
print(&quot; &quot;)
print(&quot;1:Postcards&quot;)
print(&quot; &quot;)
print(&quot;2:Letters&quot;)
print(&quot; &quot;)
print(&quot;3:Registered Newspapers&quot;)
print(&quot; &quot;)
print(&quot;4:Parcels&quot;)
print(&quot; &quot;)

print(&quot;5:Packets&quot;)
print(&quot; &quot;)
print(&quot;=============================================================================
==================================================================================
=============================================================================&quot;)
mm=int(input(&quot;INPUT ONE OPTION FROM ABOVE:-&quot;))
if mm==1:
df=pd.read_csv(&quot;C:\\Downloads\\postcard.csv&quot;)
for row in df:
a=df.data
b=df.year
plt.bar(b,a,width=0.5)
plt.xticks([2018,2019,2020])
plt.yticks([10,20,30,40,50,60,70])
plt.xlabel(&quot;Year&quot;)
plt.ylabel(&quot;Total Deliveries(in lakhs)&quot;)
plt.title(&quot;Postcard Deliveries per year(in lakhs)&quot;)
plt.show()
elif mm==2:

df=pd.read_csv(&quot;C:\\Downloads\\letters.csv&quot;)
for row in df:
a=df.data
b=df.year
plt.bar(b,a,width=0.5)
plt.xticks([2018,2019,2020])
plt.yticks([10,20,30,40,50,60,70])
plt.xlabel(&quot;Year&quot;)
plt.ylabel(&quot;Total Deliveries(in lakhs)&quot;)
plt.title(&quot;Letter Deliveries per year(in lakhs)&quot;)
plt.show()
elif mm==3:

df=pd.read_csv(&quot;C:\\Downloads\\RegNewspapers.csv&quot;)
for row in df:
a=df.data
b=df.year
plt.bar(b,a,width=0.5)
plt.xticks([2018,2019,2020])
plt.yticks([10,20,30,40,50,60,70])
plt.xlabel(&quot;Year&quot;)
plt.ylabel(&quot;Total Deliveries(in lakhs)&quot;)
plt.title(&quot;Registered Newspaper Deliveries per year(in lakhs)&quot;)
plt.show()
elif mm==4:
df=pd.read_csv(&quot;C:\\Downloads\\Parcels.csv&quot;)
for row in df:
a=df.data
b=df.year
plt.bar(b,a,width=0.5)
plt.xticks([2018,2019,2020])
plt.yticks([10,20,30,40,50,60,70])
plt.xlabel(&quot;Year&quot;)
plt.ylabel(&quot;Total Deliveries(in lakhs)&quot;)
plt.title(&quot;Parcel Deliveries per year(in lakhs)&quot;)
plt.show()
elif mm==5:
df=pd.read_csv(&quot;C:\\Downloads\\Packets.csv&quot;)
for row in df:
a=df.data
b=df.year
plt.bar(b,a,width=0.5)
plt.xticks([2018,2019,2020])
plt.yticks([10,20,30,40,50,60,70])

plt.xlabel(&quot;Year&quot;)
plt.ylabel(&quot;Total Deliveries(in lakhs)&quot;)
plt.title(&quot;Packet Deliveries per year(in lakhs)&quot;)
plt.show()
else:
print(&quot;There is no such option&quot;)
print(&quot; &quot;)
def order():
print(&quot;--------------------------------------&quot;)
print(&quot; &quot;)
print(&quot; Make Your order here &quot;)
print(&quot; &quot;)
print(&quot;--------------------------------------&quot;)
print(&quot; &quot;)
print(&quot; &quot;)
n=input(&#39;Name: &#39;)
print(&quot; &quot;)
mobile=int(input(&#39;MobileNo: &#39;))
print(&quot; &quot;)
email=input(&#39;Email_IC: &#39;)
print(&quot; &quot;)
print(&quot;Product fees&quot;)
print(&quot;Letter:-Rs55 each for any place in India;&quot;)
print(&quot; Rs150 each for International Delivery&quot;)
print(&quot;PostcarC:-Rs35 each for any place in India;&quot;)
print(&quot; Rs100 each for International Delivery&quot;)
print(&quot;Registered Newspaper:-Rs20 each for any place in India;&quot;)
print(&quot; Rs170 each for International Delivery&quot;)
print(&quot;[FOR MONTHLY SUBSCRIPTION PLEASE CONTACT THROUGH EMAIL TO
XsCourierservice@gmail.com]&quot;)
print(&quot;Parcel:-Rs70 each for any place in India;&quot;)

print(&quot; Rs150 each for International Delivery&quot;)
print(&quot;Packet:-Rs60 each for any place in India;&quot;)
print(&quot; Rs130 each for International Delivery&quot;)
product=input(&#39;Enter Product Name: &#39;)
print(&quot; &quot;)
amountprod=int(input(&quot;Enter No of Items: &quot;))
print(&quot; &quot;)
loc=input(&quot;Is this a National delivery or International Delivery? &quot;)
if loc==&#39;National&#39; or loc==&#39;national&#39;:
from_loc=input(&#39;Pickup Location(City): &#39;)
print(&quot; &quot;)
destination_loc=input(&#39;Delivery Location(City): &#39;)
print(&quot; &quot;)
if product==&#39;Letter&#39; or &#39;letter&#39;:
pay=amountprod*55
print(&quot;Amount to be payeC:- &quot;,pay)
elif product==&#39;Postcard&#39; or &#39;postcard&#39;:
pay=amountprod*35
print(&quot;Amount to be payeC:- &quot;,pay)
elif product==&#39;Registered Newspaper&#39; or &#39;registered newspaper&#39;:
pay=amountprod*20
print(&quot;Amount to be payeC:- &quot;,pay)
elif product==&#39;Parcel&#39; or &#39;parcel&#39;:
pay=amountprod*70
print(&quot;Amount to be payeC:- &quot;,pay)
elif product==&#39;Packet&#39; or &#39;packet&#39;:
pay=amountprod*60
print(&quot;Amount to be payeC:- &quot;,pay)
elif loc==&#39;International&#39; or loc==&#39;international&#39;:
from_loc=input(&#39;Pickup Location(Country,City): &#39;)
print(&quot; &quot;)

destination_loc=input(&#39;Delivery Location(Country,City): &#39;)
print(&quot; &quot;)
if product==&#39;Letter&#39; or &#39;letter&#39;:
pay=amountprod*150
print(&quot;Amount to be payeC:- &quot;,pay)
elif product==&#39;Postcard&#39; or &#39;postcard&#39;:
pay=amountprod*100
print(&quot;Amount to be payeC:- &quot;,pay)
elif product==&#39;Registered Newspaper&#39; or &#39;registered newspaper&#39;:
pay=amountprod*170
print(&quot;Amount to be payeC:- &quot;,pay)
elif product==&#39;Parcel&#39; or &#39;parcel&#39;:
pay=amountprod*150
print(&quot;Amount to be payeC:- &quot;,pay)
elif product==&#39;Packet&#39; or &#39;packet&#39;:
pay=amountprod*130
print(&quot;Amount to be payeC:- &quot;,pay)
else:
print(&quot;delivery location not available&quot;)
status=(&quot;Processing&quot;)
df=pd.read_csv(&quot;C:\\Downloads\\orderdet.csv&quot;)
df=df.append({&#39;mob&#39;:mobile,&#39;Name&#39;:n,&#39;Email&#39;:email,&#39;Product&#39;:product,&#39;ProductCount&#39;:amountprod,&#39;P
ayment&#39;:pay,&#39;from_loc&#39;:from_loc,&#39;destination_loc&#39;:destination_loc,&#39;Status&#39;:status},ignore_index=True
)
df.to_csv(&quot;C:\\Downloads\\orderdet.csv&quot;,index=False)
print(&quot; &quot;)
print(&#39;Make order successfully&#39;)
print(&quot; &quot;)
print(&quot;+========================================+&quot;)
print(&quot;|&quot;)
print(&quot;|Name: &quot;,n)
print(&quot;|Mobile: &quot;,mobile)

print(&quot;|Product:&quot;,product)
print(&quot;|Amount: &quot;,pay)
print(&quot;|&quot;)
print(&quot;+========================================+&quot;)
print(&quot; &quot;)
print(&quot;Payment is only accepted by means of CASH ON DELIVERY&quot;)
print(&quot; &quot;)
print(&quot;Sorry for the inconvienience&quot;)
print(&quot; &quot;)
input(&quot;PRESS ANY KEY TO RETURN TO MAIN MENU&quot;)
def service_track():
df1=pd.read_csv(&quot;C:\\Downloads\\orderdet.csv&quot;)
roll=int(input(&quot;Please confirm Mobile Number:- &quot;))
n=df1.loc[df1[&quot;mob&quot;]==roll]
if n.empty==False:
print(n)
else:
print(&quot;Order does not Exist&quot;)
print(&quot; &quot;)
input(&quot;PRESS ANY KEY TO CONTINUE&quot;)
def loginmenu():
print(&quot;----------------------------------------------------&quot;)
print(&quot; &quot;)
print(&quot; Welcome to Courier Management System&quot;)
print(&quot; &quot;)
print(&quot;----------------------------------------------------&quot;)
print(&quot;1. Make an Order&quot;)
print(&quot; &quot;)
print(&quot;2. Cancel an Order&quot;)
print(&quot; &quot;)
print(&quot;3. Service Track&quot;)

print(&quot; &quot;)
print(&quot;4. Our Service Network&quot;)
print(&quot; &quot;)
print(&quot;5. Return to Login Window&quot;)
print(&quot; &quot;)
print(&quot;----------------------------------------------------&quot;)
o=input(&quot;Enter your choice:- &quot;)
if o==&#39;1&#39;:
order()
elif o==&#39;2&#39;:
delete()
elif o==&#39;3&#39;:
service_track()
elif o==&#39;4&#39;:
net()
elif o==&#39;5&#39;:
display_menu()
else:
print(&quot;There is no such option&quot;)
print(&quot;Do you want to return to main menu?&quot;)
print(&quot; &quot;)
input(&quot;If yes,PRESS ANY KEY TO CONTINUE&quot;)
print(&quot; &quot;)
while True:
loginmenu()
print(&quot;----------------------------------------------------&quot;)
print(&quot; &quot;)
print(&quot; Welcome to Courier Management System&quot;)
print(&quot; &quot;)
print(&quot;----------------------------------------------------&quot;)
print(&quot; &quot;)

print(&quot;1. Signup&quot;)
print(&quot; &quot;)
print(&quot;2. Login&quot;)
print(&quot; &quot;)
print(&quot;3. Quit&quot;)
print(&quot; &quot;)
print(&quot;----------------------------------------------------&quot;)
print(&quot; &quot;)
choice = input(&quot;Enter your choice: &quot;)
print(&quot; &quot;)
if choice == &#39;1&#39;:
add_user()
elif choice == &#39;2&#39;:
login_user()
elif choice == &#39;3&#39;:
quit()
else:
print(&quot;There is no such option&quot;)
print(&quot;-------------------------------&quot;)
print(&quot; &quot;)
print(&quot; Thank you for using our system&quot;)
print(&quot; &quot;)
print(&quot;-------------------------------&quot;)

def display_menu():
print(&quot;----------------------------------------------------&quot;)
print(&quot; &quot;)
print(&quot; Welcome to Courier Management System&quot;)
print(&quot; &quot;)
print(&quot;----------------------------------------------------&quot;)
print(&quot; &quot;)

print(&quot;1. Signup&quot;)
print(&quot; &quot;)
print(&quot;2. Login&quot;)
print(&quot; &quot;)
print(&quot;3. Quit&quot;)
print(&quot; &quot;)
print(&quot;----------------------------------------------------&quot;)
choice = input(&quot;Enter your choice: &quot;)
if choice == &#39;1&#39;:
add_user()
elif choice == &#39;2&#39;:
login_user()
elif choice == &#39;3&#39;:
quit()
else:
print(&quot;There is no such option&quot;)
while True:
display_menu()