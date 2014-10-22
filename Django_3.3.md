###Step2: adminサイトを使う
* データ管理のためのページを自動で生成してくれるアプリケーション
* Adminサイトor管理ページと呼ばれる

####3.3.1アプリケーションに組み込む
adminアプリケーションはデフォルトでは無効なので追加してみる
有効にするにはsetting.pyのINSTALLED_APPSに**django.contrib.admin**を追加する

	INSTALLED_APPS = {
		'django.contrib.auth',
		'django.contrib.contenttype',
		'django.contrib.sessions',
		'django.contrib.sites',
		'django.contrib.admin',
		'mysite.todo',
	}
あとで気づいたが今回は既にデフォルトで追加されていた
しかしあとでSITE_IDがないとあとで怒られるので

	SITE_ID = 1

をsetting.pyに追加しておく

次に言語とタイムゾーンを変えておくことが推奨されてるため変更しておく

	#LANGUAGE_CODE = 'en-us'
	LANGUAGE_CODE = 'ja'

	#TIME_ZONE = 'UTC'
	TIME_ZONE = 'Asia/Tokyo'
さらにURLconfでのadminアプリケーション用のURLパターンにつけられたコメント表記を削除
これも実際はデフォルトで出来ていた

で、準備が整ったので

	./manage.py syncdb

を行い、

	./manage.py runserver
して

http://127.0.0.1:8000/admin

にアクセスしてみる

ログイン画面が表示されれば成功！


user名とpassを忘れた場合は

	./manage.py shell
	python manage.py shell
 
	from django.contrib.auth.models import User
	users = User.objects.all()
	user = users[0]
	user
	<User: ここにユーザ名が表示される>
	user.set_password('mypass')
	user.save()

をすれば良いらしい

成功したあとは少しユーザーなどをクリックしたりして試してみるとよい
右下に保存ボタンがあるがユーザーなどを変更する場合は二度とログイン出来なくなる場合があるらしいので注意が必要
このページはバックエンドのデータベース上にあるモデルに基づいて自動的に生成している

####3.3.2自作アプリケーションのモデルをadminサイト上に表示する
adminにtodoアプリケーションがないことを不思議に思いませんでしたか？
**思いました！！**

* アプリケーション内のモデルをadminに表示するにはadminというclassを内部クラスに定義してあげる必要がある

では実際にやってみましょう。

mysite/mysite/todo/models.pyの中に

	from django.contrib import admin
	admin.site.register(Todo)

を加えて再度確認してみましょう。本はだいぶ古くて参考にならないことが多いことがわかりました...


####3.3.3リレーション先のインスタンスを編集出来るようにする

*  cotegoryは単純なドロップダウンになっていて削除、編集、追加が行えない
*  categoryクラスにも上と同様のことを行うとこれが出来るようになるらしい

####3.3.4Adminサイトに表示されるモデル名やフィールド名を変更する
categoryの名前が複数形になってcategory




