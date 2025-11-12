# Blueprint（アプリケーションを分割するためのFlaskの拡張機能）とHTML表示用の関数,JSONレスポンス生成,HTTPリクエスト情報の取得,URLリダイレクト,関数名からURL生成,一時メッセージ表示のための仕組みを読み込む
from flask import Blueprint, render_template, jsonify,request, redirect, url_for, flash
from .models import Schedule
from . import db
from .forms import ScheduleForm
from datetime import datetime




# このファイル専用のルーティンググループ(「main」という名前のBlueprint（機能のまとまり）)を作成
main = Blueprint("main", __name__)

# "/" にアクセスされたときの処理（トップページ）
# ルーティングはURLとFlaskの処理を対応づけることで、URLと関数を紐付ける
# Flaskでルーティングを記述するには、route()
# render_template関数を使いhtmlファイルを表示させ、htmlファイルに簡単に値を入れる
@main.route("/")
def index(): #templates/index.htmlを表示する
    return render_template("index.html")

@main.route("/calendar")
def calendar():
    return render_template("calendar.html")

@main.route("/api/events")
def api_events(): #スケジュール一覧をJSON形式で返すAPI 
    schedules = Schedule.query.all() #データベースのScheduleテーブルから全レコードを取得
    events = []
    for s in schedules:
        events.append({
            "title": s.title,
            "start": s.start_time.isoformat(), #日時を"2025-11-12T14:00:00"のような形式に変換(JavaScriptなどで扱いやすくなる)
            "end": s.end_time.isoformat()
        })
    return jsonify(events) #pythonのリストをJSONに変換

@main.route("/api/add_event", methods=["POST"])
def add_event():
    data = request.get_json()

    #ここで文字列を datetime に変換
    start = datetime.fromisoformat(data["start"])
    end = datetime.fromisoformat(data["end"])

    new_schedule = Schedule(
        title=data["title"],
        start_time=start,
        end_time=end
    )
    db.session.add(new_schedule)
    db.session.commit()
    return jsonify({"status": "success"})

@main.route("/add", methods=["GET", "POST"])
def add_schedule(): #予定追加
    form = ScheduleForm() #Flask-WTFで作った予定入力用のフォーム
    if form.validate_on_submit(): #フォームが送信されていて入力内容が正しいかチェック
        new_schedule = Schedule(
            title=form.title.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data
        )
        db.session.add(new_schedule)
        db.session.commit()
        flash("予定を登録しました！") #テンプレート側で{{ get_flashed_messages() }}で表示
        return redirect(url_for("main.calendar"))
    return render_template("add_schedule.html", form=form) #フォームが送信されていない場合(GET),予定追加ページを表示
