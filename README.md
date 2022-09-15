## 소개
 생활 속 운동을 기록하고 발전하는 모습을 확인할 수 있습니다.


## 적용 기술
<img src="https://img.shields.io/badge/FastAPI 0.81.0-009688?style=flat-square&logo=FastAPI&logoColor=white"/>
<img src="https://img.shields.io/badge/Python 3.10.6-3776AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/MariaDB-003545?style=flat-square&logo=MariaDB&logoColor=white"/>


## How to use

1. 가상환경 생성
```bash
python -m venv venv
source venv/bin/activate
```

2. 구성요소 설치
```bash
pip install -r requirements.txt
```

3. config/secret.json 추가
- DB 접속 정보와 같이, 보안이 요구되는 정보를 별도 관리
- 위치는 아래 Structure 참고
- secret.json 파일 예시
```json
{
    "DB": {
        "user": "{ DB-USER-NAME }",
        "password": "{ DB-PASSWORD }",
        "host": "{ DB-HOST-IP-ADDRESS }",
        "port": { DB-PORT },
        "database": "{ DB-NAME } "
    }
}
```


## Structure

```bash
backend
├── config
│   ├── database.py
│   └── secrets.json
├── main.py
├── models
│   └── users.py
├── schemas
│   └── users.py
└── services
    └── user_service.py
```
