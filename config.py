# 設定変数の定義、アプリ全体で使う設定
import os  # OSの機能を使ってファイルの場所を取得する
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # プロジェクトのベースディレクトリ（このファイルがあるフォルダの絶対パス）

# どのDBを使うか指定（SQLiteのapp.db）
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "app.db")
# SQLAlchemyの無駄な警告をオフにする設定
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flaskはセッション、フォーム送信を安全に扱うために暗号化を使うのでその秘密鍵
SECRET_KEY = "your_secret_key"  # 本番では長くてランダムな文字列に変更