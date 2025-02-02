# dictionary is unique collection of key-values pairs it is mutable i.e changes can be made
#it is unordered collection of key-value pairs

country={'India':'New Delhi',
         'USA':'Washington Dc',
         'Germany':'Berlin',
         'Japan':'Tokyo'}
print(country['India'])
print(country.keys())
print(country.values())
print(country.items())
print(country.pop('Japan'))
#print(country.clear())
country.update({'Japan':'Tokyo'})
for key,values in country.items():
    print(key,values)