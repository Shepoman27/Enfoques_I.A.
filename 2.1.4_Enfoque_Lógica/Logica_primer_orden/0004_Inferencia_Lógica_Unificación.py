def unify(p1, p2, subs={}):
    if subs == None:
        return None
    elif p1 == p2:
        return subs
    elif isinstance(p1, str) and p1.islower():
        return unify_var(p1, p2, subs)
    elif isinstance(p2, str) and p2.islower():
        return unify_var(p2, p1, subs)
    elif isinstance(p1, list) and isinstance(p2, list):
        if len(p1) != len(p2):
            return None
        else:
            return unify(p1[1:], p2[1:], unify(p1[0], p2[0], subs))
    else:
        return None

def unify_var(var, x, subs):
    if var in subs:
        return unify(subs[var], x, subs)
    elif x in subs:
        return unify(var, subs[x], subs)
    else:
        subs[var] = x
        return subs
