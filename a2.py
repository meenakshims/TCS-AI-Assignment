import pandas as pd

ign=pd.read_csv("ign/ign.csv")
igns=pd.read_csv("ign/ign_score.csv")

merge=pd.merge(ign,igns,on='id',left_index=True,right_index=True)
for col in merge:
    if 'Unnamed' in col:
        del merge[col]
print(merge)
#merge.to_csv('merge.csv')

sort=igns.sort_values(by=['score'],ascending=False)
sort=sort[:10]	
print(sort['title'])

high=ign.groupby['genre'].agg([np.average])
