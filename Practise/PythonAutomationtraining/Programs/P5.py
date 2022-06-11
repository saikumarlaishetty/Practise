"""
Task:-
------
Given :-
--------
numlst = [1,2,3,4,5]

Expected:-
-----------
newlst = [1,0,2,0,3,0,4,0,5,0]
"""

numlst = [1,2,3,4,5]
numlst[:]= map(str,numlst)
res = ",0,".join(numlst)
res = res+",0"
print(res)
print(type(res))
print(list(map(int,res.split(","))))

"----------or-----------"
elist = []
for ele in numlst:
    elist.extend([int(ele),0])
print(elist)