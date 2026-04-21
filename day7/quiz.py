# 1번
# import pandas as pd
# s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
# print(s['c'])
# 2번
# import pandas as pd
# data = {'name': ['Alice', 'Bob', 'Charlie'],
#         'age': [25, 30, 35],
#         'score': [90, 85, 92]}
# df = pd.DataFrame(data)
# print(df.shape, len(df))
# # 3번
# import pandas as pd
# data={
#     '이름':['김철수','이영희','박지수'],
#     '국어'  : [85, 92, 78],
#     '영어'  : [90, 88, 95],
#     '수학'  : [80, 75, 88]
# }
# df=pd.DataFrame(data)
# print(df.head(2))
# # 4번
# import pandas as pd
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]},
#                   index=['x', 'y', 'z'])
# print(df.loc['y', 'B'], df.iloc[2, 0])
# 5번
# 2 ['Lee','Choi']
# import pandas as pd
# df = pd.DataFrame({
#     'name': ['Kim', 'Lee', 'Park', 'Choi'],
#     'score': [85, 92, 78, 95]
# })
# result = df[df['score'] >= 90]
# print(len(result), result['name'].tolist())
# # 6번
# import pandas as pd
# df=pd.DataFrame({
#     '이름'  : ['Kim', 'Lee', 'Park'],
#     '점수'  : [85, None, 92],
#     '등급'  : ['A', 'B', None]
# })
# df.fillna({'점수':0},inplace=True)
# df.fillna({'등급':0},inplace=True)
# print(df)
# # 7번
# import pandas as pd

# df = pd.DataFrame({'score': [70, 80, 90, 85, 75]})
# print(df['score'].max(), df['score'].sum(), df['score'].mean())
# # 8번
# import pandas as pd
# data={
#     '이름'  : ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
#     '부서'  : ['영업', '개발', '개발', '영업', '인사'],
#     '월급'  : [280, 350, 420, 310, 260]
# }
# df=pd.DataFrame(data)
# filtered_df=df[df['월급']>=300]
# print(filtered_df.sort_values('월급',ascending=False))
# # 9번
# import pandas as pd
# data={
#     '이름'  : ['Kim', 'Lee', 'Park', 'Choi', 'Jung'],
#     '부서'  : ['영업', '개발', '개발', '영업', '인사'],
#     '월급'  : [280, 350, 420, 310, 260]
# }
# df=pd.DataFrame(data)
# group_df=df.groupby('부서')['월급'].mean()
# print(group_df)
# # 10번
# import pandas as pd
# data_A={'학번'  : [1001, 1002, 1003, 1004],
#     '이름'  : ['김철수', '이영희', '박지수', '최민준']}

# data_B={'학번'  : [1001, 1002, 1004],
#     '국어'  : [85, 92, 78],
#     '영어'  : [90, 88, 82],
#     '수학'  : [80, 75, 95]}
# data_A=pd.DataFrame(data_A)
# data_B=pd.DataFrame(data_B)
# merged_data=data_A.merge(data_B,'left')
# merged_data=merged_data.fillna(0,inplace=True)
# merged_data['총점']=merged_data['국어']+merged_data['영어']+merged_data['수학']
# average_score=(merged_data['총점'].sum())/len(merged_data['총점'])
# filtered_data=merged_data[merged_data['총점']>=average_score]
# sorted_data=filtered_data.sort_values('이름',ascending=True)
# print(sorted_data)