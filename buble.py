def bubble_sort(data):
    banyak_data = len(data)
    for i in range(banyak_data-1):
        for j in  range(banyak_data-1):
            if data[j] > data[j+1]:
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
    return data

data = [34, 17, 42, 29, 58, 67, 23, 88, 14, 39, 51, 2, 76, 33, 49, 85, 91, 53, 27, 70, 43, 10, 63, 6, 81, 9, 25, 48, 18, 75, 77, 1, 60, 50, 21, 37, 59, 28, 62, 19, 65, 84, 11, 30, 35, 72, 68, 12, 47, 56]

def data_acak():
    data = [34, 17, 42, 29, 58, 67, 23, 88, 14, 39, 51, 2, 76, 33, 49, 85, 91, 53, 27, 70, 43, 10, 63, 6, 81, 9, 25, 48, 18, 75, 77, 1, 60, 50, 21, 37, 59, 28, 62, 19, 65, 84, 11, 30, 35, 72, 68, 12, 47, 56]
    print("List belum di urutkan")
    print(data)


while True:
    print("Pilih opsi")
    print("1. Data yang belum diurutkan")
    print("2. Urutkan Data")
    print("3. Keluar")

    pilihan = input("Masukkan pilihan yang ingin dijalankan: ")

    if pilihan == "1":
        data_acak()
    elif pilihan == "2":
        print("Data setelah diurutkan")
        print(bubble_sort(data))
    elif pilihan == "3":
        print("Program dihentikan!")
        break
    else:
        print("Pilihan tidak valid!!!")     
