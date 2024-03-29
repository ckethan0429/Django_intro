from django.shortcuts import render
import random
import math
from datetime import datetime
import requests
#from pprint import pprint
# Create your views here.


def index(request):

    return render(request, 'pages/index.html')


def dinner(request):

    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {'pick': pick}
    return render(request, 'pages/dinner.html', context)


def hello(request, name):

    context = {'name': name,}
    return render(request, 'pages/hello.html',context)

# 자기소개/ 이름과 나이를 url로 받아서 출력
def introduce(request, name, age):
    context = {'name': name,
              'age': age,
               }
    return render(request, 'pages/introduce.html', context)

# 숫자 2개를 variable routing으로 받아 곱셈결과를 출력


def times(request, num_1, num_2):
    value = num_1 * num_2
    context={'num_1': num_1,
             'num_2': num_2,
             'value': value,
            }
    return render(request, 'pages/times.html', context)

# 원의 반지름 값을 variable routing 으로 받아 원의 넓이를 출력
def area(request, radius):
    value = math.pi * radius * radius
    context = {'radius': radius,
               'value': value,
               }
    return render(request, 'pages/area.html', context)


def dtl_example(request):
    menus = ['짜장면', '탕수육', ' 짬뽕', '양장피']
    my_sentence = 'Life is short, YOu need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list':empty_list,
    }
    return render(request, 'pages/dtl_example.html', context)


def throw(request):
    return render(request, 'pages/throw.html')


def catch(request):
    #print(request.GET)
    message = request.GET.get('message')
    context = {'message': message,}
    return render(request, 'pages/catch.html', context)


def artii(request):
    return render(request, 'pages/artii.html')


def result(request):

    # 1. form 에서 날아온 데이터를 받는다
    message = request.GET.get('message')
    # 2. 'http://artii.herokuapp.com/fonts_list' 로 요청을 보내 응답결과를 .text 변환후 저장한다.
    font = requests.get('http://artii.herokuapp.com/fonts_list').text
    # 3. 저장한 데이터를 list로 바꾼다.
    font_list = font.split('\n')
    # 4. list안에 들어있는 요소(font)하나를 선택(random)해 저장한다.
    font_random = random.choice(font_list)
    # 5. 우리가 전달한 데이터와 list안에 font를 가지고 다시 요청을 보내
    # 해당 응답결과를 저장
    req = requests.get(f'http://artii.herokuapp.com/make?text={message}&font={font_random}').text
    # 6. 최종적으로 저장한 데이터를 template 으로 넘겨준다.
    print(req)
    context = {'req': req,}
    return render(request, 'pages/result.html', context)


def user_new(request):
    return render(request, 'pages/user_new.html')


def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {
        'name': name,
        'pwd': pwd,
    }
    return render(request, 'pages/user_create.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')






