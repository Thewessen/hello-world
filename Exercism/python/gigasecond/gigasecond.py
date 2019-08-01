from datetime import timedelta


def add(moment):
    """Calculate the moment when someone has lived for 10^9 seconds."""
    return moment + timedelta(seconds=10**9)
