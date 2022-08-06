from datetime import datetime

# 날짜 포맷팅
def date_formatting(data):
    tmp_date = data[0]
    result_date = str(datetime.today().month) + "월" + str(datetime.today().day - int(tmp_date)) + "일"
    return result_date