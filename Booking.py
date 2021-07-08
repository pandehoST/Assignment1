class Booking:
    def __init__(self, id, packageName, custName, checkInDate, phoneNum, discount):
        self.__id = id
        self.__packageName = packageName
        self.__custName = custName
        self.__checkInDate = checkInDate
        self.__phoneNum = phoneNum
        self.__discount = discount

    def get_id(self):
        return self.__id

    def get_packageName(self):
        return self.__packageName

    def get_custName(self):
        return self.__custName

    def get_checkInDate(self):
        return self.__checkInDate

    def get_phoneNum(self):
        return self.__phoneNum

    def get_discount(self):
        return self.__discount

    def set_id(self, id):
        self.__id = id

    def set_packageName(self, packageName):
        self.__packageName = packageName

    def set_custName(self, custName):
        self.__custName = custName

    def set_checkInDate(self, checkInDate):
        self.__checkInDate = checkInDate

    def set_phoneNum(self, phoneNum):
        self.__phoneNum = phoneNum

    def set_discount(self, discount):
        self.__discount = discount

    def __str__(self):
        return 'Index: {}, Package Name: {}, Customer Name: {}, Check-In: {}, Phone No.:{}, Discount(%) :{}'.format(self.__id, self.__packageName, self.__custName, self.__checkInDate, self.__phoneNum, self.__discount)
