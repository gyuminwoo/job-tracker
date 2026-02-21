from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

# DB 테이블 자동 생성 (ddl-auto와 비슷한 역할)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB 세션 의존성 주입 (Dependency Injection)
# @Autowired나 생성자 주입으로 Repository를 가져오는 느낌
# 요청이 들어올 때 DB 연결을 열고, 요청이 끝나면 안전하게 닫아줌(yield 사용)
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

# 지원 정보 생성 API
# response_model을 지정하면, 리턴되는 데이터를 자동으로 스키마(DTO)에 맞춰 변환하고 검증
@app.post("/jobs/", response_model=schemas.JobResponse)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
  return crud.create_job(db=db, job=job)

# 지원 정보 목록 조회 API
# List[schemas.JobResponse]를 사용하여 배열 형태로 응답
@app.get("/jobs/", response_model=List[schemas.JobResponse])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  return crud.get_jobs(db, skip=skip, limit=limit)