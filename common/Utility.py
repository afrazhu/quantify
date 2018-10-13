import os

class Utility(object):

    def mkdir(self, path):
        folder = os.path.exists(path)
        if not folder:
            os.makedirs(path)

    def addTwoDimDict(self, dict, key_a, key_b, val):
        if key_a in dict:
            dict[key_a].update({key_b: val})
        else:
            dict.update({key_a: {key_b: val}})

        return dict

utility = Utility()