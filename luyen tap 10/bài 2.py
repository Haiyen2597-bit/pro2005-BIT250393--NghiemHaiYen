
s = input("Nhập chuỗi: ")
ch = input("Nhập ký tự cần đếm: ")
if len(ch) != 1:
    print("Vui lòng nhập đúng 1 ký tự!")
else:
    count = s.count(ch)
    print(f"Ký tự '{ch}' xuất hiện {count} lần trong chuỗi.")
