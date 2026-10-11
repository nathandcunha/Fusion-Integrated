# services/leave_requests.py

from modules.leave.models import LeaveRequest
from modules.leave.selectors import get_leave_requests
from modules.leave.api.serializers import LeaveRequestSerializer
from modules.leave.api.views import LeaveRequestViewSet
from rest_framework.exceptions import PermissionDenied

# Service functions for leave requests
def create_leave_request(user, start_date, end_date, reason):
    if not user.has_perm(PERMISSION_LEAVE_REQUEST_CREATE):
        raise PermissionDenied("Permission denied")
    request = LeaveRequest(
        user=user,
        start_date=start_date,
        end_date=end_date,
        reason=reason,
        status='PENDING'
    )
    request.save()
    return request

def update_leave_request(request_id, user, **kwargs):
    request = get_leave_requests(request_id)
    if not user.has_perm(PERMISSION_LEAVE_REQUEST_UPDATE):
        raise PermissionDenied("Permission denied")
    for key, value in kwargs.items():
        setattr(request, key, value)
    request.save()
    return request

def delete_leave_request(request_id, user):
    request = get_leave_requests(request_id)
    if not user.has_perm(PERMISSION_LEAVE_REQUEST_DELETE):
        raise PermissionDenied("Permission denied")
    request.delete()
