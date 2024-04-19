class Constants:
    population_size = 500
    iteration = 1000

    weights = [
        (1, [427, 1653, 11200, 41067]),
        (1, [15, 3, 1.5, .625])
    ]
    p_min = 2_432_000
    pl_list = [5, 25, 50, 120]

    weight_names = ['cost', 'time']
    weight_prefix = ['$', 'H']

    upper_bounds = [80000, 80000, 16000, 16000]
    lower_bounds = [0, 0, 0, 0]

    # dimension
    num_coefficients = len(upper_bounds)

    trial_limit = population_size * num_coefficients // 2
    num_sources = population_size
