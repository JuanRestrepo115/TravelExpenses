from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from sqlalchemy.orm import Session
from db.connection import SessionLocal, init_db
from db.models import UserModel, ExpenseModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[Servidor] Iniciando aplicación y verificando base de datos...")
    init_db()
    yield
    print("[Servidor] Apagando aplicación...")

app = FastAPI(title="Travel Expenses API", lifespan=lifespan)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Endpoints for User operations

@app.post("/users/", tags=["User"])
def make_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    # Verify if the email is already registered
    existing_user = db.query(UserModel).filter_by(email=email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="This email is already registered.")
    
    new_user = UserModel(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "User created successfully", "user_id": new_user.id}


# Endpoints for Expense operations

@app.post("/expenses/", tags=["Expense"])
def make_expense(user_id: int, amount: float, description: str, db: Session = Depends(get_db)):
    # Verify if the user exists
    user = db.query(UserModel).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    new_expense = ExpenseModel(user_id=user_id, amount=amount, description=description)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    
    return {"message": "Expense created successfully", "expense_id": new_expense.id}



