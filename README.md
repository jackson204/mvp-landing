# mvp-landing
### Getting Started

#### Requirements
- Python 3.8 & up
- Virtual Environment (pipenv)

#### 1. Create Virtual Environment & Install Django
```
cd /path/to/dev/folder
mkdir mvp-landing
cd mvp-landing
pipenv install django==3.0.8 --python 3.8
pipenv shell
```
#### 2.創立Django Project
```
django-admin startproject mvp-landing .
python manage.py runserver
```
#### 3.建立資料庫與Django間的中介檔案
```
python manage.py migrate 
```
#### 4.創建一下 superuser 帳號
```
python manage.py createsuperuser
```
#### 5.創立Django App
```
python manage.py startapp emails

接下來我們要去 mvp-landing/settings 註冊我們這個app，讓他可以讀取到
到settings.py 找到 INSTALLED_APPS 這個 list， 加入 ‘emails’
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 加入 emails
    'emails',
]
```
#### 6.Models 
```
emails/models.py
建立 Class EmailEntry
建立資料庫和Django間的中介檔案
python manage.py makemigrations emails
同步更新資料庫的內容
python manage.py migrate 
```
#### 7.admin註冊
```
admin.site.register(EmailEntry)
```
#### 8.Routing View _urls.py_
```
  Add a URL to urlpatterns:  path('emails/', include('emails.urls'))
```

#### 9.Setting up Django Templates 創立模板
```
回到根目錄（mvp-loading) 創立一個 templates 資料夾,在裡面建立一個.Html
mvp-landing/settings
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
# 加入templates目錄
'DIRS': [os.path.join(BASE_DIR, 'templates')],
#…
```
#### 10.Static Files
```
根目錄（mvp-loading) 創立一個 static 資料夾,在裡面建立分別建立三個資料夾 img js  css

mvp-landing/settings
STATICFILES_DIRS = [
    
    os.path.join(BASE_DIR, "static"),

]
{% load static %}
<img src="{% static "my_app/example.jpg" %}" alt="My image">
```