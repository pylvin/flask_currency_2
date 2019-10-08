from flask import render_template, request, jsonify
from tasks.tasks import *
from models.models import Currency


def index():
    context={}
    if request.method == 'POST':
        range_date=request.values.get('change_date')
        start_date=range_date[:10].replace('/','.')
        end_date = range_date[13:].replace('/','.')

        data= get_data(start_date,end_date)
        a=Thread(target=data_checker(get_changes(data[0],start_date,data[1],end_date),start_date,end_date))
        a.start()
        if data:
            return jsonify(get_changes(data[0],start_date,data[1],end_date))
        else:
            return jsonify({'error':True})
    return render_template('index.html',**context)