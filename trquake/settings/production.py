# Third Party
import environ

# Local Folder
from .base import *

env = environ.Env()

DEBUG = False
AWS_LB_HOST = env("AWS_LB_HOST")
ALLOWED_HOSTS = [
    "api.afetharita.com",
    "apinew.afetharita.com",
    "afetharita.com",
    "d-back-lb-1711558828.eu-central-1.elb.amazonaws.com",
    AWS_LB_HOST,
]
# CORS_ALLOWED_ORIGINS = ["https://afetharita.com", "https://api.afetharita.com", "http://api.afetharita.com"]
CORS_ORIGIN_ALLOW_ALL = True

CSRF_TRUSTED_ORIGINS = ["https://*.afetharita.com", "http://*.afetharita.com", "https://afetharita.com"]

DATABASE_ROUTERS = ["core.db_routers.PrimaryReplicaRouter"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
    },
    "read_db": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("REPLICA_DB_NAME"),
        "USER": env("REPLICA_DB_USER"),
        "PASSWORD": env("REPLICA_DB_PASSWORD"),
        "HOST": env("REPLICA_DB_READ_HOST"),
        "PORT": "5432",
    },
    "write_db": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("REPLICA_DB_NAME"),
        "USER": env("REPLICA_DB_USER"),
        "PASSWORD": env("REPLICA_DB_PASSWORD"),
        "HOST": env("REPLICA_DB_WRITE_HOST"),
        "PORT": "5432",
    },
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": [
            env("CACHE_REDIS_URL"),  # redis://redis-prod-1.euc1.cache.amazonaws.com:6379
        ],
    }
}
CACHE_MIDDLEWARE_ALIAS = "default"  # which cache alias to use
CACHE_MIDDLEWARE_SECONDS = 60 * 7  # number of seconds to cache a page for (TTL)
# should be used if the cache is shared across multiple sites that use the same Django instance
CACHE_MIDDLEWARE_KEY_PREFIX = ""
