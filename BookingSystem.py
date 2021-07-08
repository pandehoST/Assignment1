import Booking as bk

record_list = {(1, 'Luxe Suite Package', 'Tan Eugene', '1 May 2021', '98710221', '12%'),
               (1, 'Escape Package', 'Lim Jane', '18 Apr 2021', '90596123', '18%')}
option = 0


def display_menu():
    print()
    print("========== Staycation booking record (Package) ==========")
    print("""
            [1] - Add Record 
            [2] - Update Record
            [3] - Delete Record
            [4] - Display Record
            [5] - Sort Record
            [6] - Search Record
            [0] - Exit
                        """)

    """if choice == "a":"""

    option = input("Enter your option: ")
    return int(option)


def addRec():
    id = input("Enter Index: ")
    packageName = input("Enter Package Name: ")
    custName = input("Enter Customer Name: ")
    checkInDate = input("Enter Check-In Date: ")
    phoneNum = input("Enter Customer Phone No.: ")
    discount = input("Enter Discount (%): ")

    booking = bk.Booking(id, packageName, custName, checkInDate, phoneNum, discount)
    record_list[id] = booking


def updateRec():
    id = input('Enter Record ID To Update: ')
    if id in record_list:
        packageName = input('Enter New Package Name (Leave empty to remain unchange): ')
        custName = input('Enter New Customer Name (Leave empty to remain unchange): ')
        checkInDate = input('Enter New Check-In Date (Leave empty to remain unchange): ')
        phoneNum = input('Enter New Phone Number (Leave empty to remain unchange): ')
        discount = input('Enter New Discount (Leave empty to remain unchange): ')

        if len(packageName) > 0:
            record_list[id].set_packageName(packageName)
            print('Package Name Updated')

        if len(custName) > 0:
            record_list[id].set_custName(custName)
            print('Customer Name Updated')

        if len(checkInDate) > 0:
            record_list[id].set_checkInDate(checkInDate)
            print('Check-In Date Updated')

        if len(phoneNum) > 0:
            record_list[id].set_phoneNum(phoneNum)
            print('Phone Number Updated')

        if len(discount) > 0:
            record_list[id].set_discount(discount)
            print('Discount Updated')

    else:
        print('ID not found, try again!')


def deleteRec():
    id = input("Enter Record ID To Delete: ")
    if id in record_list:
        record_list.pop(id, None)
        print('Record ID: ', id, 'Is Deleted')
    else:
        print("ID not found, try again!")


def displayRec():
    print(record_list)


def sortRec():
    opt = input("""
            Sort By:
            [9] - Check-in Date
            [8] - Package Name      
            [7] - Discount    
            
            Choose your option: 
                        """)
    if opt == 9:
        insertionSort(record_list[3])
    elif opt == 8:
        selectionSort(record_list[1])
    elif opt == 7:
        bubbleSort(record_list[5])
    else:
        print("Invalid option.")


def insertionSort(theSeq):
    n = len(theSeq)
    for i in range(1, n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1

        theSeq[pos] = value

        print('Pass: ', i, '\t', theSeq)


def selectionSort(arr, n):
    for i in range(n):
        min_index = i
        min_str = arr[i]

        for j in range(i + 1, n):
            if min_str > arr[j]:
                min_str = arr[j]
                min_index = j

        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp


def bubbleSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                noSwap = False

    if noSwap:
        pass


def searchRec():
    opt = input("""
                Sort By:
                [d] - Check-in Date
                [c] - Customer Name    
                
                Choose your option:  
                            """)
    if opt == 'd':
        linearSearch(record_list[3])
    elif opt == 'c':
        binarySearch(record_list[2])
    else:
        print("Invalid option.")

"""
    if id in record_list:
        print(record_list[id])
"""


def linearSearch(arr, x):
    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1


def binarySearch(theValues, target):
    low = 0
    high = len(theValues) - 1
    while low <= high:
        mid = (high + low) // 2

        if theValues[mid] == target:
            return mid

        elif target < theValues[mid]:
            high = mid - 1

        else:
            low = mid - 1

    return -1


while True:
    option = display_menu()
    if option == 1:
        addRec()
    elif option == 2:
        updateRec()
    elif option == 3:
        deleteRec()
    elif option == 4:
        displayRec()
    elif option == 5:
        sortRec()
    elif option == 6:
        searchRec()
    elif option == 0:
        break
    else:
        print("Invalid option.")

