from app.models import User
from app.db.database import db
from app.services.welcomeEmail import send_welcome_email

def register_user(form):
    new_user = User(
        username=form.username.data.strip(),
        email=form.email.data.lower().strip(),
    )
    new_user.password = form.password.data  

    db.session.add(new_user)
    db.session.commit()

   
    send_welcome_email(new_user.email, new_user.username)

    return True, None
