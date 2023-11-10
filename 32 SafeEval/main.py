def safeval(expression, glob=None, locals=None):
    from copy import deepcopy
    my_gl = {}
    for i in globals().keys():
        try:
            my_gl[i] = deepcopy(globals()[i])
        except:
            my_gl[i] = globals()[i]
    # if glob is None:
    #     my_gl = globals().copy()
    # else:
    #     my_gl = glob
    try:
        val = eval(expression, glob, locals)
        globals().update(my_gl)
        return val
    except NameError:
        globals().update(my_gl)
        return expression
    except Exception as ex:
        globals().update(my_gl)
        return ex

