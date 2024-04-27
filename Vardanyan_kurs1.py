import tkinter as tk
import calendar
import datetime


#
def back():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    data()


#
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
        days[i + week_days]['text'] = i + 1
        days[i + week_days]['fg'] = 'White'
        if year == now.year and month == now.month and i == now.day:
            days[i + week_days - 1]['bg'] = 'Grey50'
            days[i + week_days]['bg'] = 'Black'
        else:
            days[i + week_days]['bg'] = 'Black'
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
window.geometry('1100x600')
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
    #lbl_nedel.grid(row=1, column=i, sticky=NSEW)
    lbl_nedel.place(relx=(i * 0.1) + 0.15, rely=0.15, relheight=0.05, relwidth=0.05)

# Каждый день
for row in range(6):
    for col in range(7):
        lbl_day = tk.Label(window, text='0', height=1, width=1, font=(1, 14), bg="Grey")
        #lbl_day.grid(row=row+2, column=col, sticky=NSEW)
        lbl_day.place(rely=(row*0.1) + 0.25, relx=(col * 0.1) + 0.15, relheight=0.05, relwidth=0.05)
        days.append(lbl_day)

# Вызов функции
data()

# Закроется только при выходе
window.mainloop()