from admin.app import create_app
from config import AdminConfig

app = create_app(AdminConfig)

if __name__ == "__main__":
    app.run()
