from flask import Blueprint, redirect, url_for, flash, session
from services.auth_service import is_admin
admin_bp = Blueprint("admin", __name__)
