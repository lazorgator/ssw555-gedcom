import os


validators = {}


def validator(f):
    """Decorator that registers validators."""
    validators[f.__name__] = f
    return f


for f in os.listdir(os.path.dirname(__file__)):
    if f.endswith('.py') and '__init__' not in f:
        __import__('gedcom.validate.' + f.strip('.py'))
