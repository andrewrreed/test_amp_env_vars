
!pip3 install -r requirements.txt

import os
import xml.etree.ElementTree as ET
from cmlbootstrap import CMLBootstrap

# Set the setup variables needed by CMLBootstrap
HOST = os.getenv("CDSW_API_URL").split(
    ":")[0] + "://" + os.getenv("CDSW_DOMAIN")
USERNAME = os.getenv("CDSW_PROJECT_URL").split(
    "/")[6]  # args.username  # "vdibia"
API_KEY = os.getenv("CDSW_API_KEY") 
PROJECT_NAME = os.getenv("CDSW_PROJECT")  

# Instantiate API Wrapper
cml = CMLBootstrap(HOST, USERNAME, API_KEY, PROJECT_NAME)

# Set the STORAGE environment variable
try : 
  storage=os.environ["STORAGE"]
  print('MADE IT TO - A')
except:
  if os.path.exists("/etc/hadoop/conf/hive-site.xml"):
    print('MADE IT TO - B')
    tree = ET.parse('/etc/hadoop/conf/hive-site.xml')
    root = tree.getroot()
    for prop in root.findall('property'):
      if prop.find('name').text == "hive.metastore.warehouse.dir":
        storage = prop.find('value').text.split("/")[0] + "//" + prop.find('value').text.split("/")[2]
  else:
      print('MADE IT TO - C')
    storage = "/user/" + os.getenv("HADOOP_USER_NAME")

#   storage_environment_params = {"STORAGE":storage}
#   print("DATA_LOCATION A:", os.environ['DATA_LOCATION'])
#   storage_environment = cml.create_environment_variable(storage_environment_params)
#   os.environ["STORAGE"] = storage


print("DATA_LOCATION B:", os.environ['DATA_LOCATION'])
# print("STORAGE", os.environ["STORAGE"])