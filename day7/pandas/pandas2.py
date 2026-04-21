import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
path = 'https://github.com/dongupak/DataML/raw/main/csv/'
weather_file = path + 'weather.csv'
# 1. 데이터 읽기 및 월(month) 정보 추출
weather = pd.read_csv(weather_file, encoding='CP949')
weather['month'] = pd.DatetimeIndex(weather['일시']).month
# missing_data=weather[weather['평균풍속'].isna()]
# 2. 월별 데이터를 저장할 리스트 초기화
monthly = [ None for x in range(12) ]      # 달별로 구분된 12개의 None 값
monthly_wind = [ 0 for x in range(12) ]    # 각 달의 평균 풍속(이미지상 평균기온)을 담을 리스트
# weather.fillna(weather['평균풍속'].mean(),inplace=True)
# monthly_means=weather.groupby('month').mean()
# print(monthly_means)
weather['year'] = pd.DatetimeIndex(weather['일시']).year
weather.drop('일시',axis=1,inplace=True)
yearly_means=weather.groupby('year').mean()
yearly_wind=[i for i in weather['year']]
# 반복문을 이용한 월별 데이터 분리 및 평균 계산
for i in range(12):
    # 해당 월에 맞는 데이터만 필터링
    target_month_data = weather[weather['month'] == i + 1]
    
    # numeric_only=True를 추가하여 숫자 데이터가 있는 컬럼만 평균을 계산하도록 함
    # 결과에서 ['평균기온'] 값만 추출
    monthly_wind[i] = target_month_data.mean(numeric_only=True)['평균기온']
# 2. groupby를 사용하여 연도별 평균 계산 (가장 권장되는 방식)
# numeric_only=True를 넣어 문자열 컬럼 오류 방지
yearly_means = weather.groupby('year').mean(numeric_only=True)

# 확인용 출력
print(yearly_means)

# 3. 막대 그래프 시각화
# yearly_means.index는 '연도', yearly_means['평균기온']은 해당 연도의 기온 평균값입니다.
# plt.bar(yearly_means.index, yearly_means['평균기온'], color='green')
plt.hist(weather['평균기온'], bins=1000, color='skyblue', edgecolor='black',density=True)
plt.xlabel('Year')
plt.ylabel('Average Temperature')
plt.title('Yearly Average Temperature')
plt.grid(axis='y', alpha=0.3)
plt.show()