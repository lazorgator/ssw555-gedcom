import os


validators = {}


def validator(f):
    """Decorator that registers validators."""
    print('REGISTER: ', f.__name__)
    validators[f.__name__] = f
    return f


for f in os.listdir(os.path.dirname(__file__)):
    if f.endswith('.py'):
        __import__('gedcom.validate.' + f.strip('.py'))
