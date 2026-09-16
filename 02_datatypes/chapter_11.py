# import arrow
from collections import namedtuple

# brewing_time = arrow.utcnow()
# brewing_time.to("Europe/Rome")

chaiProfiles = namedtuple("chaiProfile", ["flavor","aroma"])

print(f"chaiProfiles {chaiProfiles}")

