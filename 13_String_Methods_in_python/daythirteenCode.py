#strings are immutable
s="munawar"
print(len(s))
print(s.upper())

a="MUNAWAR HUSSAIN"
print(a.lower())

k="MUNAWAR HUSSAIN   kamal abid     and  ali"
p=(k.strip())
print(p)

m="munaawar!!!!!!!!!!!!!  munaawar"
print(m.rstrip("!"))

r="munaawar!!!!!!!!!!!!!  munaawar"
print(r.replace("munaawar","Munu"))

sp="munaawar  !!!!!!!!!!!!  munaawar"
print(sp.split(" "))
c="capitalize"
print(c.capitalize())

center="Well come to console"
print(center)
print(center.center(50))
print(len(center))

str="munaawar  !!!!!!!!!!!!  munaawar"
print(str.count("munaawar"))

st="munaawar  !!!!!!!!!!!!  munaawar end"
print(st.endswith("end"))

f="hello every one"
print(f.find("o"))
print(f.find("m"))

ind="hello "
print(ind.index("h"))
#print(ind.index("  "))

n="hello4"
print(n.isalnum())

i="hello4"
print(i.isalpha())

l="lower"
print(l.lower())
print(c.lower())

p="hello world\n"
print(p.isprintable())

spa=" "
print(spa.isspace())

title="This is a title"
print(title.istitle())

cap="this"
print(cap.isupper())


start="starting python course"
print(start.startswith("starting"))

swap="munawar"
print(swap.swapcase())

t="i am munawar"
print(t.title())