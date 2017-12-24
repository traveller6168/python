def get_ext(fname):
    dot = fname.rfind('.')
    if dot == -1:
        return ''
    else:
        return fname[dot +1:]