from flask import current_app as app

from app.models import load_user


@app.context_processor
def inject_user_class():
    user = load_user()
    topbar_items = user.class_ids
    print(topbar_items)
    return dict(topbar_items=topbar_items)
