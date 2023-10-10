def call():
    print('calling someone i dont know')
    return 'call done'

class Phone:
    price = 26990
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'knox', 'processor']
    def call(self):
        print('calling one person')
    def send_sms(self, phone, sms):
        text = f'sending SMS to: {phone} and message: {sms}'
        return text 

my_phone = Phone()
print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(77827, 'Missy, I missed to miss you')
print(result)