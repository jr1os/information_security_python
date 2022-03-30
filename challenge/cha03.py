segundos = int(input())

minutos = segundos / 60

segundos = int(segundos - (minutos * 60))

horas = minutos / 60 
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))
