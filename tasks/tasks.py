from threading import Thread
import requests
import json
import os
import xmltodict

from models.models import Currency


def get_data(start_date,end_date):
    start = requests.get(f'https://www.cbar.az/currencies/{start_date}.xml')
    end = requests.get(f'https://www.cbar.az/currencies/{end_date}.xml')
    start_date_data = json.loads(json.dumps(xmltodict.parse(start.text)))
    end_date_data = json.loads(json.dumps(xmltodict.parse(end.text)))
    for i in start_date_data['ValCurs']['ValType']:
        if i['@Type'] == 'Xarici valyutalar':
            start_date_data =i['Valute']
    for i in end_date_data['ValCurs']['ValType']:
        if i['@Type'] == 'Xarici valyutalar':
            end_date_data = i['Valute']
    return [start_date_data,end_date_data]

def get_changes(start_valutes,start_date,end_valutes,end_date):
    for i in range(len(end_valutes)):
        check = float(end_valutes[i]['Value']) - float(start_valutes[i]['Value'])
        if check > 0:
            end_valutes[i]['status']='up'
            end_valutes[i]['changes'] = round(check, 10)
            end_valutes[i]['from'] = start_date
            end_valutes[i]['to'] = end_date


        elif check == 0:
            end_valutes[i]['status'] = 'No Changes'
            end_valutes[i]['changes'] = 0
            end_valutes[i]['from'] = start_date
            end_valutes[i]['to'] = end_date

        else:
            end_valutes[i]['status'] = 'down'
            end_valutes[i]['changes'] = round(check, 10)
            end_valutes[i]['from'] = start_date
            end_valutes[i]['to'] = end_date


    return end_valutes



def data_checker(all_data,start_date,end_date):
    if Currency.filter(from_date=start_date, to_date=end_date).first():
        print('var')
    else:
        for i in all_data:
            a = Currency(name=i['Name'],code=i['@Code'],from_date=i['from'],to_date=i['to'],
                         status=i['status'],changes=i['changes'],value=i['Value'])
            a.save()