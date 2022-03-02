#!/usr/bin/env python
# coding: utf-8

# In[28]:


import datetime
import pytz
import oci
from oci.config import from_file

DAYS_OLD = 90

# Start print time info
start_datetime = datetime.datetime.now().replace(tzinfo=pytz.UTC)
start_time_str = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# For User based key checks
start_date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
api_key_time_max_datetime = start_datetime - datetime.timedelta(days=DAYS_OLD)


# Using the default profile from a different file
config = from_file(file_location="<Config_File_Loc>", profile_name='DEFAULT')

identityClient = oci.identity.IdentityClient(config)
user = identityClient.get_user(config["user"]).data

usersList = identityClient.list_users("<Tenancy_OCID>").data
print("Total Users in OCI: ", len(usersList))

for users in usersList:
        usersKeys = identityClient.list_api_keys(users.id).data
        for keys in usersKeys:
            print("Key 1: Is it more than 90 days old?", usersKeys[keys].time_created <= api_key_time_max_datetime)
        


# In[ ]:




