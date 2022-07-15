from utils import *


__author__ = 'kqureshi,zlisto'


def alpha_calculation(interactions) -> pd.Series:
    """
    Compute alphas using interactions data
    """    
    n = interactions.groupby(COIN)[INTERACTIONS].sum()
    L1, L2, L3 = [n[k].sum() for k in INTERACTIONS]
    N = n.sum().sum()
    n_c = interactions.groupby(COIN)[INTERACTIONS].sum().sum(axis=1)
    v_c = interactions.groupby(COIN).apply(lambda x: x[['num_tweets']].T.dot(x.followers_count)).num_tweets
    return ((N/ L1) * n_c.div(v_c)).sort_values()

def fetch_alphas() -> pd.Series:
    interactions = pd.read_parquet(INTERACTIONS_PATH)
    return alpha_calculation(interactions=interactions)
