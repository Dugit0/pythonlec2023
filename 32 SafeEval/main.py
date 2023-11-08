def safeval(expression, globals=None, locals=None):
    try:
        return eval(expression, {}, locals)
    except NameError:
        return expression
    except Exception as ex:
        return ex

