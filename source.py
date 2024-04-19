import random
from numpy import dot

from constants import Constants


class Source:
    def __init__(self):
        while True:
            self.features = [random.uniform(0, ub) for ub in Constants.upper_bounds]
            if Source.in_constraints(self.features):
                break
        self.obj_func = self.calc_obj_func(self.features)
        self.fit = self.calc_fit(self.obj_func)
        self.trials = 0

    def work_on(self, sources: list):
        diff = self
        while diff.features == self.features:
            # ,,,
            diff = random.choice(sources)

        ind = random.randint(0, len(self.features) - 1)
        y = self.features[ind]
        yp = diff.features[ind]

        while True:
            fi = random.uniform(-1, 1)
            y_new = y + fi * (y - yp)

            new_features = self.features.copy()
            new_features[ind] = y_new
            if Source.in_constraints(new_features):
                break

        new_obj_func = Source.calc_obj_func(new_features)
        new_fit = Source.calc_fit(new_obj_func)

        if new_fit > self.fit:
            self.features = new_features
            self.obj_func = new_obj_func
            self.fit = new_fit
            self.trials = 0
        else:
            self.trials += 1

    @staticmethod
    def calc_fit(x: float) -> float:
        if x >= 0:
            return 1 / (1 + x)
        return 1 + abs(x)

    @staticmethod
    def in_constraints(features: list[float]) -> bool:
        if dot(features, Constants.pl_list) > Constants.p_min:
            for feature in features:
                if feature <= 0:
                    return False
            return True
        return False

    @staticmethod
    def calc_obj_func(features: list[float]) -> float:
        result = 0
        for weight, coefficients in Constants.weights:
            c = weight * dot(features, coefficients)
            result += c
        return result

    def __repr__(self) -> str:
        def format_output(i, coefficients):
            x = dot(self.features, coefficients) / 1_000_000
            return f'{Constants.weight_names[i]}: {round(x, 2)}M{Constants.weight_prefix[i]}'

        obj_funcs = [format_output(i, coefficients) for i, (_, coefficients) in enumerate(Constants.weights)]
        feats = [f'L{i + 1}: {round(feat)}' for i, feat in enumerate(self.features)]
        p_total = round(dot(self.features, Constants.pl_list) / 1_000_000, 2)
        return (f'features: {', '.join(feats)}\n'
                f'{', '.join(obj_funcs)}\n'
                f'p total = {p_total}GB')
