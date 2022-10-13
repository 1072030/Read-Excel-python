from cProfile import label
from random import Random
from urllib import response
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import io
import random
from fastapi import Response
def outputImage(data:dict):
    print(data['密封圈'])
    r = random.randint(1,40)
    fig = sns.histplot(data['密封圈'],bins=40).get_figure()
    with io.BytesIO() as fig_bytes:
        fig.savefig(fig_bytes,format='png')
        fig_bytes.seek(0)
        response = Response(fig_bytes.getvalue(),media_type='image/png')
        return response