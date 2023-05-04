import os
import sys
import yaml

locator_file= (os.path.join(os.getcwd(), '\\features\\locators.yaml'))
print(locator_file)
locators =yaml.load(open(locator_file),Loader=yaml.FullLoader)
    
