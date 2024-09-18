from xopt import VOCS, Evaluator, Xopt
from xopt.generators import ExpectedImprovementGenerator

def xopt_evaluate(input):
    mirror_pitch = input["mirror_pitch"]
    mirror.pitch.set(mirror_pitch)
    time.sleep(1)
    xpos = dg1_wave8.xpos # .get?
    results["xpos"] = xpos
    results["objective"] = (xpos - DG1_WAVE8_XPOS)**2
    return results

class XAgent:
    
    def __init__(self):
        vocs = VOCS(variables={"mirror_pitch":[MIRROR_NOMINAL-SEARCH_DELTA,MIRROR_NOMINAL+SEARCH_DELTA]},
                objectives={"objective":"MINIMIZE"})
        evaluator = Evaluator(function=xopt_evaluate)
        generator = ExpectedImprovementGenerator(vocs=vocs)
        # by default Bayesian generators assume NO noise
        generator.gp_constructor.use_low_noise_prior = False
        self.X = Xopt(vocs=vocs,evaluator=evaluator,generator=generator)
        print(self.X)

    def random_sampling(self, n_samples=3):
        # To do random sampling at the beginning
        self.X.random_evaluate(n_samples)

    def learn(self, n_steps=20):
        # To run the optimization
        for i in range(n_steps):
            self.X.step()

    def visualize_model(self):
        # Visualize model
        self.X.generator.visualize_model()
        plt.show()

    def plot_objectives(self):
        # Visualize progress of optimization
        self.X.data.plot(x="mirror_pitch",y="objective") # replace objective with xpos if desired

# The model built here corresponds to the objective, not X position. More steps to get that model.

