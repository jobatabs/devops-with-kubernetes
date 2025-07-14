from os import makedirs, path

def safe_open_w(place):
    ''' Open "path" for writing, creating any parent directories as needed.
    '''
    makedirs(path.dirname(place), exist_ok=True)
    return open(place, 'wb')
