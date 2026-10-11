# api/serializers.py

from rest_framework import serializers
from modules.leave.models import LeaveRequest
from modules.leave.services import create_leave_request, update_leave_request, delete_leave_request

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ['id', 'user', 'start_date', 'end_date', 'reason', 'status', 'created_at', 'updated_at']

    def create(self, validated_data):
        return create_leave_request(
            validated_data['user'],
            validated_data['start_date'],
            validated_data['end_date'],
            validated_data['reason']
        )

    def update(self, instance, validated_data):
        return update_leave_request(
            instance.id,
            validated_data['user'],
            **validated_data
        )

    def delete(self, instance):
        delete_leave_request(instance.id, instance.user)
