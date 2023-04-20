from dataclasses import dataclass

@dataclass
class Person:
    user_name: str = None
    email: str = None
    first_name: str = None
    last_name: str = None
    password: str = None