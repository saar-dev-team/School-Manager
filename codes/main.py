from fastapi import FastAPI,status,HTTPException

app = FastAPI()

#login 

passwords_dict = {}

@app.post("/NewAccount")
def new_account (username: str, password: str):
    if len(password) != 8:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="password length must be 8 ."
            )
    else:
        passwords_dict[username] = password
        raise HTTPException(
            status_code = status.HTTP_201_CREATED,
            detail = "new account succesfuly created !"
        )