from patient import Patient

ds = []

while True:
    print(f'''\n
    0. Thoát Chương trình
    1. Thêm bệnh nhân
    2. Cập nhật thông tin bệnh nhân
    3. Xóa bệnh nhân
    4. Xem thông tin tất cả bệnh nhân
    5. Xem Thông tin bệnh nhân
    6. Tìm bệnh nhân theo Tên
    7. Số lượng bệnh nhân
    ''')
    select = input("Mời chọn chức năng:  ")

    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            id = input("Nhập Id Bệnh nhân:  ")
            name = input("Nhập Tên Bệnh nhân:  ")
            sv = Patient(id , name)
            ds.append(sv)

        elif select == 2:
            id = input("Nhập Id Bệnh nhân bạn cần sửa :  ")
            for i in ds:
                if i.get_id() == id:
                    i.set_Name( input("Nhập vào tên mới:  ") )
                    i.show_info()

        elif select == 4:
            if len(ds) == 0:
                print("\n hiện không có Bệnh nhân . Bạn vui lòng thêm Bệnh nhân mói vào danh sách !")
            else:
                print(f"\nHiện có {len(ds)} Bệnh nhân ")
                for i in ds:
                    i.show_info()

        elif select == 3:
            id = input("Nhập Id Bệnh nhân cần xóa :  ")
            for i in ds:
                if i.get_id() == id:
                    ds.remove(i)
                    print("Bạn đã xóa Bệnh nhân thành công ")
                    continue

        elif select == 5:
            id = input("Nhập Id Bệnh nhân cần xem thông tin :  ")
            for i in ds:
                if i.get_id() == id:
                    i.show_info()
                    continue

        elif select == 6:
            ten = input("Nhập Tên Bệnh nhân cần tìm :  ")
            for i in ds:
                if i.get_Name() == ten:
                    i.show_info()

        elif select == 7:
            print(f"\nHiện có { len(ds) } Bệnh nhân \n")
    else:
        print("\nBạn phải nhập số. Vui Lòng nhập lại !")