import os

try:
    print(os.environ['DATA_LOCATION'])
except:
    print('DATA_LOCATION env variable is NOT present')

try:
    print(os.environ['TEST_VAR_1'])
except:
    print('TEST_VAR_1 env variable is NOT present')