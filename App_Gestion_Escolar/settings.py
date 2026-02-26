from pathlib import Path

# (Alumno) BASE_DIR apunta a la carpeta raíz del proyecto (donde está manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# ⚠️ Importante:
# (Alumno) Yo NO puedo saber tu SECRET_KEY real. Mantén el que Django te generó.
SECRET_KEY = "REEMPLAZA_ESTO_POR_TU_SECRET_KEY_REAL"

# (Alumno) En desarrollo dejamos DEBUG=True
DEBUG = True

ALLOWED_HOSTS = []

# Apps instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # (Alumno) Apps del liceo
    'alumnos',
    'profesores',
    'cursos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'App_Gestion_Escolar.urls'

# (Alumno) Templates globales + templates por app (APP_DIRS=True)
# Parte II pide carpeta templates global con base.html [oai_citation:4‡App Gestión Escolar - Parte II.pdf](sediment://file_0000000022f871f59602c21a77c5cc76)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # carpeta templates global en la raíz
        'APP_DIRS': True,  # también busca templates dentro de cada app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'App_Gestion_Escolar.wsgi.application'

# (Alumno) DB por defecto (SQLite) para esta etapa
# La Parte II no exige MySQL todavía.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'es-cl'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_TZ = True

# (Alumno) STATIC global: Parte II pide carpeta /static en la raíz + estilos.css central [oai_citation:5‡App Gestión Escolar - Parte II.pdf](sediment://file_0000000022f871f59602c21a77c5cc76)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'