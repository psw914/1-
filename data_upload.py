import os, django, csv, sys


# 일반 파이썬앱(스크립트)에서 django ORM을 사용하려면 다음의 설정 필요
# django 환경설정 파일 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thefirst.settings")
# django settings 메모리 로딩 적용
django.setup()


from first import models #이건 꼭 django.setup() 아래에 있어야 됨
CSV_PATH = "datas/csv2022.csv"

with open(CSV_PATH,"r",encoding="utf-8") as file:
    data_rows = csv.reader(file, skipinitialspace=True)
    # 첫 번째 줄 제외
    next(data_rows, None)

    # print(list(data_rows))
    
    #공백 라인 제거
    data_rows = list(data_rows)
    
    data_rows = list(filter(None,data_rows))
    # print("후", data_rows)

    # DB 테이블에 한 레코드 씩 입력하기
    for row in data_rows:
        if row[0] != None or row[0] != "":
            # cook_name = row[0],
            # count = row[1],
            # unit_price = row[2],
            
            
            # 중복 데이터를 허용함
            # models.Foods.objects.create(
            #     cook_name = row[0],
            #     count = row[1],
            #     unit_price = row[2],
            # )

            #중복 필터링 후 업로드 하기
            models.Foods.objects.update_or_create(
                # 중복값 확인
                cook_year = row[0],
                cook_name = row[1],
                # count = count,
                # unit_price = unit_price,
                # 중복값이 없을 때

                defaults = {
                  "cook_year":row[0],
                  "cook_name":row[1],
                  "count":row[2],
                  "unit_price":row[3].replace(",",""),
                }
            )

        else:
            continue