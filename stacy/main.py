# patricia.stacy.main.py

import numpy as np
from scipy import stats

jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
np.mean(jogadores)
np.median(jogadores)
np.quantile(jogadores, [0, 0.25, 0.50, 0.75, 1])
np.std(jogadores, ddof=1)

stats.describe(jogadores)
