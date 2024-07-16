import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
who = list(set([i for i in data['whoAmI']]))
one_hot = data
for im in who:
  one_hot[im] = 0
  one_hot.loc[one_hot['whoAmI'] == im, im] = 1
one_hot.drop(one_hot.columns[[0]], axis=1, inplace=True)  
print(one_hot) 