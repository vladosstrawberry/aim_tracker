import json


class App:
    arrr = list()

    def __init__(self, file):
        """Open json data and add to list"""
        with open(file, 'r') as json_file:
            self.array = json.load(json_file)

    def run():
        while(True):
            print("1. Print all aims")
            print("2. ...")
            print("5. exit")
            answer = input()
            if(answer == 1):
                pass
            if(answer == 2):
                pass
            if(answer == 5):
                break

    def change_aim(self):
        aim_input = -1
        while(True):
            aim = 0
            for mainAim, subAim in self.array.items():
                print(str(aim) + ". " + mainAim)
                aim += 1
            if(aim != 0):
                while(aim < aim_input < 0 or aim_input != -100):
                    print("1What to change? if you want to exit press -100 ")
                    aim_input = int(input())
                if(aim_input == -100):
                    break
                elif(aim_input != -100):
                    aim_input_check = 0
                    for mainAim, subAim in self.array.items():
                        if(aim_input_check == aim_input):
                            while(True):
                                aim = 0
                                aim_input = -1
                                for subAim, task in self.array[mainAim].items():
                                    print(str(aim) + ". " + subAim)
                                    aim += 1
                                while((0 < aim_input and aim_input < (aim + 1)) or aim_input != -100):
                                    print("2What to change? if you want to exit press -100 ")
                                    aim_input = int(input())
                                if(aim_input == -100):
                                    break
                                else:
                                    aim_input_check = 0
                                    for subAim, task in self.array[mainAim].items():
                                        if(aim_input_check == aim_input):
                                            while(True):
                                                aim = 0
                                                aim_input = -1
                                                for task, description in self.array[mainAim][subAim].items():
                                                    print(str(aim) + ". " + task)
                                                    aim += 1
                                                while(0 < aim_input < aim or aim_input != -100):
                                                    print(
                                                        "3What to change? if you want to exit press -100 ")
                                                    aim_input = input()
                                                if(aim_input == -100):
                                                    break
                                                else:
                                                    aim_input_check = 0
                                                    for task, description in self.array[mainAim][subAim].items():
                                                        if(aim_input_check == aim_input):
                                                            task = "new_task"
                                                            description = "New_descr"
                                                        print(task + " .... " + description)
                                                        aim_input_check += 1
                                        aim_input_check += 1
                        aim_input_check += 1
            else:
                print("No Aims")
                break

    def display_aims(self):
        w = 0
        for i, j in self.array.items():
            for j, v in self.array[i].items():
                print(str(w) + ". " + j)
                for v, n in self.array["MainAim"][j].items():
                    result = str(v) + " then " + str(n)
                    print(result)
                w += 1

    def add_aims():
        pass


if __name__ == '__main__':
    Ap = App("new.json")
    Ap.display_aims()
    Ap.change_aim()
    Ap.display_aims()
