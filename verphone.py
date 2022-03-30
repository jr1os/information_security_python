import phonenumbers

from phonenumbers import geocoder, carrier


phone = input('Insert phone number with form +551140028922: ')

phone_num = phonenumbers.parse(phone)
carrier_phone = carrier.name_for_number(phone_num, 'pt')

print(geocoder.description_for_number(phone_num, 'pt'))
print(carrier_phone)
