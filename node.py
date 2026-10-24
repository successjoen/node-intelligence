THRESHOLD = 30

def sensor_read():
    return 50

def check_threshold(temp):
    if not isinstance(temp, (int, float)):
        print("Type Error: check_threshold needs a number, but got a", type(temp).__name__)
        return None
    if temp > THRESHOLD:
        return "ON"
    else:
        return "OFF"

def fan_output(state):
    if state is None:
        print("Fan: no change")
        return
    print("Fan is:", state)

temp = sensor_read()
decision = check_threshold(temp)
fan_output(decision)

# test with a wrong connection
fan_output(check_threshold("hot"))