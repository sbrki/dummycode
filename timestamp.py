import pytz
from datetime import datetime
ts = int(datetime.now(pytz.timezone("Europe/Zagreb")).timestamp())
print(ts)
