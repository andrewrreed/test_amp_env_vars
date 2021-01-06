!pip3 install git+https://github.com/fastforwardlabs/cmlbootstrap#egg=cmlbootstrap

import os
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

# Check for the DATA_LOCATION env variable that was set via .project-metadata.yaml
print('----BEFORE USING BOOTSTRAP----')
try:
    print(os.environ['DATA_LOCATION'])
except:
    print('DATA_LOCATION env variable is NOT present')

# ## COMMENT THIS OUT FOR TESTING TO SEE THAT IT WORKS
# # Set dummy environment variable via CMLBootstrapAPI
# storage_environment_params = {"TEST_VAR_1":'this_is_test_var_1'}
# storage_environment = cml.create_environment_variable(storage_environment_params)

# Check for the DATA_LOCATION env variable that was set via .project-metadata.yaml
print('----AFTER USING BOOTSTRAP----')
try:
    print(os.environ['DATA_LOCATION'])
except:
    print('DATA_LOCATION env variable is NOT present')