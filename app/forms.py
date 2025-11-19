from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired # 入力チェック
from wtforms import PasswordField

# Flask-WTFを使って予定を入力するフォーム
class ScheduleForm(FlaskForm):
    title = StringField("予定タイトル", validators=[DataRequired()])
    start_time = DateTimeField("開始日時", format="%Y-%m-%d %H:%M", validators=[DataRequired()])
    end_time = DateTimeField("終了日時", format="%Y-%m-%d %H:%M", validators=[DataRequired()])
    submit = SubmitField("登録")

class LoginForm(FlaskForm):
    username = StringField("ユーザー名", validators=[DataRequired()])
    password = PasswordField("パスワード", validators=[DataRequired()])
    submit = SubmitField("ログイン")
