from enum import Enum


class Changes(str, Enum):
    """Changes enumeration."""

    TITLE_CHANGE = "TITLE CHANGE"
    DESCRIPTION_CHANGE = "DESCRIPTION CHANGE"
    TICKET_TYPE_CHANGE = "TICKET TYPE CHANGE"
    STATUS_CHANGE = "STATUS CHANGE"
    ASSIGNED_DEVELOPER_CHANGE = "ASSIGNED DEVELOPER CHANGE"
    PRIORITY_CHANGE = "PRIORITY CHANGE"