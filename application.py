from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    HOST = '0.0.0.0'  # Azure requires this
    PORT = int(environ.get('PORT', 5000))  # Azure sets this automatically
    app.run(HOST, PORT)  # No ssl_context, Azure handles HTTPS
