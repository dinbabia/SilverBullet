from datetime import datetime
import time

def logger(func):
    def wrapper():
        print("-"*50)
        print(f"> Execution started {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}")
        func()
        print(f"> Execution completed {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-"*50)
    return wrapper

@logger
def task_1():
    print("Executing task!")
    time.sleep(2)
    print("Task Completed!")

# We can either do both below
# Option 1 (recommended)
# task_1()
# Option 2
# logger(task_1())


# --------------------------- Logger with Arguments ---------------------------------------
def logger_with_args(func):
    def wrapper(*args, **kwargs):
        print("-"*50)
        print(f"> Execution started {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}")
        func(*args, **kwargs)
        print(f"Running Function: {func.__name__}")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
        print(f"> Execution completed {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-"*50)
    return wrapper

@logger_with_args
def starting_automation_session(session_name: str, tester_name: str):
    print(f"Executing {session_name} by {tester_name}")
    time.sleep(2)
    print("Testing Done!")


starting_automation_session(session_name="Demo Test", tester_name="Din")


