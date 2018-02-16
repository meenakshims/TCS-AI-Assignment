import pandas as pd
import matplotlib.pyplot as plt

ign=pd.read_csv("ign/ign.csv")
igns=pd.read_csv("ign/ign_score.csv")

#1.
merge=pd.merge(ign,igns,on='id',left_index=True,right_index=True)
for col in merge:
    if 'Unnamed' in col:
        del merge[col]
print(merge)
#merge.to_csv('merge.csv')

#2.
sort=igns.sort_values(by=['score'],ascending=False)
sort=sort[:10]	
print(sort['title'])

#3.
#igns['avg_rating']=igns.groupby(by=['title']).mean()
#sort1=igns.sort_values(by=['avg_rating'],ascending=True)
#print(igns)


#4.
genre=igns.groupby(igns['genre'])
plt.hist('genre',20)
plt.show()





