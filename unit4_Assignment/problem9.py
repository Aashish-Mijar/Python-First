# 9. Create a class PinLocker with a private variable __pin. Add methods to view and change the pin. Try to access the pin directly and show the error. 

class PinLocker:
    def __init__(self, pin):
        self.__pin = pin

    def view_pin(self):
        print("Current PIN:", self.__pin)

    def change_pin(self, new_pin):
        self.__pin = new_pin
        print("PIN changed successfully.")

locker = PinLocker(1234)
locker.view_pin()
locker.change_pin(5678)
locker.view_pin()
print(locker.__pin)
