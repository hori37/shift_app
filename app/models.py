from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db  # __init__.py で作ったDB


# ユーザーモデル（ログイン用）
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # ユーザーID
    username = db.Column(db.String(64), unique=True, nullable=False)  # ユーザー名
    password_hash = db.Column(db.String(128), nullable=False)  # パスワード（ハッシュ化）

    # パスワードを保存するときにハッシュ化する関数
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # パスワードが正しいか確認する関数
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


#シフトを保存するテーブルの定義
class Shift(db.Model):
    __tablename__ = 'shifts'

    id = db.Column(db.Integer, primary_key=True)  #ID（自動で割り振られる主キー）
    title = db.Column(db.String(100))             #シフトの名前（日勤、夜勤）
    start_time = db.Column(db.DateTime)           #開始時間
    end_time = db.Column(db.DateTime)             #終了時間

#予定を保存するテーブルの定義
class Schedule(db.Model):
    __tablename__ = 'schedules'

    id = db.Column(db.Integer, primary_key=True)  #ID（自動で割り振られる主キー）
    title = db.Column(db.String(100))             #予定の名前（病院、買い物）
    start_time = db.Column(db.DateTime)           #開始時間
    end_time = db.Column(db.DateTime)             #終了時間
    all_day = db.Column(db.Boolean, default=False)
    note = db.Column(db.Text)         #メモ欄
    color = db.Column(db.String(20))  # 色指定

# 勤務タイプモデル（勤務名・色・文字色）
class ShiftType(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 一意のID
    name = db.Column(db.String(50), unique=True, nullable=False)  # 勤務名
    color = db.Column(db.String(20), nullable=False)  # 背景色
    text_color = db.Column(db.String(20), nullable=False, default="#FFFFFF")  # 文字色
