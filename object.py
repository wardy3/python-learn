import pprint
pp = pprint.PrettyPrinter(indent=4)

class switch(object):
    def __init__(self, switch_name):
        self.switchname = switch_name
        self.int = dict()

    def show_flogi(self):
        print("Running a sh flogi da on switch %s" % self.switchname)

        self.int["fc1/1"] = { "vsan": 3, "pwwn": "10:00:23", "alias": "host_hba6"}
        self.int["fc1/2"] = { "vsan": 3, "pwwn": "10:00:33", "alias": "host_hba5"}
        self.int["fc1/2"] = { "vsan": 3, "pwwn": "10:00:43", "alias": "host_hba4"}
        self.int["fc2/4"] = { "vsan": 1, "pwwn": "10:00:53", "alias": "host_hba3"}
        self.int["fc2/5"] = { "vsan": 3, "pwwn": "10:00:63", "alias": "host_hba2"}
        self.int["fc2/6"] = { "vsan": 3, "pwwn": "10:00:73", "alias": "host_hba1"}


switch1 = switch("aurfcseg1")

switch1.show_flogi()

pp.pprint(switch1)