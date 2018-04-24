from time import time
from functools import partial


def timeit(func, validator=lambda x: True, rep=50):
    time_record = []
    i = 0
    try:
        for i in range(rep):
            print('Running test {} of {}'.format(i+1, rep))
            start = time()
            x = func()
            if validator(x):
                time_record.append(time() - start)
            else:
                print('Test failed!')
    except KeyboardInterrupt:
        pass

    print('Success {} of {}'.format(len(time_record), i+1))
    if len(time_record) > 0:
        average = sum(time_record)/len(time_record)
        if isinstance(func, partial):
            function_name = func.func.__qualname__
        elif callable(func):
            function_name = func.__qualname__
        else:
            function_name = ''
        print('{:.4f} seconds per {}'.format(average, function_name))

    return time_record
