REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'apps.auth.AuthPrefixJWTAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'API Tasks',
    'DESCRIPTION': 'API Tasks Description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'SECURITY': [{'KamronAuth': []}],
    'SECURITY_SCHEMES': {
        'KamronAuth': {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'Kamron <token>',
            'description': 'Custom token auth using prefix: Kamron <token> or Bearer Kamron <token>',
        },
    },
    'SWAGGER_UI_SETTINGS': {
        'persistAuthorization': True,
    },
}
