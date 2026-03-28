import datetime
def kybertime():
    nbm = 0
    now: datetime.datetime = datetime.datetime.now()
    vibor = input("Куда вы хотите переместиться? (+ для будущего, - для прошлого.): ")
    secvibor = input('Что вы хотите выбрать? (sec - для секунд, min - для минут, hour - для часов, days - для дней.): ')
    if vibor =='-':
        if secvibor =='days':
            mbn = int(input("На сколько дней вы хотите переместиться назад: "))
            kogdato = now-datetime.timedelta(days=mbn)
        elif secvibor == 'hour':
            mbn = int(input("На сколько часов вы хотите переместиться назад: "))
            kogdato = now-datetime.timedelta(hours=mbn)
        elif secvibor =='min':
            mbn = int(input("На сколько минут вы хотите переместиться назад: "))
            kogdato = now-datetime.timedelta(minutes=mbn)
        elif secvibor == 'sec':
            mbn = int(input("На сколько секунд вы хотите переместиться назад: "))
            kogdato = now-datetime.timedelta(days=mbn)
        print(kogdato)
    if vibor == '+':
        if secvibor =='days':
            nbm = int(input("На сколько дней вы хотите переместиться вперёд: "))
        kogdato = now+datetime.timedelta(days=nbm)
        if secvibor == 'hour':
            nbm = int(input("На сколько часов вы хотите переместиться вперёд: "))
            kogdato = now+datetime.timedelta(hours=nbm)
        elif secvibor =='min':
            nbm = int(input("На сколько минут вы хотите переместиться вперёд: "))
            kogdato = now+datetime.timedelta(minutes=nbm)
        elif secvibor == 'sec':
            nbm = int(input("На сколько секунд вы хотите переместиться вперёд: "))
            kogdato = now-datetime.timedelta(days=nbm)
        print(kogdato)

kybertime()