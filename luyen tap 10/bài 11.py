

def bai1():
    print("Bạn đã chọn Bài 1")
    path = input("Nhập đường dẫn tệp nhạc: ")
    file_name = path.replace("\\", "/").split("/")[-1]
    song_name = file_name.rsplit(".", 1)[0]
    print("Tên file:", file_name)
    print("Tên bài hát:", song_name)


def bai2():
    print("Bạn đã chọn Bài 2")
    s = input("Nhập chuỗi: ")
    ch = input("Nhập ký tự cần đếm: ")
    print(f"Số lần xuất hiện ký tự '{ch}':", s.count(ch))


def bai3():
    print("Bạn đã chọn Bài 3")

    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    n = int(input("Nhập số nguyên không âm: "))
    if n < 0:
        print("Không có giai thừa cho số âm!")
    else:
        print(f"{n}! =", factorial(n))



while True:
    print("\n--- MENU ---")
    print("1. Bài 1")
    print("2. Bài 2")
    print("3. Bài 3")
    print("4. Bài 4")
    print("5. Bài 5")
    print("6. Bài 6")
    print("7. Bài 7")
    print("8. Bài 8")
    print("9. Bài 9")
    print("10. Bài 10")
    print("0. Thoát")

    choice = input("Chọn bài tập (0-10): ")

    if choice == "0":
        print("Thoát chương trình. Tạm biệt!")
        break
    elif choice == "1":
        bai1()
    elif choice == "2":
        bai2()
    elif choice == "3":
        bai3()

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
