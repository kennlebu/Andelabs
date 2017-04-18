class MobilePhone:
    def __init__(self, brand):
        self.imei = 'IEDF34343435235'
        self.brand = brand

    def getIMEIcode():
        return self.imei

    def dial():
        num =  input("Enter a number to dial: ")
        print('Dialing {} ...'.format(num))

    def receive():
        print('Receiving a call')

    def sendMessage():
        msg = input('Enter text message: ')
        num = input('Enter number of recepient: ')
        print('Sending message to {} ...')


class Samsung(MobilePhone):
    def __init__(self, brand):
        self.brand = brand
        self.imei = 'SAMS123455667'

    def getIMEIcode():
        return self.imei

    def startBluetoothConnection():
        print('Samsung bluetooth device turned on')

    def startWifiConnection():
        print('Samsung wifi turned on')

class Nokia(MobilePhone):
    def __init__(self, brand):
        self.brand = brand
        self.imei_sim1 = 'NOK1234546787800'
        self.imei_sim2 = 'NOK0976382525474'

    def getIMEIcode(sim):
        if sim == 1: return self.imei_sim1
        if sim == 2: return self.imei_sim2

    def startBluetoothConnection():
        print('Nokia bluetooth device turned on')

    def sendMessage():
        msg = input('Enter message to send: ')
        print('Sending Nokia broadcast message to your contacts')


class SamsungS5(Samsung):
    def __init__(self):
        self.brand = 'Galaxy S5'

    def readFingerprint():
        print('Authorized! Fingerprint matches')
        
