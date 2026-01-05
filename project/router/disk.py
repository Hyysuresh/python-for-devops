from fastapi  import APIRouter, HTTPException
from service.service_disk import get_check_disk

router = APIRouter()

@router.get('/disk',status_code=200 )
def get_disk():
    try:
        disk  = get_check_disk()
        return disk
    except:
        raise HTTPException(
            status_code = 500,
            detail = "Internal Server Error"
        )