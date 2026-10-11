# api/views.py

from rest_framework import viewsets
from modules.leave.models import LeaveRequest
from modules.leave.api.serializers import LeaveRequestSerializer
from modules.leave.services import get_leave_requests

class LeaveRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows leave requests to be viewed or edited.
    """
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Filter leave requests by the current user
        """
        user = self.request.user
        return get_leave_requests().filter(user=user)

    def perform_create(self, serializer):
        """
        Assign the current user as the requestor
        """
        serializer.save(user=self.request.user)
