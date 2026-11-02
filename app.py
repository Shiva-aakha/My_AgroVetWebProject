# app.py
from flask import Flask
from config import Config
from extensions import db, login_manager
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)

    from routes.auth import auth_bp
    from routes.shop import shop_bp
    from routes.booking import booking_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(booking_bp)

    @app.route('/')
    def index():
        from flask import render_template
        return render_template('index.html')

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)