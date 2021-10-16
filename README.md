# GIS Spatial Analysis and Policy Recommendations for Disabled

![수상](https://user-images.githubusercontent.com/87461728/137341169-df8a09d7-50c8-43ab-a495-f6f2dbc990da.jpg)

`🏆제 3회 대구 빅데이터 분석 경진대회 대상`  `🥇공공부분 1위`  `#대구디지털산업진흥원`  `#대구은행`  `#Flower팀`

## Introduction

Notification: [link](https://www.dip.or.kr/home/notice/boardRead.ubs?sfpsize=20&sfcategory=&fboardcd=notice&sfclassification=&sfkind=&sfsearch=ftitle&sfkeyword=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0+%EB%B6%84%EC%84%9D+%EA%B2%BD%EC%A7%84%EB%8C%80%ED%9A%8C&fboardnum=5066&sfpage=1)

주제: 지식정보취약계층의 도서관 문화 재정립

* 공공도서관 편의시설 개선
  * 우선적으로 개선해야할 공공도서관 도출
  * [Visualization -1](https://app.powerbi.com/view?r=eyJrIjoiMzc0ZjAxMzQtNDBiMy00OTVjLTgzYWItYjY0MTFlMWU2ZGI3IiwidCI6IjE0ZjVkMzljLTA0NTQtNDcyOC05YTMxLTRhMzliZTJjZGMzOSJ9) 
* 최적 입지 제안
  * 수요자 측면과 공급자 측면을 모두 고려한 대구시 점자도서관 이전 입지 선정
  * [Visualization -2](https://app.powerbi.com/view?r=eyJrIjoiNTE1ZDdhY2MtZDYzZC00ZTAyLTg5ZDItMzM2ZTA3MzI1OGM0IiwidCI6IjE0ZjVkMzljLTA0NTQtNDcyOC05YTMxLTRhMzliZTJjZGMzOSJ9&pageName=ReportSection)
* 챗봇 개발
  * 지식정보취약계층의 공공도서관 이용 편리성 증가

참가자: 양수영, 윤혜윤, 이미혜

대상 수상

* Article: [link](https://www.nocutnews.co.kr/news/5640010)

## Tech Stack

#### Analysis

* Python: 데이터 전처리, 군집 분석, ~~OpenRouteService API~~, OSMNX, 챗봇 개발
* Qgis: 향유도 분석, 수요예측도 분석
* Power BI: 향유도 시각화
* GEODA: 공간자기상관 분석

#### Chatbot

* Django
* Kakao Map API

#### DevOps

* Amazon EC2 Linux Ubuntu
* Apache

## Dataset

* 나드리콜 승하차 데이터
* 전국도시철도 역사정보 표준데이터
* 전국도서관 표준데이터
* 대구시 버스정류소
* 공공도서관 시설 및 설비
* 공공도서관 인적자원
* 공공도서관 장애인용 특수자료 수 / 지식정보취약계층 서비스 이용자 수
* 공공도서관 지식정보취약계층 관련 예산

## Result

![image-20211015225241048](https://user-images.githubusercontent.com/87461728/137498525-a1079fd5-15b1-4f04-88cd-435b0ada086c.png)

용산역 ~ 감산역 일대, 서부정류장역 ~ 영남대역 일대 등 대체적으로 지하철 역과 공원 인근에서 최적 입지가 선정됨

---

자세한 분석 과정 및 결과는 [presentation](https://github.com/yoonhyeyoon/Daegu-bigdata-contest/tree/main/presentation)의 분석 보고서와 pdf파일을 참고해주시길 바랍니다 :blush:
