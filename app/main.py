from flask import Flask
from app.api.employee import employee_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(employee_bp)

if __name__ == "__main__":
    app.run(debug=True)