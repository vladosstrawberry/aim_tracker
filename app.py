import json


class App:
    main_names = dict()

    def __init__(self, file):
        self.file = file
        try:
            with open(file, 'r') as f:
                self.main_names = json.load(f)
        except OSError:
            print("No such file, will do a new one")
            f = open(file, 'w+')
            f.close()
        print("Initialized")

    def run(self):
        run = True
        while run:
            print("1. Print all aims")                                   # display_aims()
            print("1. Print Special Aim")                                # display_aims(aim)
            print("1. Print Special SubAim of Aim")                      # display_aims(aim, sub)
            print("1. Print Special Task of SubAim of Aim")              # display_aims(aim, sub, task)
            print("1. Print non completed Tasks")
            print("2. Delete Aim")
            print("2. Delete Aim's SubAim")
            print("2. Delete Aim's SubAim's Task")
            print("3. Add an Aim")                                       # add_aim()
            print("3. Add a  SubAim")                                   # add_sub_aim()
            print("3 Add a task")                                       # add_task()
            print("4. Change an Aim")
            print("4. Change a SubAim of Aim")
            print("4. Change a task of SubAim of Aim")                  # change_task()
            print("4. Change a value of SubAm of Aim")                  # change_task_value()
            print("4. Change step by step")                             # change_step_by_step()
            print("4. Change by concrete path")                         # change_by_concrete_path()
            print("5. exit")
            answer = int(input())
            if answer == 1:
                self.display_print_menu()
            if answer == 2:
                self.display_delete_menu()
            if answer == 3:
                self.display_add_menu()
            if answer == 4:
                self.display_change_menu()
            if answer == 5:
                run = False

    def display_print_menu(self):
        run = True
        while run:
            print("1. Print all aims")  # display_aims()
            print("2. Print Special Aim")  # display_aims(aim)
            print("3. Print Special SubAim of Aim")  # display_aims(aim, sub)
            print("4. Print Special Task of SubAim of Aim")  # display_aims(aim, sub, task)
            print("5. Print non completed Tasks")
            print("6. Go back")
            answer = int(input())
            if answer == 1:
                self.display_aims()
            elif answer == 2:
                self.display_aims(main="get")
            elif answer == 3:
                self.display_aims(main="get", sub_aim="get")
            elif answer == 4:
                self.display_aims(main="get", sub_aim="get", task="get")
            elif answer == 5:
                self.display_list_to_do()
            elif answer == 6:
                run = False
            else:
                print("Enter a digit in range 1-4")

    def display_change_menu(self):
        run = True
        while run:
            print("How do you want to change everything?")
            print("1. Change an Aim")                   # change_aim_name()
            print("2. Change a SubAim of Aim")          # change_sub_aim_name()
            print("3. Change a task of SubAim of Aim")  # change_task()
            print("3. Change a value of SubAm of Aim")  # change_task_value()
            print("3. Change step by step")  # change_step_by_step()
            print("3. Change by concrete path")  # change_by_concrete_path()
            print("4. Go back")
            print("Enter in in format: 'main_aim sub_aim task'")
            print("if you don't know the task or sub_aim, fill it with None")
            answer = int(input("Answer: "))
            if answer == 1:
                self.change_aim_name()
            elif answer == 2:
                self.change_sub_aim_name()
            elif answer == 3:
                print("1. Step by step")
                print("2. by path 'main sub task'")
                print("else go back")
                answer_to_four = int(input())
                if answer_to_four == 1:
                    self.change_step_by_step()
                elif answer_to_four == 2:
                    self.change_by_concrete_path()
            elif answer == 4:
                run = False

    def display_add_menu(self):
        run = True
        while run:
            print("1. Add an Aim")
            print("2. Add a  SubAim")
            print("3. Add a task")
            print("4. Exit")
            answer = int(input())
            if answer == 1:
                self.add_aim()
            elif answer == 2:
                self.add_sub_aim()
            elif answer == 3:
                self.add_task()
            elif answer == 4:
                run = False
            else:
                print("Enter a digit in range 1-4")

    def display_delete_menu(self):
        run = True
        while run:
            print("1. Delete Aim")
            print("2. Delete Aim's SubAim")
            print("3. Delete Aim's SubAim's Task")
            print("4. Exit")
            answer = int(input())
            if answer == 1:
                self.delete_aim()
            elif answer == 2:
                self.delete_sub_aim()
            elif answer == 3:
                self.delete_task()
            elif answer == 4:
                run = False
            else:
                print("Enter a digit in range 1-4")

    def add_aim(self):
        aim_to_add = input("Enter an aim name: ")
        if aim_to_add not in self.main_names:
            self.main_names.update({aim_to_add: {}})
            self.save()
        else:
            print("Main Aim " + aim_to_add + " already exists")

    def add_sub_aim(self, main_aim=None):
        if main_aim is None:
            main_aim = self.get_main_aim()
        sub_aim_to_add = input("Enter a sub_aim name: ")
        if sub_aim_to_add not in self.main_names[main_aim]:
            self.main_names[main_aim].update({sub_aim_to_add: {}})
            self.save()
        else:
            print("Sub Aim " + sub_aim_to_add + " already exists")

    def add_task(self, main_aim=None, sub_aim=None):
        if main_aim == "None" or (main_aim not in self.main_names):
            main_aim = self.get_main_aim()
        if sub_aim  == "None" or (sub_aim not in self.main_names[main_aim]):
            sub_aim = self.get_sub_aim(main_aim)
        task_to_add = input("Enter a task to add")
        if task_to_add not in self.main_names[main_aim][sub_aim]:
            self.main_names[main_aim][sub_aim].update({task_to_add: "New"})
            self.save()
        else:
            print("Task " + task_to_add + " already exists")

    def change_aim_name(self, main_aim=None):
        if main_aim is None or main_aim or main_aim not in self.main_names:
            main_aim = self.get_main_aim()
        new_main_aim = input("Enter new text")
        if new_main_aim not in self.main_names or new_main_aim == main_aim:
            new_args = self.main_names[main_aim]
            self.delete_aim(main_aim)
            self.main_names.update({new_main_aim : new_args})
            self.save()
        else:
            print("Such aim exists")

    def change_sub_aim_name(self, main_aim=None, sub_aim=None):
        if main_aim is None or main_aim or main_aim not in self.main_names:
            main_aim = self.get_main_aim()
        if len(self.main_names[main_aim]) == 0:
            print("Main aim - " + main_aim + " is empty, add new subaims.")
            return
        if sub_aim  is None or (sub_aim not in self.main_names[main_aim]):
            sub_aim  = self.get_sub_aim(main_aim)
        new_sub_aim = input("Enter new text")
        if new_sub_aim not in self.main_names[main_aim] or new_sub_aim == sub_aim:
            new_args = self.main_names[main_aim][sub_aim]
            self.delete_sub_aim(main_aim,sub_aim)
            self.main_names.update({new_sub_aim: new_args})
            self.save()
        else:
            print("Such aim exists")

    def change_step_by_step(self):
        main_aim = self.get_main_aim()
        if not len(self.main_names[main_aim]) == 0:
            sub_aim = self.get_sub_aim(main_aim)
            if not len(self.main_names[main_aim][sub_aim]) == 0:
                task = self.get_task(main_aim, sub_aim)
                self.work_with_task(main_aim, sub_aim, task)
            else:
                print("No tasks here")
        else:
            print("No sub aims here")


    def change_by_concrete_path(self, parameter=None):
        if parameter == None:
            parameter = input("Enter the path")
        main_aim, sub_aim, task = parameter.split(" ")
        if main_aim == "None" or (main_aim not in self.main_names):
            main_aim = self.get_main_aim()
        if not len(self.main_names[main_aim]) == 0:
            if sub_aim  == "None" or (sub_aim not in self.main_names[main_aim]):
                sub_aim  = self.get_sub_aim(main_aim)
            if not len(self.main_names[main_aim][sub_aim]) == 0:
                if task     == "None" or (task    not in self.main_names[main_aim][sub_aim]):
                    task     = self.get_task(main_aim, sub_aim)
                print("Working with MAIN AIM - " + main_aim)
                print("Working with SUB AIM - " + sub_aim)
                print("Working with TASK - " + task + " its value: " + self.main_names[main_aim][sub_aim][task])
                self.work_with_task(main_aim, sub_aim, task)

    def change_task_state(self, main_aim, sub_aim, task):
        print("Change - " + main_aim + " " + sub_aim + " " + task)
        self.main_names[main_aim][sub_aim][task] = input("Enter smth to change the value: ")
        self.save()

    def change_task(self, main_aim, sub_aim, task):
        self.main_names[main_aim][sub_aim].pop(task)
        self.task_names.pop(task)
        task = input("Enter new task: ")
        self.main_names[main_aim][sub_aim].update({task: "Incompleted"})
        self.task_names.update({task: "Incompleted"})
        print("New task " + task + " " + "Incompleted")
        self.save()

    def get_main_aim(self):
        to_return = ""
        run = True
        for item in self.main_names:
            print(item)
        while run:
            to_return = input("Enter a main_aim to edit ")
            if to_return in self.main_names:
                run = False
            else:
                print("Enter a valid main_aim")
        return to_return

    def get_sub_aim(self, main_aim):
        to_return = ""
        run = True
        self.display_sub_aims(main_aim)
        while run:
            to_return = input("Enter a sub_aim to edit ")
            if to_return in self.main_names[main_aim]:
                run = False
            else:
                print("Enter a valid sub_aim")
        return to_return

    def get_task(self, main_aim, sub_aim):
        to_return = ""
        run = True
        while run:
            self.display_aims(main_aim, sub_aim)
            to_return = input("Enter a task to edit")
            if to_return in self.main_names[main_aim][sub_aim]:
                run = False
            else:
                print("Enter a valid task")
        return to_return

    def work_with_task(self, main_aim, sub_aim, task):
        run = True
        while run:
            desion = int(input("\n1. to change a state."
                               "\n2. to change the task name."
                               "\n3.print "
                               "\n4. exit"))
            if desion == 1:
                self.change_task_state(main_aim, sub_aim, task)
            elif desion == 2:
                self.change_task(main_aim, sub_aim, task)
            elif desion == 3:
                print("Task - " + task + " value: " + self.main_names[main_aim][sub_aim][task])
                break
            elif desion == 4:
                print("Exit")
                run = False
            else:
                print("Enter a valid number")

    def delete_task(self, main_aim=None, sub_aim=None, task=None):
        if main_aim is None or (main_aim not in self.main_names):
            main_aim = self.get_main_aim()
        if sub_aim  is None or (sub_aim not in self.main_names[main_aim]):
            sub_aim  = self.get_sub_aim(main_aim)
        if task     is None or (task    not in self.main_names[main_aim][sub_aim]):
            task     = self.get_task(main_aim, sub_aim)
        answer = input("Do you really want to delete task: " + task + "\n If yew - print y else n")
        if answer.lower() == 'y':
            self.main_names[main_aim][sub_aim].pop(task)
            self.save()
            print("Deleted")
        else:
            print("Terminated")

    def delete_sub_aim(self, main_aim=None, sub_aim=None):
        if main_aim is None or (main_aim not in self.main_names):
            main_aim = self.get_main_aim()
        if sub_aim  is None or (sub_aim not in self.main_names[main_aim]):
            sub_aim  = self.get_sub_aim(main_aim)

        answer = input("Do you really want to delete sub_aim: " + sub_aim + "\n If yes - print Y else N")
        if answer.lower() == 'y':
            self.main_names[main_aim].pop(sub_aim)
            self.save()
            print("Deleted")
        else:
            print("Terminated")

    def delete_aim(self, main_aim=None):
        if main_aim is None or main_aim not in self.main_names:
            main_aim = self.get_main_aim()

        answer = input("Do you really want to delete main_aim: " + main_aim + "\n If yes - print Y else N")
        if answer.lower() == 'y':
            self.main_names.pop(main_aim)
            self.save()
            print("Deleted")
        else:
            print("Terminated")

    def display_sub_aims(self, main_aim):
        print(main_aim)
        for sub_aim, task in self.main_names[main_aim].items():
            print("\t" + sub_aim)

    def display_list_to_do(self, main=None, sub_aim=None):
        if main == "get":
            main = self.get_main_aim()
        if sub_aim == "get":
            sub_aim = self.get_sub_aim(main)

        aim_to_print = dict()
        if main is None:
            aim_to_print = dict()
            for main_aim, sub_aim in self.main_names.items():
                sub_to_print = dict()
                for sub_aim, task in self.main_names[main_aim].items():
                    tas_to_print = dict()
                    for task, state in self.main_names[main_aim][sub_aim].items():
                        if state != "Completed":
                            tas_to_print.update({task: state})
                    if len(tas_to_print) != 0:
                        sub_to_print.update({sub_aim: tas_to_print})
                if len(sub_to_print) != 0:
                    aim_to_print.update({main_aim: sub_to_print})
            print("FOR ALL AIMS IN YOUR LIST")
            if len(aim_to_print) != 0:
                for m, s in aim_to_print.items():
                    print(m)
                    if s is not None:
                        for s, t in aim_to_print[m].items():
                            print("\t" + s)
                            if t is not None:
                                for t, d in aim_to_print[m][s].items():
                                    print("\t\tTask: " + t + " state " + d)
        elif main in self.main_names:
            for main_aim, sub_aim in self.main_names.items:
                if main_aim == main:
                    sub_to_print = dict()
                    if sub_aim in self.main_names[main]:
                        tas_to_print = dict()
                        for task, state in self.main_names[main][sub_aim].items():
                            if state != "Completed":
                                tas_to_print.update({task: state})
                        if len(tas_to_print) != 0:
                            sub_to_print.update({sub_aim: tas_to_print})
                    else:
                        for sub_aim, task in self.main_names[main].items():
                            tas_to_print = dict()
                            for task, state in self.main_names[main][sub_aim].items():
                                if state != "completed":
                                    tas_to_print.update({task: state})
                            if len(tas_to_print) != 0:
                                sub_to_print.update({sub_aim: tas_to_print})

                    if len(sub_to_print) != 0:
                        aim_to_print.update({main: sub_to_print})
            print("For all sub aims in - " + main)
            if len(aim_to_print) != 0:
                for m, s in aim_to_print.items():
                    print(m)
                    if s is not None:
                        for s, t in aim_to_print[m].items():
                            print("\t" + s)
                            if t is not None:
                                for t, d in aim_to_print[m][s].items():
                                    print("\t\tTask: " + t + " state " + d)
        else:
            print("No such main aim " + main)

    def display_aims(self, main=None, sub_aim=None, task=None):
        if main == "get":
            if not len(self.main_names) == 0:
                main = self.get_main_aim()
            else:
                main = None
        if sub_aim == "get":
            if main is not None or len(self.main_names[main]) == 0:
                sub_aim = self.get_sub_aim(main)
            else:
                sub_aim = None
        if task == "get":
            if not len(self.main_names[main][sub_aim]) == 0:
                task = self.get_task(main, sub_aim)
            else:
                task = None

        if main is None:
            for main_aim, sub_aim in self.main_names.items():
                print(main_aim)
                for sub_aim, task in self.main_names[main_aim].items():
                    print("\t" + sub_aim)
                    for task, task_description in self.main_names[main_aim][sub_aim].items():
                        print("\t\t" + task + "\t" + task_description)
        elif main in self.main_names:
            if sub_aim in self.main_names[main]:
                if task in self.main_names[main][sub_aim]:
                    print("Task: " + task + " description: " + self.main_names[main][sub_aim][task])
                else:
                    print("SubAim: " + sub_aim)
                    for task, task_description in self.main_names[main][sub_aim].items():
                        print("\t\t" + task + "\t" + task_description)
            else:
                print(main)
                for sub_aim, task in self.main_names[main].items():
                    print("\t" + sub_aim)
                    for task, task_description in self.main_names[main][sub_aim].items():
                        print("\t\t" + task + "\t" + task_description)
        else:
            print("No such main aim: " + main)


    def save(self):
        with open("app.json", 'w') as file:
            json.dump(self.main_names, file)

    def add_aims():
        pass


if __name__ == '__main__':
    Ap = App("appdd.json")
    Ap.run()
