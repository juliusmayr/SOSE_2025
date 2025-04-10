from my_functions import build_experiment
from my_functions import build_person
from my_functions import estimate_max_hr
from datetime import datetime
if __name__ == "__main__":

    print(build_experiment(
        'Maximale_HF',
        'datetime',
        'Julius Mayr',
        'Maximale Leistung'
    ))
    
    print(build_person (
        'Simon',
        'Schwarzer',
        'male',
        23
    ))
   

    print(estimate_max_hr (
        23,
        'male'
    ))
   