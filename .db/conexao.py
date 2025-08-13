from sqlalchemy import create_engine

def conectar():
    engine = create_engine("sqlite:///meu_banco.db")
    with engine.connect() as conn:
        result = conn.execute("SELECT sqlite_version();")
        print(f"Versão do SQLite: {result.fetchone()[0]}")