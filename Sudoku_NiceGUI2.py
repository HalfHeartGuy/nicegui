import datetime
from nicegui import ui

starttime = None

ui.markdown('## Sudoku Game')

sudoku_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

label = ui.label().classes('absolute top-0 right-0')

def isduplicate(value: str):
    if value and value.isdigit():
        return sudoku_numbers.count(int(value) == 1)

def start_timer(button):
    global starttime
    starttime = datetime.datetime.now()
    ui.timer(1.0, timer)

def timer():
    if starttime is not None:
        diff = datetime.datetime.now() - starttime
        past = int(diff.total_seconds()+1)
        label.set_text(f"Gaming time: {past} seconds")

with ui.grid(columns=3):
    for i in range(len(sudoku_numbers)):
        ui.input(value=sudoku_numbers[i], validation={"This number already exists": lambda value: isduplicate(value)})

start_button = ui.button("Start Sudoku Game", on_click=start_timer)

ui.run()