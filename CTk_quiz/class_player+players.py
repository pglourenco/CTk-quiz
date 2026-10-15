import os

class Player:                           #1 classe Player corresponde a 1 ficheiro
    def __init__(self, name):
        self.name = name
        self.file_name_first_try = rf'C:\Users\Pedro\Desktop\python 2023 telhas\tkinter\players\#{self.name}'
        self.file_name = rf'C:\Users\Pedro\Desktop\python 2023 telhas\tkinter\players\{self.name}'
        self.points = 0

    
    def add_points(self, amount: int):
        self.points += amount

    def save_player_data_first_try(self):
        f = open(self.file_name_first_try, 'w', encoding='utf-8-sig')
        f.write(f'{self.name}, {self.points}')
        f.close()

    def save_player_data(self):
        f = open(self.file_name, 'w', encoding='utf-8-sig')
        f.write(f'{self.name}, {self.points}')
        f.close()

    def __repr__(self) -> str:
        return '(' + self.name + ', ' + str(self.points) + ')'

class Players:                          #1 classe Players corresponde à pasta players
    def __init__(self):
        self.all_first_try = ()     #tuplos para não repetir nomes
        self.all = ()

        #self.load_first_try()
        self.load()
    
    def load(self):
        file_names = []
        folder_path = rf'C:\Users\Pedro\Desktop\python 2023 telhas\tkinter\players'
        for file_name in os.listdir(folder_path):
            print(file_name)
            file_names.append(file_name)
            #f = open(str(folder_path + '\\' + file_name), 'r')
            #files.append(f)
        print(file_names)

        all_list = []
        for file_name in file_names:
            f = open(str(folder_path + '\\' + file_name), 'r', encoding='utf-8-sig')
            for line in f:
                l = line.strip().split(', ')
                p = Player(l[0])
            all_list.append(p)
            f.close()
        self.all = tuple(all_list)

ps = Players()
print(ps.all)