ignored_keys = ["note_id", "created_at", "updated_at", "link_id"]


def remove_keys(d, keys):
    r = dict(d)

    for key in keys:
        try:
            del r[key]
        except Exception:
            pass
    return r
