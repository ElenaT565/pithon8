# Модуль для записи резуьтатов вычислений

from datetime import datetime as data
path = 'log.txt'
def log_exec(first, second, oper, res):
    log = f'{data.now()} | {first} {oper} {second} = {res}\n'
    with open(path, 'a') as base:
        base.write(log)