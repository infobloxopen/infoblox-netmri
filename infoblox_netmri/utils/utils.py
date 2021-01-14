import re
from pydoc import safeimport


def locate(path, forceload=False):
    """Locate an object by name or dotted path, importing as necessary."""
    parts = [part for part in path.split('.') if part]
    module, n = None, 0
    while n < len(parts):
        nextmodule = safeimport('.'.join(parts[:n + 1]), forceload)
        if nextmodule:
            module, n = nextmodule, n + 1
        else:
            break
    for part in parts[n:]:
        try:
            module = getattr(module, part)
        except AttributeError:
            raise RuntimeError('Object: {} not found'.format(path))
    return module


def to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def check_api_availability(f):
    def wrapper(self, *args):
        func_name = f.__name__
        if getattr(self.broker, func_name, None):
            return f(self, *args)
        else:
            raise RuntimeError(
                "Api call not available for current API version: {}".format(self.broker.client.api_version))

    return wrapper


def to_underscore_notation(name):
    name = str(name)
    if "." not in name:
        return "v{}_0_0".format(name)
    elif name.count(".") == 1:
        return "v{}_0".format(name.replace(".", "_"))
    else:
        return "v{}".format(name.replace(".", "_"))
