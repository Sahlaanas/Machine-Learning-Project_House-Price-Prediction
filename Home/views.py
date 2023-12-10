from django.shortcuts import render
from django.http import HttpResponse
import pickle
import json
import numpy as np

with open('/Users/mac/Desktop/bnglr_hs_prdcn_project/model/columns.json', 'r') as json_file:
    data = json.load(json_file)
    columns = data['data_columns']
    

model = pickle.load(open('model/bglr_house_price_model.pickle','rb'))
# Create your views here.
def Home(request):
    try:
        return render(request, 'index.html', {'dropdown_data': columns})
    except FileNotFoundError:
        return render(request, 'index.html')


def formInfo(request):
    location = request.GET['location']
    location = location.lower()
    bhk = request.GET['bhk']
    area = request.GET['area']
    bath = request.GET['bath']
    loc_index = columns.index(location)

    x = np.zeros(len(columns))
    x[0] = area
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    y_pred = model.predict([x])[0]
    return render(request, 'result.html',{'prediction' : np.round(y_pred)*100000}) 




