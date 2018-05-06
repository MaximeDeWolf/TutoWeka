import sys

_string_to_bool ={
    '1': True,
    '0': False
}

def _clean_class(class_):
    return _string_to_bool[class_.split()[-1]]

def _clean_probability(proba):
    return float(proba.split('*')[0])

def extract_caravan_predictions(file_):
    caravan_predictions = []
    for line in file_:
        data = line.split()
        instance_number = data[0]
        predicted_class = _clean_class(data[2])
        probability = _clean_probability(data[4])
        caravan_predictions.append((instance_number, predicted_class, probability))
    return caravan_predictions

if __name__ == '__main__':
    predictions_file = sys.argv[1]
    corrections_file = sys.argv[2]
    predictions = open(predictions_file, 'r')
    corrections = open(corrections_file, 'r')
    #remove the first lie
    predictions.readline()
    extracted_predictions = extract_caravan_predictions(predictions)
