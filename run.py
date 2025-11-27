# ➀アプリ起動用ファイル
from app import create_app

# __init__.pyのcreate_app()を呼びアプリを構築
app = create_app()

# このファイルが直接実行されたときだけ、アプリを起動する（python run.pyで直接実行の場合）
if __name__ == "__main__":
    # Flaskアプリを起動（debug=Trueでエラー表示がわかりやすくするため開発中のみ。本番はFalseにする）
    app.run(debug=True,port=5000)