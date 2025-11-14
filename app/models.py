# __init__.py で作った db（SQLAlchemyのインスタンス）を読み込む
from . import db

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