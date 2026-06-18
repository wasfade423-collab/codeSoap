import os

DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', ''),
    'database': os.environ.get('DB_NAME', 'smartport_gateway'),
    'auth_plugin': 'mysql_native_password'
}

PORT = int(os.environ.get('PORT', 8000))