from logic.arithmetic import *


NUM_1 = None
NUM_2 = None
CALC_SYMBOL = None
FUNC_PRESSED = False

def to_display(num, display):
    global NUM_1, NUM_2, CALC_SYMBOL, FUNC_PRESSED
    current_text = display.cget("text")

    # Handle the 'clear'-button
    if num == "C":
        current_text = "0"
        NUM_1, NUM_2, CALC_SYMBOL = None, None, None
        FUNC_PRESSED = False
    
    # Handle change sign
    elif num == "+/-":
        if FUNC_PRESSED or current_text in ["0", "0."]:
            return
        if "-" in current_text:
            current_text = current_text[1:]
        else:
            current_text = "-" + current_text

    # Don't allow multiple dots
    elif (num == ".") and ("." in current_text):
        if not FUNC_PRESSED:
            return

    elif FUNC_PRESSED:
        FUNC_PRESSED = False
        if num == ".":
            current_text = f"0{num}"
        else:
            current_text = f"{num}"

    # Handle lonely zero
    elif current_text == "0":
        if num == "0" or num == "+/-":
            return
        elif num == ".":
            current_text = current_text + str(num)
        else:
            current_text = str(num)
    
    # All the rest of the cases
    else:
        current_text += str(num)
    display["text"] = current_text


def store_nums(symbol, display):
    global NUM_1, CALC_SYMBOL, NUM_2, FUNC_PRESSED

    # If error, don't do anything
    if display.cget("text") == "ERROR":
        return

    # Prevent from auto calculating if same func button is pressed twice
    if symbol == CALC_SYMBOL and FUNC_PRESSED:
        return

    # Prevent pressing '=' if func is just pressed
    if symbol == "=" and FUNC_PRESSED:
        return
        
    FUNC_PRESSED = True

    # Handle square root first, because it only needs one argument
    if symbol == "\u221A":
        NUM_1 = _convert_string_to_num(display.cget("text"))
        CALC_SYMBOL = "\u221A"
        calculate(display)
        NUM_1, NUM_2, CALC_SYMBOL = None, None, None
    elif symbol == "=" and not NUM_1:
        return    
    elif not NUM_1:
        NUM_1 = _convert_string_to_num(display.cget("text"))
        CALC_SYMBOL = symbol
    else:
        NUM_2 = _convert_string_to_num(display.cget("text"))
        result = calculate(display)
        if symbol == "=":
            NUM_1, NUM_2, CALC_SYMBOL = None, None, None
        else:
            NUM_1 = result
            NUM_2 = None
            CALC_SYMBOL = symbol
    # print(f"NUM_1 is now {NUM_1}")
    # print(f"NUM_2 is now {NUM_2}")
    # print(f"CALC_SYMBOL is now {CALC_SYMBOL}\n")

def _convert_string_to_num(num_text):
    if "." in num_text:
        num = float(num_text)
    else:
        num = int(num_text)
    return num


def calculate(display):
    global NUM_1, NUM_2, CALC_SYMBOL
    try:
        result = func_map[CALC_SYMBOL](NUM_1, NUM_2)
        display["text"] = str(result)
    except Exception:
        display["text"] = "ERROR"
        return
    return result

def delete_one(display):
    global FUNC_PRESSED

    if not FUNC_PRESSED:
        current_text = display.cget("text")
        if len(current_text) == 1:
            display["text"] = "0"
        else:
            display["text"] = current_text[:-1]