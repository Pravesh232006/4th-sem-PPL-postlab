import time

def log_transaction(action, amount):
    f = open("ledger.txt", "a")
    t = time.strftime("%Y-%m-%d %H:%M:%S")

    f.write(t + " | " + action + " | " + str(amount) + "\n")
    f.close()