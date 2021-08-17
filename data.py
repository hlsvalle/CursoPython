from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual)
    print(type(data_atual))
    data_atual_str = data_atual.strftime('%d/%m/%Y') #Transformando a data atual em str
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    hora_atual = time(hour=14, minute=23, second=50)
    print(hora_atual)

def trabalhando_com_datetime():
    data_viagem = datetime.now() - timedelta(days=1)
    #print(datetime.now().weekday())  # retornou 0
    print(data_viagem)
    # datahora_atual = datetime.now()
    # print((datahora_atual))
    # hora = datahora_atual.strftime('%H:%M:%S')
    # print(hora)

#def retornando_hora_cuiaba(hora_cuiaba):



if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()