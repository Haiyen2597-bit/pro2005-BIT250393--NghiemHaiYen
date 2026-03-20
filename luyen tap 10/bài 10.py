
strings = []
for i in range(5):
    s = input(f"Nhập chuỗi thứ {i+1}: ")
    strings.append(s)


n = len(strings)
step = 1
for i in range(n):
    for j in range(0, n-i-1):
        if len(strings[j]) < len(strings[j+1]):

            strings[j], strings[j+1] = strings[j+1], strings[j]

        print(f"Bước {step}: {strings}")
        step += 1

print("\nDanh sách sau khi sắp xếp theo độ dài giảm dần:")
print(strings)
