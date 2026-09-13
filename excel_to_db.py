import os

import pandas as pd
import pymysql
from dotenv import load_dotenv

load_dotenv()

# 엑셀 파일 읽기
df = pd.read_excel("sample.xlsx")
print("엑셀 데이터:")
print(df)

# DB 연결
conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = conn.cursor()

# 기존 데이터 삭제 (중복 방지)
cursor.execute("DELETE FROM employees")

# insert
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO employees (이름, 부서, 연봉, 입사년도, 성과등급)
        VALUES (%s, %s, %s, %s, %s)
    """, (row["이름"], row["부서"], row["연봉"], row["입사년도"], row["성과등급"]))

conn.commit()
conn.close()

print(f"\n총 {len(df)}건 insert 완료!")
