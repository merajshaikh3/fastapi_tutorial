# Documentation: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# The below function will generate a hash for a given password
def get_password_hash(password):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

