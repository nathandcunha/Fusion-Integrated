# registry.py

from modules.accesscontrol import registry

group = {
    "section": "HR",
    "items": [
        {
            "label": "Leave Requests",
            "icon": "FaRegCalendarAlt",
            "links": [
                {"label": "All Requests", "to": "/api/leave/requests/"},
                {"label": "Create Request", "to": "/api/leave/request/"}
            ]
        }
    ]
}

registry.register(group)
