# アプリ初期化ファイル
# Flask本体とSQLAlchemy（DB操作ライブラリ）を読み込む
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# データベース操作用の変数（グローバルに使えるようにする）
db = SQLAlchemy() #DBインスタンス
login_manager = LoginManager()
migrate = None

# Flaskアプリを作成する関数（run.pyから呼び出される）
def create_app():
    # Flaskアプリのインスタンスを作成
    app = Flask(__name__)

    # アプリにデータベース機能を追加
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

    # 設定ファイル（config.py）を読み込む
    app.config.from_pyfile("../config.py")

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "main.index"

    global migrate
    migrate = Migrate(app, db)

    # モデルとルートは拡張機能の初期化後に読み込む
    from app.models import User  # ← dbを使うモデル
    from .routes import main     # ← ルーティング


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(main)

    return app
