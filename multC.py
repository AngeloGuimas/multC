import keyboard
import pyperclip
import time
import sys

def main():
    print("This script allows the user to create a small clipboard history and easily access 9 copied contents simultaneously.\n")
    print("Use the shortcuts ctrl+c and ctrl+v to copy and paste contents to/from clipboard.\n")
    print("Use the shortcuts alt + <1-9 key> to change the current content of clipboard according to the copy history (max 9 copies).\n")
    print("Use the alt+delete shortcut to delete the current clipboard contents and clipboard history.\n")
    print("obs1: This script only works with textual contents.\n")
    print("obs2: This script only runs in Windows and Linux enviroments.\n")
    
    copy_var=[]
    
    def ctrl_c():
        time.sleep(1)
        if(len(copy_var)>=9):
            copy_var.pop(0)
            copy_var.append(pyperclip.paste())
        else:
            copy_var.append(pyperclip.paste())
        
    def shortkey_number(n_key):
        if(len(copy_var)>=n_key):
            pyperclip.copy(copy_var[n_key-1])

    def del_list():
        copy_var.clear()
        pyperclip.copy("")

    
    while True:
        keyboard.add_hotkey('ctrl+c', lambda: ctrl_c())
        keyboard.add_hotkey('alt+1', lambda: shortkey_number(1))
        keyboard.add_hotkey('alt+2', lambda: shortkey_number(2))
        keyboard.add_hotkey('alt+3', lambda: shortkey_number(3))
        keyboard.add_hotkey('alt+4', lambda: shortkey_number(4))
        keyboard.add_hotkey('alt+5', lambda: shortkey_number(5))
        keyboard.add_hotkey('alt+6', lambda: shortkey_number(6))
        keyboard.add_hotkey('alt+7', lambda: shortkey_number(7))
        keyboard.add_hotkey('alt+8', lambda: shortkey_number(8))
        keyboard.add_hotkey('alt+9', lambda: shortkey_number(9))
        keyboard.add_hotkey('alt+delete', lambda: del_list())
        keyboard.wait()

if __name__ == "__main__":
    sys.exit(main())
