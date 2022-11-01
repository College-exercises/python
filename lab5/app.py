import utils

while True:
    val = input("app.py input: ")
    if val == "q":
        break
    try:
        print(utils.process_item(int(val)))
    except ValueError as ex:
        print(f"Stopping app.py execution: {ex}")
        break
