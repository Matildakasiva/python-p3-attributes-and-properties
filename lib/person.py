#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    pass
    approved_jobs = APPROVED_JOBS
    def __init__(self, name="", job=""):
        self.name = name
        self.job = job

    def set_name(self, name):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return
        self._name = name.title()

    def get_name(self):
        return self._name

    name = property(get_name, set_name)

    def set_job(self, job):
        if job not in self.approved_jobs:
            print("Job must be in list of approved jobs.")
            return
        self._job = job

    def get_job(self):
        return self._job

    
