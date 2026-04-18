import numpy as np
import torch
import torch.nn
import torch.optim as optim
import os
import pandas as pd
import math
import chess.pgn
import io
from utils import data_utils

print(torch.__version__)
device = torch.device("mps")
DATA_PATH = os.path.join(os.environ['DATA_ROOT'], "lichess-01-23", "samples")
DATA_FILE = os.path.join(
    DATA_PATH,
    "small_sample.parquet"
)

data_df = data_utils.load_data_without_clk(DATA_FILE)