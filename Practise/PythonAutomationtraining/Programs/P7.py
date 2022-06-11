"""
Given:-
-------
alst = ["blr","chn","mum","tpuram","blr","blr","chn","hyd","blr"]

Expected:-
-----------
unique values in the lst are = ["mum", "tpuram","hyd"]
duplicates                   = ["blr","chn"]
"""
alst = ["blr","chn","mum","tpuram","blr","blr","chn","hyd","blr"]

unique = []
duplicates = []
for a in alst:
    if alst.count(a) > 1:
        if a not in duplicates:
            duplicates.append(a)
    else:
        unique.append(a)

print(unique)
print(duplicates)