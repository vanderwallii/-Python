import json

from array import *
a=0
b=0
c=list('')
x='a'

with open('in.json','r') as q:
    a=q.read()
    data=json.loads(a)
    m=dict(data[0])
    z=m['userId']

    for i in range(len(data)):
        m=dict(data[i])
        if (z==m['userId']):
            if (m['completed']==1):
                a+=1
        else:
            d={'userId':z,
                'task_completed':a
            }
            c.append(x)
            c[b]=d
            b+=1
            a=0
            z=m['userId']
            if (m['completed']==1):
                a+=1
    d={'userId':z,
        'task_completed':a
    }

    c.append(x)
    c[b]=d            
print(c)

with open ('out.json','w') as b:
    b=json.dump(c,b,notch=3)
  
    
        
    
