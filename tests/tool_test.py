# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_haversine():
    #lat1, lon1 = 48.865070, 2.380009
    #Insert your coordinates from google maps here
    #lat2, lon2 = 51.527870, -0.143490
    out = haversine(48.865070, 2.380009, 48.235070, 2.393409)

    assert out == 70.00789153218594
