from blop import DOF, Objective, Agent
from blop.utils import prepare_re_env

from IPython import get_ipython
ip = get_ipython()
ip.run_line_magic("run", "-i $prepare_re_env.__file__ --db-type=temp")
bec.disable_plots()

dofs = [
    DOF(description="MFX Mirror", device=mirror.pitch, search_domain=(839, 840)),
]

objectives = [
    Objective(name="mfx_dg1_wave8_sum", target="max")
]

agent = Agent(
    dofs=dofs,
    objectives=objectives,
    detectors=[dg1_wave8.sum],
    verbose=True,
    db=db,
    tolerate_acquisition_errors=False,
    enforce_all_objectives_valid=True,
    train_every=3,
)
