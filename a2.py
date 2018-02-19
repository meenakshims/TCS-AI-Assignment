import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ign=pd.read_csv("ign/ign.csv")
igns=pd.read_csv("ign/ign_score.csv")

#1.Read and merge the dataset into single dataframe
merge=pd.merge(ign,igns,on='id',left_index=True,right_index=True)
for col in merge:
    if 'Unnamed' in col:
        del merge[col]
print(merge)
merge.to_csv('merge.csv')
print('---------------')

#2.Provide the names of 10 movies rated highest.
sort=igns.sort_values(by=['score'],ascending=False)
topten=sort[:10]	
print(topten['title'])
print('---------------')


#3.Rank the movie names by their highest average rating scores.
merge['score']=merge['score'].astype(float)
rank_1 = merge.groupby('title')[['score']].mean()
rank=rank_1['score'].rank(ascending=True)
print(rank)
print('---------------')




#5.Find the group that provides the highest average movie ratings when split into genre groups.
high_avg = merge.groupby('genre')[['score']].mean()
high_avg = high_avg.sort_values(by='score',ascending=False)
print(high_avg.head(1))
print('---------------')

#6.Provide a table with the average rating of a movie by each genre group along with the movie title.

table = pd.pivot_table(merge, values='score', index=['genre', 'title'])
print(table)

#4. Plot movie scores across each genre.
merge.hist(by="genre", column="score", figsize=(25,50),grid =True)
plt.show()




