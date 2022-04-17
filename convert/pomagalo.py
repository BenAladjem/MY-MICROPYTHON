a = "IMEI=865456053906614&data=216,14241;222,55;210,40&345&fgh&3ed&34"
b = a.split('&')
print(b)
imei = int([x for x in b if "IMEI" in x][0].split('=')[1])
data = [x for x in b if "data" in x]
print(imei, type(imei))

print(data)