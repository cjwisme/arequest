"""
Django settings for arequest project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# 根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# 加签
SECRET_KEY = 'h7a(18o@6c=h(&ambtwh^$!62o_1q46n^ze7xfnl-h!3^e^t)2'

# 调试模式
DEBUG = True
ALLOWED_HOSTS = []

# 生成模式
# DEBUG = False
# 允许访问的地址
# ALLOWED_HOSTS = [""]  


# 注册应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'arequest_demo.apps.ArequestDemoConfig',
    'bresponse_demo.apps.BresponseDemoConfig',
    'creview.apps.CreviewConfig',
    'dclassview.apps.DclassviewConfig',
    'emodels.apps.EmodelsConfig',
]

# 中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由访问地址
ROOT_URLCONF = 'arequest.urls'

# 模板
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 服务器协议
WSGI_APPLICATION = 'arequest.wsgi.application'


# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456',  # 数据库用户密码
        'NAME': 'django_demo'  # 数据库名字
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

# 权限认证
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# 国际化
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

# 时区
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# 静态资源存放地址
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# 静态资源访问路由
STATIC_URL = '/static/'


# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-CACHES-BACKEND
# 缓存
# 1. pip3 install django-redis-cache
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'TIMEOUT':300,
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = 'default'

