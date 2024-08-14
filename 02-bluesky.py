import asyncio
from databroker import Broker
from bluesky import RunEngine
from bluesky.plans import scan
from bluesky.callbacks.best_effort import BestEffortCallback

loop = asyncio.get_event_loop()
RE = RunEngine({}, loop=loop)
db = Broker.named("temp")
RE.subscribe(db.insert)
bec = BestEffortCallback()
RE.subscribe(bec)


from ophyd.sim import det, motor

motor.delay = 0.5
