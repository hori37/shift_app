# アプリ起動ファイル
# appフォルダの中にある create_app 関数を読み込む
from app import create_app

# Flaskアプリを作成（設定やルーティングを含む）
app = create_app()

# このファイルが直接実行されたときだけ、アプリを起動する
if __name__ == "__main__":
    # Flaskアプリを起動（debug=True でエラー表示がわかりやすくなる）
    app.run(debug=True,port=5050)