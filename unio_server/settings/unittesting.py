from .default import *

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'LOGGING': {
            'version': 1,
            'loggers': {
                'djongo': {
                    'level': 'DEBUG',
                    'propogate': False,
                }
            },
         },
        'NAME': 'unio',
        'CLIENT': {
            'host': 'localhost',
            'port': 27017,
        }
    }
}