from fastapi import FastAPI, status, HTTPException
from pwdlib import PasswordHash

app = FastAPI()


#login_________________________________________________
# Password hashing
password_hash = PasswordHash.recommended()

# Temporary database
passwords_dict = {}


@app.post("/NewAccount", status_code=status.HTTP_201_CREATED)
def new_account(username: str, password: str):

    if len(password) != 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password length must be 8."
        )

    if username in passwords_dict:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists."
        )

    coded_password = password_hash.hash(password)

    passwords_dict[username] = {
        "hashed_password": coded_password
    }

    return {
        "message": "New account successfully created!",
        "username": username
    }
#______________________________________________________