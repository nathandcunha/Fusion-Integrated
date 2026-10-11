# contracts.py

from typing import List, Dict, Optional

# API endpoints
LEAVE_REQUEST_CREATE = '/api/leave/request/'
LEAVE_REQUEST_LIST = '/api/leave/requests/'
LEAVE_REQUEST_DETAIL = '/api/leave/request/{request_id}/'

# Permissions
PERMISSION_LEAVE_REQUEST_CREATE = 'leave.request.create'
PERMISSION_LEAVE_REQUEST_READ = 'leave.request.read'
PERMISSION_LEAVE_REQUEST_UPDATE = 'leave.request.update'
PERMISSION_LEAVE_REQUEST_DELETE = 'leave.request.delete'

