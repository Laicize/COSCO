from .Workload import *
from datetime import datetime
from framework.database.Database import *

class DFW(Workload):
    def __init__(self, num_workloads,database):
        super().__init__()
        self.num_workloads = num_workloads
        self.db = database
        
    def generateNewContainers(self, interval):
        workloadlist = []
        containers = []
        applications = ['yolo', 'pocketsphinx', 'aeneas']
        for i in range(self.num_workloads):
            CreationID = self.creation_id
            appSelection = np.random.randint(0,2)
            application = applications[appSelection]
            workloadlist.append((CreationID, application))
            print(application)
            self.creation_id += 1
        self.createdContainers += workloadlist
        self.deployedContainers += [False] * len(workloadlist)
        return self.getUndeployedContainers()