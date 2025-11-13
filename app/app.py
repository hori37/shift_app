# Flask本体と必要な機能を読み込む
from flask import Flask

# Blueprint（ルーティングのまとまり）を読み込む
from routes import main  # ← routes.py に main = Blueprint(...) がある前提

# SQLAlchemy（DB操作ライブラリ）を読み込む
from models import db  # ← models.py に db = SQLAlchemy() がある前提

# Flaskアプリケーションを作成
app = Flask(__name__)

# アプリの設定（DBの場所やセキュリティキーなど）
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///schedule.db"  # ← SQLiteを使う場合
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False              # ← 変更通知を無効化
app.config["SECRET_KEY"] = "your_secret_key"                      # ← フォームやセッション用の秘密鍵

# DBをアプリに紐づける（初期化）
db.init_app(app)

# Blueprint（main）をアプリに登録
app.register_blueprint(main)

# アプリを起動（開発モード）
if __name__ == "__main__":
    app.run(debug=True)