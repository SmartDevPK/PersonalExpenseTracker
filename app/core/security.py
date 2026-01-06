import os
from flask_cors import CORS

def init_security(app):
    origins = os.getenv("CORS_ORIGINS", "*").split(",")

    # Clean whitespace
    origins = [origin.strip() for origin in origins]

    CORS(
        app,
        resources={r"/api/*": {"origins": origins}},
        supports_credentials=True
    )
