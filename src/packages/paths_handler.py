import os
from decouple import config

class PathHandler:
    def __init__(self):
        self.mcda = config('MCDA_SCRIPT_PATH')
        self.geoprocess = config('GEOPROCESS_SCRIPT_PATH')
        self.gronormalize = config('GEONORMALIZE_SCRIPT_PATH')
