import os  # OSの機能を使ってファイルの場所を取得する

# プロジェクトのベースディレクトリ（このファイルがある場所）
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Flaskアプリの秘密鍵（セッションやフォームの保護に使う）
SECRET_KEY = "your_secret_key"  # 後でランダムな文字列に変更すると安全

# データベースの場所（ローカルのSQLite）
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.db")

# SQLAlchemyの警告（無駄な警告）をオフにする設定
SQLALCHEMY_TRACK_MODIFICATIONS = False