from datetime import *


def diffDate(x):
    try:
        date = datetime.strptime(str(x), '%Y-%m-%d')
        nowDate = datetime.now()
        diff = nowDate - date

        return diff.days

    except:
        return (f'Format Error {x}')
