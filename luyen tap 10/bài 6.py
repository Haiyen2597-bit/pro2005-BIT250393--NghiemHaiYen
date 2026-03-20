
s = input("Nhập chuỗi: ")

reversed_s = ""

for i in range(len(s)-1, -1, -1):
    reversed_s += s[i]

print("Chuỗi đảo ngược:", reversed_s)
