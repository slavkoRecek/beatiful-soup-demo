from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    logo_url: str


@dataclass
class Page:
    name: str
    customers: list[Customer]
