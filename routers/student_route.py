from fastapi import APIRouter

router = APIRouter(tags=['Student'])

@router.get('/health-check')
def heath_check():
    return {
        'code': 200, 
        'message': 'Good'
    }