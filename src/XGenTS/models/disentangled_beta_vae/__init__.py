r"""This module is the implementation of the Disentangled Beta VAE proposed in
(https://arxiv.org/abs/1804.03599).
This model adds a new parameter to the :math:`\beta`-VAE loss function corresponding to the target 
value for the KL between the prior and the posterior distribution. It is progressively increased
throughout training.


Available samplers
-------------------

.. autosummary::
    ~XGen.samplers.NormalSampler
    ~XGen.samplers.GaussianMixtureSampler
    ~XGen.samplers.TwoStageVAESampler
    ~XGen.samplers.MAFSampler
    ~XGen.samplers.IAFSampler
    :nosignatures:
"""

from .disentangled_beta_vae_config import DisentangledBetaVAEConfig
from .disentangled_beta_vae_model import DisentangledBetaVAE

__all__ = ["DisentangledBetaVAE", "DisentangledBetaVAEConfig"]
