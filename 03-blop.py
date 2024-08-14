from blop import DOF, Objective, Agent
from blop.utils import prepare_re_env

from IPython import get_ipython
ip = get_ipython()
ip.run_line_magic("run", "-i $prepare_re_env.__file__ --db-type=temp")
bec.disable_plots()

# Center position most commonly close to the trajectory
MIRROR_NOMINAL = -535
# Search +- the delta from the nominal
SEARCH_DELTA = 5
# WAVE8 goal positions
DG1_WAVE8_XPOS = 0
# DG2 unused for now
DG2_WAVE8_XPOS = 0
# How close are we trying to get to the target?
WAVE8_TOL = 0.1
# If the WAVE8 poxition is above this value or below negative this value, don't trust the value
WAVE8_MAX_VALUE = 10

dofs = [
    DOF(
        description="MFX Mirror",
        device=mirror.pitch,
        search_domain=(MIRROR_NOMINAL - SEARCH_DELTA, MIRROR_NOMINAL + SEARCH_DELTA),
    ),
]

objectives = [
    Objective(
        name="mfx_dg1_wave8_xpos",
        target=(DG1_WAVE8_XPOS - WAVE8_TOL, DG1_WAVE8_XPOS + WAVE8_TOL),
        trust_domain=(-1 * WAVE8_MAX_VALUE, WAVE8_MAX_VALUE),
    ),
]

agent = Agent(
    dofs=dofs,
    objectives=objectives,
    detectors=[dg1_wave8.xpos],
    verbose=True,
    db=db,
    tolerate_acquisition_errors=False,
    enforce_all_objectives_valid=True,
    train_every=3,
)
# RE(agent.learn("qei", n=20))
# Options for optimizer: https://github.com/NSLS-II/blop/blob/main/src/blop/bayesian/acquisition/config.yml
# Signature: https://github.com/NSLS-II/blop/blob/76ddd5a64db4a7eddd99c5d1bd3a92823b2ccb23/src/blop/agent.py#L388
