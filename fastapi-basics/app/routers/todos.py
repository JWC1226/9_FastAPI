# TODO 공통 주소: /todos >> 라우팅 설정(등록)
from fastapi import APIRouter

router = APIRouter(prefix="/todos")
# ・prefix >>> Spring @RequestMapping

# TODO [GET] /todos/health
# - response: "ok"
# - 함수명: health_check
@router.get("/health")
def health_check():
    return "ok"