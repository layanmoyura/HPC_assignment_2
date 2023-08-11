import numpy as np
import pandas as pd

np.random.seed(3397)
df = pd.DataFrame(np.random.randint(0,100,size=(1000000, 20)))
df.to_csv('data.csv', index=False)
