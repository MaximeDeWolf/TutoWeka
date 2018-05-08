import sys

_string_to_bool ={
    '1': True,
    '0': False
}

def _clean_class(class_):
    """extract the class from the class text of the results
    """
    return int(class_.split(':')[-1])

def _clean_probability(proba):
    """extract the probability from the probability text of the results
    """
    return float(proba.split('*')[-1])

def extract_caravan_predictions(file_):
    """Extract the prediction from the results.
    The extracted prediction are a list of tuples.
    A tuple has this form: (#instance, predicted_class, probability)
    """
    caravan_predictions = []
    for line in file_:
        data = line.split()
        instance_number = int(data[0])
        predicted_class = _clean_class(data[2])
        probability = _clean_probability(data[4])
        caravan_predictions.append((instance_number, predicted_class, probability))
    return caravan_predictions

def select_best_predictions(predictions, class_to_select, nbr_of_instance=None):
    """Select a amount of a pecular instance among
    these that have the biggest probability.
    """
    if nbr_of_instance is None:
        nbr_of_instance = len(predictions)
    filtered_predictions = list(filter(lambda x: x[1]==class_to_select ,predictions))
    #sort according to the probability
    sorted_predictions = sorted(filtered_predictions, key=lambda x:x[2])
    sorted_predictions.reverse()
    if(len(sorted_predictions) <= nbr_of_instance):
        return sorted_predictions
    else:
        return sorted_predictions[:nbr_of_instance]

def format_predictions(predictions, nbr_of_elements, default_class):
    """Create a list that has the same format than the corrections file.
    """
    formatted_predictions = []
    #sort according to instance number
    sorted_predictions = sorted(predictions, key=lambda x:x[0])
    count = 0
    for i in range(nbr_of_elements):
        current_instance = sorted_predictions[count][0]
        #print("Current index: {}, next instance to treat: {}".format(i+1, current_instance))
        if i+1 == current_instance:
            formatted_predictions.append(sorted_predictions[count][1])
            count+=1
        else:
            formatted_predictions.append(default_class)
    return formatted_predictions

def correct_predictions(predictions, corrections, interesting_class):
    nbr_correct_prediction = 0
    for prediction, correction in zip(predictions, corrections):
        #print("Expected {} but {} found.".format(prediction, correction))
        if interesting_class == prediction and prediction == int(correction):
            nbr_correct_prediction += 1
    return nbr_correct_prediction

if __name__ == '__main__':
    predictions_file = sys.argv[1]
    corrections_file = sys.argv[2]
    predictions = open(predictions_file, 'r')
    corrections = open(corrections_file, 'r')
    #remove the first line
    predictions.readline()
    extracted_predictions = extract_caravan_predictions(predictions)
    best_predictions = select_best_predictions(extracted_predictions, 1, nbr_of_instance=800)
    predictions_results = format_predictions(best_predictions, 4000, 0)
    #print(predictions_results)
    correct_predictions = correct_predictions(predictions_results, corrections, 1)
    print(correct_predictions)
