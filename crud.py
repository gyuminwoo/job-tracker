from sqlalchemy.orm import Session

import models
import schemas


# 지원 정보 생성 (Create) - 자바 JPA의 save() 역할
def create_job(db: Session, job: schemas.JobCreate):
  # DTO(Schema)로 받은 데이터를 Entity(Model)로 변환
  db_job = models.Job(
    company_name=job.company_name,
    position=job.position,
    status=job.status
  )
  db.add(db_job)     # 영속성 컨텍스트(메모리)에 객체를 추가
  db.commit()        # 실제 DB에 반영
  db.refresh(db_job) # DB에서 자동 생성된 ID값을 db_job 객체에 동기화
  return db_job

# 지원 정보 전체 조회 (Read) - 자바 JPA의 findAll() 역할
def get_jobs(db: Session, skip: int = 0, limit: int = 100):
  # offset과 limit을 사용해 페이징 처리까지 간단하게 구현 가능
  return db.query(models.Job).offset(skip).limit(limit).all()

# 자바 스프링에서는 @Transactional 어노테이션이 있을 시 메서드가 종료될 때 commit() 발생
# 파이썬 SQLAlchemy 기본 설정에서는 개발자가 명시적으로 db.commit()을 호출해주어야 commit() 발생
# db.refresh()를 호출해야 데이터베이스가 생성한 고유 id값을 파이썬 객체가 반환 가능