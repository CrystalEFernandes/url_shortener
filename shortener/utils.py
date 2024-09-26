import hashlib
import string

BASE62=string.digits +string.ascii_letters
def generate_base62(num):
    if num==0:
        return BASE62[0]
    
    base62=[]
    while num:
        num,rem=divmod(num,62)
        base62.append(BASE62[rem])

    return ''.join(reversed(base62))

def generate_alias(long_url,custom_alias=None):
    if custom_alias:
        return custom_alias
    else:
        url_hash=int(hashlib.md5(long_url.encode()).hexdigest(),16)
        return generate_base62(url_hash)
