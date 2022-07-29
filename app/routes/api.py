from flask import Blueprint
from app.models import get_db

bp = Blueprint('api', __name__, url_prefix='/api')