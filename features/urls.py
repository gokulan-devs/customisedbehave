import os
import yaml

urls_file= (os.path.join(os.getcwd(), 'urls.yaml'))
urls =yaml.load(open(urls_file),Loader=yaml.FullLoader)
    