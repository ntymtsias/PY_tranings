data = [1, 55, 101, 44, 106 , 199, 109, 
        114, 166, 155, 199, 223, 144, 156 ]
print(data)

min_value = 100
max_value = 200

# print(len(data))
# for index in range(len(data)-1, -1,-1):
#     if data[index] < min_value or data[index] > max_value:
#         del data[index]

# print(data) 
    
top_idx = len(data) - 1
for idx, data_value in enumerate(reversed(data)):
    if data_value < min_value or data_value > max_value:
        del data[top_idx - idx]
print(data)