import  copy

values = [2,3,5,7,11,'13',17,19,23,29]
transformation = lambda values: values
transformed_values = list(map(transformation,values))

if values==transformed_values:
    print("Ok")
else:
    print("fail")

print(transformed_values)