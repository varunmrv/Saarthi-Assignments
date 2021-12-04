dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]
a=dict()
for i in dict_list:
    j=frozenset(i.items())
    if j in a.keys():
        a[j]+=1
    else:
        a[j]=1
res=[]
for k in a:
    l=dict(k)
    res.append(l)
print(res)
