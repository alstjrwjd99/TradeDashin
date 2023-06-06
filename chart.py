import pickle
import time
import matplotlib.pyplot as plt
from stockHandle import *
import matplotlib

matplotlib.use('TkAgg')

# 주식 데이터를 로드합니다.
with open('data.pickle', 'rb') as f:
    data = pickle.load(f, encoding='utf-8')

# 초기 가격을 설정합니다.
price_list = [getPrice(data)]
time_list = [time.time()]
mxprice = 0
mnprice = 1000000000
update_interval = 15  # 업데이트 간격 (초)

# 가로선 객체를 저장할 변수를 초기화합니다.
max_line = None
min_line = None

setMaxprice = int(input("최고 가격을 입력하세요 : "))
setMinprice = int(input("최저 가격을 입력하세요 : "))


# 차트를 그리는 함수 정의
def update_chart():
    global max_line, min_line  # 전역 변수로 선언
    
    # 기존 가로선이 있을 경우 제거합니다.
    if max_line is not None:
        max_line.remove()
    if min_line is not None:
        min_line.remove()

    # 차트를 그립니다.
    plt.plot(time_list, price_list)

    max_line = plt.axhline(mxprice, color='r', linestyle='--')  # 가로축에 max 선을 그립니다
    min_line = plt.axhline(mnprice, color='b', linestyle='--')  # 가로축에 min 선을 그립니다
    plt.axhline(setMaxprice, color='k', linestyle='--')            # 최대 입력 값을 선을 그립니다.
    plt.axhline(setMinprice, color='k', linestyle='--')            # 최소 입력 값을 선을 그립니다.

    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title(data)
    plt.pause(0.02)  # 차트를 업데이트하고 잠시 멈춥니다


# 주기적으로 가격을 업데이트하고 차트를 그립니다.
while True:
    # 15초 대기
    time.sleep(update_interval)
    price = getPrice(data)
    mxprice = max(mxprice, price)
    mnprice = min(mnprice, price)

    # 가격을 업데이트하고 리스트에 추가합니다.
    price_list.append(price)
    time_list.append(time.time())

    print(price_list)
    # 차트를 업데이트합니다.
    update_chart()
