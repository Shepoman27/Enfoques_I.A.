class Task:
    def __init__(self, name, duration, subtasks=None):
        self.name = name
        self.duration = duration
        self.subtasks = subtasks or []

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.name} ({self.duration})"

class TaskHierarchy:
    def __init__(self, tasks=None):
        self.tasks = tasks or []

    def add_task(self, task):
        self.tasks.append(task)

    def get_task_by_name(self, name):
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    def get_subtasks(self, task):
        return task.subtasks

    def get_duration(self, task):
        return task.duration

    def is_primitive(self, task):
        return not task.subtasks

    def is_compound(self, task):
        return bool(task.subtasks)

class Plan:
    def __init__(self, task, start_time, end_time):
        self.task = task
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.task.name} ({self.start_time}-{self.end_time})"

def execute_task(task_hierarchy, task, start_time):
    if task_hierarchy.is_primitive(task):
        end_time = start_time + task_hierarchy.get_duration(task)
        return Plan(task, start_time, end_time)
    else:
        subtask_plans = []
        for subtask in task_hierarchy.get_subtasks(task):
            subtask_plan = execute_task(task_hierarchy, subtask, start_time)
            subtask_plans.append(subtask_plan)
            start_time = subtask_plan.end_time
        end_time = max(plan.end_time for plan in subtask_plans)
        return Plan(task, subtask_plans[0].start_time, end_time)

task_hierarchy = TaskHierarchy()
shopping_list = Task("Shopping List", 0.1)
shopping = Task("Shopping", 2.0, [shopping_list])
cooking = Task("Cooking", 5.0)
eating = Task("Eating", 0.5)
dinner_party = Task("Dinner Party", 0.1, [shopping, cooking, eating])
task_hierarchy.add_task(shopping_list)
task_hierarchy.add_task(shopping)
task_hierarchy.add_task(cooking)
task_hierarchy.add_task(eating)
task_hierarchy.add_task(dinner_party)

plan = execute_task(task_hierarchy, dinner_party, 0)
print(plan)
