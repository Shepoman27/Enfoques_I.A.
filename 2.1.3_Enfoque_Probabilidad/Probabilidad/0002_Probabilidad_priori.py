def posterior_probability(height, weight, training_data):
    # modelo de probabilidad a posteriori
    male_count = 0
    female_count = 0
    for data_point in training_data:
        if data_point['gender'] == 'male':
            male_count += 1
        else:
            female_count += 1
    male_probability = male_count / len(training_data)
    female_probability = female_count / len(training_data)
    prior = prior_probability(height, weight)
    male_posterior = (male_probability * prior) / ((male_probability * prior) + (female_probability * (1 - prior)))
    female_posterior = (female_probability * (1 - prior)) / ((male_probability * prior) + (female_probability * (1 - prior)))
    return {'male': male_posterior, 'female': female_posterior}
