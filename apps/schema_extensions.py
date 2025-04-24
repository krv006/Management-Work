# apps/schema_extensions.py

from drf_spectacular.extensions import OpenApiAuthenticationExtension


class KamronAuthScheme(OpenApiAuthenticationExtension):
    target_class = 'apps.auth.AuthPrefixJWTAuthentication'  # Bu juda muhim
    name = 'KamronAuth'  # Bu nom settings.py > SECURITY_SCHEMES bilan mos bo'lishi kerak

    def get_security_definition(self, auto_schema):
        return {
            'type': 'http',
            'scheme': 'bearer',
            'bearerFormat': 'JWT',
            'description': 'Authorization: Kamron <token> yoki Bearer Kamron <token>',
        }
