# on AWS python script
# 0. install dependencies (pycurl)
# 1. Make APIs to Particle Device Cloud -> Get published Sensor Data
# 2. (optional) Make data format alignment -> database schema
# 3. Make APIs calls to Database to insert dataframe
# 4. Verify data correctly inserted



# particle cloud (STRUCT)

# struct sensor_data
# {
#     const char* accel_id;
#     const char* description;
#     const char* patient_id;
#     const float x;
#     const float y;
#     const float z;
# };

# Publish to Device Cloud

# AWS's python script. Get struct -> unfold python varibles

from ipdb import set_trace as debug
import sys
sys.path.append('database')   
from database.database import *
# import pycurl
from io import BytesIO
import json
import uuid
import colored_traceback.always
#### Set up HTTP cURL #####
# b_obj = BytesIO()

# para_list =  ['x', 'y', 'z']
# para_dic = dict()
# for p in para_list:
#     crl = pycurl.Curl()
#     url = 'https://api.particle.io/v1/devices/e00fce686d200543393e0bba/' + p + '?access_token=3a45f46a1ebf53a33f0e3b70c576f5d05da776a4'
#     crl.setopt(crl.URL, url)
#     crl.setopt(crl.WRITEDATA, b_obj)
#     crl.perform()
#     crl.close()
#     sensor_value = b_obj.getvalue()
#     mock_value = '{"cmd":"VarReturn","name":"x","result":0,"coreInfo":{"last_app":"","last_heard":"2020-04-06T22:19:47.836Z","connected":true,"last_handshake_at":"2020-04-06T22:10:11.994Z","deviceID":"e00fce686d200543393e0bba","product_id":13}}'
#     format_value = json.loads(sensor_value)
#     print("Sensor Value " + sensor_value)
#     print("Format data ")
#     print(format_value['result'])
#     # if value == "result":
#     if 'result' in format_value:
#         para_dic[p] = format_value['result']


# # mock accel_id, patient_id, description
# para_dic["accel_id"] = uuid.uuid4()
# para_dic["patient_id"] = uuid.uuid4()
# para_dic["description"] = "testing accel data"
#     #json_list.append(sensor_value)
# #print('jsonlist')
# #print(json_list)

# # Set URL value
# # curl -G https://api.particle.io/v1/devices/e00fce686d200543393e0bba/command -d access_token=3a45f46a1ebf53a33f0e3b70c576f5d05da776a4


# # Perform a file transfer
# #crl.perform()

# # End curl session
# #crl.close()

# # Get the content stored in the BytesIO object (in byte characters)
# # Decode the bytes stored in get_body to HTML and print the result
# mock_value = '{"cmd":"VarReturn","name":"x","result":1.1,"coreInfo":{"last_app":"","last_heard":"2020-04-02T23:04:39.659Z","connected":true,"last_handshake_at":"2020-04-02T23:03:16.391Z","deviceID":"e00fce686d200543393e0bba","product_id":13}}'

# print('Output of GET request:\n%s' % sensor_value.decode('utf8'))

# # clean data and format data
# # ('00000000-0000-0000-0000-000000000010', '00000000-0000-0000-0001-000000000000', 'test accel 1', '10000000-0000-0000-0000-000000000000', 1, 2, 3)
# # accel_id should be uuid
# accel_id = para_dic['accel_id']
# description = para_dic['description']
# patient_id = para_dic['patient_id']
# x = para_dic['x']
# y = para_dic['y']
# z = para_dic['z']

# source for secrets and DB info
db = get_db()

accel_id = uuid.uuid4()
description = "dashboard local test"
patient_id = uuid.uuid4()
x = 1.1
y = 1.1
z = 1.1
# db, accel_id, description, patient_id, x, y, z
insert_accel(db, accel_id, description, patient_id, x, y, z)



# verify data
retrieved_accel = []
print("accel_id to find: ", accel_id)
retrieved_accel = find_by_accel_id(db, accel_id)
print(retrieved_accel)
# for dic in retrieved_accel:
#     if (dic['x'] == para_dic['x'] and dic['y'] == para_dic['y'] and dic['z'] == para_dic['z']):
#         print("all tests have passed")