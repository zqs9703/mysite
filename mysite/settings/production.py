"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['101.132.74.63']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysite_db',
        'USER': 'zqs_blog',
        'PASSWORD': 'DATABASE_PASSWORD',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#发送邮件位置
#https://docs.djangoproject.com/2.0/ref/settings/#email
#https://docs.djangoproject.com/2.0/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'zqs970313@163.com'
EMAIL_HOST_PASSWORD = 'os.environ[EMAIL_HOST_PASSWORD]' #授权码
EMAIL_SUBJECT_PREFIX = '[二哈的博客]'
EMAIL_USE_SSL = True #与SMYP服务器通信时，是否启动TLS链接（安全链接）

ADMINS = (
    ('admin', 'zqs970313@163.com'),

)

#日志文件
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    #日志文件存放位置
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/mysite_debug.log',
        },
        #错误发送邮件
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    #日志记录器
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}