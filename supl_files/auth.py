# core/auth.py

from datetime import datetime, timedelta
import bcrypt
import jwt
# The import "from core.settings import settings" has been removed.

def hash_password(plain: str) -> str:
    return bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode()

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())

def create_access_token(subject: str) -> str:
    # Values from settings are now hardcoded
    JWT_EXPIRES_MINUTES = 60
    JWT_SECRET = "supersecret"
    JWT_ALGORITHM = "HS256"
    
    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRES_MINUTES)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decode_access_token(token: str) -> str:
    # Values from settings are now hardcoded
    JWT_SECRET = "supersecret"
    JWT_ALGORITHM = "HS256"
    
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return payload.get("sub")