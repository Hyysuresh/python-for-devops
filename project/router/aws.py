from fastapi  import APIRouter, HTTPException
from service.aws_s3 import get_s3_bucket
from service.aws_ec2 import ec2_instance_show

router = APIRouter()

@router.get('/s3',status_code=200 )
def get_aws():
    try:
        aws  = get_s3_bucket()
        return aws
    except:
        raise HTTPException(
            status_code = 500,
            detail = "Internal Server Error"
        )
    
@router.get('/ec2',status_code=200 )
def get_aws_ec2():
    try:
        aws_ec2  = ec2_instance_show()
        return aws_ec2
    except:
        raise HTTPException(
            status_code = 500,
            detail = "Internal Server Error"
        )