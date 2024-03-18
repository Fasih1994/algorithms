from time import monotonic_ns

def record_time(func):
    def wrap(*args, **kwargs):
        start_time = monotonic_ns()
        func_return = func(*args, **kwargs)
        print(f"Run Time for {func.__name__} is {(monotonic_ns()-start_time)/1000000} mili seconds!")
        return func_return
    return wrap