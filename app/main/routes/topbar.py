from flask import current_app as app
# from flask_login import login_required

# from app.models import load_user

@app.context_processor
def inject_user_class():
    # user = load_user()
    # topbar_items = user.class_ids
    return 
