# helpers to connect web2py backend with svelte frontend

import json


def svelte(_page='Index'):
    def wrapper_outer(func):
        def wrapper(*a, **kw):
            # wrapper to connect controller with svelte view
            response.view = 'svelte/public/index.html'
            result = func(*a, **kw)
            result.update({'_page': _page})
            return result
        return wrapper
    return wrapper_outer
