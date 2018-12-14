from functools import wraps

def para(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return "<p>" + str(func(*args, **kwargs)) + "</p>"
    return wrapper

@para
def outname(name):
    return "이름:" + name + "님"

@para
def outage(age):
    return "나이:" + str(age)

print(outname("김상형"))
print(outage(29))
print(outname.__name__)

