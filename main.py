from classdata import *
print("Это простая генетическая симуляция с всего\nодним параметром, тг автора: @vladimir_shtyka")

sim = Simulation(50)    #50 стартовых клеток в симуляции

while True:
    command = input("Введите инструкцию (help для помощи): ").lower()
    if command == "help":
        print("t - сделать шаг симуляции\ntt - сделать 10 шагов симуляции\nb - получить таблицу клеток (геном/количество)\nx - сбросить количество и геном клеток\nf - перезапуск симуляции и замерка шагов за которые\nклетка достигла максимального генома (10)\ne - выйти")
    elif command == "e":
        break
    elif command == "t":
        sim.step()
        sim.printdata()
    elif command == "tt":
        for i in range(10):
            sim.step()
        sim.printdata()
    elif command == "b":
        sim.table()
    elif command == "x":
        sim = Simulation(50)
        sim.printdata()
    elif command == "f":
        sim = Simulation(50)
        count = 0
        while sim.maxcell() != 10:
            sim.step()
            count += 1
        sim.printdata()
        print(f"Клетка в симуляции достигла максимального гена за {count} шагов")
    else:
        print("Неизвестная инструкция")
print("Удачи :D")
