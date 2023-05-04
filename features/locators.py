import os
import yaml

locator_file= (os.path.join(os.getcwd(), '/features/locators.yaml'))
locators =yaml.load(open(locator_file),Loader=yaml.FullLoader)
    
