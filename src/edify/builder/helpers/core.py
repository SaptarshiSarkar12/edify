import re


def as_type(type, options={}):
    def as_type_fn(value=None):
        return {
            'type': type,
            'value': value,
            'options': options,
        }
    return as_type_fn


def deferred_type(type, options={}):
    type_fn = as_type(type, options)
    return type_fn(type_fn)


def create_stack_frame(type):
    return {
        'type': type,
        'quantifier': None,
        'elements': [],
    }


def assertion(condition, message):
    if not condition:
        raise Exception(message)


def escape_special(s):
    return re.escape(s)


def deep_copy(o):
    if isinstance(o, list):
        return [deep_copy(e) for e in o]
    if isinstance(o, dict):
        return {k: deep_copy(v) for k, v in o.items()}
    return o


def apply_subexpression_defaults(expr):
    out = {**expr}
    out['namespace'] = "" if 'namespace' not in out else out['namespace']
    out['ignore_flags'] = True if 'ignore_flags' not in out else out['ignore_flags']
    out['ignore_start_and_end'] = True if 'ignore_start_and_end' not in out else out['ignore_start_and_end']
    assertion(type(out['namespace']) == str, 'namespace must be a string')
    assertion(type(out['ignore_flags']) == bool, 'ignore_flags must be a boolean')
    assertion(type(out['ignore_start_and_end']) == bool, 'ignore_start_and_end must be a boolean')
    return out
