import os
import yaml

urls_file= (os.path.join(os.getcwd(), 'features/urls.yaml'))
urls =yaml.load(open(urls_file),Loader=yaml.FullLoader)
    
