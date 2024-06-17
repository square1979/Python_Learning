"""
    继承：把已有类的内容提供新的类，只需关心新功能
    用法：class 类名（父类名）：
            类内容体
    如果父类中的成员中存在同名成员，左边优先级最高【成员方法同】
"""


# 单继承的使用方法
class Phone:
    IMEI = None
    producer = "Google"

    @staticmethod
    def call_by_4g():
        print("4g通话")


class Phone2022(Phone):
    face_id = "10001"  # 面部识别ID

    @staticmethod
    def call_by_5g():
        print("2022年新功能，5g通话")


# phone = Phone2022()
# print(phone.producer)
# phone.call_by_4g()
# phone.call_by_5g()


# 多继承的使用方法
class NFCReader:
    nfc_type = "第五代"
    producer = "Nike"

    @staticmethod
    def read_card():
        print("NFC读卡")

    @staticmethod
    def write_card():
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外线遥控"

    @staticmethod
    def control():
        print("红外线遥控已开启")


class MyPhone(Phone2022, NFCReader, RemoteControl):
    pass


phone = MyPhone()
phone.call_by_4g()
phone.call_by_5g()
phone.read_card()
phone.write_card()
phone.control()
