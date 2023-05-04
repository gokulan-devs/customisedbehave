import os

data_file= (os.path.join(os.getcwd(), 'feature/data/examples.csv'))

table = {}
f = open(data_file)
      # Get column names
    
for line in f.readlines():
    columns = [x.strip() for x in line.split(',')]
    if line.startswith(":"):
        scenario=columns[0][1:]
        table[scenario]={"count":0,"columns":{},"data":[]}
        for column in columns[1:]:
            table[scenario]["columns"][column]=""
    else:
        scenario=columns[0]
        listofkeys=table[scenario]["columns"].keys()
        count=table[scenario]["count"]
        data_dict={}
        for keys,values in zip(listofkeys,columns[1:]):
            data_dict[keys]=values
        data_set=data_dict.copy()
        table[scenario]["data"].append(data_set)
        table[scenario]["count"]=count+1
f.close()
data_table=table.copy()
