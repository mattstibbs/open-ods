import os

TARGET_SCHEMA_VERSION = '008'
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://openods:openods@localhost:5432/openods')
CACHE_TIMEOUT = int(os.environ.get('CACHE_TIMEOUT', '30'))
APP_HOSTNAME = os.environ.get('APP_HOSTNAME', 'localhost:5000/api')
API_USER = os.environ.get('API_USER', 'user')
API_PASS = os.environ.get('API_PASS', 'pass')
LIVE_DEPLOYMENT = os.environ.get('LIVE_DEPLOYMENT', 'FALSE')
INSTANCE_NAME = os.environ.get('INSTANCE_NAME', 'Development')

print(str.format("Database URL: {0}", DATABASE_URL))
print(str.format("Cache Timeout: {0}", CACHE_TIMEOUT))
print(str.format("App Hostname: {0}", APP_HOSTNAME))
print(str.format("App User: {0}", API_USER))
print(str.format("App Password: {0}", API_PASS))