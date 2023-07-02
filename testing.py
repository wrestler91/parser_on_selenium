data = {'brand': {'gender': {'model': 
                             {'price': 'price1',
                              'disc': 'disc',
                              'name': 'name',}}}}


result: list = []
for brand, gender_data in data.items():
    for gender, model_data in gender_data.items():
        for model, detail_data in model_data.items():
            values = detail_data.values()
            temp = [model, *values, gender, brand]
            result.append(temp)