from enum import Enum


class TicketType(str, Enum):
    """Ticket type enumeration."""

    BUG_ERROR = "BUG/ERROR"
    FEATURE_REQUEST = "FEATURE REQUEST"
    TASK = "TASK"
    INCIDENT = "INCIDENT"
    CHANGE_REQUEST = "CHANGE REQUEST"
    SUPPORT_HELPDESK = "SUPPORT/HELPDESK"
    DOCUMENTATION = "DOCUMENTATION"
    SECURITY = "SECURITY"
    FEEDBACK = "FEEDBACK"
    OTHER = "OTHER"