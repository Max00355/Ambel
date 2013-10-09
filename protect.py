import hashlib

salt = "11asd33''1]3'1'23''sf'''23'12312;3;sa'df'sdf''35'56''36'26'2'266'262'26'26'62'ds'f'sd's'123'123'sdf;sd;f'w35'234'12'"

def protect(string):
    for x in range(1000):
        string = hashlib.sha512(string).hexdigest()
    return string
