import csv
from os import name
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Library
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import json
import requests

# Create your views here.
# data = None

# def read_data(table_name):
#     with open(f'/home/ubuntu/chatbot/libraries/{table_name}.csv', 'r', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         global data
#         data = list(reader)
#     return


# def footer(table_name, class_name, bulk_list):
#     class_name.objects.bulk_create(bulk_list)
    
#     with open(f'/home/ubuntu/chatbot/libraries/{table_name}.csv', 'w') as csvfile:
#         writer = csv.writer(csvfile)
#     return


# def add_libraries(request):
#     read_data('libinfo')
#     if not data:
#         return HttpResponse('Nothing to update')

#     arr = []
#     for row in data:
#         arr.append(Library(
#             name=row[0],
#             seat=row[1],
#             loan_cnt=row[2],
#             loan_tern=row[3]
#         ))

#     footer('libinfo', Library, arr)
#     return HttpResponse('Libraries table updated')

# def csv_to_df(request):
#     df = pd.read_csv("/home/ubuntu/chatbot/libraries/libinfo_df.csv")
#     d = '구수산도서관'
#     idx = df.index[(df['name'] == d)]
#     ans = df.loc[idx]['seat']
#     return HttpResponse(idx)

df = pd.read_csv("/home/ubuntu/chatbot/libraries/libinfo_df.csv")


# 도서관 명
@csrf_exempt
def choice(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    
    if any(df['name'].str.contains(return_str)):
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': '어떤 정보가 필요하신가요? :)'
                    }
                }],
                'quickReplies': [{
                    'label': '편의시설',
                    'action': 'message',
                    'messageText': f'{return_str}의 편의시설'
                    },
                    {
                    'label': '세부정보',
                    'action': 'message',
                    'messageText': f'{return_str}의 세부정보'
                    },
                    ]
                }
            }) 
    else:
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': '띄어쓰기 없이 정확한 도서관이름을 말씀해주세요!'
                    }
                }]
            }
        })        


# 편의시설
@csrf_exempt
def facilities(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    idx = return_str.index('의')
    name = return_str[:idx]
    info = return_str[idx+2:]

    if info == '편의시설':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': 'https://www.google.com/'
                    }
                }],
                'quickReplies': [{
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                    }],
                } 
            })


# 세부정보
@csrf_exempt
def details(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    idx = return_str.index('의')
    name = return_str[:idx]
    info = return_str[idx+2:]

    if info == '세부정보':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': '하단의 버튼 중 필요하신 세부정보를 선택해주세요!'
                    }
                }],
                'quickReplies': [{
                    'label': '비도서자료수',
                    'action': 'message',
                    'messageText': f'{name}의 비도서자료수'
                    },
                    {
                    'label': '전자자료수',
                    'action': 'message',
                    'messageText': f'{name}의 전자자료수'
                    },
                    {
                    'label': '장애인용 특수자료',
                    'action': 'message',
                    'messageText': f'{name}의 장애인용 특수자료'
                    },
                    {
                    'label': '좌석수',
                    'action': 'message',
                    'messageText': f'{name}의 좌석수'
                    },
                    {
                    'label': '전자시스템 현황',
                    'action': 'message',
                    'messageText': f'{name}의 전자시스템 현황'
                    },
                    {
                    'label': '위치',
                    'action': 'message',
                    'messageText': f'{name}의 위치'
                    },
                    {
                    'label': '운영시간',
                    'action': 'message',
                    'messageText': f'{name}의 운영시간'
                    },
                    ]
                }
            }) 


# 세부정보 - 대답
@csrf_exempt
def ans(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    idx = return_str.index('의')
    name = return_str[:idx]
    name_idx = df.index[(df['name'] == name)]
    info = return_str[idx+2:]

    if info == '비도서자료수':
        col1 = int(df.loc[name_idx]['시청각자료(점)'])
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': f"{name}의 시청각자료는 총 {col1}점입니다."
                    }
                }],
                'quickReplies': [{
                    'label': '전자자료수',
                    'action': 'message',
                    'messageText': f'{name}의 전자자료수'
                    },
                    {
                    'label': '장애인용 특수자료',
                    'action': 'message',
                    'messageText': f'{name}의 장애인용 특수자료'
                    },
                    {
                    'label': '좌석수',
                    'action': 'message',
                    'messageText': f'{name}의 좌석수'
                    },
                    {
                    'label': '전자시스템 현황',
                    'action': 'message',
                    'messageText': f'{name}의 전자시스템 현황'
                    },
                    {
                    'label': '위치',
                    'action': 'message',
                    'messageText': f'{name}의 위치'
                    },
                    {
                    'label': '운영시간',
                    'action': 'message',
                    'messageText': f'{name}의 운영시간'
                    },
                    {
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                    }
                    ]
                } 
            })

    elif info == '전자자료수':
        col2 = int(df.loc[name_idx]['전자저널(종)'])
        col3 = int(df.loc[name_idx]['전자도서(종)'])
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': f"{name}의 전자저널은 총 {col2}종이고,\n전자도서는 총 {col3}종입니다."
                    }
                }],
                'quickReplies': [{
                    'label': '비도서자료수',
                    'action': 'message',
                    'messageText': f'{name}의 비도서자료수'
                    },
                    {
                    'label': '장애인용 특수자료',
                    'action': 'message',
                    'messageText': f'{name}의 장애인용 특수자료'
                    },
                    {
                    'label': '좌석수',
                    'action': 'message',
                    'messageText': f'{name}의 좌석수'
                    },
                    {
                    'label': '전자시스템 현황',
                    'action': 'message',
                    'messageText': f'{name}의 전자시스템 현황'
                    },
                    {
                    'label': '위치',
                    'action': 'message',
                    'messageText': f'{name}의 위치'
                    },
                    {
                    'label': '운영시간',
                    'action': 'message',
                    'messageText': f'{name}의 운영시간'
                    },
                    {
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                    }
                    ]
                } 
            })

    elif info == '장애인용 특수자료':
        col4 = int(df.loc[name_idx]['인쇄용 자료'])
        col5 = int(df.loc[name_idx]['비도서'])
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': f"{name}의 인쇄용 자료는 총 {col4}개이고,\n비도서 자료는 총 {col5}개입니다."
                    }
                }],
                'quickReplies': [{
                    'label': '비도서자료수',
                    'action': 'message',
                    'messageText': f'{name}의 비도서자료수'
                    },
                    {
                    'label': '전자자료수',
                    'action': 'message',
                    'messageText': f'{name}의 전자자료수'
                    },
                    {
                    'label': '좌석수',
                    'action': 'message',
                    'messageText': f'{name}의 좌석수'
                    },
                    {
                    'label': '전자시스템 현황',
                    'action': 'message',
                    'messageText': f'{name}의 전자시스템 현황'
                    },
                    {
                    'label': '위치',
                    'action': 'message',
                    'messageText': f'{name}의 위치'
                    },
                    {
                    'label': '운영시간',
                    'action': 'message',
                    'messageText': f'{name}의 운영시간'
                    },
                    {
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                    }]
                } 
            })

    elif info == '좌석수':
        col6 = int(df.loc[name_idx]['총 좌석 수(석)'])
        col7 = int(df.loc[name_idx]['노인 및 장애인 열람석(석)'])
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': f"{name}의 좌석 수는 총 {col6}석이고,\n노인 및 장애인 열람석은 총 {col7}석입니다."
                    }
                }],
                'quickReplies': [{
                    'label': '비도서자료수',
                    'action': 'message',
                    'messageText': f'{name}의 비도서자료수'
                    },
                    {
                    'label': '전자자료수',
                    'action': 'message',
                    'messageText': f'{name}의 전자자료수'
                    },
                    {
                    'label': '장애인용 특수자료',
                    'action': 'message',
                    'messageText': f'{name}의 장애인용 특수자료'
                    },
                    {
                    'label': '전자시스템 현황',
                    'action': 'message',
                    'messageText': f'{name}의 전자시스템 현황'
                    },
                    {
                    'label': '위치',
                    'action': 'message',
                    'messageText': f'{name}의 위치'
                    },
                    {
                    'label': '운영시간',
                    'action': 'message',
                    'messageText': f'{name}의 운영시간'
                    },
                    {
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                    }
                    ]
                } 
            })

    elif info == '전자시스템 현황':
        col8 = int(df.loc[name_idx]['이용자용 컴퓨터 수(대)'])
        col9 = int(df.loc[name_idx]['무인자동대출/반납기(대)'])
        col10 = str(df['모바일도서관 서비스 유무'].values[name_idx])[2]
        if col10 == '유':
            col10 = '가능'
        elif col10 == '무':
            col10 = '불가능'

        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': f"{name}의 이용자용 컴퓨터 수는 총 {col8}대,\n무인자동대출과 반납기는 총 {col9}대이며,\n모바일도서관 서비스는 {col10}합니다."
                    }
                }],
                'quickReplies': [{
                    'label': '비도서자료수',
                    'action': 'message',
                    'messageText': f'{name}의 비도서자료수'
                    },
                    {
                    'label': '전자자료수',
                    'action': 'message',
                    'messageText': f'{name}의 전자자료수'
                    },
                    {
                    'label': '장애인용 특수자료',
                    'action': 'message',
                    'messageText': f'{name}의 장애인용 특수자료'
                    },
                    {
                    'label': '좌석수',
                    'action': 'message',
                    'messageText': f'{name}의 좌석수'
                    },
                    {
                    'label': '전자시스템 현황',
                    'action': 'message',
                    'messageText': f'{name}의 전자시스템 현황'
                    },
                    {
                    'label': '위치',
                    'action': 'message',
                    'messageText': f'{name}의 위치'
                    },
                    {
                    'label': '운영시간',
                    'action': 'message',
                    'messageText': f'{name}의 운영시간'
                    },
                    {
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                    }]
                } 
            })

    elif info == '운영시간':
        col11 = str(df['이용시간'].values[name_idx])[2:-2]

        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': f"{col11}입니다."
                    }
                }],
                'quickReplies': [{
                    'label': '비도서자료수',
                    'action': 'message',
                    'messageText': f'{name}의 비도서자료수'
                    },
                    {
                    'label': '전자자료수',
                    'action': 'message',
                    'messageText': f'{name}의 전자자료수'
                    },
                    {
                    'label': '장애인용 특수자료',
                    'action': 'message',
                    'messageText': f'{name}의 장애인용 특수자료'
                    },
                    {
                    'label': '좌석수',
                    'action': 'message',
                    'messageText': f'{name}의 좌석수'
                    },
                    {
                    'label': '전자시스템 현황',
                    'action': 'message',
                    'messageText': f'{name}의 전자시스템 현황'
                    },
                    {
                    'label': '위치',
                    'action': 'message',
                    'messageText': f'{name}의 위치'
                    },
                    {
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                    }],
                } 
            })


# Kakao API 지도 
@csrf_exempt
def showmap(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']
    idx = return_str.index('의')
    name = return_str[:idx]
    info = return_str[idx+2:]
    params = {"query": f"{name}"}
    url = "https://dapi.kakao.com/v2/local/search/keyword.json?"
    apikey = ""
    headers = {"Authorization": f"KakaoAK {apikey}"}
    res = requests.get(url, headers=headers, params=params)
    document = json.loads(res.text)
    
    lib_id = document['documents'][0]['id']
    if info == '위치':
        goal_url = f'https://map.kakao.com/link/map/{lib_id}'
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': f"{goal_url}"
                    }
                }],
                'quickReplies': [{
                    'label': '비도서자료수',
                    'action': 'message',
                    'messageText': f'{name}의 비도서자료수'
                    },
                    {
                    'label': '전자자료수',
                    'action': 'message',
                    'messageText': f'{name}의 전자자료수'
                    },
                    {
                    'label': '장애인용 특수자료',
                    'action': 'message',
                    'messageText': f'{name}의 장애인용 특수자료'
                    },
                    {
                    'label': '좌석수',
                    'action': 'message',
                    'messageText': f'{name}의 좌석수'
                    },
                    {
                    'label': '전자시스템 현황',
                    'action': 'message',
                    'messageText': f'{name}의 전자시스템 현황'
                    },
                    {
                    'label': '운영시간',
                    'action': 'message',
                    'messageText': f'{name}의 운영시간'
                    },
                    {
                    'label': '처음으로',
                    'action': 'message',
                    'messageText': '처음으로'
                    },
                    ]
                }
            })
