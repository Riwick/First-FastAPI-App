from fastapi import APIRouter, Depends

from auth.base_config import current_user
from tasks.tasks import send_email_report

email_router = APIRouter(prefix='/report', tags=['reports'])


@email_router.get('/send_email')
def get_report(user=Depends(current_user)):
    send_email_report.delay(user.username)
    return {
        'status': 200,
        'data': 'Письмо отправлено',
        'details': None
    }
