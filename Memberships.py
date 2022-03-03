#!/usr/bin/env python
# coding: utf-8

# In[54]:


import requests
import csv
import sys
import json
import datetime
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from pprint import pprint
import time
import pandas as pd
import math


today = datetime.now()
print(today)



## 2022
def updateUser(fn,ln,email,date):
    un = fn[0]+ln
    parameters = {"values":{"_x002F_entry_x005B_1_x005D__x002F__x0040_site_x005B_1_x005D_":"US","_x002F_entry_x005B_1_x005D__x002F__x0040_directoryPath_x005B_1_x005D_":"ids://EXPLOITATION/cn="+un+",ou=US,ou=Migrate-from-v4,o=EXPLOITATION,dc=archimed,dc=local","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_cn_x0027__x005D__x005B_1_x005D_":un,"_x002F_entry_x005B_1_x005D__x002F__x0040_name_x005B_1_x005D_":un,"_x002F_entry_x005B_1_x005D__x002F__x0040_password_x005B_1_x005D_":"","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_mail_x0027__x005D__x005B_1_x005D_":email,"_x002F_entry_x005B_1_x005D__x002F__x0040_expirationDate_x005B_1_x005D_":date,"_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_givenName_x0027__x005D__x005B_1_x005D_":fn,"_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_sn_x0027__x005D__x005B_1_x005D_":ln,"_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_birthday_x0027__x005D__x005B_1_x005D_":"","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_department_x0027__x005D__x005B_1_x005D_":"Dallas (TX) - Alliance fran\u00e7aise","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_telephoneNumber_x0027__x005D__x005B_1_x005D_":"","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_street_x0027__x005D__x005B_1_x005D_":"Texas (TX)","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_postalCode_x0027__x005D__x005B_1_x005D_":"","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_l_x0027__x005D__x005B_1_x005D_":""}}
    r=t.post('https://www.culturetheque.com/pro/US/portal/user.svc/UpdateUser', json=parameters)
    json_string=r.text
    dictionary = json.loads(json_string)
    return dictionary


#create a cultureteque account
def create_ct (un, fn, ln, email,date):
    parameters = {"scopeName":"US","userTypeName":"Users","values":{"_x002F_entry_x005B_1_x005D__x002F__x0040_directoryPath_x005B_1_x005D_":"","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_cn_x0027__x005D__x005B_1_x005D_":"","_x002F_entry_x005B_1_x005D__x002F__x0040_name_x005B_1_x005D_":un,"_x002F_entry_x005B_1_x005D__x002F__x0040_password_x005B_1_x005D_":"HITB301?","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_mail_x0027__x005D__x005B_1_x005D_":email,"_x002F_entry_x005B_1_x005D__x002F__x0040_expirationDate_x005B_1_x005D_":date,"_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_givenName_x0027__x005D__x005B_1_x005D_":fn,"_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_sn_x0027__x005D__x005B_1_x005D_":ln,"_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_birthday_x0027__x005D__x005B_1_x005D_":"","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_department_x0027__x005D__x005B_1_x005D_":"Dallas (TX) - Alliance fran\u00e7aise","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_telephoneNumber_x0027__x005D__x005B_1_x005D_":"","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_street_x0027__x005D__x005B_1_x005D_":"Texas (TX)","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_postalCode_x0027__x005D__x005B_1_x005D_":"","_x002F_entry_x005B_1_x005D__x002F_attribute_x005B__x0040_name_x003D__x0027_l_x0027__x005D__x005B_1_x005D_":""}}
    #r=t.post('https://www.culturetheque.com/EXPLOITATION/pro/US/Portal/User.svc/AddUser', json=parameters)
    r=t.post('https://www.culturetheque.com/pro/US/Portal/user.svc/AddUser', json=parameters)
    json_string=r.text
    dictionary = json.loads(json_string)
    return dictionary



print ("Logging in to cultureteque ...")
ctlogin = {'username': 'yourusername', 'password': 'yourpassword'}
t = requests.Session()
#r = t.post('https://www.culturetheque.com/EXPLOITATION/pro/US/Portal/logon.svc/logon', data=ctlogin)
r = t.post('https://www.culturetheque.com/pro/US/Portal/logoff.aspx?returnUrl=/exploitation/pro/&changeUser=true', data=ctlogin)
if r.status_code == 200:
    print ("Cultureteque login successful!")
else:
    print ("login failure")


# In[60]:

#data containing all students
#data containing new students
all_ = pd.read_csv('export_2110918905.csv')
new = pd.read_excel('export_19868713.xls')


# In[61]:


new.shape, all_.shape


# In[62]:


new.columns, all_.columns


# In[63]:


f = new.merge(all_,how='left',on='Email')
f = f[['Student code','Last name','First name','Phone','Zip code','Address','City','State or Province','Email','Member ID','Type of membership','Expires on']]
f.to_csv('processed.csv',index=False)


# In[64]:


f


# https://stackoverflow.com/questions/24085680/why-do-backslashes-appear-twice

# In[69]:


#store data
successes = []
failures = []
cc_emails = []
success_renewals = []
fail_renewals=[]


# In[70]:




# In[71]:


#for ln,fn,e,ed in zip(test['Last name'].values,test['First name'].values,test['Email'].values,test['Expires on'].values):
for ln,fn,e,ed in zip(f['Last name'].values,f['First name'].values,f['Email'].values,f['Expires on'].values):
    #e = 'monkey10@gmail.com'
    print(ln,fn,e,ed)
    ed = str(ed)
    if ed == 'nan':
        continue
    xldt = datetime.strptime(str(ed), "%m/%d/%Y")
    excel_date = ed.split('/')
    excel_date = excel_date[2]+"-"+excel_date[0]+"-"+excel_date[1]+"T00:00:00-06:00" #"2022-03-05T00:00:00-06:00"
    print("processing %s %s %s" % (ln,fn,e))
    print(excel_date)

    emailsearch = {"query":{"Area":"USERS","Query":"mail=\"%s\"" % e,"Parameters":{},"Filters":"","SelectedDocuments":[],"SelectedFacets":[],"ReboundName":"","ReboundCount":0,"ViewCode":"LIST","Sorters":[],"ClientUtcOffset":-5},"start":0,"limit":100}
    while True:
        try:
            r=t.post('https://www.culturetheque.com/pro/US/Portal/searcharea.svc/find?_dc=1601252718088',json=emailsearch)
            print(r.status_code)
            if r.status_code == 200:
                break
            else:
                sleep(1)
                print("sleep sleep sleep")
                break
        except Exception as e:
            print (e)
    json_string = r.text
    dictionary = json.loads(json_string)
    #print(dictionary)
    #print('\n')
    #print(dictionary['d']['Results'])

    #cc
    cc_emails.append(e)

    #if dictionary['d']['Facets'][0]['Entries'] == []: # new users
    if dictionary['d']['Results'] == []: # new users
        print('creating new for ', e)
        take = 1
        un = fn[:take]+ln
        new = create_ct(un,fn,ln,e,excel_date)
        print(new)
        print(len(new['errors']))
        if len(new['errors']) == 0:
            successes.append([fn,ln,e])
            continue

        if take > len(fn):
            failures.append([fn,ln,e])

        while len(new['errors']) > 0:
            take = take+1
            un = fn[:take]+ln
            new = create_ct(un,fn,ln,e,excel_date)
            print(new)
            if len(new['errors']) == 0:
                successes.append([fn,ln,e])
            if take > len(fn):
                print(take,len(fn))
                break
    else: #re new users
        try:
            #dictionary['d']['Results'][0]["ExpirationDate"]
            dictionary['d']['Results'][0]["ExpirationDate"]
            print(dictionary['d']['Results'][0]["ExpirationDate"])
        except KeyError:
            print ("KeyError")
            continue
        '''ct_date = dictionary['d']['Results'][0]["ExpirationDate"]
        ct_date = ct_date.split('(')
        ct_date = ct_date[1].split(')')
        ct_date[0] = float(ct_date[0])/1000
        ct_dt = datetime.fromtimestamp(ct_date[0])
        if ct_dt < xldt:'''
        print('updating usr for ', e)
        up = updateUser(fn,ln,e,excel_date)
        if len(up['errors']) == 0:
            success_renewals.append([fn,ln,e])
        else:
            fail_renewals.append([fn,ln,e])

    #break


# In[72]:


print("Successful New Accounts:")
for success in successes:
    print ("%s %s %s" % (success[1],success[0],success[2]))
print('')

print("Successful REnewed Accounts:")
for sr in success_renewals:
    print ("%s %s %s" % (sr[1],sr[0],sr[2]))
print('')

print("Failed Renewals (doesnt use naming convention)")
for fr in fail_renewals:
    print ("%s %s %s" % (fr[1],fr[0],fr[2]))
print('')

print("Just Failed for some other reason (new account with user name taken?):")
for failure in failures:
    print ("%s %s %s" % (failure[1],failure[0],failure[2]))
print('')

#constant contact email addresses
print("The following emails needs to be pasted into constant contact:")
for email in set(cc_emails):
    print(email)


# In[ ]:





# https://www.culturetheque.com/pro/US/Portal/logoff.aspx?returnUrl=/exploitation/pro/&changeUser=true
