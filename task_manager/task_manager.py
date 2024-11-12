import json

class Task:
    def __init__(self,id,title,completed=False):
        self.id=id
        self.title=title
        self.completed=completed

    def to_dict(self):
        return{
            'id':self.id,
            'title':self.title,
            'completed':self.completed
        }
    
    @classmethod
    def from_dict(cls, task_dict):
        return cls(task_dict['id'], task_dict['title'], task_dict['completed'])

    def __repr__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Task(id={self.id}, title='{self.title}', status={status})"

    def add_task(self,tasks,title):
        id=len(tasks)+1
        
        print(f"Task {title} is added with ID:{id}")

    def view_tasks(self,tasks):
        if not tasks:
            print("No tasks")
        else:
            for i in tasks:
                print(i)
    
    def delete_tasks(self,tasks,id):
        for t in tasks:
            if t.id == id:
                tasks.remove(t)
                print(f"Task No:{id} got deleted successfully")
        print(f"Task ID {id} not found")

    def mark_as_completed(self,tasks,id):
        for i in tasks:
            if i.id == id:
                i.completed = True
                print(f'Task {id} marked as completed')
        print(f"Task ID {id} not found")

    def save_tasks(self,tasks,filename="tasks.json"):
        with open(filename,'w') as file:
            json.dump([task.to_dict() for task in tasks], file)
        print("Tasks are saved to file")

    def load_tasks(self,filename="tasks.json"):
        try:
            with open(filename,'r') as file:
                tasks =json.load(file)
            
            print('Task loaded successfully from file')
            return tasks
        except FileNotFoundError:
            print('No saved tasks found.')


T=Task(1,'science')
tasks = T.load_tasks()
if tasks is None:  
    tasks = []


while True:
    print("\nTask Manager")
    print("1.Add tasks\n2.view tasks\n3.delete tasks\n4.Marking as completed\n5.sava the tasks")
    option=int(input("eneter your option:"))

    match(option):
        case 1:
            title=input("give a title of task:")
            T.add_task(tasks,title)
        case 2:
            T.view_tasks(tasks)
        case 3:
            id=int(input('enter the id of the tasks:'))
            T.delete_tasks(tasks,id)
        case 4:
            id=int(input())
            T.mark_as_completed(tasks,id)
        case 5:
            T.save_tasks(tasks)
            break
        case _:
            print('invalid option:')
