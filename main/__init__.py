app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
     app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")