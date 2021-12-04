a=[]
Entities_list=["kolkata", "delhi"]
utterance_list=["How far is <> from <>", "How is the weather in <>"]
for i in (utterance_list):
    c=i.count('<>')
    for j in range(len(Entities_list)):
        m=i
        for k in range(c):
            m=m.replace("<>",Entities_list[k],1)
        a.append(m)
        n=i
        for k in reversed(range(c)):
            n=n.replace("<>",Entities_list[k],1)
        a.append(n)
 

print(list(set(a)))
