"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""

def paper_doll(text):
    return ''.join([x*3 for x in text])

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))