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

# Set dummy environment variable via CMLBootstrapAPI
storage_environment_params = {"TEST_VAR_1":'this_is_test_var_1'}
storage_environment = cml.create_environment_variable(storage_environment_params)

# if "TEST_VAR_1" in os.environ:
#     print(os.environ["TEST_VAR_1"])

assert "TEST_VAR_1" in os.environ

# Set second environment variable via CMLBootstrapAPI
storage_environment_params = {"TEST_VAR_2":'this_is_test_var_2'}
storage_environment = cml.create_environment_variable(storage_environment_params)

assert "TEST_VAR_1" in os.environ
assert "TEST_VAR_2" in os.environ

# if "TEST_VAR_1" in os.environ:
#     print(os.environ["TEST_VAR_1"])

# if "TEST_VAR_2" in os.environ:
#     print(os.environ["TEST_VAR_2"])