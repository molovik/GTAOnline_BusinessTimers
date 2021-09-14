from tkinter import *
import time


# счетчики времени бизнеса
clock_car = 0
timer_car = False
clock_bunker = 0
timer_bunker = False
clock_coke = 0
timer_coke = False
clock_meth = 0
timer_meth = False
clock_meth = 0
timer_meth = False
clock_club = 0
timer_club = False


# сброс времени бизнеса
def reset_car1():
    global clock_car
    global timer_car
    clock_car = 1200
    if timer_car == False:
        timer_car = True
        count_car()
def reset_car2():
    global clock_car
    global timer_car
    clock_car = 1800
    if timer_car == False:
        timer_car = True
        count_car()
def reset_car3():
    global clock_car
    global timer_car
    clock_car = 2400
    if timer_car == False:
        timer_car = True
        count_car()
def reset_car4():
    global clock_car
    global timer_car
    clock_car = 3000
    if timer_car == False:
        timer_car = True
        count_car()
def reset_bunker():
    global clock_bunker
    global timer_bunker
    clock_bunker = 8400
    if timer_bunker == False:
        timer_bunker = True
        count_bunker()
def reset_coke():
    global clock_coke
    global timer_coke
    clock_coke = 7200
    if timer_coke == False:
        timer_coke = True
        count_coke()
def reset_meth():
    global clock_meth
    global timer_meth
    clock_meth = 8640
    if timer_meth == False:
        timer_meth = True
        count_meth()
def reset_club():
    global clock_club
    clock_club = 0
    if timer_club == False:
        club_clock['text']="пусто"
def start_club():
    global timer_club
    if timer_club == False:
        timer_club = True
        count_club()
def more_club():
    global clock_club
    global timer_club
    if clock_club < 72000:
        clock_club = clock_club+3600
    if timer_club == False:
        club_clock['text']=int(clock_club/720),"%"


# таймеры бизнесов
def count_car():
    global timer_car
    if timer_car == True:
        global clock_car
        if clock_car < 1:
            car_timer="готово"
        else:
            car_time_count=time.gmtime(clock_car)
            car_time_time=time.strftime("%H:%M:%S",car_time_count)
            car_timer=str(car_time_time)
        car_clock['text']=car_timer   # Или label.config (text = display)
        car_clock.after(1000, count_car) # задержка обновления таймера, в милисекундах
        clock_car -= 1
def count_bunker():
    global timer_bunker
    if timer_bunker == True:
        global clock_bunker
        if clock_bunker < 1:
            bunker_timer="пусто"
        else:
            bunker_time_count=time.gmtime(clock_bunker)
            bunker_time_time=time.strftime("%H:%M:%S",bunker_time_count)
            bunker_timer=str(bunker_time_time)
        bunker_clock['text']=bunker_timer
        bunker_clock.after(1000, count_bunker)
        clock_bunker -= 1
def count_coke():
    global timer_coke
    if timer_coke == True:
        global clock_coke
        if clock_coke < 1:
            coke_timer="пусто"
        else:
            coke_time_count=time.gmtime(clock_coke)
            coke_time_time=time.strftime("%H:%M:%S",coke_time_count)
            coke_timer=str(coke_time_time)
        coke_clock['text']=coke_timer
        coke_clock.after(1000, count_coke)
        clock_coke -= 1
def count_meth():
    global timer_meth
    if timer_meth == True:
        global clock_meth
        if clock_meth < 1:
            meth_timer="пусто"
        else:
            meth_time_count=time.gmtime(clock_meth)
            meth_time_time=time.strftime("%H:%M:%S",meth_time_count)
            meth_timer=str(meth_time_time)
        meth_clock['text']=meth_timer
        meth_clock.after(1000, count_meth)
        clock_meth -= 1
def count_club():
    global timer_club
    if timer_club == True:
        global clock_club
        if clock_club > 71999:
            club_timer="полон"
        else:
            club_timer=int(clock_club/720),"%"
        club_clock['text']=club_timer
        club_clock.after(1000, count_club)
        clock_club += 1


okno = Tk()
okno.title("GTAOnline_BusinessTimers")
okno.geometry('320x350')


# настройка элементов в окне
car_name = Label(okno, text="продажа авто", fg="black", font="Verdana 15 bold")
car_clock = Label(okno, text="готово", fg="black", font="Verdana 15 bold")
car_sell_1 = Button(okno, text='одна', width=6, command=lambda:reset_car1())
car_sell_2 = Button(okno, text='две', width=6, command=lambda:reset_car2())
car_sell_3 = Button(okno, text='три', width=6, command=lambda:reset_car3())
car_sell_4 = Button(okno, text='четыре', width=6, command=lambda:reset_car4())
bunker_name = Label(okno, text="сырье бункер", fg="black", font="Verdana 15 bold")
bunker_clock = Label(okno, text="пусто", fg="black", font="Verdana 15 bold")
bunker_suply = Button(okno, text='заполнено', width=15, command=lambda:reset_bunker())
coke_name = Label(okno, text="сырье кокаин", fg="black", font="Verdana 15 bold")
coke_clock = Label(okno, text="пусто", fg="black", font="Verdana 15 bold")
coke_suply = Button(okno, text='заполнено', width=15, command=lambda:reset_coke())
meth_name = Label(okno, text="сырье мет", fg="black", font="Verdana 15 bold")
meth_clock = Label(okno, text="пусто", fg="black", font="Verdana 15 bold")
meth_suply = Button(okno, text='заполнено', width=15, command=lambda:reset_meth())
club_name = Label(okno, text="товар в клубе", fg="black", font="Verdana 15 bold")
club_clock = Label(okno, text="пусто", fg="black", font="Verdana 15 bold")
club_sell = Button(okno, text='продать', width=15, command=lambda:reset_club())
club_start = Button(okno, text='старт', width=6, command=lambda:start_club())
club_more = Button(okno, text='+5%', width=6, command=lambda:more_club())


# настройка положения элементов в окне
car_name.place(x=10, y=0)
car_clock.place(x=200, y=0)
car_sell_1.place(x=20, y=30)
car_sell_2.place(x=80, y=30)
car_sell_3.place(x=140, y=30)
car_sell_4.place(x=200, y=30)
bunker_name.place(x=10, y=70)
bunker_clock.place(x=200, y=70)
bunker_suply.place(x=20, y=100)
coke_name.place(x=10, y=140)
coke_clock.place(x=200, y=140)
coke_suply.place(x=20, y=170)
meth_name.place(x=10, y=210)
meth_clock.place(x=200, y=210)
meth_suply.place(x=20, y=240)
club_name.place(x=10, y=280)
club_clock.place(x=200, y=280)
club_sell.place(x=20, y=310)
club_start.place(x=190, y=310)
club_more.place(x=250, y=310)


okno.mainloop()