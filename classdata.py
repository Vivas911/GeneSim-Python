from random import *            #ъъъъъъ, я не понимааааюююю :((((
class Cell():
    def __init__(self, gen):
        self.gen = gen

    def givbir(self):    #give birth - родить
        mutate = randint(1,10) <= 4
        if mutate and self.gen in range(2,10):
            return Cell(self.gen + choice([1,-1]))
        elif mutate and self.gen == 1:
            return Cell(self.gen + 1)
        else:
            return Cell(self.gen)

class Simulation():
    def __init__(self, cells):
        self.cells = []
        for i in range(cells):
            self.cells.append(Cell(1))
            
    def maxcell(self):
        maxgen = 1
        for cell in self.cells:
            if maxgen < cell.gen:
                maxgen = cell.gen
        return maxgen

    def table(self):
        gene_table = [0,0,0,0,0,0,0,0,0,0]
        for cell in self.cells:
            gene_table[cell.gen-1] += 1
        print("Ген\tКоличество клеток")
        for level, count in enumerate(gene_table):
            print(f"{level+1}\t{count}")

    def printdata(self):
        if len(self.cells) < 3000:
            print(f"Количество клеток - {len(self.cells)}")
        else:
            print(f"Количество клеток - {len(self.cells)} (максимум)")
        sumgen = 0
        for cell in self.cells:
            sumgen += cell.gen
        print(f"Средний ген клеток - {sumgen/len(self.cells)}")
        print(f"Максимальный ген у клетки - {self.maxcell()}")

    def step(self):
        newcells = []
        for cell in self.cells:
            for move in range(10-(cell.gen-1)):
                if randint(1,10) <= cell.gen:
                    if len(newcells) < 3000:
                        newcells.append(cell.givbir())
                        
        self.cells = newcells
