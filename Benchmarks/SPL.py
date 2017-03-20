from __future__ import division

from deap import base, creator, tools
import re
import requests
import pdb


sign = lambda x: '1' if x>0 else '0'


def load_product_url(fm_name):
    feature_names = []
    featureNum = 0
    cnfNum = 0
    cnfs = []

    feature_name_pattern = re.compile(r'c (\d+)\$? (\w+)')
    stat_line_pattern = re.compile(r'p cnf (\d+) (\d+)')

    features_names_dict = dict()
    source = requests.get('https://zenodo.org/record/265808/files/'+fm_name+'.dimacs').text.encode('ascii').split('\n')

    for line in source:
        if line.startswith('c'):  # record the feature names
            m = feature_name_pattern.match(line)
            """
            m.group(1) id
            m.group(2) name
            """
            features_names_dict[int(m.group(1))] = m.group(2)

        elif line.startswith('p'):
            m = stat_line_pattern.match(line)
            """
            m.group(1) feature number
            m.group(2) cnf
            """
            featureNum = int(m.group(1))
            cnfNum = int(m.group(2))

            # transfer the features_names into the list if dimacs file is valid
            assert len(features_names_dict) == featureNum, "There exists some features without any name"
            for i in range(1, featureNum+1):
                feature_names.append(features_names_dict[i])
            del features_names_dict

        elif line.endswith('0'):  # the cnf
            cnfs.append(map(int, line.split(' '))[:-1])  # delete the 0, store as the lint list

        else:
            assert True, "Unknown line" + line
    assert len(cnfs) == cnfNum, "Unmatched cnfNum."

    return feature_names, featureNum, cnfs, cnfNum


class DimacsModel:
    def __init__(self, fm_name):
        self.name = fm_name
        _, self.featureNum, self.cnfs, self.cnfNum = load_product_url(fm_name)

        self.cost = []
        self.used_before = []
        self.defects = []
        while True:
            content = requests.get('https://zenodo.org/record/265807/files/'+fm_name+'.dimacs.augment')
            if content.status_code == 200: break
        lines = content.text.encode('ascii')
        lines = lines.split('\n')[1:]
        lines = map(lambda x:x.rstrip(), lines)
        for l in lines:
            if not len(l): continue
            _, a, b, c = l.split(" ")
            self.cost.append(float(a))
            self.used_before.append(bool(int(b)))
            self.defects.append(int(c))

        creator.create("FitnessMin", base.Fitness, weights=[-1.0] * 5, vioconindex=list())
        creator.create("Individual", str, fitness=creator.FitnessMin)

        self.creator = creator
        self.Individual = creator.Individual

        self.toolbox = base.Toolbox()
        self.toolbox.register("evaluate", self.eval_ind)
        self.eval = self.toolbox.evaluate

    def eval_ind(self, ind, normalized=True):
        """
        return the fitness, but it might be no needed.
        Args:
            ind:

        Returns:

        """
        convio = 0
        ind.fitness.vioconindex = []
        for c_i, c in enumerate(self.cnfs):
            corr = False
            for x in c:
                if sign(x) == ind[abs(x)-1]:
                    corr = True
                    break
            if not corr:
                ind.fitness.vioconindex.append(c_i)
                convio += 1

        unselected, unused, defect, cost = 0, 0, 0, 0
        for i, selected in enumerate(map(int, ind)):
            if not selected:
                unselected += 1
            else:
                cost += self.cost[i]
                if self.used_before[i]:
                    defect += self.defects[i]
                else:
                    unused += 1
        if normalized:
            ind.fitness.values = (convio/self.cnfNum,
                                  unselected/self.featureNum,
                                  unused/self.featureNum,
                                  defect/sum(self.defects),
                                  cost/sum(self.cost))
        else:
            ind.fitness.values = (convio, unselected, unused, defect, cost)


        return ind.fitness.values


if __name__ == '__main__':
    p = DimacsModel('webportal')
