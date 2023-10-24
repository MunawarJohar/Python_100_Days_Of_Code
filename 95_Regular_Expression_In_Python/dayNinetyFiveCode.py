
import re
pattern=r"[A-Z]cyclone"
text='''this is a text for Cyclone and Dyclone  and more about Ccyclone and much more.'''
matches=re,finditer(pattern,text)
for match in matches:
   print(match.span())
   print(text[match.span()[0]:match.span()[1]])
# match=re.search(pattern,text)
# print(match)