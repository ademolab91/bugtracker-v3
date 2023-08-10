import reflex as rx
from ..models import User
from .base import State
from pydantic import EmailStr
from ..enumerations import Role
from typing import Optional


class AuthState(State):
    """The authentication state for sugnup and login"""

    name: str = ""
    email: EmailStr = ""
    password: str = ""
    confirm_password: str = ""
    role: Optional[Role]

    @rx.var
    def is_admin(self):
        """Check if user is admin"""
        return self.role == Role.ADMIN

    @rx.var
    def is_assigned_admin(self):
        """Check if user is assigned admin"""
        return self.role == Role.ASSIGNED_ADMIN

    @rx.var
    def is_project_manager(self):
        """Check if user is project manager"""
        return self.role == Role.PROJECT_MANAGER

    @rx.var
    def is_developer(self):
        """Check if user is developer"""
        return self.role == Role.DEVELOPER

    @rx.var
    def is_submitter(self):
        """Check if user is submitter"""
        return self.role == Role.SUBMITTER

    def signup(self):
        """Signup user"""
        if self.password != self.confirm_password:
            return rx.window_alert("Passwords do not match")
        with rx.session() as session:
            if session.query(User).filter_by(email=self.email).one():
                return rx.window_alert("User already exists")
            self.user = User(name=self.name, email=self.email, password=self.password)
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/dashboard")

    def login(self):
        """Login user"""
        with rx.session() as session:
            user = session.query(User).where(User.email == self.email).one_or_none()
            if user and user.password == self.password:
                self.user = user
                self.name = user.full_name
                self.role = user.role
                return rx.redirect("/")
            return rx.window_alert("Invalid credentials")
