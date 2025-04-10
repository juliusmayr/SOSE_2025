from my_classes import Subject, Supervisor, Experiment
from my_classes import Person, estimate_max_hr, calculate_age
from datetime import datetime, date
if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("FirstName", "LastName")
    subject = Subject("FirstName", "LastName", "female", 30)
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)


    print(experiment)