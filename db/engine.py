from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

DATABASE_URL = "postgresql://neondb_owner:npg_V0JWLUqO3oXk@ep-rough-sea-adw3s1z3.c-2.us-east-1.aws.neon.tech/neondb"

engine = create_engine(
    DATABASE_URL,
    echo=False,  # 關閉 SQL 查詢日誌，避免過多輸出
    poolclass=StaticPool,  # 使用靜態連接池
    pool_pre_ping=True,  # 連接前檢查連接是否有效
    pool_recycle=300,  # 5分鐘回收連接
)

def get_db():
    """取得資料庫連線的生成器函數"""
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
