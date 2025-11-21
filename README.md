# 🕒 shift_app（シフトと予定管理Webアプリ）

## 📘 概要
【シフト】【予定】を重ねて管理し一目で確認できるシンプルなスケジュールアプリです。
日勤・夜勤・当直などの勤務をカレンダー上で直感的に登録し、プライベートの予定も重ねて管理できる。祝日表示や色分けで視認性を高めています。 
Webフレームワークの基礎学習のため作成しました。
---

## 🛠 開発環境
| 項目 | 内容 |
|------|------|
| 言語 | Python（Flask） / JavaScript |
| フロントエンド | FullCalendar / Bootstrap |
| バックエンド | Flask / SQLAlchemy |
| データベース | SQLite（開発用） / MySQL（本番想定） |
| 認証 | Flask-Login |
| IDE | VS Code |
| バージョン管理 | Git / GitHub |
| OS | Windows 11 |

---

## 🧩 機能一覧
| カテゴリ | 内容 |
|------------|------|
| ユーザー管理 | 新規登録・ログイン・ログアウト・パスワード変更 |
| データ登録 | フォーム入力によるデータ追加・バリデーション処理 |
| 更新／削除 | 登録データの編集・削除機能 |
| セッション管理 | ログインユーザー情報の保持とアクセス制御 |
| エラーハンドリング | 例外処理／404ページ／入力エラーメッセージ表示 |

---

## 📂 ディレクトリ構成
shift_app/
├── app.py
├── models.py
├── routes.py
├── templates/
│   ├── index.html
│   ├── calendar.html
│   └── add_schedule.html
├── static/
│   ├── css/
│   └── js/
└── README.md

---

## 🗄 データベース構成
### 📘 ER図
> 画像を `docs/er_diagram.png` に差し替えてください。  
> 例：  
> ![ER図](./docs/er_diagram.png)

### テーブル定義例：users
| カラム名 | 型 | 説明 |
|-----------|----|------|
| id | INT | 主キー（AUTO_INCREMENT） |
| name | VARCHAR(50) | ユーザー名 |
| email | VARCHAR(100) | メールアドレス |
| password | VARCHAR(255) | ハッシュ化されたパスワード |
| created_at | DATETIME | 登録日時 |

---

## 🧠 設計方針・工夫点
- MVC構成（Flask Blueprint + SQLAlchemy + Jinja2）で保守性と拡張性を確保
- シフト登録モードでは保存後に翌日に自動切替 → 連続入力を効率化
- FullCalendarを用いた直感的なUIで予定とシフトを一目で把握
- 祝日API連携で自動背景色表示 →視認性向上
- ユーザー追加による勤務タイプ拡張機能は削除 → 安定性重視
- .gitignore や requirements.txt を整備し、プロジェクトの再現性を確保
- 画面遷移を最小化しモーダルフォームで予定・シフトを登録、編集、削除操作可能 → ユーザー体験が向上
- - UI設計の工夫
- 予定入力はタイトル・時間・色を指定
- シフト登録は連続入力＆ワンクリックで勤務区分選択できるスマートなUI
- モーダルフォームを活用し、予定とシフトで使い分けができる
  
---

## 📊 UML / 設計資料
> 以下のファイルを差し替えてください（今はプレースホルダー画像です）：
>
> - `docs/usecase.png`：ユースケース図  
> - `docs/uml_sequence.png`：シーケンス図  
> - `docs/class_diagram.png`：クラス図  
>
> 例：  
> ![シーケンス図](./docs/uml_sequence.png)

---

## 💬 使用技術のポイント
- **Servlet & JSP**：HTTPリクエスト処理・セッション管理・リダイレクト制御  
- **DAOパターン**：DB操作の共通化・保守性向上  
- **SQL**：CRUD・JOIN・トランザクション  
- **HTML/CSS**：UI / フォーム入力補助  
- **Tomcat**：WARデプロイ・ローカルテスト環境構築  

---

## 🧭 今後の拡張予定
- 管理者専用の勤務タイプ編集画面
- Dockerによる環境構築自動化
- シフト集計機能（勤務時間の合計・勤務回数）
- モバイル対応UI（レスポンシブデザイン強化）
- テストコード整備（pytest）

---

## 📸 画面キャプチャ（例）
> - `docs/login_screen.png`  
> - `docs/list_screen.png`  
>
> 例：  
> ![ログイン画面](./docs/login_screen.png)

---

## 🧾 ライセンス・著作権
このプロジェクトは学習目的で作成したものであり、商用利用は想定していません。  
各種ライブラリ・ツールのライセンスはそれぞれの作者に帰属します。

---

## 👤 作成者
- **氏名（またはGitHubアカウント）**：Your Name  
- **開発期間**：2025年○月〜○月  
- **連絡先**：your-email@example.com  
- **GitHub**：https://github.com/yourname/java-webapp-portfolio

---

## ✅ 最終更新日
2025-11-11

---

> ✏️ **編集方法**：VS Code / Typora などの Markdown 対応エディタで開くと、見出しや画像をプレビューできます。
