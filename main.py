import json

class Laptop:
    """Это класс Ноутбук"""
    # Способ создания объекта (конструктор)
    def __init__(self, id, os, ddr, ssd, proc, color, dysplay):
        self.id = id
        self.os = os
        self.ddr = ddr
        self.ssd = ssd
        self.proc = proc
        self.color = color
        self.dysplay = dysplay

    def __str__(self):
        s_str = f' Id: {Laptop.format_text(self.id)}\n ' \
                f'Операционная система: {Laptop.format_text(self.os)}\n ' \
                f'Оперативная память: {Laptop.format_text(self.ddr)} GB\n ' \
                f'Размер диска: {Laptop.format_text(self.ssd)} GB\n ' \
                f'Процессор: {Laptop.format_text(self.proc)} \n ' \
                f'Цвет: {Laptop.format_text(self.color)}\n ' \
                f'Диагональ: {Laptop.format_text(self.dysplay)} дюймов'
        return s_str

    def format_text(f):
        buf = '\033'+'[33m'+'{}'+'\033[0m'
        return buf.format(f)

class Laptop_filter(Laptop):
    def __int__(self, id, os, ddr, ssd, proc, color, dysplay):
        super().__init__(id, os, ddr, ssd, proc, color, dysplay)

    def name_os(self, uslov):
        buf = '\033' + '[33m' + '{}' + '\033[0m'
        if self.os == uslov:
            # return f'Id ноутбука:{buf.format(self.id)}, оперативная память: {buf.format(self.ddr)}' # 1 вариант вывода
            return f'{Laptop_filter(self.id, self.os, self.ddr, self.ssd, self.proc, self.color, self.dysplay)}' # 2 вариант вывода
    def name_ddr(self, uslov):
        buf = '\033' + '[33m' + '{}' + '\033[0m'
        try:
            if int(self.ddr) >= int(uslov):
                # return f'Id ноутбука:{buf.format(self.id)}, оперативная память: {buf.format(self.ddr)}' # 1 вариант вывода
                return f'{Laptop_filter(self.id, self.os, self.ddr, self.ssd, self.proc, self.color, self.dysplay)}' # 2 вариант вывода
        except: return  -1
    def name_ssd(self, uslov):
        try:
            if int(self.ssd) >= int(uslov):
                return f'{Laptop_filter(self.id, self.os, self.ddr, self.ssd, self.proc, self.color, self.dysplay)}' # 2 вариант вывода
        except: return  -1
    def name_color(self, uslov):
        if self.color == uslov:
            return f'{Laptop_filter(self.id, self.os, self.ddr, self.ssd, self.proc, self.color, self.dysplay)}' # 2 вариант вывода
    def name_diagn(self, uslov):
        try:
            if int(self.dysplay) >= int(uslov):
                return f'{Laptop_filter(self.id, self.os, self.ddr, self.ssd, self.proc, self.color, self.dysplay)}' # 2 вариант вывода
        except: return  -1

def o_f():
    with open("data_laptop.json", "r") as file:
        json_dump = json.load(file)
    return json_dump

def start(param, uslov):
    # param = [1, 2, 3, 4, 5] выборка
    for i in o_f():
        lapto = Laptop_filter(i, o_f()[i][0], o_f()[i][1], o_f()[i][2], o_f()[i][3], o_f()[i][4], o_f()[i][5])
        dictt = {"1": lapto.name_ddr(uslov), "2": lapto.name_ssd(uslov), "3": lapto.name_diagn(uslov), "4": lapto.name_os(uslov), "5": lapto.name_color(uslov)}
        result = dictt[param]
        if result != None:
            print("------------------------------------------------------------")
            print(result)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(Laptop("1", "RedOs", 4, 500, "i3", "Пурпурный", "17"))   #Образец
    while True:
        nabor = {"1": 'оперативной памяти.',
                 "2": 'объему жесткого диска.',
                 "3": 'диагонали дисплея.',
                 "4": 'операционной системе.',
                 "5": 'цвету.', }
        print('\n Активирован фильтр ноутбуков.\n<<< Список критериев отбора:\n'
              '1 - ОЗУ\n'
              '2 - Объем жесткого диска\n'
              '3 - Диагональ дисплея\n'
              '4 - Операционная система\n'
              '5 - Цвет\n'
              'q - Выход из программы. >>')

        param = input('Введите необходимый критерий отбора: ')
        if param in ["1", "2", "3", "4", "5"]:
            print(f'Вы выбрали фильтр по {nabor[param]}')
            uslov = input('Теперь введите минимальное значение критерия: ')
            start(param, uslov)
        elif param != "q":
            print('Введен неверный параметр!')
        else: break








