def div(func):
    def wrapper():
        return "<div>" + str(func()) + "</div>"
    return wrapper

def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@div
@para
def outname():
    return "김상형"

@para
@div
def outage():
    return "29"

print(outname(),outage())
print(outage(),outname())


def divice(func):
    def wrapper():
        return"<di>" + str(func()) + "</di>"
    return wrapper

def service(func):
    def wrapper():
        return"<s>" + str(func()) + "</s>"
    return wrapper

@divice
@service
def outername():
    return "gallaxy"

@divice
@service
def outerage():
    return "2년"

print(outername())
print(outerage())
