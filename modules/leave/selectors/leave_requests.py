# selectors/leave_requests.py

from modules.leave.models import LeaveRequest
from modules.leave.services import create_leave_request, update_leave_request, delete_leave_request
from modules.leave.api.serializers import LeaveRequestSerializer
from modules.leave.api.views import LeaveRequestViewSet

# Selector functions for retrieving leave requests
def get_leave_requests(request_id=None):
    if request_id:
        return LeaveRequest.objects.get(id=request_id)
    return LeaveRequest.objects.all()
