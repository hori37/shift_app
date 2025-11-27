# Flask-WTF（WTFormsをFlask用に拡張したライブラリ）を使って予定を入力し- {{ form.xxx }} のように テンプレートでフォームを呼び出す
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, SubmitField
from wtforms.validators import DataRequired # 入力チェック
from wtforms import PasswordField

# 使用してない
class ScheduleForm(FlaskForm):
    title = StringField("予定タイトル", validators=[DataRequired()])
    start_time = DateTimeField("開始日時", format="%Y-%m-%d %H:%M", validators=[DataRequired()])
    end_time = DateTimeField("終了日時", format="%Y-%m-%d %H:%M", validators=[DataRequired()])
    submit = SubmitField("登録")

# ログインフォームは使用している
class LoginForm(FlaskForm):
    username = StringField("ユーザー名", validators=[DataRequired()])
    password = PasswordField("パスワード", validators=[DataRequired()])
    submit = SubmitField("ログイン")
