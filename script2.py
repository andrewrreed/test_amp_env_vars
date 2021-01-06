import os

try:
    print(os.environ['DATA_LOCATION'])
except:
    print('DATA_LOCATION env variable is NOT present')