import random

from constants import Constants
from source import Source


def main():
    print(f'sources: {Constants.num_sources}')
    print(f'iterations: {Constants.iteration}')
    print(f'limit: {Constants.trial_limit}\n')

    all_sources = [Source() for _ in range(Constants.num_sources)]
    global_min = Source()
    for _ in range(Constants.iteration):
        # worker bees
        for source in all_sources:
            source.work_on(all_sources)

        # onlooker bees
        sum_fit = 0
        for source in all_sources:
            sum_fit += source.fit

        num_bees = Constants.population_size
        src_index = 0
        while num_bees > 0:
            r = random.random()
            source = all_sources[src_index]
            probability = source.fit / sum_fit
            if probability > r:
                num_bees = num_bees - 1
                source.work_on(all_sources)
            src_index = (src_index + 1) % Constants.num_sources

        # scout bees
        for i, source in enumerate(all_sources):
            if source.trials >= Constants.trial_limit:
                all_sources[i] = Source()

        # memorize best result
        local_min = min(all_sources, key=lambda x: x.obj_func)
        if local_min.obj_func < global_min.obj_func:
            global_min = local_min
    print(global_min)


if __name__ == '__main__':
    main()
