
msg_ = []

msg_.append("")
msg_[0] = "Enter an equation"

msg_.append("")
msg_[1] = "Do you even know what numbers are? Stay focused!"

msg_.append("")
msg_[2] = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_.append("")
msg_[3] = "Yeah... division by zero. Smart move..."

msg_.append("")
msg_[4] = "Do you want to store the result? (y / n):"

msg_.append("")
msg_[5] = "Do you want to continue calculations? (y / n):"

msg_.append("")
msg_[6] = " ... lazy"

msg_.append("")
msg_[7] = " ... very lazy"

msg_.append("")
msg_[8] = " ... very, very lazy"

msg_.append("")
msg_[9] = "You are"

msg_.append("")
msg_[10] = "Are you sure? It is only one digit! (y / n)"

msg_.append("")
msg_[11] = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_.append("")
msg_[12] = "Last chance! Do you really want to embarrass yourself? (y / n)"

memory = 0

def is_number(v):
    try:
        float(v)
        return True
    except ValueError:
        return False


def calculate(v1, v2, oper):
    if oper == "+":
        result = v1 + v2
    elif oper == "-":
        result = v1 - v2
    elif oper == "*":
        result = v1 * v2
    elif oper == "/":
        result = v1 / v2
    return result

def invoke_memory(v):
    global memory
    if v == "M":
        v = memory
    return v

def is_one_digit(v):
    if (v > -10) and (v < 10) and v.is_integer():
        return True
    else:
        return False

def check(v1, v2, oper):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]
    if (v1 == 1 or v2 == 1) and oper == "*":
        msg = msg + msg_[7]
    if (v1 == 0 or v2 == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


while True:
    print(msg_[0])
    x, oper, y = input().split()

    x = invoke_memory(x)
    y = invoke_memory(y)

    if not (is_number(x) and is_number(y)):
        check(x, y, oper)
        print(msg_[1])
        continue

    if not oper in "+-*/":
        print(msg_[2])
        continue

    x = float(x)
    y = float(y)

    try:
        result = calculate(x, y, oper)
        check(x, y, oper)
        print(result)
        print(msg_[4])
        store = input()
        if store == "y":
            if store == "y" and is_one_digit(result) == True:
                print(msg_[10])
                if input() == "y":
                    print(msg_[11])
                    if input() == "y":
                        print(msg_[12])
                        if input() == "y":
                            memory = result

            elif store == "y" and is_one_digit(result) == False:
                memory = result
            """"
            if is_one_digit(result):
                msg_index = 10
                choice_store_one_digit = input(f"{msg_[msg_index]}\n").lower()
                # if choice_store_one_digit == 'y':
                while msg_index < 12 and choice_store_one_digit == 'y':
                    msg_index += 1
                    choice_store_one_digit = input(f"{msg_[msg_index]}\n").lower()

                if choice_store_one_digit == 'y':
                    memory = result
            else:
                memory = result
            """
        # continue?
        print(msg_[5])
        if input() == 'n':
            break

    except ZeroDivisionError:
        check(x, y, oper)
        print(msg_[3])
        continue





