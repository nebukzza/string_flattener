#!/usr/bin/python3

strings= ["f541e3f0-6c56-4ead-8a35-2ab4eff598b5", "c66b99d2-525e-4ee3-a120-a2c6b14e8c25", 
          "ba75f0b7-1c13-40c8-aa77-0d708d224fc0", "bd7ea710-5a5d-48d2-9366-e0ad476ad7a9", 
          "c7c73afe-7cd5-42e5-b013-04ee95ae6991", "ab297ae7-2d3a-4388-91b6-4cdbfedb50e6", 
          "7e999ff1-bb77-4135-a46b-ce0e55de850f", "fe3e6bf5-c987-4e6c-92d0-0516f6652e09", 
          "899a527f-90a9-493b-9496-8af0511f784f", "b6e8f79f-155b-4637-bd03-ff02a9bf12a7", 
          "820ecdbb-accd-4b5c-a431-8f6aa9e13eac", "c9eb10e2-8c5a-4cb7-bf10-ebc568e6b4a9", 
          "202b7c1b-e2bc-45cb-bc1f-d2dd5b3c4fa0", "35d44cca-3ec2-4656-b770-794ef7ad7d93", 
          "b00ff852-1b52-4008-b6a2-8f8654469844", "ea8f1f27-57fa-43df-a9e0-617b6cff7601", 
          "f9361d1a-72c2-42ec-b5a2-68b0dc52c66c",]
c= 0

dic = {key: [] for key in range(16)}

for string in strings:
    c=0
    #print(string)
    for s in string[0:16]:
        #print(s)
        dic[c].append(s)
        c = c+1
        #print(c)
        #c=0
for i in range(16):
    counter = len(sorted(set(dic[i])))
    char = sorted(set(dic[i]))
    #print(char[0])
    if counter == 1:
        print(char[0], end='')
        #print(, end='')
    else:
        print('*', end='')
