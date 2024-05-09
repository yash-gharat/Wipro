file = open('sample.txt', 'w')

try:
    file.write('python is a beginer friendly language')
finally:
    file.close()

# with open('sample.txt', 'w') as file:
#     file.write('python is a awesome')
#     file.close()
    
with open('sample.txt', 'r') as file:
    data = file.read()
    print(data)
    file.close()