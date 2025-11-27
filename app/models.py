# DBのテーブル定義
from flask_login import UserMixin # UserMixinを継承することでログイン機能の便利セット使える
from werkzeug.security import generate_password_hash, check_password_hash
from app import db  # __init__.py で作ったDB


# User（ログイン用）
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # データ型、primary_keyをtrueでデータが必ず追加される ユーザーID
    username = db.Column(db.String(64), unique=True, nullable=False)  # ユーザー名
    password_hash = db.Column(db.String(128), nullable=False)  # パスワード（ハッシュ化）

    # パスワードを保存するときにハッシュ化する関数
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # パスワードが正しいか確認する関数
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# Shift
class Shift(db.Model):
    __tablename__ = 'shifts'
    id = db.Column(db.Integer, primary_key=True)  # ID（自動で割り振られる主キー）
    title = db.Column(db.String(100))             # シフト名
    start_time = db.Column(db.DateTime)           # 開始時間
    end_time = db.Column(db.DateTime)             # 終了時間


# Schedule
class Schedule(db.Model):
    __tablename__ = 'schedules'
    id = db.Column(db.Integer, primary_key=True)  # ID（自動で割り振られる主キー）
    title = db.Column(db.String(100))             # 予定の名前
    start_time = db.Column(db.DateTime)           # 開始時間
    end_time = db.Column(db.DateTime)             # 終了時間
    all_day = db.Column(db.Boolean, default=False)
    note = db.Column(db.Text)         # メモ
    color = db.Column(db.String(20))  # 色指定


# ShiftType（勤務名・色・文字色）
class ShiftType(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID（自動で割り振られる主キー）
    name = db.Column(db.String(50), unique=True, nullable=False)  # 勤務名
    color = db.Column(db.String(20), nullable=False)  # 背景色
    text_color = db.Column(db.String(20), nullable=False, default="#FFFFFF")  # 文字色
