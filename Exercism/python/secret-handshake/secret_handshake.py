def commands(number: int) -> list:
    """Lists a secret handshake"""
    secret = ["wink", "double blink", "close your eyes", "jump"]
    contain = map(lambda b: bool(int(b)), f"{number:0{len(secret)+1}b}"[::-1])
    code = [s for s, b in zip(secret, contain) if b]
    return code[::-1] if next(contain) else code
