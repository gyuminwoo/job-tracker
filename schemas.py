# pydantic: 데이터 유효성 검사 라이브러리
from pydantic import BaseModel


# 생성용 DTO (request)
class JobCreate(BaseModel):
  company_name: str
  position: str
  status: str = "지원 완료"

# 응답용 DTO (response)
# JobCreate를 상속받아 회사명, 직무, 상태를 그대로 가져오고 DB에서 생성된 id만 추가
class JobResponse(JobCreate):
  id: int

  # SQLAlchemy 모델(Entity)을 Pydantic 모델(DTO)로 자동 변환해주는 설정
  model_config = {"from_attributes": True}