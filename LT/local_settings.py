SECRET_KEY = '@n35^kkz7nuzso1(5kpf0i^@&1nc0^-1ysjz#4@jztro^c!frocheese'

ALLOWED_HOSTS = ['jlochran.pythonanywhere.com', '127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'jimlochran@gmail.com'
EMAIL_HOST_PASSWORD = 'Organug07'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


DEBUG = False
