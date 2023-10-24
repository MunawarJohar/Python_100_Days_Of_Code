# old method for f string 
letter="Hey my name is {} and I am from {} "
country="Pakistan"
name="Munawar Hussain"
print(letter.format(name,country))
print(f"Hey my name is {name} and I am from {country}.")
price=4.211231
text=f"For only {price:.2f} Dollars!"
print(text)
#for printing {{brackets}}
print(f"Hey my name is {{name}} and I am from {{country}}.")