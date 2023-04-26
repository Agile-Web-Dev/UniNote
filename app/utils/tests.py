ignored_keys = ["note_id", "created_at", "updated_at"]


def remove_keys(d, keys):
    r = dict(d)

    for key in keys:
        del r[key]
    return r
