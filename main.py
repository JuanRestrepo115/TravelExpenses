from db.connection import init_db, SessionLocal

if __name__ == "__main__":
    
    init_db()


    session = SessionLocal()
    try:
        
        print("Sesión de base de datos abierta correctamente.")
    finally:
        session.close()