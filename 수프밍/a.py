# # cd a/b  >>> /가 없으면 상대 경로
# # cd /a/b >>> /는 절대 경로
# # / (루트)
# # ~ (홈)


# True + True 
# # true가 1로 바뀌어서(type이 바뀜) 2가 나옴

# #*****object에 따라 +(더하기)가 다르게 작용
# #set은 +이 안 됨>> dir(set)을 하면
# print(dir(set))
# #__add__가 있어야 덧셈 가능

# #자료형
# frozenset{{1,2}} #frozen set

# 10은 binary일 때 4자리
# 10만은 17자리
# 10의 100승은 333자리
# print('Bob\b\bOB')
# print(1,'A','B',sep='T')


# a=[]
# a=a.append() >> a.append는 return 값이 없으므로 none임

# import matplotlib.pyplot as plt
# import time
# a=[]
# id_a=id(a)
# b=[]
# for i in range(10):
#     t1=time.time()
#     a.append(i)
#     t2=time.time()
#     b.append(t2-t1)
#     if id(a) != id_a:
#         print('gang')
# plt.plot(a,b)
# plt.show()

# # 여기서 그래프가 들쭉 날쭉한 이유: 리스트에는 기본적으로 adress가 할당돼 있는데 할당된 adress를 다 쓰면 그때 새로 할당을 받기 떄문에 그 과정에서 시간이 조금 더 걸림

# # a = a + [3,4] vs a += [3,4]
# a = [0,1,2]
# print(f"{id(a) = }, {a = }")

# a = a + [3,4] # copy
# print(f"{id(a) = }, {a = }")

# a += [3,4] # view
# print(f"{id(a) = }, {a = }")

# # b = a.copy() vs c = copy.deepcopy(a)

# import copy

# a = [[1,2,3],[4,5,6]]
# b = a.copy() # shallow copy
# c = copy.deepcopy(a) # deep copy

# a[-1] = ["four","five","six"]
# print(f"{a = }")
# print(f"{b = }")
# print(f"{c = }")

# # my_script.py
# def my_function():
#     print("Hello from my_function!")

# if __name__ == "__main__":
#     print("Hello from __main__!")
#     my_function()

# # my_function()

import yfinance as yf
import matplotlib.pyplot as plt

# 함수 정의: 종목 코드를 받아 해당 주식의 daily return 계산
def get_daily_return(stock_symbol):
    try:
        # 종목 코드를 사용하여 주가 데이터 가져오기
        stock_data = yf.download(stock_symbol, start="2022-01-01", end="2024-04-01")
        
        # 일일 수익률 계산
        stock_data['Daily_Return'] = stock_data['Adj Close'].pct_change()
        
        return stock_data[['Adj Close', 'Daily_Return']]
    
    except Exception as e:
        print("Error occurred:", e)
        return None

# 테슬라(TSLA)와 오라클(ORCL)의 주가 데이터 및 daily return 가져오기
tesla_data = get_daily_return("TSLA")
oracle_data = get_daily_return("ORCL")

# 파일에 쓰기
def write_to_file(data, filename):
    with open(filename, 'w') as f:
        f.write(data.to_csv())

# 결과를 파일에 쓰기
write_to_file(tesla_data, "tesla_data.csv")
write_to_file(oracle_data, "oracle_data.csv")

# 그래프 그리기
def plot_stock_data(data, stock_name):
    plt.figure(figsize=(10, 6))
    data['Adj Close'].plot(label='Adj Close')
    plt.title(f"{stock_name} 주가")
    plt.xlabel('날짜')
    plt.ylabel('가격')
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{stock_name}_stock_price.png")
    plt.show()

# 테슬라 주가 그래프 그리기
plot_stock_data(tesla_data, "테슬라")

# 오라클 주가 그래프 그리기
plot_stock_data(oracle_data, "오라클")

print("그래프가 성공적으로 생성되었습니다.")
