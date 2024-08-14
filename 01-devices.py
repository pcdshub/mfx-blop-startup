# Load most devices from happi
from happi import Client

client = Client.from_config("/cds/group/pcds/pyps/apps/hutch-python/device_config/happi.cfg")

mirror = client.load_device(name="mr1l4_homs")

dg1_ipm = client.load_device(name="mfx_dg1_ipm")
dg1_pim = client.load_device(name="mfx_dg1_pim")
dg2_ipm = client.load_device(name="mfx_dg2_ipm")
dg2_pim = client.load_device(name="mfx_dg2_pim")

# Add missing wave8 (not in happi right now)
from pcdsdevices.ipm import Wave8

dg1_wave8 = Wave8("MFX:DG1:BMMON", name="mfx_dg1_wave8")
dg1_wave8.sum.kind = "hinted"
dg2_wave8 = Wave8("MFX:DG2:BMMON", name="mfx_dg2_wave8")
dg2_wave8.sum.kind = "hinted"
