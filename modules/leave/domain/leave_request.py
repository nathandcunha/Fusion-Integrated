# domain/leave_request.py

from modules.leave.models import LeaveRequest
from modules.leave.selectors import get_leave_requests
from modules.leave.services import create_leave_request, update_leave_request, delete_leave_request
from modules.leave.api.serializers import LeaveRequestSerializer
from modules.leave.api.views import LeaveRequestViewSet

# Business logic for leave requests
def approve_leave_request(request_id):
    request = get_leave_requests(request_id)
    request.status = 'APPROVED'
    request.save()

def reject_leave_request(request_id):
    request = get_leave_requests(request_id)
    request.status = 'REJECTED'
    request.save()
