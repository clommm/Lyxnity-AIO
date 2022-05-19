from modules.variables import Checker
from modules.functions import *

def start():
    reset_stats()
    while 1:
        clear()
        ascii()
        print("\n\n")
        clear()
        ascii()
        print("\n\n")
        print(f"    [{pink}Pick Combo File{reset}]")
        file_path = get_file("Combo File","Combo File")
        get_focus()
        if not file_path:
            print(f"    [{pink}No File Detected{reset}]")
            sleep(1)
            return
        with open(file_path,errors="ignore") as file:
            original_combos = file.read().splitlines()
            after_combos = list(set(original_combos))
            duplicates = len(original_combos)-len(after_combos)
        print(f"    [{pink}Imported {len(original_combos)} Combos{reset}]")
        if duplicates != 0:
            print(f"    [{pink}Removed {duplicates} Duplicates{reset}]")
        sleep(1)
        Checker.time = get_time()
        edit(after_combos)
        print("\n\n")
        print(f"    [{pink}Finished Removing Capture{reset}]")
        input(f"    [{pink}Press Enter To Go Back{reset}]")
        return
def edit(combos):
    for combo in combos:
        if ":" in combo:
            email = combo.split(":")[0].rstrip()
            password = combo.split(":")[1]
            if " " in password:
                password = password.split(" ")[0]
            log(None,email+":"+password)
            save("Capture_Remove",None,Checker.time,email+":"+password)
