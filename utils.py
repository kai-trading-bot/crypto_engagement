import os
import pandas as pd
from utils import *

ROOT = os.path.dirname(os.path.abspath(__file__))
COIN = 'coin'
INTERACTIONS = ['like_count', 'reply_count', 'retweet_count']
INTERACTIONS_PATH = ROOT + '/data/interactions.parquet.gz'

