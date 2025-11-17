# アプリ初期化ファイル
# Flask本体とSQLAlchemy（DB操作ライブラリ）を読み込む
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# データベース操作用の変数（グローバルに使えるようにする）
db = SQLAlchemy()

migrate = None


# Flaskアプリを作成する関数（run.pyから呼び出される）
def create_app():
    # Flaskアプリのインスタンスを作成
    app = Flask(__name__)

    # 設定ファイル（config.py）を読み込む
    app.config.from_pyfile("../config.py")

    # アプリにデータベース機能を追加
    db.init_app(app)

    global migrate
    migrate = Migrate(app, db)

    # ルーティング（URLと画面の動き）を読み込む
    from .routes import main
    app.register_blueprint(main)

    # 作成したアプリを返す
    return app