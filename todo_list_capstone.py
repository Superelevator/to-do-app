import os


# comment
def display_tasks(tasks):
    os.system('clear')
    print("Tasks\n")
    for task in tasks:
        print(task)

class Task:
    def __init__(self, name, status_symbol=" ", to_remove=False):
        self.name = name
        self.status_symbol = status_symbol
        self.to_remove = to_remove
    def __repr__(self):
        return f"[{self.status_symbol}] {self.name}"
    def update(self):
        if self.status_symbol == " ":
            self.status_symbol = "X"
        elif self.status_symbol == "X":
            self.to_remove=True
    

tasks = []

while True:
    display_tasks(tasks)
    user_input = input("\nTask name: ")
    for selected_id in range(len(tasks)):
        if tasks[selected_id].name == user_input:
            selected_task = tasks[selected_id]
            selected_task.update()
            if selected_task.to_remove == True:
                tasks.pop(selected_id)
            break
    else:
        tasks.append(Task(user_input))
    
    
