from django.shortcuts import render, HttpResponse
# Create your views here.
import random

topics = [
    {'id': 1, 'title': 'routing', 'body' : 'Routing is ..'},
    {'id': 2, 'title': 'view', 'body': 'view is ..'},
    {'id': 3, 'title': 'Model', 'body': 'Model is ..'},

]
def index(request):
    global topcis
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return HttpResponse(f'''
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <h2>Welcome</h2>
        Hello, Django
    </body>
    </html>
    ''')

def create(request):
    return HttpResponse('<h1>Random</h1>'+ str(random.random()))

def read(request , id):
    return HttpResponse('Read!' + id)