# Hackphaistus : 눈 관상을 통한 사용자 능력치 분석 서비스

Hackphaistus🔥는 사용자의 관상을 분석하여, 능력치를 제시해주는 서비스입니다.<br/>
관상이라는 정적인 소재에 사용자의 능력치 분석이라는 컨셉을 추가하여, 트렌디하면서도 색다른 경험을 제공합니다.<br/>
해당 서비스를 통해 나의 사진을 넣고, 능력치를 확인하며 즐거움을 느껴보세요.


<img width="1680" alt="스크린샷 2022-01-26 오후 2 17 02" src="https://user-images.githubusercontent.com/85851785/151108007-b8cc7e74-6c06-4bd1-bf9a-a78a4dcc9ff2.png">

![ezgif com-gif-maker-2](https://user-images.githubusercontent.com/85851785/151111264-cc95fad6-2b38-4f52-bdf2-795bb45d11b7.gif)




## Features
![대지 1](https://user-images.githubusercontent.com/85851785/151108783-b4fffffb-fed3-4141-891c-72a88e6cac74.png)




## Design Prototype
[Figma Prototype](https://www.figma.com/file/PS2Uh2ZoxMXotOkz6aZg1w/Hackphaistus-Prototype?node-id=0%3A1)




### Tech Stack
```
Frontend : React
WSGI : Gunicorn
Web Server : Nginx
Backend : Flask 
AI : Flask / dlib / OpenCV /  Pytorch 
Database : MySQL, S3 Bucket
API Documentation : Swagger
Etc : RabbitMQ (Queue), Docker, AWS
```

|         Frontend         |      Backend      |         etc          |
| :----------------------: | :---------------: | :------------------: |
| ![React](https://img.shields.io/badge/React-v17.0.2-20232A?style=flat&logo=react&logoColor=61DAFB) ![JavaScript](https://img.shields.io/badge/javascript-ES6+-%23323330.svg?style=flat&logo=javascript&logoColor=%23F7DF1E) ![NPM](https://img.shields.io/badge/NPM-v6.14.14-%23000000.svg?style=flat&logo=npm&logoColor=white) | ![Flask](https://img.shields.io/badge/flask-v2.0.2-green?logo=flask) ![Python](https://img.shields.io/badge/python-v3.8.8-3670A0?style=flat&logo=python&logoColor=ffdd54) ![Swagger](https://img.shields.io/badge/Swagger-v2.9.2-%23Clojure?style=flat&logo=swagger) ![Gunicorn](https://img.shields.io/badge/gunicorn-v20.1.0-darkgreen?logo=gunicorn) ![RabbitMQ](https://img.shields.io/badge/rabbitmq-v3.9.13-orange?logo=rabbitmq) ![OpenCV](https://img.shields.io/badge/opencv-v4.5.5.62-%23white.svg?style=flat&logo=opencv) ![PyTorch](https://img.shields.io/badge/PyTorch-v1.10.1-%23EE4C2C.svg?style=flat&logo=PyTorche) ![MySQL](https://img.shields.io/badge/mysql-v8.0.27-%2300f.svg?style=flat&logo=mysql) | ![Docker](https://img.shields.io/badge/docker-v20.10.22-%230db7ed.svg?style=flat&logo=docker) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=flat&logo=amazon-aws) ![AmazonS3](https://img.shields.io/badge/amazons3-red?logo=amazons3) ![Nginx](https://img.shields.io/badge/Nginx-v1.20.2-brightgreen?logo=nginx) ![github](https://img.shields.io/badge/github-gray?logo=github) ![VScode](https://img.shields.io/badge/VScode-v1.52.1-blue?logo=visual-studio-code) [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Naereen/badges)|


### Used Model
[Face Alignment](https://github.com/davisking/dlib) from Dlib library


### System Architecture
![0125_System Architecture](https://user-images.githubusercontent.com/85851785/151111455-73adc106-d221-4038-80dc-494793eb7bbc.png)




## Initialization
* Clone the repository
```
$ git clone https://github.com/SiliconValleyInternship-2A22/Hackphaistus.git <br/>
$ cd Hackphaistus
```

#### Docker
* docker compose build and up
```
$ cd Hackphaistus <br/>
$ docker-compose up --build
```




## Detail Introduction of the Service 
* [Presentation Documentation]()
* [Design Doc](https://bouncy-tuck-1ec.notion.site/Read-me-566537ed671845d68302e3feb7134329)
* [Flagly](https:flagly.org/courses/328/)







## ✏️TEAM _ 2A22
  
  2022 Silicon Valley Winter Online Internship Program - Team A '2A22'
  
  |👩‍💻 Seoyeong Kim|👩‍🎨 Su-A Jang|🕵️‍ Dayeon Hong|
|:------:|:------:|:------:|
|**[@ksy990628](https://github.com/ksy990628)**|**[@su-aJ815](https://github.com/su-aJ815)**|**[@Dayeon-Hong](https://github.com/Dayeon-Hong)**|
