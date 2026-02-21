from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# DB 주소 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///./job_tracker.db"

# DB 엔진 생성 (실제 통신 담당)
engine = create_engine(
  SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread:": False}
)

# DB 세션 팩토리 생성 (DB에 접속하기 위한 세션을 만들어줌)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모든 모델(Entity) 클래스가 상속받을 기본 클래스
Base = declarative_base()