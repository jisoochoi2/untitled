# untitled

엑셀 데이터를 읽어서 MySQL 데이터베이스에 저장하는 파이썬 스크립트입니다.

## 구성

- `excel_to_db.py` — `sample.xlsx`를 읽어 `employees` 테이블(이름, 부서, 연봉, 입사년도, 성과등급)에 insert
- `sample.xlsx`, `test.xlsx` — 예제 엑셀 데이터
- `src/Main.java` — IntelliJ 기본 템플릿 (사용 안 함)

## 실행 방법

1. 의존성 설치
   ```
   pip install pandas pymysql python-dotenv
   ```

2. `.env` 파일 생성 (git에 포함되지 않음)
   ```
   DB_HOST=localhost
   DB_PORT=3306
   DB_USER=root
   DB_PASSWORD=비밀번호
   DB_NAME=python_study
   ```

3. 스크립트 실행
   ```
   python3 excel_to_db.py
   ```
