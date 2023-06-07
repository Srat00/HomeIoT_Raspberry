
from pymongo import MongoClient
from data_fetcher import get_decibel_data

from django.shortcuts import render
def index(request):
    # 몽고디비에서 데이터 가져오기
    data = get_decibel_data()
    print(data)
    # 데이터를 템플릿에 전달하여 렌더링
    return render(request, 'index.html', {'data': data})
