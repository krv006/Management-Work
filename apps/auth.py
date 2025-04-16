from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class AuthPrefixJWTAuthentication(JWTAuthentication):
    def get_raw_token(self, header):
        """
        Custom token parser: looks for 'Bearer Kamron <token>' or 'Kamron <token>'
        """
        if header is None:
            return None

        try:
            if isinstance(header, bytes):
                header = header.decode('utf-8')

            # print(f"Header received: {header}")
            parts = header.split()

            # if 'Bearer Kamron <token>'
            if len(parts) == 3 and parts[0] == 'Bearer' and parts[1] == 'Kamron':
                # print(f"Token extracted: {parts[2]}")  # Debugging
                return parts[2]

            # if 'Kamron <token>'
            if len(parts) == 2 and parts[0] == 'Kamron':
                # print(f"Token extracted: {parts[1]}")  # Debugging
                return parts[1]

            raise AuthenticationFailed(
                'Authorization header must be in format: "Bearer Kamron <token>" or "Kamron <token>"')

        except Exception as e:
            print(f"Error: {e}")
            raise AuthenticationFailed(f'Invalid Authorization header format: {str(e)}')
