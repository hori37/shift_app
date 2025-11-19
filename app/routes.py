# Blueprint（アプリケーションを分割するためのFlaskの拡張機能）とHTML表示用の関数,JSONレスポンス生成,HTTPリクエスト情報の取得,URLリダイレクト,関数名からURL生成,一時メッセージ表示のための仕組みを読み込む
from flask import Blueprint, render_template, jsonify,request, redirect, url_for, flash
from .models import Schedule
from app import db
from .forms import ScheduleForm
from datetime import datetime
from flask import Flask
import requests
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User



# このファイル専用のルーティンググループ(「main」という名前のBlueprint（機能のまとまり）)を作成
main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index(): #templates/index.htmlを表示する
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        # ユーザーが存在し、パスワードが正しいか確認
        if user and user.check_password(password):
            login_user(user)  # ログイン成功
            return redirect(url_for("main.calendar"))
        else:
            flash("ユーザー名またはパスワードが違います")

    return render_template("index.html")  # ログインフォームを表示

@main.route("/calendar")
@login_required
def calendar():
    return render_template("calendar.html")

#色を決める
def get_shift_color(title):
    if title == "日勤":
        return "#F0F4C3"
    elif title == "夜勤":
        return "#81D4FA"
    elif title == "当直":
        return "#FFCDD2"
    else:
        return "#9E9E9E"  # グレー（予定など）

# "/" にアクセスされたときの処理（トップページ）
# ルーティングはURLとFlaskの処理を対応づけることで、URLと関数を紐付ける
# Flaskでルーティングを記述するには、route()
# render_template関数を使いhtmlファイルを表示させ、htmlファイルに簡単に値を入れる


def get_shift_class(title):
    if title == "日勤":
        return "shift-day"
    elif title == "夜勤":
        return "shift-night"
    elif title == "当直":
        return "shift-duty"
    else:
        return "normal-event"

@main.route("/api/events", methods=["GET", "POST"])
def api_events(): #スケジュール一覧をJSON形式で返すAPI
    db.session.commit()  # 明示的にコミット(保存直後の反映を確実にするために、強制的にコミット後に再取得)
    if request.method == "GET":

        schedules = Schedule.query.all() #データベースのScheduleテーブルから全レコードを取得
        events = [{
            "id": s.id,
            "title": s.title,
            "start": s.start_time.isoformat(), #日時を"2025-11-12T14:00:00"のような形式に変換(JavaScriptなどで扱いやすくなる)
            "end": s.end_time.isoformat(),
            "allDay": s.all_day,
            "className": get_shift_class(s.title),
            "note": s.note,
            "color": s.color
        } for s in schedules]
        return jsonify(events) #pythonのリストをJSONに変換

    elif request.method == "POST":
        # 新規登録処理
        data = request.get_json()
        print("POST受信:", data)
        start = datetime.fromisoformat(data["start"])
        end = datetime.fromisoformat(data["end"])
        all_day = data.get("allDay", False)

        new_schedule = Schedule(
            title=data["title"],
            start_time=start,
            end_time=end,
            all_day=all_day,
            note=data.get("note", ""),
            color=data.get("color", "#66bb6a")

        )
        db.session.add(new_schedule)
        db.session.commit()
        return jsonify({"status": "success"})


@main.route("/api/add_event", methods=["POST"]) #新規登録
def add_event():
    data = request.get_json()

    #ここで文字列を datetime に変換
    start = datetime.fromisoformat(data["start"])
    end = datetime.fromisoformat(data["end"])

    all_day = data.get("allDay", False)

    new_schedule = Schedule(
        title=data["title"],
        start_time=start,
        end_time=end,
        all_day=all_day,
        note=data.get("note", ""),
        color=data.get("color", "#66bb6a")

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

@main.route("/api/update_event", methods=["POST"])
def update_event():
    data = request.get_json()
    event = Schedule.query.get(data["id"])
    if event:
        event.title = data["title"]
        event.start_time = datetime.fromisoformat(data["start"])
        event.end_time = datetime.fromisoformat(data["end"])
        event.all_day = data.get("allDay", False)
        event.note = data.get("note", "")
        event.color = data.get("color", "#66bb6a")
        db.session.commit()
    return jsonify({"status": "updated"})

@main.route("/api/delete_event", methods=["POST"])
def delete_event():
    data = request.get_json()
    print("受け取ったID:", data["id"])
    event = Schedule.query.get(data["id"])
    if event:
        db.session.delete(event)
        db.session.commit()
        return jsonify({"status": "deleted"})
    else:
        return jsonify({"status": "not found"}), 404
    
@main.route("/api/holidays")
def get_holidays():
    try:
        start = request.args.get("start")
        end = request.args.get("end")

        res = requests.get("https://holidays-jp.github.io/api/v1/date.json")
        data = res.json()

        events = []
        for date in data.keys():
            events.append({
                "start": date,
                "end": date,
                "display": "background",
                "color": "#ffecec"
            })

        return jsonify(events)
    except Exception as e:
        print("祝日取得エラー:", e)
        return jsonify([]), 500
