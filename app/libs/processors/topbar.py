from flask import current_app as app
from flask import session

from app.models import load_user


@app.context_processor
def inject_user_class():
    user = load_user()

    topbar_items = []

    if user is not None:
        topbar_items = user.class_ids

    return dict(topbar_items=topbar_items, active_class=session.get("class_id"))
