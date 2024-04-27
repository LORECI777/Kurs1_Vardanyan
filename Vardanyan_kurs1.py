import tkinter as tk
import calendar
import datetime


# Функция назад
def back():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    data()


# Функция вперед
def next():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    data()


# Отображение дней и месяца
def data():

    # Изменение текста на месяц
    lbl0['text'] = calendar.month_name[month] + ', ' + str(year)
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        b_month_days = calendar.monthrange(year - 1, 12)[1]
    else:
        b_month_days = calendar.monthrange(year, month - 1)[1]
    week_days = calendar.monthrange(year, month)[0]

    # Нынешний день
    for i in range(month_days):

        day_num = i + 1
        days[i + week_days]['text'] = day_num
        days[i + week_days]['fg'] = 'White'
        # Выделение сегодняшнего дня
        if year == now.year and month == now.month and day_num == now.day or \
            (now.day == 6 and week_days == 6) or \
            (now.day == 7 and week_days == 7):
            days[i + week_days]['bg'] = 'Grey50'
            days[i + week_days]['fg'] = 'White'
        else:
            days[i + week_days]['bg'] = 'Black'

        # Отмечаем субботу и воскресенье
        current_date = datetime.date(year, month, day_num)
        if current_date.weekday() == 5:  # Суббота
            days[i + week_days]['fg'] = 'Red'
        elif current_date.weekday() == 6:  # Воскресенье
            days[i + week_days]['fg'] = 'Red'

    # Дни прошлого месяца
    for i in range(week_days):
        days[week_days - i - 1]['text'] = b_month_days - i
        days[week_days - i - 1]['fg'] = 'Grey65'
        days[week_days - i - 1]['bg'] = 'Black'
    # Дни следующего месяца
    for i in range(6 * 7 - month_days - week_days):
        days[week_days + month_days + i]['text'] = i + 1
        days[week_days + month_days + i]['fg'] = 'Grey65'
        days[week_days + month_days + i]['bg'] = 'Black'


# Создание окна
window = tk.Tk()
window.title('Календарь дня программистов')
window.config(bg='Black')
window.geometry('1200x650')
# Список и дата
days = []
now = datetime.datetime.now()
year = now.year
month = now.month

# Кнопка назад
lbl_back = tk.Label(window, text='', bg='White')
lbl_back.place(relx=0.03, rely=0.05, relheight=0.075, relwidth=0.055)
b_butt = tk.Button(window, text='<<<', bg="Black", fg='White', command=back, cursor="hand2")
b_butt.place(relx=0.0325, rely=0.0525, relheight=0.07, relwidth=0.05)

# Кнопка вперед
lbl_next = tk.Label(window, text='', bg='White')
lbl_next.place(relx=0.92, rely=0.05, relheight=0.075, relwidth=0.055)
next_butt = tk.Button(window, text='>>>', bg="Black", fg='White', command=next, cursor="hand2")
next_butt.place(relx=0.9225, rely=0.0525, relheight=0.07, relwidth=0.05)

# Название месяца
lbl0 = tk.Label(window, text='Календарь', width=1, height=1, bg="Black", fg='White', font=(1, 17))
lbl0.place(relx=0.33, rely=0.05, relheight=0.05, relwidth=0.3)

# Дни недели
for i in range(7):
    lbl_nedel = tk.Label(window, text=calendar.day_abbr[i], height=1, width=1, font=(1, 10), bg="Black", fg='White')
    # lbl_nedel.grid(row=1, column=i, sticky=NSEW)
    lbl_nedel.place(relx=(i * 0.1) + 0.15, rely=0.15, relheight=0.05, relwidth=0.05)

# Каждый день
for row in range(6):
    for col in range(7):
        lbl_day = tk.Label(window, text='0', height=1, width=1, font=(1, 14), bg="Grey")
        # lbl_day.grid(row=row+2, column=col, sticky=NSEW)
        lbl_day.place(rely=(row*0.1) + 0.25, relx=(col * 0.1) + 0.15, relheight=0.05, relwidth=0.05)
        days.append(lbl_day)

# Вызов функции
data()


# Узнать когда будет день программиста (256 день от начала календарного года)
def programms_day():
    global year
    year_str = int(lbl_entr_day.get())

    try:
        year = int(year_str)
        if year < 0:
            print("Год должен быть положительным числом.")
            return
    except ValueError:
        print("Введите корректный год в виде числа, например 2022")
        return

    # Определение нужной даты
    programmer_day = datetime.date(year, 1, 1) + datetime.timedelta(255)

    print("День программиста в", year, "году будет", programmer_day.strftime('%d.%m.%Y'))
    lbl_program_day7 = tk.Label(window, text=f'День программиста в {year} году будет {programmer_day.strftime("%d.%m.%Y")}',
                                fg='White', bg='Black', font=(1, 13))
    lbl_program_day7.place(relx=0.01, rely=0.9, relheight=0.06, relwidth=0.5)

    data()


# Кнопка для дня программиста
lbl_program_day = tk.Label(window, text='', bg='White')
lbl_program_day.place(relx=0.725, rely=0.8475, relheight=0.06, relwidth=0.2055)
butt_program_day = tk.Button(window, text='Узнать день программиста', font=(1, 13),
                             fg='White', bg="Black", command=programms_day, cursor='hand2')
butt_program_day.place(relx=0.7278, rely=0.853, relheight=0.05, relwidth=0.2)

lbl_program_day2 = tk.Label(window,
                           text='Введите год, чтобы узнать день программиста (256 день от начала календарного года): ',
                           bg='Black', fg='White', font=(1, 13))
lbl_program_day2.place(relx=0.01, rely=0.848, relheight=0.06, relwidth=0.6)
lbl_entr_day = tk.Entry(window, bg='DarkGrey', font=(1, 14))
lbl_entr_day.place(relx=0.62, rely=0.848, relheight=0.05, relwidth=0.08)


# Закроется только при выходе
window.mainloop()