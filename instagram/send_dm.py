from instabot import Bot
import shutil

# "config/" ディレクトリを削除する前に、Botインスタンスを作成してから削除するべきです。
bot = Bot()

username = "tikua_n"

# ログイン
bot.login(username="tikua_n",  # Instagramのユーザー名を入力
          password="Marokiti1192")  # Instagramのパスワードを入力

# DMメッセージ
message = "メッセージ内容です"

# 送信先のユーザー名
user_name = "tiikuan"

# DM送信
bot.send_message(message,  # メッセージ
                [user_name]  # 送付先のユーザー名をリストで指定
                )

# "config/" ディレクトリを削除
shutil.rmtree("config/")
  