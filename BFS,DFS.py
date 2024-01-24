#!/usr/bin/env python
# coding: utf-8

# In[96]:


g={'1':['2','3'],
  '2':['4','5'],
  '3':['6','7'],
  '4':[],
  '5':[],
  '6':[],
  '7':[]}
vis=[]
k=[]
goal='3'
def bfs(vis,g,node):
    vis.append(node)
    k.append(node)
    while(k):
        m=k.pop(0)
        print(m ,end="  ")
        for i in g[m]:
            if i not in vis:
                 if goal not in vis:
                    vis.append(i)
                    k.append(i)
    if goal in vis:
        print("\n",goal,"is found")
    else:
        print("none")
    
bfs(vis,g,'1')


# In[92]:


gr={'1':['2','3'],
  '2':['4','5'],
  '3':['6','7'],
  '4':[],
  '5':[],
  '6':[],
  '7':[]}
vis=[]
goal='6'
def dfs(vis,gr,node):
    if node not in vis:
        if goal not in vis:
            vis.append(node)
            print(vis)
            for i in gr[node]:
                dfs(vis,gr,i)
dfs(vis,gr,'1')
if goal in vis:
    print("\n",goal,"is found")
else:
    print(goal,"is not found")


# In[ ]:




