# アプリ初期化ファイル
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #既存のDBを変更した際にmigrationするため
from flask_login import LoginManager


# 拡張機能のインスタンス化
db = SQLAlchemy() # SQLAlchemyをインスタンス化
login_manager = LoginManager() # ログイン管理システム、LoginManagerをインスタンス化
migrate = None # グローバル変数として存在を明示しておく


# Flaskアプリを作成する関数（run.pyから呼び出される）
def create_app():
    # Flaskアプリのインスタンス作成
    app = Flask(__name__)

    # 設定ファイル（config.py）を読み込む、開発用と本番用で設定を切り替えやすいため
    app.config.from_object("config")  # ここで設定をまとめて読み込む

    # create_app()の中で初期化してアプリに紐付ける
    db.init_app(app) # SQLAlchemy（DB操作ライブラリ）をFlask アプリに接続しdb.Model使えるようにする
    login_manager.init_app(app) # ログイン管理機能をFlaskアプリに接続しユーザーのログイン状態をセッションで管理できるようにする

    # LoginManagerの設定
    login_manager.login_view = "main.index"  # ログインしていない人はトップページにリダイレクト

    # migrateをインスタンス化、db.init_app(app) の後
    global migrate
    migrate = Migrate(app, db)

    # モデル、ルートは拡張機能の初期化後に読み込む
    from app.models import User
    from .routes import main

    # LoginManagerをユーザーIDを使用して現在のユーザーを識別するための関数
    @login_manager.user_loader
    def load_user(user_id): # @login_requiredを使うから必要、current_userも使える
        return User.query.get(int(user_id))
    
    # Blueprint の登録
    app.register_blueprint(main) # routes.py に書いた @main.route(...) を有効にする
    return app
