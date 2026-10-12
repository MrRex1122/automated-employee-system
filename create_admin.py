import os
from app import create_app, db
from app.models import User

# Explicit environment input only. Never ship a default administrator password.
password = os.environ.get("ADMIN_PASSWORD")
if not password:
    raise SystemExit("Set ADMIN_PASSWORD to a unique secret before running create_admin.py")

app = create_app()

with app.app_context():
    admin = User.query.filter_by(username="admin").first()
    if not admin:
        admin = User(username="admin", role="admin")
        db.session.add(admin)
    admin.set_password(password)
    admin.role = "admin"
    db.session.commit()
    print("Administrator credentials configured from ADMIN_PASSWORD")
