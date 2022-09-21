## 소개
 생활 속 운동을 기록하고 발전하는 모습을 확인할 수 있습니다.

</br>

## 적용 기술
<div>
 <img src="https://img.shields.io/badge/Python 3.10.6-3776AB?style=flat-square&logo=Python&logoColor=white"/>
 <img src="https://img.shields.io/badge/FastAPI 0.81.0-009688?style=flat-square&logo=FastAPI&logoColor=white"/>
</div>
<div>
  <img src="https://img.shields.io/badge/MariaDB 10.7.3-003545?style=flat-square&logo=MariaDB&logoColor=white"/>
</div>
<div>
 <img src="https://img.shields.io/badge/Docker 20.10.17-2496ED?style=flat-square&logo=Docker&logoColor=white"/>
</div>

</br>

## How to use
### Docker
1. Docker, Docker-compose 설치 필요
2. project 최상단, docker-compose.yml과 동등한 위치에 .env 파일 생성
3. .env file
   ```json
   MYSQL_HOST=<host>
   MYSQL_PORT=<port>
   MYSQL_ROOT_PASSWORD=<root_password>
   MYSQL_DATABASE=<database_name>
   MYSQL_USER=<user_name>
   MYSQL_PASSWORD=<user_password>
   ```
4. Docker Compose
   ```bash
   docker-compose build
   docker-compose up -d
   ```


### Python
1. 가상환경 생성
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. 구성요소 설치
   ```bash
   pip install -r requirements.txt
   ```

3. /backend/app/config/secret.json 추가
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

4. 실행
   ```bash
   uvicorn app.main:main --reload
   ```

</br>
