#!/usr/bin/env python
# coding: utf-8

# In[3]:


def design(stop,design):
        r=''
        if design == 2:
            hyphen='_'
        else:
            hyphen='*'
        for a in range(0,stop):
            r+=hyphen
        print(r)
        
def colour(textual_data,color):
    a="\033[3{};1m ".format(str(color)) #31:Red,32:Green,33:Yellow,34:Blue,35:Purple,36:Cyan,37:White
    return (a+str(textual_data))
 
def datarep(left_side_data,right_side_data):
    print("\n{0:>00}{1:>25}{2:>28}{3:>15}\n".format((colour('|',2)),(colour(left_side_data,4)),(colour(right_side_data,1)),(colour('|',2))),end='')
    
def center(textual_data):
    print("\n{0:<15}".format(''),end='')
    print("{0:>22}".format(textual_data))
    
def message(textual_data,time_interface):
    for char in textual_data:
        print(char,end='')
        time.sleep(time_interface)
try:
    import sys
    import time
    import numpy as np
    import pandas as pd
    from datetime import datetime,date
    import math, random
    import os
    from getpass import getpass
    import mysql.connector as sqltor
    get_ipython().run_line_magic('matplotlib', 'inline')
    import matplotlib.pyplot as plt
    import pyautogui as pyg
    from cryptography.fernet import Fernet as fr  
    import webbrowser
    start1=True
except ImportError as err:
    design(60,2)
    design(60,2)
    center(colour('Error Occurs while Importing Libraries\n Error: {}'.format(err),1))
    design(60,2)
    center(colour('Check All Libraries Presence',4))
    design(60,2)
    sys.exit()
    start1=False

if start1 :
    if os.path.exists('Boot_Memory.csv'):
        pyg.alert("Boot_Memory.csv at local Path - Found \n        All Opeartions Established Successfully !!\n\nNote :\n\t❖ Deletion of this file results Boot-Recovery        \n\ti.e. Fresh Start by Rebuilding New Database (clearing all previous data).        \n\t❖ Its path should be local with respect to Dev Bank.ipynb\n\t❖ Don't make any Changes in this file. ",'Dev Bank CRM')
        start2=True ## Showing Avail. of prior created Boot_Memory.csv
    else:
        a=['Version','MySQL Password','Database Name','Path','Secret_Key','*CAUTION : CHANGES RESULTS ERRORs & Deletion (whole file) results Mester Reset*']
        df=pd.DataFrame(a,columns=['DevBank'])
        df.to_csv('Boot_Memory.csv')
        pyg.alert('As Boot_Memory.csv absent\nNew Boot_Memory Established Successfully !!\n\n        The System will have Master Restart/Start !!\n\nNote :\n\t❖ Deletion of this file results Boot-Recovery        \n\ti.e. Fresh Start by Rebuilding New Database (clearing all previous data).        \n\t❖ Its path should be local with respect to Dev Bank.ipynb\n\t❖ Don-t make any Changes in this file. ' ,'Dev Bank CRM')
        start2=False
        ## Showing the Availab. of Database but not of Boot_Memory.csv
auth=''
acnum=''
        
def boot_data(index_value):
    df=pd.read_csv('Boot_Memory.csv')
    a=df.at[index_value,'DevBank']
    return a

 
if start1 :
    df=pd.read_csv('Boot_Memory.csv')
    if df.at[0,'DevBank'] == 'Version':
        df.at[0,'DevBank']= '4.1.3'
        df.to_csv('Boot_Memory.csv')
        design(60,2)
        center(colour('Boot_Memory Found @local_path',2))
        design(60,2)
        time.sleep(0.2)
        design(60,2)
        m=getpass('♕ Provide MySQL DBMS Password│ ')
        t=input('♕ Provide Any Existing Database Name│ ')
        df.at[1,'DevBank']= m
        df.at[2,'DevBank']= t
        df.to_csv('Boot_Memory.csv')
        design(60,2)
        center(colour('❖ Important Points ❖',1))
        design(60,2)
        datarep('Types of A/C','Saving & Current')
        center(colour('For Saving',4))
        datarep('Min. Bal','2000')
        datarep('Service Chg.','0.5%')
        datarep('Min. Bal. Def. Chg.','5%')
        datarep('A/C will Suspended','Bal<100')
        design(60,2)
        time.sleep(0.1)
        center(colour('For Current',4))
        datarep('Min. Bal','10000')
        datarep('Service Chg.','0%')
        datarep('Min. Bal. Def. Chg.','5%')
        datarep('A/C will Suspended','Bal<100')
        design(60,2)
        time.sleep(0.1)
        design(60,2)
        datarep('Version',df.at[0,'DevBank'])
        center(colour('Made under Supervision of',2))
        center(colour('MR. Shah & Company',2))
        center(colour('Mansion3058 ',4))
        design(60,2)
        center(colour('★ The Above Message only Shows Once ★',1))
        design(60,2)
        time.sleep(0.3)
        #Creating a Directory for Dev BanK Files
        design(60,2)
        center(colour('Select Drive for Storage',4))
        datarep(' Press 1 ➤','D Drive')
        datarep(' Press 2 ➤','E Drive')
        datarep('Any Key ➤','C Drive')
        design(60,2)
        c=input('● Condition Chosen │ ')
        if c =='1':
            p="D:/"
        elif c=='2':
            p="E:/"
        else:
            p="C:/"
        d="Dev Bank"
        df.at[3,'DevBank']= p
        df.at[4,'Secret_Key']= fr.generate_key().decode()
        df.to_csv('Boot_Memory.csv')
        webbrowser.open('file:///'+p)
        design(60,2)
        center(colour('❖ Repositories Created Sucsfly ❖',2))
        design(60,2)
        time.sleep(0.2)
## Checking the Availabilities of the Directories
d="Dev Bank"
p=df.at[3,'DevBank']
path=os.path.join(p,d)
if os.path.exists(path) is False:
    os.mkdir(path)
d="Report Graphs"
p_dir=p+"Dev Bank/"
path=os.path.join(p_dir,d)
if os.path.exists(path) is False:
    os.mkdir(path)
d="ACC Statement"
path=os.path.join(p_dir,d)
if os.path.exists(path) is False:
    os.mkdir(path)
d="Others"
path=os.path.join(p_dir,d)
if os.path.exists(path) is False:
    os.mkdir(path)
## Checking the Availabilities of the Directories    

##PRIVACY OCCURS HERE
fernet=fr(df.at[4,'Secret_Key'])  #Creating object
def encrypt(data):
    x=fernet.encrypt(data.encode())
    return x.decode()

def decrypt(data):
    x=fernet.decrypt(data).decode()
    return x
##PRIVACY OCCURS HERE
if start1 :
    try:
        mycon=sqltor.connect(host="localhost",user="root",passwd=boot_data(1),database=boot_data(2))
        files=mycon.cursor(buffered=True)
        if start2 is False:
            try:
                files.execute('use devbank')
                files.execute('drop database devbank;')
                files.execute('create database if not exists devbank')
                
            except sqltor.Error:
                files.execute('create database if not exists devbank')
        else:
            files.execute('create database if not exists devbank')
        files.execute('use devbank')
        start3=True
    except sqltor.Error as err:
        start3=False
        a='⚠-❌ Something went Wrong ❌-⚠ \n Database Refuse to Connect\n\n Error : {}'.format(err)
        pyg.alert(a,'Dev Bank CRM')
        design(60,2)
        center(colour(a,1))
        design(60,2)
        sys.exit()
        
if start1  and start3 :
    try:
        files.execute('Select * from devcus;')
    except sqltor.Error:
        sql='''create table if not exists devcus(
            cusid char(12) primary key,
            acnum integer,
            ac_type char(10),
            name char(20),
            passw blob,
            dob date,
            age int(3),
            uaid bigint(20),
            gender char(1),
            phone bigint(20),
            crdate date,
            crtime time,
            active tinyint(1) default 0,
            balance integer
        )'''
        files.execute(sql)
    try:
        files.execute('Select * from staff;')
    except sqltor.Error:
            sql='''create table if not exists staff(
                id char(12) primary key,
                name char(20) not null ,
                pasw blob,
                post char(20) not null
                    )'''
            files.execute(sql)
            #Inserting Default Values into Staff Tables 
            files.execute("insert into staff values('arman@dev','Arman Singh','{}','manager')".format(encrypt('arman123')))
            mycon.commit()
            files.execute("insert into staff values('aman@dev','Aman Kaur','{}','teller')".format(encrypt('aman123')))
            mycon.commit()
            files.execute("insert into staff values('rahul@dev','Rahul Kumar','{}','cashier')".format(encrypt('rahul123')))
            mycon.commit()
    try:
        files.execute('Select * from acstatement;')
    except sqltor.Error:
        sql='''create table if not exists acstatement(
                cusid char(12),
                description varchar(50),
                chqnum varchar(20) default '0',
                Withdrawn varchar(20) default '----',
                Deposit varchar(20) default '----',
                trandate date,
                trantime time,
                operation char(10),
                balance varchar(20)
 
            )'''
        files.execute(sql)
    try:
        files.execute('Select * from atm;')
    except sqltor.Error:
        sql='''create table if not exists atm(
                    cusid char(12),
                    atmnumber varchar(20),
                    date timestamp default current_timestamp,
                    pin blob,
                    status char(12) default 'Active'
 
                )'''
        files.execute(sql)
    try:
        files.execute('Select * from application;')
    except sqltor.Error:
        sql='''create table if not exists application(
                cusid char(12),
                application varchar(20),
                date timestamp default current_timestamp,
                status char(12) default 'Unaccepted'
 
            )'''
        files.execute(sql)
    try:
        files.execute('Select * from blocktrans;')
        start3=True
    except sqltor.Error:
        sql='''create table if not exists blocktrans(
                    cusid char(12),
                    cheqnum char(12),
                    date timestamp default current_timestamp
 
                )'''
        files.execute(sql)
message('Welcome to Dev Bank CRM (Customer Relation Management) System',0.2)
print()
while True:
    def vals(data):
        if data !='' and data!=' ':
            if data.isalpha():
                return True
            else:
                design(50,1)
                center(colour("❌ Enter Data is Not valid ❌\n",1))
                design(50,1)
        else:
            design(50,1)
            center(colour("❌ Null Value unacceptable ❌\n",1))
            design(50,1)
    def valn(data):
        if data.isdigit()  :
            return True
        else:
            design(60,2)
            center(colour('❌ Given Number is not valid ❌',1))
            design(60,2)
            
    def nonzero(numeric_data_in_string_form):
        if numeric_data_in_string_form[0] != '0':
            return True
        else:
            design(60,2)
            center(colour('❌ Zero at First place Unacceptable ❌',1))
            design(60,2)
            
    def valcon(data,length_condition):
        if len(data) == length_condition:
            return True        
        else:
            design(60,2)
            center(colour('❌ Given Argument Unacceptable ❌',1))
            design(60,2)
            
    def alpha(numeric_data):
        num=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
        tens=["Ten","Eleven","Tweleve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        wrd=""
        r=1
        numeric_data=str(numeric_data)
        if numeric_data[0]!="0":
            if len(numeric_data)==7:
                if numeric_data[0]=="1":
                    wrd+=tens[int(numeric_data[1])]+ " Lakhs "
                    numeric_data=numeric_data[2::]
                    while int(numeric_data[0])==0 and r<5:
                        numeric_data=numeric_data[1::]
                        r=r+1
                else:
                    wrd+=nty[int(numeric_data[0])]+ " "+num[int(numeric_data[1])] + " Lakhs "
                    numeric_data=numeric_data[2::]
                    while int(numeric_data[0])==0 and r<5:
                        numeric_data=numeric_data[1::]
                        r=r+1
            if len(numeric_data)==6:
                wrd+=num[int(numeric_data[0])]+ " Lakhs "
                numeric_data=numeric_data[1::]
                while int(numeric_data[0])==0 and r<5:
                    numeric_data=numeric_data[1::]
                    r=r+1
            if len(numeric_data)==5:
                if numeric_data[0]=="1":
                    wrd+=tens[int(numeric_data[1])]+ " Thousand "
                    numeric_data=numeric_data[2::]
                else:
                    wrd+=nty[int(numeric_data[0])]+ " "+num[int(numeric_data[1])] + " Thousand "
                    numeric_data=numeric_data[2::]
            if len(numeric_data)==4:
                wrd+=num[int(numeric_data[0])]+" Thousand "
                numeric_data=numeric_data[1::]
            if len(numeric_data)==3:
                if numeric_data[0]!="0":
                    wrd+=num[int(numeric_data[0])]+" Hundred "
                    numeric_data=numeric_data[1::]
                else:
                    numeric_data=numeric_data[1::]
            if len(numeric_data)<=2:
                if len(numeric_data)==1:
                    wrd+=num[int(numeric_data)]
                elif int(numeric_data)<20:
                    if numeric_data[0]=="0":
                        wrd+=num[int(numeric_data[1])]
                    else:
                        wrd+=tens[int(numeric_data[1])]
                else:
                    wrd+=str(nty[int(numeric_data[0])])+" "+str(num[int(numeric_data[1])])
            else:
                design(60,2)
                center(colour("Out of Range 9999999",1))
                design(60,2)
        return wrd
    
    def unique(column,data):
        df=usdetails('staff','a')
        if df.empty is False:
            for a in df[column]:
                if a==data:
                    break
                    return False
                else:
                    return True
        else:
            return True
 
    def usdetails(author,cusid):
        if author=='staff':
            if cusid!='a':
                files.execute("select cusid,acnum,ac_type,name,dob,uaid,age,phone,active,balance from devcus where cusid = '{}' ".format(cusid))
                dt=files.fetchall()
                df=pd.DataFrame(dt,columns=["Cust ID","A/C_Num","A/C Type","Name","DOB","UAID (Aadhar No.)","Age","Phone","Status","Balance"])
                df.set_index('Cust ID',inplace=True)
                return df
            elif cusid=='a':
                files.execute("select cusid,acnum,ac_type,name,dob,uaid,age,phone,active,balance from devcus")
                dt=files.fetchall()
                df=pd.DataFrame(dt,columns=["Cust ID","A/C_Num","A/C Type","Name","DOB","UAID (Aadhar No.)","Age","Phone","Status","Balance"])
                df.set_index('Cust ID',inplace=True)
                return df
        elif author=='cus':
            files.execute("select cusid,acnum,ac_type,name,dob,uaid,age,gender,phone,crdate,crtime,balance from devcus where cusid = '{}' ".format(cusid))
            dt=files.fetchall()
            df=pd.DataFrame(dt,columns=["Cust ID","A/C_Num","A/C Type","Name","DOB","UAID (Aadhar No.)","Age","M/F","Phone",                                        "Admisn.Date","Admisn.Time","Balance"])
            df.set_index('Cust ID',inplace=True)
            return df
        else:
            files.execute("select * from devcus where cusid = '{}' ".format(cusid))
            dt=files.fetchall()
            df=pd.DataFrame(dt,columns=["Cust ID","A/C_Num","A/C Type","Name","key","DOB","Age","UAID (Aadhar No.)","M/F","Phone","Admisn.Date","Admisn.Time","Status","Balance"])
            df.set_index('Cust ID',inplace=True)
            return df
        
    def hasatm():
        files.execute("select cusid,atmnumber,date,status from atm ")
        dt=files.fetchall()
        df=pd.DataFrame(dt,columns=["Cust ID","ATM Card No.","Applied Date","Status"])
        df.set_index('Cust ID',inplace=True)
        return df
    
    def applatm(cusid):
        df=hasatm()
        if cusid in df.index:
            design(60,2)
            center(colour('❖ You already have ATM Card ❖',4))
            design(60,2)
        else:
            design(60,2)
            center(colour('★ Pin should be = 4 digit ★',1))
            cn=getpass('➤ Enter Pin for Your ATM Card │ ')
            if valn(cn)  and valcon(cn,4):
                design(60,2)
                acnum=''
                digits = "989006500058525800"
                for i in range(10):
                    acnum+=digits[math.floor(random.random() * 10)]
                acnum='3058'+acnum
                files.execute("insert into atm(cusid,atmnumber,pin,status) values(%s,%s,%s,%s)"                                  ,(cusid,acnum,encrypt(cn),'Unactive'))
                mycon.commit()
                files.execute("insert into application(cusid,application) values(%s,%s)"                                  ,(cusid,'ATM '+acnum))
                mycon.commit()
                design(60,2)
                pyg.alert('Application Submitted Successfully','Dev CRM -'+str(cusid))
                center(colour('❖ Application Submitted Successfully ❖',2))
                datarep('ATM No.',acnum)
                center(colour('For ATM Card visit Bank',2))
                design(60,2)
    
    def atmdetails():
        files.execute("select * from atm")
        dt=files.fetchall()
        df=pd.DataFrame(dt,columns=["Cust ID","ATM Number","Date","Pin","Status"])
        df.set_index('Cust ID',inplace=True)
        return df
        
    def leave(cusid):
        design(60,2)
        center(colour('✌ Thanks for Visit ✌ ',2))
        datarep('User Id ➤',cusid)
        t=datetime.now()
        datarep('Leave at ➤',t.strftime("%H:%M:%S"))
        center(colour(d.strftime("%A, %B %d"),4))
        center(colour('★ Have a Good Day ★',2))
        design(60,2)
        time.sleep(0.2)
 
    def status(cusid,category):
        if category=='Account':
            df=usdetails('staff',cusid)
            if df.at[cusid,'Status'] == 1:
                return True
            else:
                return False
        elif category=='ATM':
            df=hasatm()
            if df.at[cusid,'Status'] == 'Unactive':
                return False
            else:
                return True
        else:
            df=appldetails()
            if df.at[cusid,'Status'] == 'Unaccepted':
                return False
            else:
                return True
            
    def appldetails():
        files.execute("select * from application")
        dt=files.fetchall()
        df=pd.DataFrame(dt,columns=["Cust ID","Application","Date","Status"])
        df.set_index('Cust ID',inplace=True)
        return df
        
    def updstatus(cusid,category,active_or_not):
        if category=='Account':
            files.execute("update devcus set active='{}' where cusid='{}'".format(active_or_not,cusid))
            mycon.commit()
            design(60,2)
            center(colour("❖ Changes made Successfully ❖",2))
            design(60,2)
            design(60,2)
            datarep('Current Status ➤',active_or_not)
            design(60,2)
        elif category=='ATM':
            files.execute("update atm set status='{}' where cusid='{}'".format(active_or_not,cusid))
            mycon.commit()
            design(60,2)
            center(colour("❖ Changes made Successfully ❖",2))
            design(60,2)
            design(60,2)
            datarep('Current Status ➤',active_or_not)
            design(60,2)
        else:
            if status(cusid,'Appl') is False:
                files.execute("update application set status='{}' where cusid='{}'".format(active_or_not,cusid))
                mycon.commit()
                design(60,2)
                center(colour("❖ Apllication Accepted Successfully ❖",2))
                design(60,2)
            else:
                design(60,2)
                center(colour("❖ Apllication Already Accepted ❖",1))
                center(colour(" ✌ No Changes Detected ✌ ",2))
                design(60,2)
 
    def is_date(date_in_string_format):
        format = "%Y-%m-%d"
        try:
            datetime.strptime(date_in_string_format, format)
            return True
        except ValueError:
            return False
    
    def acstatement(x,p):
        design(60,2)
        cn=input('(OPTIONAL) Statement From the Date(format : YYYY-MM-DD) of│ ')
        if is_date(cn) == False:
            files.execute("select description,chqnum,Withdrawn,Deposit,trandate,trantime,balance from acstatement where cusid = '{}' ".format(x))
        else:
            files.execute("select description,chqnum,Withdrawn,Deposit,trandate,trantime,balance from acstatement where cusid = '{}' and trandate >= '{}' ".format(x,cn))
        dt=files.fetchall()
        df=pd.DataFrame(dt,columns=["Description","ChqNum.","Dr.Amt","Cr.Amt","Transaction Date","Transaction Time","Balance"])
        df.set_index('Transaction Date',inplace=True)
        if df.empty is not True:
            design(60,2)
            t='Cusid : '+x
            center(colour(t+'A/C Statement ',5))
            d=datetime.now()
            if is_date(cn) :
                datarep('From ',cn)
                datarep('To ',str(d)[:19:])                                                                    
            else:
                datarep('As on ',str(d))
            design(60,2)
            print(df)
            design(60,2)
            time.sleep(0.2)
            if p!='s':
                graph(df,cn)
            design(60,2)
            cn=input('\n➤ Want to Save this Data 【y/n】 │ ')
            if cn == 'Y' or cn=='y':
                if p!='s':
                    design(60,2)
                    datarep('Press 1 ➤','Statement')
                    datarep('Press 2 ➤','Graph')
                    datarep('Press 3 ➤','Both')
                    datarep('Any Key ➤',' Back')
                    design(60,2)
                    c=input('\n● Condition Chosen │ ')
                    if c == '1':
                        save(df,'ac')
                        design(60,2)
                    elif c == '2':
                        graph(df,'y')
                        design(60,2)
                    elif c == '3':
                        design(60,2)
                        center(colour('❖ For Statement ❖',5))
                        save(df,'ac')
                        design(60,2)
                        center(colour('❖ For Graphical Data ❖',5))
                        design(60,2)
                        graph(df,'y')
                        design(60,2)
 
                    else:
                        design(60,2)
                        center(colour('✤ Back to Menu ✤',4))
                        design(60,2)
                else:
                    
                    (df,'other')
                    
            else:
                design(60,2)
                center(colour('✤ Proposal Rejected ✤',6))
                design(60,2)
        else:
            design(60,2)
            center(colour('✤ No Record Found ✤',4))
            design(60,2)
        
        return df
    
    def graph(df,f):
        l1=[]
        l2=[]
        clr=[]
        xa=df.index
        xa=xa.values
        y=df['Balance']
        y=y.values
        for a in range(len(xa)):
            l1.append(a+1)
            l2.append(float(y[a]))
            if acty(x,0) == 'saving':
                if l2[a] < 2000 :
                    clr.append('r')
                elif l2[a] == 2000 or l2[a] < 4000:
                    clr.append('b')
                else:
                    clr.append('g')
            else:
                if l2[a] < 10000 :
                    clr.append('r')
                elif l2[a] == 10000 or l2[a] < 20000:
                    clr.append('b')
                else:
                    clr.append('g')
        plt.figure(figsize=(10,5))
        plt.grid(True)
        d=datetime.now()
        if is_date(f) :
            cn=f+' to '+ str(d)
            plt.title('Change in Balance from '+cn)
            plt.xlabel(cn)
        else:
            plt.title('Change in Balance as on'+str(d)[:19:])
            plt.xlabel('Interval of Time')
        plt.ylabel('Balance in Rupees')
        plt.bar(l1,l2,color=clr)
        if f == 'y':
            design(60,2)
            b=input('\n➤ Enter the Name for  Document │ \t ')
            design(60,2)
            d=boot_data(3)+'Dev Bank\Report Graphs'
            p=os.path.join(d,b+'.pdf')
            if os.path.exists(p):
                design(60,2)
                center(colour('【 File Name Already Exists 】',1))
                design(60,2)
                design(60,2)
                a=input('\n➤ Want to Replace or Overwrite ? 【y/n】 │ ')
                design(60,2)
                if vals(a)  :
                    if a=='y' or a=='Y':
                        d=date.today()
                        t=datetime.now()
                        n='Balances Report till ' + t.strftime("%H:%M:%S")+ ' ' + str(d) + ' Dev Bank ID :- ' + x
                        plt.title(n)
                        plt.savefig(p)
                        center(colour('❖ Graph Save Successfully ❖',2))
                        datarep('Document Name ➤',b+'.pdf')
                        datarep('Path ➤ ',p)
                        p=os.path.join(boot_data(3)+'Dev%20Bank/Report%20Graphs/',b+'.pdf')
                        webbrowser.open('file:///'+p)
                        design(60,2)
                else:
                    design(60,2)
                    center(colour('❖ Try Again with Different Name ❖',4))
                    design(60,2)
            else:
                plt.savefig(p)
                center(colour('❖ Graph Save Successfully ❖',2))
                datarep('Document Name ➤ ',b+'.pdf')
                datarep('Path ➤ ',p)
                p=os.path.join(boot_data(3)+'Dev%20Bank/Report%20Graphs/',b+'.pdf')
                webbrowser.open('file:///'+p)
                design(60,2)
        else:
            plt.show()
        
    def amountstatus(x,a,c,b):
        while True:
            if c == 'aa' or c=='ac':
                if c =='aa':
                    files.execute("select description,chqnum,Deposit,trandate,trantime from acstatement where deposit={} and cusid = '{}' and operation = 'Add' ".format(a,x))
                    dt=files.fetchall()
                    break
                else:
                    files.execute("select description,chqnum,Deposit,trandate,trantime from acstatement where chqnum={} and cusid = '{}' and operation = 'Add'".format(a,x))
                    dt=files.fetchall()
                    break
 
            else:
                if c == 'wa':
                    files.execute("select description,chqnum,Withdrawn,trandate,trantime from acstatement where withdrawn={} and cusid = '{}' and operation = 'Less' ".format(a,x))
                    dt=files.fetchall()
                    break
                else:
                    files.execute("select description,chqnum,Withdrawn,trandate,trantime from acstatement where chqnum={} and cusid = '{}' and operation = 'Less' ".format(a,x))
                    dt=files.fetchall()
                    break
                    
        if dt == []:
            design(60,2)
            center(colour('❖ No Such Transaction Found ❖',1))
            design(60,2)
        else:
            df=pd.DataFrame(dt,columns=["Reference description","Cheq No.","Amount","Transaction Date","Transaction Time"])
            df.set_index('Reference description',inplace=True)
            return print(df)
    
    def cheqnum(x,c):
        files.execute("select chqnum,description from acstatement where cusid = '{}' and operation ='Less';".format(x))
        dt=files.fetchall()
        df=pd.DataFrame(dt,columns=["Cheq No.","description"])
        df.set_index('Cheq No.',inplace=True)
        if c in df.index :
            design(60,2)
            center(colour('☛ Cheque already in System',1))
            center(colour('❖ Changes unmade Yet ❖',4))
            design(60,2)
            
        else:
            return True
        
        
    def blcdup(x,c):
        files.execute("select cheqnum,date from blocktrans where cusid = '{}'".format(x))
        dt=files.fetchall()
        df=pd.DataFrame(dt,columns=["Cheq No.","Date"])
        df.set_index('Cheq No.',inplace=True)
        if c in df.index :
            design(60,2)
            center(colour('☛ Cheque already Blocked',1))
            center(colour('❖ Changes unmade Yet ❖',4))
            design(60,2)   
        else:
            return True
        
    def chcid(x):
        if x!='' and x!=' ':
            op=x[::-1]
            p=1
            if op[0]=='v':
                df1=staffdetails()
                if x in df1.index:
                    return True,'staff'
                else:
                    design(60,1)
                    center(colour('✋【Unauthenticated】 Id has given ✋\n',1))
                    design(60,1)
                    return False,'staff'
            elif x[0]=='d':
                df1=usdetails('staff','a')
                if x in df1.index:
                    return True,'cus'
                else:
                    design(60,1)
                    center(colour('✋【Unauthenticated】 Id has given ✋\n',1))
                    design(60,1)
                    return False,'cus'
            else:
                design(60,1)
                center(colour('✋【Unauthenticated】 Id has given ✋\n',1))
                design(60,1)
                return False,'cus'
        else:
            design(60,1)
            center(colour('✋【Unauthenticated】 Id has given ✋\n',1))
            design(60,1)
            return False,'staff'
 
    def staffdetails():
        files.execute('select * from staff')
        d=files.fetchall()
        df1=pd.DataFrame(d,columns=['id','name','key','post'])
        df1.set_index('id',inplace=True)
        return df1
    
    def login(x,y,z):
        if y == 'staff':
            df=staffdetails()
            if decrypt(df.at[x,'key']) == z:     
                return True
            else:
                design(60,2)
                datarep('Paswrd is【Wrong】as ID',x)
                design(60,2)
                
        else:
            df=usdetails('login',x)
            if decrypt(df.at[x,'key']) == z:
                return True
            else:
                design(60,2)
                datarep('Paswrd is【Wrong】as ID',x)
                design(60,2)
                
            
    def chcauth(x,y):
        df1=staffdetails()
        if y=='addcus' or y=='updcus':
            if df1.at[x,'post'] == 'manager' or df1.at[x,'post'] == 'teller':
                return True
            else:
                pyg.alert('☛ Authorisation Error\n● You Are not Authorised for this Task','Dev CRM - '+str(x))
                print('Your are NOT AUTHORISED for this fuction.')
        elif y=='updcash':
            if df1.at[x,'post'] == 'manager' or df1.at[x,'post'] == 'cashier':
                return True
            else:
                pyg.alert('☛ Authorisation Error\n● You Are not Authorised for Updating Balances of Customers.','Dev CRM - '+str(x))
                print('☛ Your are NOT AUTHORISED for updating Cash Balances.')
                
    def acty(x,y):
        if y == 0:
            df=usdetails('staff',x)
            return df.at[x,'A/C Type']
        else:
            df=usdetails('staff',x)
            ty=df.at[x,'A/C Type']
            if ty=='saving':
                files.execute("update devcus set ac_type='{}' where cusid='{}'".format('current',x))
                mycon.commit()
            else:
                files.execute("update devcus set ac_type='{}' where cusid='{}'".format('saving',x))
                mycon.commit()
 
    def phnchg(x):
        df=usdetails('staff',x)
        p=df.at[c,'Phone']
        design(60,2)
        datarep('At Present',p)
        design(60,2)
        d=input('➤ Want to Change Number of Customer 【y/n】 │ ')
        if d=='y' or d=='Y':
            phn=input('☛ New Phone Number \t │')
            if valn(phn)  and valcon(phn,10)  and nonzero(phn) :
                phn=int(phn)
                files.execute("update devcus set phone='{}' where cusid='{}'".format(phn,x))
                mycon.commit()
                return True
        else:
            design(60,2)
            center(colour('❖ Changes unmade Yet ❖',4))
            design(60,2)
 
    def cusbal(x):
        df=usdetails('staff',x) 
        return df.at[x,'Balance']
    
    def blchq(x,c):
        if c == 'b':
            d=input('➤ Want to Block Any Transaction Continue 【y/n】 │ ')
            if d == 'y' or d=='Y':
                design(60,2)
                d=input('\n➤ Enter Cheque Number │ ')
                if valn(d)  and nonzero(d) :
                    if cheqnum(x,d) :
                        if blcdup(x,d) :
                            files.execute("insert into blocktrans(cusid,cheqnum) values(%s,%s)",(x,d))
                            mycon.commit()
                            design(60,2)
                            t='Blocking Successfully for \n' + 'Cheque No. '+str(d)
                            pyg.alert(t,'Dev CRM - '+str(x))
                            center(colour('Changes made Successfully',2))
                            design(60,2)
                else:
                    design(60,2)
                    center(colour('❖ Changes unmade Yet ❖',4))
                    design(60,2)
        else:
            if c=='h':
                files.execute("select * from blocktrans where cusid='{}'".format(x))
            else:
                files.execute("select * from blocktrans where cusid = '{}' and cheqnum = '{}'".format(x,c))
            d=files.fetchall()
            df1=pd.DataFrame(d,columns=['ID','Cheq No.','Entered Date'])
            df1.set_index('Cheq No.',inplace=True)
            return df1
            
    def pswpwr(x):
        if len(x)>=6:
            if x.isalpha():
                design(60,2)
                center(colour("✤ Password Status : 【Too Weak】✤",1))
                design(60,2)
            elif x=="" or x==" ":
                design(60,2)
                center(colour("✤ Password Status : 【Null】 ✤",1))
                design(60,2)
            else:
                return True
        else:
            design(60,2)
            center(colour("✤ Password must >= 6 digit ✤ ",1))
            design(60,2)
    
    def pswmatch(x,y):
        if x==y:
            return True
        else:
            design(60,2)
            center(colour('✤ Password Not Match ✤',1))
            design(60,2)
            
    def changepsw(x,y,z,forget):
        design(60,2)
        ph=''
        x=decrypt(x)
        if forget==False:
            ph=getpass('\n➤ Current Password/PIN │ \t ')
            design(60,2)
        if ph == x:
            if z==1 or z==0:
                design(60,2)
                print('Password must have 6 digits including at least ')
                datarep('1','Number')
                datarep('1','capital char')
                design(60,2)
                design(60,2)
                ph=getpass('\n➤ New Password │ \t ')
                if pswpwr(ph) :
                    ph2=getpass('➤ Confirm Password │ \t ')
                    design(60,2)
                    if pswmatch(ph,ph2) :
                        if z == 1:  #if Z==1 it means Staff Password Conversion else of Customer
                            files.execute("update staff set pasw ='{}' where id='{}'".format(encrypt(ph),y))
                            mycon.commit()
                            pyg.alert('❖ Password Sets Successfully ❖','Dev Staff - '+str(y))
                            design(60,2)
                            center(colour('❖ Password Sets Successfully ❖',2))
                            design(60,2)
                        elif z == 0:
                            files.execute("update devcus set passw ='{}' where cusid='{}'".format(encrypt(ph),y))
                            mycon.commit()
                            pyg.alert('❖ Password Sets Successfully ❖','Dev CRM - '+str(y))
                            design(60,2)
                            center(colour('❖ Password Sets Successfully ❖',2))
                            design(60,2)
            else:
                design(60,2)
                center(colour('★ PIN must have 4 digits ★',1))
                design(60,2)
                ph=getpass('\n➤ New PIN │ \t ')
                if valn(ph) :
                    if valcon(ph,4) :
                        ph2=getpass('➤ Confirm PIN │ \t ')
                        design(60,2)
                        if pswmatch(ph,ph2) :
                            files.execute("update atm set pin ='{}' where cusid='{}'".format(encrypt(ph),y))
                            mycon.commit()
                            pyg.alert('❖ Pin Change Successfully ❖','Dev CRM - '+str(y))
                            design(60,2)
                            center(colour('❖ Pin Change Successfully ❖',2))
                            design(60,2)
        else:
            design(60,2)
            center(colour('❖ Pssword/PIN is unmatched ❖ ',1))
            design(60,2)
                            
    def chcbal(x,y):
        if y == 'saving':
            if x >= 2000 and x < 1000000:
                return True
            else:
                center(colour('Saving A/C Initial Bal.',4))
                datarep('★ I.Bal >= 2000 ','I.Bal < 10 Lakh ★')
                
        elif y =='current':
            if x >= 10000 and x < 10000000:
                return True
            else:
                center(colour('Current A/C Initial Bal.',4))
                datarep('★ I.Bal >= 10000 ','I.Bal < 1 Crore ★')
                
    def amtmang(i,b,v,a,p,c):
        files.execute("update devcus set balance ='{}' where cusid='{}'".format(b,i))
        mycon.commit()
        if p=='Add':
            files.execute("insert into acstatement(cusid,description,chqnum,Deposit,operation,trandate,trantime,balance) values(%s,%s,%s,%s,%s,%s,%s,%s)"                                  ,(i,v,c,a,p,dt()[0],dt()[1],str(b)))
        else:
            files.execute("insert into acstatement(cusid,description,chqnum,Withdrawn,operation,trandate,trantime,balance) values(%s,%s,%s,%s,%s,%s,%s,%s)"                                  ,(i,v,c,a,p,dt()[0],dt()[1],str(b)))
        mycon.commit()
        if v != 'Def.Chg. 5%' and v!='Service Chg. 0.5%':
            if '+Trf By' not in v :
                chcdef(i,b,a)
                pyg.alert('❖ Transaction Successful ❖ \n\n Now Balance\t: {}'.format(cusbal(i)),'Dev CRM - '+str(i))
                design(60,2)
                center(colour('❖ Transaction Successful ❖',2))
                datarep('Now Balance ➤',cusbal(i))
                design(60,2)
 
    def dt():
        a=date.today()
        b=datetime.now()
        b=b.strftime("%H:%M:%S")
        return a,b
 
    def minmax(x,y):
        df=usdetails('staff',x)
        a=df.at[x,'A/C Type']
        design(60,2)
        if a == 'saving':
            if y >= 100 and y < 1000000:
                return True
            else:
                center(colour('❖ For Saving A/C ❖',4))
                datarep('• Min Deposit',' >=100')
                datarep('• Max Deposit',' < 10 Lakhs')
        else:
            if y >= 200 and y < 10000000:
                return True
            else:
                center(colour('❖ For Current A/C ❖',4))
                datarep('• Min Deposit',' >=200')
                datarep('• Max Deposit',' < 1 Crore')
        design(60,2)
                
    def addmoney(x):
        ty=acty(x,0)
        p=cusbal(x)
        design(60,2)
        df=usdetails('staff',x)
        design(60,2)
        datarep('Present Balance ➤',p)
        datarep('Account Number  ➤',str(df.at[x,'A/C_Num']))
        datarep('A/C Type of Cus ➤',ty)
        design(60,2)
        c=input('\n➤ Want to add Money ? 【y/n】 │ ')
        if c == 'Y' or c=='y':
            a=input('➤ Amount to be Added \t │ ')
            if valn(a)  and nonzero(a) :
                a=int(a)
                if minmax(x,a):
                    design(60,2)
                    datarep('Amount in Words │ ',alpha((a)))
                    design(60,2)
                    center(colour('Deposit in Refrence',4))
                    design(60,2)
                    datarep('Press 1 ➤','Cash')
                    datarep('Press 2 ➤','Cheque')
                    datarep('Press 3 ➤','Others')
                    datarep('Any Num','Back')
                    design(60,2)
                    cn=input('\n● Condition Chosen │ \t  ')
                    design(60,2)
                    if valn(cn) :
                        cn=int(cn)
                        if cn > 3 or cn <= 0:
                            center(colour('❖ Back to Main Menu ❖',4))
                        else:
                            if cn == 1:
                                t='Cash Deposit'
                                b=p+a
                                amtmang(x,b,t,str(a),'Add','0')
                            elif cn == 2:
                                design(60,2)
                                c=input('\n➤ Cheque No. \t│ ')
                                y=input('➤ Bank Name. in short form e.g. SBI \t│ ')
                                design(60,2)
                                if valn(c)  and nonzero(c) :
                                    y=y.upper()
                                    if vals(y.replace(' ','')) :
                                        t=y+' Cheq No.' + c
                                        b=p+a
                                        amtmang(x,b,t,str(a),'Add',c)
                            elif cn == 3:
                                design(60,2)
                                c=input("\nRef. (No Special Character)\t │ ")
                                if vals(c.replace(' ','')) :
                                    design(60,2)
                                    b=p+a
                                    amtmang(x,b,c.upper(),str(a),'Add','0')
                            else:
                                center(colour('❖ Back to Main Menu ❖',4))
                                design(60,2)
        else:
            design(60,2)
            center(colour('❖ Back to Main Menu ❖',4))
            design(60,2)
#        This is For Charging Interest >> below:     
    def cg(x,a):
        p=cusbal(x)
        cg=a//100*0.5
        design(60,2)
        datarep('Service Chg.(0.5%) Deducted ➤',cg)
        design(60,2)
        p=p-cg
        amtmang(x,p,'Service Chg. 0.5%',str(cg),'Less','0')
        
    def validation(x):
        center(colour('❖ Validation Started ❖',5))
        a=input('● Enter Your Dev A/C Number │ ')
        if valn(a) :
            df=usdetails('staff',x)
            if df.at[x,'A/C_Num'] == int(a):
                b=input('● Enter Your Regd. Mob. No. │ ')
                if valn(b) :
                    if df.at[x,'Phone'] == int(b):
                        u=input('● Enter Your Aadhar Card No. │ ')
                        if valn(b)  and df.at[x,"UAID (Aadhar No.)"] ==int(u):
                            design(60,2)
                            center(colour('❖ As Per Given Details ❖',2))
                            datarep('Name    ➤',df.at[x,'Name'])
                            datarep('CutID   ➤',x)
                            datarep('A/C NO. ➤',a)
                            datarep('Mob. No.➤',b)
                            design(60,2)
                            return True
                        else:
                            design(60,2)
                            center(colour('❌❌ Validation Failed ❌❌',1))
                            design(60,2)
                            return False
                    else:
                        design(60,2)
                        center(colour('❌❌ Validation Failed ❌❌',1))
                        design(60,2)
                        return False
            else:
                design(60,2)
                center(colour('❌❌ Validation Failed ❌❌',1))
                design(60,2)
                return False
                
    def defchg(x,a):
        p=cusbal(x)
        cg=a//100*5
        design(60,2)
        print('\n\t Minimum Bal. Defaulting Charges ➤',cg)
        design(60,2)
        p=p-cg
        amtmang(x,p,'Def.Chg. 5%',str(cg),'Less','0')
        
    def chcdef(x,b,a):
        a=int(a)
        t=acty(x,0)
        if t =='saving' and b<2000 or t =='current' and b<10000:
            design(60,2)
            center(colour('◆ As A/C Balance < Minimum Balance',1))
            center(colour('◆ Rate of Int. will charge @ 5%',1))
            design(60,2)
            defchg(x,a)
            
    def suspension(x):
        ty=acty(x,0)
        if ty == 'saving':
            if cusbal(x) < 100 :
                return True
            else:
                return False
 
        else:
            if cusbal(x) < 1000:
                return True
            else:
                return False
 
    def lessmoney(x):
        p=cusbal(x)
        ty=acty(x,0)
        df=usdetails('staff',x)
        design(60,2)
        datarep('Present Balance ➤',p)
        datarep('Account Number  ➤',str(df.at[x,'A/C_Num']))
        datarep('A/C Type of Cus ➤',ty)
        design(60,2)
        c=input('\n➤ Want to Deduct Amount ? 【y/n】 │ ')
        if c == 'Y' or c=='y':
            a=input('Amount to be Deducted \t│ ')
            if valn(a)  and nonzero(a) :
                design(60,2)
                datarep('Amount in Words │ ',alpha(a))
                design(60,2)
                a=int(a)
                if a >=100:
                    if a < p:
                        center(colour('Deducted in Refrence',4))
                        design(60,2)
                        datarep('Press 1 ➤','Withdrwn Cash')
                        datarep('Press 2 ➤','Self_Cheq/DD')
                        datarep('Press 3 ➤','Transfer')
                        datarep('Press 4 ➤','NEFT/RTGS')
                        datarep('Press 5 ➤','Others')
                        datarep('Any Num','Back')
                        design(60,2)
                        cn=input('\n● Condition Chosen │ \t  ')
                        design(60,2)
                        if valn(cn) :
                            cn=int(cn)
                            if cn > 5 or cn <= 0:
                                center(colour('❖ Back to Main Menu ❖',4))
                            else:
                                if cn == 1:
                                    t='Cash Wihdrawn'
                                    b=p-a
                                    amtmang(x,b,t,str(a),'Less','0')
                                else:
                                    if cn == 2:
                                        design(60,2)
                                        c=input('\n● Cheque No. \t│ ')
                                        design(60,2)
                                        if valn(c)  and nonzero(c) :
                                            if cheqnum(x,c) :
                                                df=blchq(x,'h')
                                                if c in df.index:
                                                    design(60,2)
                                                    t='Cheque No. 【'+c+'】 is TERMINATED/BLOCK \n'+                                                    'As per Account Holder Wish \n'+ '❖ Changes Unmade Yet ❖'
                                                    pyg.alert(t,'Dev CRM')
                                                    center(colour('✋ This Cheque is Termminated ✋',1))
                                                    center(colour('● As per Account Holder',6))
                                                    center(colour('❖ Changes Unmade ❖',4))
                                                    design(60,2)
                                                else:
                                                    if ty=='saving':
                                                        t='Cheq. '+ c
                                                        b=p-a
                                                        amtmang(x,b,t,str(a),'Less',c)
                                                        cg(x,a)
                                                    else:
                                                        t='Cheq. '+ c
                                                        b=p-a
                                                        amtmang(x,b,t,str(a),'Less',c)
                                    elif cn==3:
                                        design(60,2)
                                        c=input('\n● Cheque No. \t│ ')
                                        design(60,2)
                                        if valn(c)  and nonzero(c) :
                                            if cheqnum(x,c) :
                                                transfund(x,'s',str(a),c)
                                    elif cn == 4:
                                        design(60,2)
                                        c=input('\n● Cheque No. \t│ ')
                                        design(60,2)
                                        if valn(c)  and nonzero(c) :
                                            if cheqnum(x,c) :
                                                c2=input('● Ref to. (No Special Character) \t│ ')
                                                if int(c) > 0 and vals(c2.replace(' ',''))  and c2 !='' or c2 !=' ':
                                                    if ty=='saving':
                                                        t='NEFT/RTGS ' + c2
                                                        b=p-a
                                                        amtmang(x,b,t,str(a),'Less',c)
                                                        cg(x,a)
                                                    else:
                                                        t='NEFT/RTGS ' + c2
                                                        b=p-a
                                                        amtmang(x,b,t,str(a),'Less',c)
                                                else:
                                                    design(60,2)
                                                    center(colour('❖ Invalid Data has Given ❖',1))
                                                    design(60,2)
 
                                    else:
                                        design(60,2)
                                        c=input('\n● Ref to \t│ ')
                                        design(60,2)
                                        if valn(c) is False:
                                            c=c.upper()
                                            if ty=='saving':
                                                b=p-a
                                                amtmang(x,b,c,str(a),'Less','0')
                                                cg(x,a)
                                            else:
                                                b=p-a
                                                amtmang(x,b,c,str(a),'Less','0')
                    else:
                        design(60,2)
                        datarep('● Maximum Drawing < ',p)
                        design(60,2)
                else:
                    design(60,2)
                    center(colour('● Minimum Drawing ➤ 100 ',1))
                    design(60,2)
        else:
            design(60,2)
            center(colour('❖ Back to Main Menu ❖',4))
            design(60,2)
            
    def chcacnum(a):
        files.execute("select cusid,acnum,ac_type,name,balance from devcus where acnum = '{}'".format(a))
        dt=files.fetchall()
        if dt == []:
            return False
        else:
            df=pd.DataFrame(dt,columns=["Cusid","A/C Num","A/C Type","Name","Balance"])
            df.set_index('A/C Num',inplace=True)
            return df
            
    def transfund(x,y,a,i):
        p=cusbal(x)
        ty=acty(x,0)
        dfx=usdetails('staff',x)
        if valn(a)  and nonzero(a) :
            a=int(a)
            if a >=100:
                if a < p:
                    design(60,2)
                    if i=='0' and y!='s':
                        b=input('\n● Enter Beneficiary Account Number │ ')
                    elif i!='0' or y=='s':
                        print('● Enter Beneficiary Account Number : ',end='')
                        b='3058'+input('3058')
                    design(60,2)
                    if valn(b)  and nonzero(b) :
                        if y == 's':
                            if chcacnum(b) is not False:
                                design(60,2)
                                df=chcacnum(b)
                                if df.at[int(b),'Cusid'] != x:
                                    datarep('Name',df.at[int(b),'Name'])
                                    datarep('A/C Type',df.at[int(b),'A/C Type'])
                                    design(60,2)
                                    c=input('\n➤ Want to Benefit Amount ? 【y/n】 │ ')
                                    if c == 'Y' or c=='y':
                                        c='-Trf To '+ df.at[int(b),'Name'] + ' ' + b
                                        t=datetime.now()
                                        y=p-a
                                        if i=='0':
                                            receipt(int(b),df.at[int(b),'Name'],a,t.strftime("%H:%M:%S"),d.strftime("%A, %B %d"),'Dev Bank')
                                            amtmang(x,y,c,a,'Less','0')
                                        else:
                                            amtmang(x,y,c,a,'Less',i)
                                        c='+Trf By '+ dfx.at[x,'Name'] + ' ' + str(dfx.at[x,'A/C_Num']) 
                                        y=df.at[int(b),'Balance']
                                        y=y+a
                                        if i=='0':
                                            amtmang(df.at[int(b),'Cusid'],y,c,a,'Add','0')
                                        else:
                                            amtmang(df.at[int(b),'Cusid'],y,c,a,'Add',i)
                                        design(60,2) 
                                        center(colour('❖ Amount Transfer Successfully ❖',2))
                                        datarep(b+' Credited',a)
                                        design(60,2)
                                        if i=='0':
                                            t='❖ Amt. Transfer Successfully ❖' + '\n'+ b +' Credited' + str(a)
                                            pyg.alert(t,'Dev CRM -'+ str(x))
                                        if ty=='saving':
                                            cg(x,a)
                                    else:
                                        design(60,2)
                                        center(colour('❖ Transaction Terminated ❖',1))
                                        design(60,2)
                                else:
                                    design(60,2)
                                    center(colour("❖ You Can't Benefit Your Own A/C ❖",1))
                                    design(60,2)
                            else:
                                design(60,2)
                                center(colour('❖ No Such Dev Account Found ❖',1))
                                design(60,2)
                        else:
                            if chcacnum(b) is False:
                                if len(b) >= 9 and len(b) <= 18:
                                    df=chcacnum(b)
                                    if b!= dfx.at[x,'A/C_Num']:
                                        design(60,2)
                                        c=input('\n➤ Want to Benefit Amount ? 【y/n】 │ ')
                                        design(60,2)
                                        if c == 'Y' or c=='y':
                                            c='-To '+ b
                                            y=p-a
                                            t=datetime.now()
                                            receipt(int(b),'Unknown',a,t.strftime("%H:%M:%S"),d.strftime("%A, %B %d"),'UnKnown')
                                            amtmang(x,y,c,a,'Less','0')
                                            design(60,2)
                                            center(colour('❖ Amount Transfer Successfully ❖',2))
                                            datarep(b+' Credited',a)
                                            design(60,2)
                                            t='❖ Amt. Transfer Successfully ❖' + '\n'+ b+' Credited' + str(a)
                                            pyg.alert(t,'Dev CRM - '+str(x))
                                            if ty=='saving':
                                                cg(x,a)
                                else:
                                    design(60,2)
                                    center(colour('❖ Invalid A/C Number has given ❖',1))
                                    design(60,2)
                            else:
                                design(60,2)
                                center(colour('✋ Given A/C No. is of Dev Bank ✋',1))
                                center(colour('● Kindly Choose 1. Option - ',2))
                                center(colour("★ 'Benefit same Bank' ★",4))
                                design(60,2)
 
                else:
                    design(60,2)
                    center(colour('❖ Balance Defeciency Occurs ❖',1))
                    design(60,2)
 
            else:
                design(60,2)
                center(colour('❖ Minimum Fund tranfer > = 100 ❖',1))
                design(60,2)
 
    def save(x,t):
        design(60,2)
        b=input('\n● Enter the Name of the Document │ \t ')
        design(60,2)
        if t == 'ac':
            d=boot_data(3)+'Dev Bank\ACC Statement'
            p=os.path.join(d,b+'.csv')
        else:
            d=boot_data(3)+"Dev Bank\Others"
            p=os.path.join(d,b+'.csv')
        if os.path.exists(p):
            design(60,2)
            center(colour('❖ File Name Already Exists ❖',1))
            design(60,2)
            design(60,2)
            a=input('\n➤ Want to Replace or Overwrite ? 【y/n】 │ ')
            design(60,2)
            if vals(a)  :
                if a=='y' or a=='Y':
                    x.to_csv(p)
                    design(60,2)
                    center(colour('❖ Document Save Successfully ❖',2))
                    datarep('Document Name ➤',b+'.csv')
                    datarep('Path : ',p)
                    p=os.path.join(boot_data(3)+'Dev%20Bank/ACC%20Statement',b+'.csv')
                    webbrowser.open('file:///'+p)
                    design(60,2)
                else:
                    design(60,2)
                    center(colour('✌ Try Again with Different Name ✌',4))
                    design(60,2)
        else:
            x.to_csv(p)
            design(60,2)
            center(colour('❖ Document Save Successfully ❖',1))
            datarep('Document Name ➤',b+'.csv')
            datarep('Path : ',p)
            p=os.path.join(boot_data(3)+'Dev%20Bank/ACC%20Statement',b+'.csv')
            webbrowser.open('file:///'+p)
            design(60,2)
    
    def receipt(x,y,z,a,d,b):
        t='Dev Bank CRM \n Kapurthala Road Jalandhar \n Transfer Memo as per Tansac.\n\n Benef. Bank : ' + b +        '\n Benef. A/C  : ' + str(x) + '\n Benef. Name : ' + y + '\n Amount(fig) : ' + str(z) +         '\n Amount(wrd) : ' + alpha(str(z)) + '\n Trnsc. Time : ' + str(a) + '\n Trnsc. Date : ' + str(d) +        '\n Thanks for Operation'
        
        pyg.alert(t,'Dev Bank CRM - '+ str(x))
        time.sleep(0.5)
        
    def hasE(cusid):
        df=usdetails('now',cusid)
        if df.at[cusid,'Status']==1:
            return True
        else:
            return False
        
    def calculateAge(birthDate):
        today = date.today() 
        age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
        return age
    def addcus():
        design(60,2)
        datarep('Press S ➤','Saving A/C')
        datarep('Press C ➤','Current A/C')
        design(60,2)
        design(60,2)
        cond=input('\nA/C Type \t│ ')
        design(60,2)
        center(colour('★ Be Sure Any Error ★',4))
        center(colour('➤ will make System ➤',4))
        center(colour('All entered data erase',4))
        design(60,2)
        if cond == 'S' or cond=='s':
            s=1
            typ='saving'
        elif cond == 'C' or cond=='c':
            s=2
            typ='current'
        else:
            design(60,2)
            center(colour('❌ Wrong Condition Chosen ❌',1))
            design(60,2)
            s=3
            return s
        if s!=3:
            while True:
                design(60,2)
                nam=input('\n● Enter Full Name of the person│ ')
                if vals(nam.replace(' ','')) :
                    nam=nam.capitalize()
                    dob=input('● D.O.B YYYY-MM-DD (Age >=18 and < 80) │ ')
                    if is_date(dob) :
                        dob2=dob.replace('-',',')
                        dob2=datetime.strptime(dob2,'%Y,%m,%d').date()
                        age=calculateAge(dob2)
                        if age >= 80 or age < 18:
                            center(colour('★ Age > 80 and < 18 is not allowed ★',1))
                        else:
                            uaid=input('● UAID (Aadhar Card No.) │ ')
                            if unique('UAID (Aadhar No.)',int(uaid)):
                                if valcon(uaid,12)  and valn and nonzero(uaid) :
                                    gen=input("● Gender M/F : ")
                                    if gen == 'm' or gen=='M' or gen == 'F' or gen == 'f':
                                        gen=gen.upper()
                                        phn=input("● Contact No. : ")
                                        if valn(phn)  and valcon(phn,10)  and nonzero(phn) :
                                            phn=int(phn)
                                            design(60,2)
                                            if cond == 'S' or cond == 's':
                                                center(colour('Minimum Saving A/C Bal.',4))
                                                datarep(' >= 2000 ',' <=1 Lakh')
                                            else:
                                                center(colour('Minimum Current A/C Bal.',4))
                                                datarep(' >= 10000 ',' <=10 Lakh')
                                            design(60,2)
                                            bal=input('● Enter the initial Amount│ ')
                                            if valn(bal)  and nonzero(bal) :
                                                bal=int(bal)
                                                if chcbal(bal,typ) :
                                                    design(60,2)
                                                    datarep('Amount in Words │ ',alpha(str(bal)))
                                                    design(60,2)
                                                    acnum=''
                                                    devid='dev'
                                                    digits = "987456154542525874"
                                                    for i in range(4):
                                                        acnum+=digits[math.floor(random.random() * 10)]
                                                    for i in range(4) :
                                                        devid += digits[math.floor(random.random() * 10)]
                                                    acnum=int('3058'+acnum)
                                                    files.execute("insert into devcus(cusid,acnum,ac_type,name,age,gender,phone,balance,crdate,crtime,uaid,dob) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"                                                                  ,(devid,acnum,typ,nam,age,gen,phn,bal,dt()[0],dt()[1],int(uaid),dob))
                                                    mycon.commit()
                                                    files.execute("insert into acstatement(cusid,description,Deposit,trandate,trantime,balance,operation) values(%s,%s,%s,%s,%s,%s,%s)"                                                                  ,(devid,'Initial Amount',str(bal),dt()[0],dt()[1],str(bal),'Add'))
                                                    mycon.commit()
                                                    t='Customer Created Successfully ! \n\n '+                                                    'Account Type : '+typ+'\n\n'+                                                    'Cust. Credentials :- '+'\n'+                                                    'Customer Id : '+devid+'\n'+                                                    'A/C Number  : '+str(acnum)+'\n\n'+                                                    'Cust. General Info :- '+'\n'+                                                    'Name : '+nam+'\n'+                                                    'UAID :'+str(uaid)+'\n'+                                                    'D.O.B :'+str(dob)+'\n'+                                                    'Age  : '+str(age)+'\n'+                                                    'Gend : '+gen+'\n'+                                                    'Mob. : '+str(phn)+'\n'+                                                    'Balance : '+str(bal) +' : '+ alpha(str(bal))+'\n'
                                                    pyg.alert(t,'Dev Bank CRM')
                                                    acstatus=True
                                                    return acstatus,devid
                                                    break
                                    else:
                                        design(60,2)
                                        center(colour("★ Gender Either M/F or m/f ★",1))
                                        design(60,2)
                            else:
                                design(60,2)
                                center(colour("★ Duplicacy of UAID Occurs ★",1))
                                design(60,2)
                                
                    else:
                        design(60,2)
                        center(colour("★ Wrong D.O.B has Given ★",1))
                        design(60,2)
                else:
                    design(60,2)
                    center(colour("★ Changes Unmade Yet ★",1))
                    design(60,2)
                    return False,'not'
                    break
    design(60,2)
    center(colour('♕ Welcome to Dev Bank',4)),center(colour('The Bank of Technical Era',2))
    design(60,2)
    d=date.today()
    t=datetime.now()
    print("\nDATE:-",d.strftime("%A, %B %d"),"\t   TIME:-",t.strftime("%H:%M:%S"))
    design(60,2)
    a=os.path.getmtime('Dev Bank.ipynb')
    datarep('Last Visit ',time.ctime(a))
    design(60,2)
    while True:
        if start3 :
            datarep('Press 1 ➤','Login/Apply E-Banking')
            datarep('Press 0 ➤','System Exit')
            datarep('Any Num ➤','Read T&C')
            design(60,2)
            center(colour('★ You have Agreed ours T&C ★',2))
            design(60,2)
            time.sleep(0.1)
            design(60,2)
            st=input("\n● Condition Chosen  : ")
            if valn(st) :
                if int(st) == 1:
                    design(60,2)
                    x=input("\n\t♕ User Id\t➤\t\t")
                    response=chcid(x)
                    if response[0] :
                        if response[1] == 'staff':
                            pasw=getpass('\t♕ Key\t\t➤\t\t')
                            design(60,2)
                            response2=login(x,response[1],pasw)
                            if response2 :
                                while True:
                                    design(60,2)
                                    df=staffdetails()
                                    print('\n\t\t♕ Welcome',df.at[x,'name'],'【{}】'.format(df.at[x,'post']))
                                    design(60,2)
                                    datarep('Press 1 ➤','Add New Customer')
                                    datarep('Press 2 ➤','Change Password')
                                    datarep('Press 3 ➤','View Cust. Details')
                                    datarep('Press 4 ➤','Update Cust.Details')
                                    datarep('Press 5 ➤','Update Balances')
                                    datarep('Press 6 ➤','See Apllications')
                                    datarep('Press 7 ➤','A/C Statements')
                                    datarep('Any Num ➤','Exit')
                                    design(60,2)
                                    cn2=input("\n● Condition Chosen │ \t")
                                    if valn(cn2) :
                                        cn2=int(cn2)
                                        design(60,2)
                                        if cn2 == 1:
                                            if chcauth(x,'addcus') :
                                                response2=addcus()
                                                if response2 !=3:
                                                    if response2[0] :
                                                        design(60,2)
                                                        center(colour('❖ Account Crtd. Successfully ❖',2))
                                                        design(60,2)
                                                        time.sleep(0.1)
                                                        response=usdetails('staff',response2[1])
                                                        print(response)
                                        elif cn2 == 2:
                                            df1=staffdetails()
                                            p=df1.at[x,'key']
                                            changepsw(p,x,1,False)
                                        elif cn2 == 3:
                                            design(60,2)
                                            datarep("Type 'devs' ➤",'For all')
                                            print('● Enter Customer ID │ ',end='')
                                            c='dev'+input('dev')
                                            if c=='devs':
                                                design(60,2)
                                                response=usdetails('staff','a')
                                                design(60,2)
                                                center(colour('✤ Accounts Details ✤',5))
                                                design(60,2)
                                                design(60,2)
                                                print(response)
                                                time.sleep(0.1)
                                                cn=input('\n➤ Want to Save this Data 【y/n】 │ ')
                                                if cn == 'Y' or cn=='y':
                                                    save(response,'ad')
                                                    design(60,2)
                                                else:
                                                    design(60,2)
                                                    center(colour('✤ Proposal Rejected ✤',6))
                                                    design(60,2)
                                            else:
                                                response=chcid(c)
                                                if response[0]  and response[1] == 'cus':
                                                    design(60,2)
                                                    response=usdetails('staff',c)
                                                    design(60,2)
                                                    center(colour('✤ Accounts Details ✤',5))
                                                    design(60,2)
                                                    design(60,2)
                                                    print(response)
                                                    time.sleep(0.1)
                                                    design(60,2)
                                        elif cn2 == 4:
                                            if chcauth(x,'updcus') :
                                                design(60,2)
                                                center(colour('✤ Things Can be Updated ✤',4))
                                                design(60,2)
                                                datarep('Press 1 ➤','A/C Type')
                                                datarep('Press 2 ➤','Phone')
                                                datarep('Any Num ➤','Back')
                                                design(60,2)
                                                cn=input('\n● Condition Chosen │ \t  ')
                                                if valn(cn) :
                                                    cn=int(cn)
                                                    if cn > 2 or cn <= 0:
                                                        center(colour('❖ Back to Main Menu ❖',4))
                                                    else:
                                                        print('● Enter Customer ID │ ',end='')
                                                        c='dev'+input('dev')
                                                        response=chcid(c)
                                                        if response[0]  and response[1] == 'cus':
                                                            if cn == 1:
                                                                response=acty(c,0)
                                                                bal=cusbal(c)
                                                                if response == 'saving' and bal>=10000:
                                                                    design(60,2)
                                                                    datarep('At Present ➤','Saving A/c')
                                                                    design(60,2)
                                                                    d=input('\n● Convert Saving A/C to Current A/C - 【y/n】 │ ')
                                                                    if d =='Y' or d=='y':
                                                                        acty(c,1)
                                                                        design(60,2)
                                                                        pyg.alert('Successfuly Converted to Current A/c','Dev Staff - '+ str(x))
                                                                        center(colour('❖ Successfuly Converted to Current A/c ❖',2))
                                                                        design(60,2)
                                                                        time.sleep(0.1)
                                                                    else:
                                                                        design(60,2)
                                                                        center(colour('❖ Changes unmade Yet ❖',4))
                                                                        design(60,2)
                                                                elif response == 'current' and bal>=2000:
                                                                    design(60,2)
                                                                    datarep('At Present ➤','Current A/c')
                                                                    design(60,2)
                                                                    d=input('\n● Convert Current A/C to Saving A/C - 【y/n】 │ ')
                                                                    if d =='Y' or d=='y':
                                                                        acty(c,1)
                                                                        design(60,2)
                                                                        pyg.alert('Successfuly Converted to Saving A/c','Dev Staff - '+ str(x))
                                                                        center(colour('❖ Successfuly Converted to Saving A/c ❖',2))
                                                                        design(60,2)
                                                                        time.sleep(0.1)
                                                                    else:
                                                                        design(60,2)
                                                                        center(colour('✌ Changes Yet Unmade ✌',4))
                                                                        design(60,2)
                                                                else:
                                                                    design(60,2)
                                                                    pyg.alert('Balance Insufficient for Conversion','Dev Staff - '+ str(x))
                                                                    center(colour('❖ Balance Insufficient for Conversion ❖',1))
                                                                    design(60,2)
                                                                    design(60,2)
                                                                    datarep('current ➤','Bal>=10000')
                                                                    datarep('Saving  ➤','Bal>=2000')
                                                                    design(60,2)
 
                                                            elif cn == 2:
                                                                if phnchg(c) :
                                                                    design(60,2)
                                                                    pyg.alert('Ph. No. Successfully Updated','Dev Staff - '+ str(x))
                                                                    center(colour('✌ Ph. No. Successfully Updated ✌',2))
                                                                    design(60,2)
                                                                    time.sleep(0.1)
 
                                                        else:
                                                            design(60,2)
                                                            center(colour('❌ Wrong Customer ID has Given ❌',1))
                                                            design(60,2)
                                                            time.sleep(0.1)
                                        elif cn2 == 5:
                                            if chcauth(x,'updcash') :
                                                design(60,2)
                                                center(colour('Things Can be Done',4))
                                                design(60,2)
                                                datarep('Press 1 ➤','Add Money')
                                                datarep('Press 2 ➤','Withdrw Money')
                                                datarep('Any Num ➤','Back')
                                                design(60,2)
                                                cn=input('\n● Condition Chosen │ \t  ')
                                                if valn(cn) :
                                                    cn=int(cn)
                                                    if cn > 2 or cn <= 0:
                                                        center(colour('❖ Back to Main Menu ❖',4))
                                                    else:
                                                        print('● Enter Customer ID │ ',end='')
                                                        c='dev'+input('dev')
                                                        response=chcid(c)
                                                        if response[0]  and response[1] == 'cus':
                                                            if cn == 1:
                                                                addmoney(c)
                                                                time.sleep(0.2)
                                                            else:
                                                                lessmoney(c)
                                                                time.sleep(0.2)
                                        elif cn2 == 6:
                                            if chcauth(x,'updcus') :
                                                design(60,2)
                                                center(colour('❖ E-Applications below ❖',5))
                                                design(60,2)
                                                df=appldetails()
                                                if df.empty:
                                                    design(60,2)
                                                    center(colour('✤ No Record Found ✤',4))
                                                    design(60,2)
                                                else:
                                                    design(60,2)
                                                    print(df)
                                                    design(60,2)
                                                    datarep('Press 1 ➤','Update Status')
                                                    datarep('Any Key ➤','Back')
                                                    design(60,2)
                                                    cn=input('\n● Condition Chosen │ \t  ')
                                                    if valn(cn) :
                                                        cn=int(cn)
                                                        if cn > 2 or cn <= 0:
                                                            center(colour('❖ Back to Main Menu ❖',4))
                                                        else:
                                                            print('\n● Enter Customer ID │ ',end='')
                                                            c='dev'+input('dev')
                                                            response=chcid(c)
                                                            if response[0]  and response[1] == 'cus':
                                                                updstatus(c,'Appl','Accepted')
                                                                if status(c,'Appl') is False:
                                                                    updstatus(c,'ATM','Active')
                                        elif cn2==7:
                                            print('● Enter Customer ID │ ',end='')
                                            c='dev'+input('dev')
                                            response=chcid(c)
                                            if response[0]  and response[1] == 'cus':
                                                acstatement(c,'s')
 
                                        else:
                                            leave(x)
                                            break
                        else:
                            if hasE(x) :
                                if suspension(x) is False:
                                    pasw=getpass('\t♕ Key\t\t➤\t\t')
                                    design(60,2)
                                    response2=login(x,response[1],pasw)
                                    if response2 :
                                        while True:
                                            design(60,2)
                                            df=usdetails('staff',x)
                                            print('\n\t\t♕ Welcome',df.at[x,'Name'],'【{}】'.format(x))
                                            design(60,2)
                                            datarep('Press 1 ➤','Your Details')
                                            datarep('Press 2 ➤','Change Password')
                                            datarep('Press 3 ➤','Online Support')
                                            datarep('Press 4 ➤','E-banking')
                                            datarep('Any Num ➤','Exit')
                                            design(60,2)
                                            if int(cusbal(x))>=2000 and acty(x,0) =='saving':
                                                if int(cusbal(x)) > 4000:
                                                    m=2
                                                else:
                                                    m=4
                                            elif int(cusbal(x))>=10000 and acty(x,0) == 'current':
                                                if int(cusbal(x)) > 20000:
                                                    m=2
                                                else:
                                                    m=4
                                            else:
                                                m=1
                                            center(colour('★ Present Balance【 {} 】★'.format(str(cusbal(x))),m))
                                            design(60,2)
                                            cn2=input("\n● Condition Chosen │ \t")
                                            design(60,2)
                                            if valn(cn2) :
                                                cn2=int(cn2)
                                                design(60,2)
                                                if cn2 > 4 or cn2 <= 0 :
                                                    leave(x)
                                                    break
                                                else:
                                                    if cn2 == 1:
                                                        df=usdetails('cus',x)
                                                        design(60,2)
                                                        center(colour('❖ Your Details are below ❖',5))
                                                        design(60,2)                             
                                                        print(df)
                                                        design(60,2)                             
                                                        design(60,2)
                                                        time.sleep(0.1)
                                                    elif cn2 == 2:
                                                        df1=usdetails('login',x)
                                                        p=df1.at[x,'key']
                                                        changepsw(decrypt(p),x,0,False)
                                                    elif cn2 == 3:
                                                        design(60,2)
                                                        center(colour('✤ Available Online Support ✤',4))
                                                        design(60,2)
                                                        datarep('Press 1 ➤','ATM Support')
                                                        datarep('Press 2 ➤','Request A/C Statement')
                                                        datarep('Any Num ➤','Back')
                                                        design(60,2)     
                                                        cn=input('\n● Condition Chosen │ ')
                                                        design(60,2)    
                                                        if valn(cn) :
                                                            cn=int(cn)
                                                            if cn>2 or cn<=0:
                                                                design(60,2)
                                                                center(colour('❖ Back to Main Menu ❖',4))
                                                                design(60,2)
                                                            else:
                                                                if cn == 1:
                                                                    df=hasatm()
                                                                    if x in df.index:
                                                                        while True:
                                                                            design(60,2)
                                                                            center(colour('✤ Available ATM Support ✤',4))
                                                                            design(60,2)
                                                                            datarep('Press 1 ➤','Change ATM PIN')
                                                                            datarep('Press 2 ➤','ON/OFF ATM Card')
                                                                            datarep('Any Num ➤','Back')
                                                                            design(60,2)     
                                                                            cn=input('● Condition Chosen │ ')
                                                                            design(60,2)    
                                                                            if valn(cn) :
                                                                                cn=int(cn)
                                                                                if cn > 2 or cn <= 0:
                                                                                    design(60,2)
                                                                                    center(colour('❖ Back to Main Menu ❖',4))
                                                                                    design(60,2)
                                                                                    break
                                                                                else:
                                                                                    if cn == 1:
                                                                                        df1=atmdetails()
                                                                                        p=df1.at[x,'Pin']
                                                                                        changepsw(p,x,2,False)
                                                                                        time.sleep(0.1)
                                                                                    else:
                                                                                        if status(x,'Appl.') :
                                                                                            if status(x,'ATM') :
                                                                                                design(60,2)
                                                                                                datarep('ATM Status ➤', 'Active/ON')
                                                                                                datarep('Press 1 ➤','Make Unactive/OFF')
                                                                                                datarep('Any Key ➤','BacK')
                                                                                                design(60,2)
                                                                                                cn=input('\n● Condition Chosen │\t ')
                                                                                                if valn(cn)  :
                                                                                                    cn=int(cn)
                                                                                                    if cn > 1 or cn <=0:
                                                                                                        center(colour('✤ Back to Menu ✤',4))
                                                                                                    else:
                                                                                                        updstatus(x,'ATM','Unactive')
                                                                                                        time.sleep(0.1)
                                                                                            else:
                                                                                                design(60,2)
                                                                                                datarep('ATM Status ➤', 'Unactive/OFF')
                                                                                                datarep('Press 1 ➤','Make Active/ON')
                                                                                                datarep('Any Key ➤','BacK')
                                                                                                design(60,2)
                                                                                                cn=input('\n● Condition Chosen │\t ')
                                                                                                if valn(cn)  :
                                                                                                    cn=int(cn)
                                                                                                    if cn > 1 or cn <=0:
                                                                                                        design(60,2)
                                                                                                        center(colour('✤ Back to Menu ✤',4))
                                                                                                        design(60,2)
                                                                                                    else:
                                                                                                        updstatus(x,'ATM','Active')
                                                                                                        time.sleep(0.1)
                                                                                        else:
                                                                                            design(60,2)
                                                                                            center(colour('Your ATM is Temporarily OFF',1))
                                                                                            center(colour('as application Unccepted Yet',2))
                                                                                            center(colour('Wait till it get Accepted',2))
                                                                                            design(60,2)
                                                                                            time.sleep(0.2)
 
                                                                    else:
                                                                        design(60,2)
                                                                        center(colour("✤ You don't have ATM yet ✤",4))
                                                                        design(60,2)
                                                                        time.sleep(0.1)
                                                                        design(60,2)
                                                                        cn=input('\n➤ Want to have an ATM Card ? 【y/n】 │ ')
                                                                        if vals(cn) :
                                                                            if cn == 'Y' or cn == 'y':
                                                                                applatm(x)
                                                                            else:
                                                                                design(60,2)
                                                                                center(colour('❖ Back to Main Menu ❖',4))
                                                                                design(60,2)
                                                                elif cn == 2:
                                                                    design(60,2)
                                                                    acstatement(x,'u')                                                                            
                                                    else:
                                                        design(60,2)
                                                        center(colour('✤ Available Facilities ✤',4))
                                                        design(60,2)
                                                        datarep('Press 1 ➤','Transfer Fund')
                                                        datarep('Press 2 ➤','Check Transactions')
                                                        datarep('Press 3 ➤','Block Transactions')
                                                        datarep('Any Num','Back')
                                                        design(60,2)     
                                                        cn=input('\n● Condition Chosen │ ')
                                                        design(60,2)    
                                                        if valn(cn) :
                                                            cn=int(cn)
                                                            if cn > 3 or cn <= 0:
                                                                design(60,2)
                                                                center(colour('❖ Back to Main Menu ❖',4))
                                                                design(60,2)
                                                            else:
                                                                if cn == 2:
                                                                    design(60,2)
                                                                    center(colour('✤ Available Options ✤',4))
                                                                    design(60,2)
                                                                    datarep('Press 1 ➤','Check Acceptance')
                                                                    datarep('Press 2 ➤','Check Drwaings')
                                                                    datarep('Any Num ➤','Back')
                                                                    design(60,2)     
                                                                    cn=input('\n● Condition Chosen │ ')
                                                                    design(60,2)    
                                                                    if valn(cn) :
                                                                        cn=int(cn)
                                                                        if cn > 2 or cn <= 0:
                                                                            design(60,2)
                                                                            center(colour('❖ Back to Main Menu ❖',4))
                                                                            design(60,2)
                                                                        else:
                                                                            design(60,2)
                                                                            datarep('Press 1 ➤','Via Amount')
                                                                            datarep('Press 2 ➤','Via Chq.No.')
                                                                            datarep('Any Num ➤','Back')
                                                                            design(60,2)     
                                                                            cn2=input('\n● Condition Chosen │ ')
                                                                            design(60,2)    
                                                                            if valn(cn2) :
                                                                                cn2=int(cn2)
                                                                                if cn2 > 2 or cn2 <= 0:
                                                                                    design(60,2)
                                                                                    center(colour('❖ Back to Main Menu ❖',4))
                                                                                    design(60,2)
 
                                                                                else:
                                                                                    if cn == 1:
                                                                                        if cn2 == 1:
                                                                                            design(60,2)
                                                                                            a=input('\n● Amount\t│ ')
                                                                                            if valn(a) :
                                                                                                design(60,2)
                                                                                                amountstatus(x,a,'aa','0')
                                                                                                design(60,2)
                                                                                        else:
                                                                                            design(60,2)
                                                                                            a=input('\n● Cheque No. │ ')                                                    
                                                                                            if valn(a) :
                                                                                                b=input('● Bank Name in Short form e.g. SBI│ ')
                                                                                                if vals(b) :
                                                                                                    design(60,2)
                                                                                                    amountstatus(x,a,'ac',b)
                                                                                                    design(60,2)
                                                                                    else:
                                                                                        if cn2 == 1:
                                                                                            design(60,2)
                                                                                            a=input('\n● Amount\t│ ')
                                                                                            if valn(a) :
                                                                                                design(60,2)
                                                                                                amountstatus(x,a,'wa','0')
                                                                                                design(60,2)
                                                                                        else:
                                                                                            design(60,2)
                                                                                            a=input('\n● DD/Self cheque \t│ ')
                                                                                            if valn(a) :
                                                                                                design(60,2)
                                                                                                amountstatus(x,a,'wc','0')
                                                                                                design(60,2)
 
                                                                elif cn == 3:
                                                                    design(60,2)
                                                                    center(colour('✤ Available Options ✤',4))
                                                                    design(60,2)
                                                                    datarep('Press 1 ➤','Block a Cheque')
                                                                    datarep('Press 2 ➤','Block (Back/History)')
                                                                    datarep('Any Num ➤','Back')
                                                                    design(60,2)     
                                                                    cn=input('\n● Condition Chosen │ ')
                                                                    design(60,2)    
                                                                    if valn(cn) :
                                                                        cn=int(cn)
                                                                        if cn > 2 or cn <= 0:
                                                                            design(60,2)
                                                                            center(colour('❖ Back to Main Menu ❖',4))
                                                                            design(60,2)
                                                                        else:
                                                                            if cn == 1:
                                                                                blchq(x,'b')
                                                                            else:
                                                                                df=blchq(x,'h')
                                                                                if df.empty:
                                                                                    design(60,2)
                                                                                    center(colour('✤ No Record Found ✤',4))
                                                                                    design(60,2)
                                                                                else:
                                                                                    design(60,2)
                                                                                    center(colour('❖ Block Trans. History ❖',4))
                                                                                    print(df)
                                                                                    design(60,2)
                                                                                    center(colour('✤ Things can be done ✤',4))
                                                                                    datarep('Press 1 ➤','Block Back')
                                                                                    datarep('Press 2 ➤','Save the Data')
                                                                                    datarep('Any Key ➤','Back Menu')
                                                                                    design(60,2)
                                                                                    cn=input('\n● Condition Chosen │ ')
                                                                                    if cn == '1':
                                                                                        design(60,2)
                                                                                        c=input('\n● Enter the Cheque Number │ ')
                                                                                        if valn(c) :
                                                                                            if c in df.index:
                                                                                                df=blchq(x,c)
                                                                                                design(60,2)
                                                                                                print(df)
                                                                                                design(60,2)
                                                                                                cn=input('\n➤ Want to back this cheque 【y/n】 │ :')
                                                                                                if cn == 'Y' or cn=='y':
                                                                                                    files.execute("delete from blocktrans where cusid ='{}' and cheqnum ='{}' ".format(x,c))
                                                                                                    mycon.commit()
                                                                                                    t='Successfully Block Back \n'+'Chq No. '+str(c)
                                                                                                    pyg.alert(t,'Dev CRM-'+str(x))
                                                                                                    design(60,2)
                                                                                                    center(colour('Successfully Block-Back',2))
                                                                                                    design(60,2)
                                                                                                else:
                                                                                                    design(60,2)
                                                                                                    center(colour('✤ Proposal Rejected ✤',6))
                                                                                                    design(60,2)
                                                                                            else:
                                                                                                design(60,2)
                                                                                                center(colour('✤ No Block Cheque Found ✤',4))
                                                                                                design(60,2)
 
                                                                                    elif cn == '2':
                                                                                        cn=input('\n➤ Want to Save this Data 【y/n】 │ ')
                                                                                        if cn == 'Y' or cn=='y':
                                                                                            save(df,'ad')
                                                                                            design(60,2)
                                                                                        else:
                                                                                            design(60,2)
                                                                                            center(colour('✤ Proposal Rejected ✤',6))
                                                                                            design(60,2)
                                                                                    else:
                                                                                        design(60,2)
                                                                                        center(colour('❖ Back to Main Menu ❖',4))
                                                                                        design(60,2)
                                                                else:
                                                                    design(60,2)
                                                                    center(colour('✤ Transfer Fund ✤',4))
                                                                    design(60,2)
                                                                    datarep('Press 1 ➤','Benefit Same Bank')
                                                                    datarep('Press 2 ➤','Benefit Another Bank')
                                                                    datarep('Any Num ➤','Back')
                                                                    design(60,2)     
                                                                    cn=input('\n● Condition Chosen │ ')
                                                                    design(60,2)    
                                                                    if valn(cn) :
                                                                        cn=int(cn)
                                                                        if cn > 2 or cn <= 0:
                                                                            design(60,2)
                                                                            center(colour('❖ Back to Main Menu ❖',4))
                                                                            design(60,2)
                                                                        else:
                                                                            p=cusbal(x)
                                                                            design(60,2)
                                                                            datarep('Present Balance ➤',p)
                                                                            design(60,2)
                                                                            a=input('● Amount to be Transfer \t│ ')
                                                                            if valn(a)  and nonzero(a) :
                                                                                design(60,2)
                                                                                datarep('Amount in Words │ ',alpha(a))
                                                                                design(60,2)
                                                                                ty=acty(x,0)
                                                                                z=p-int(a)
                                                                                if z < 100 and p>=int(a) and ty=='saving':
                                                                                    pyg.alert('As the Balance gonna less than 100\n'+                                                                                    'it will results in 【 SUSPENSION of your Account 】: '+str(x)+                                                                                    'Kindly Cancel this Transaction to AVOID SUSPENSION','Dev CRM -'+ str(x))
                                                                                elif z < 1000 and p>=int(a) and ty=='current':
                                                                                    pyg.alert('As the Balance gonna less than 1000\n'+                                                                                    'it will results in 【 SUSPENSION of your Account 】: '+str(x)+                                                                                    'Kindly Cancel this Transaction to AVOID SUSPENSION','Dev CRM -'+ str(x))
                                                                                c=input('\n➤ Want to Transfer Amount ? 【y/n】 │ ')
                                                                                if c == 'Y' or c=='y':
                                                                                    if cn == 1:
                                                                                        transfund(x,'s',str(a),'0')
                                                                                    else:
                                                                                        transfund(x,'o',str(a),'0')
                                                                                else:
                                                                                    design(60,2)
                                                                                    center(colour('✤ Changes Unmade Yet ✤',4))
                                                                                    design(60,2)
                                    else:
                                        design(60,2)
                                        cn=input('➤ Do You Forget Your Password 【y/n】 │')
                                        if cn == 'Y' or cn=='y':
                                            if validation(x) == True:
                                                changepsw('',x,0,True)
                                        else:
                                            design(60,2)
                                            center(colour('✤ Proposal Rejected ✤',6))
                                            design(60,2)
                                            break
                                else:
                                    design(60,2)
                                    design(60,2)
                                    center(colour('✋ Oops Your Account has【Suspended】✋',1))
                                    center(colour('Reason For this may be',3))
                                    datarep('A/C Bal. ➤','< Oprt. Bal.')
                                    center(colour('Opertaing Balance for',5))
                                    datarep('Saving A/C ➤','Bal > 100')
                                    datarep('Curent A/C ➤','Bal > 1000')
                                    center(colour('❖ To know more visit our Bank ❖',6))
                                    design(60,2)
                                    design(60,2)
                                    break
                            else:
                                design(60,2)
                                center(colour("✋ You don't have Dev E-Banking Yet ✋",1))
                                center(colour('➤ Want to Apply for that',4))
                                datarep('Press Y ➤','For Yes')
                                datarep('Any Key ➤','For No')
                                design(60,2)
                                c=input('\n● Condition Chosen │ ')
                                if c=='Y'or c=='y':
                                    design(60,2)
                                    if validation(x) == True:
                                        center(colour('✤ Few Steps Ahead ✤',4))
                                        design(60,2)
                                        ph=getpass('\n● Create Your Password │ ')
                                        if pswpwr(ph) :
                                            ph2=getpass('● Confirm Your Password │ ')
                                            if pswmatch(ph,ph2) :
                                                ph=encrypt(ph)
                                                files.execute("update devcus set passw = '{}',active = 1 where cusid='{}' ".format(ph,x))
                                                mycon.commit()
                                                design(60,2)
                                                t='Well Done '+ '\nYour E-Banking Activated Successfully'                                                'Try Login using Your Credentials \n'+'Login Id and Password'
                                                pyg.alert(t,'Dev Bank')
                                                center(colour('Your E-Banking Activated Successfully',2))
                                                center(colour('Login Credentials are',6))
                                                datarep('Cust ID','Password')
                                                center(colour('Hope You Know T&C of Dev Bank',2))
                                                design(60,2)
                                                time.sleep(0.3)
                                            else:
                                                design(60,2)
                                                center(colour('❌❌ Validation Failed ❌❌',1))
                                                design(60,2)
                                                break
                                        else:
                                            design(60,2)
                                            center(colour('❌❌ Validation Failed ❌❌',1))
                                            design(60,2)
                                            break
                                else:
                                    design(60,2)
                                    center(colour('✤ Proposal Rejected ✤',6))
                                    design(60,2)
                                    break
                elif int(st) == 0:
                    pyg.alert('✤ System Closes Successfully ✤\nThanks for Your Concern')
                    design(60,2)
                    design(60,2)
                    center(colour('✤ System Closes Successfully ✤',1))
                    center(colour('❖ Thanks for Your Concern ❖',1))
                    design(60,2)
                    mycon.close()
                    sys.exit()
                else:
                    design(60,2)
                    if os.path.exists('T&C.txt'):
                        f = open("T&C.txt", "r")
                        pyg.alert(f.read(),'Dev Bank CRM T&C')
                        design(60,2)
                    else:
                        f='T&C.txt File not Found \n If you deleted or lost \n\n Download it from \n https://devbank.netlify.app'
                        pyg.alert(f,'Dev Bank CRM T&C')
                        center(colour(f,1))
                        datarep('File Name ➤','T&C.txt')
                        design(60,2)
        else:
            design(60,2)
            center(colour('!! ❌❌❌❌❌❌ System Faces Error ❌❌❌❌❌❌ !! \n',1))
            center(colour('Prior Errors Needs to be Corrected\nBefore Opeartions',5))
            design(60,2)
            mycon.close()
            sys.exit()
            break

