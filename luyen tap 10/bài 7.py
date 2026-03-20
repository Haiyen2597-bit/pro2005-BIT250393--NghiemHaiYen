
password_correct = "python123"


password = ""

while password != password_correct:
    password = input("Nhập mật khẩu: ")
    if password != password_correct:
        print("Sai mật khẩu, vui lòng thử lại!")

print("Đăng nhập thành công!")
