from flask_login import login_required
from flask import current_app as app

from app.models import load_user

@login_required
@app.context_processor
def inject_userClass():
    user = load_user()
    topbar_items=user
    return topbar_items
    
