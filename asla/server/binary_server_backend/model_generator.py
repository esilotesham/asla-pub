from databasehelper import DatabaseHelper
import pickle
import os


class ModelGenerator:
    """
    The classifier class that will invoke the classifier on some data
    """

    def __init__(self, classifier):
        self.model = None
        self.scaler = None
        self.db_helper = DatabaseHelper()
        self.classifier = classifier

    def train(self):
        """
        Trains on data with an ML Classification Algorithm
        Creates a model and a scaler to be used for prediction
        Stores the model and the scaler in the database
        """
        x, y = self.get_data()
        self.model, self.scaler = self.classifier.create_model(x, y)

    def get_data(self):
        """Returns the features(x) and the labels(y) to train on"""
        y_train = []
        x_train = []
        try:
            training_data = self.db_helper.check_and_fetch(True)
            root_path = os.path.dirname(os.path.abspath('..'))
            rel_path = 'binary_server_backend/headers.csv'
            headers_file = os.path.join(root_path, rel_path)
            print headers_file
            header_string = open(headers_file)
            headers = header_string.read().split(',')
            for datum in training_data:
                x_train_row = []
                y_train.append(float(datum['label']))
                for header in headers[1:]:
                    x_train_row.append(float(datum[header]))
                x_train.append(x_train_row)
        except Exception:
            print Exception
        return x_train, y_train

    def store_model(self):
        """Stores the model in the database"""
        model = pickle.dumps(self.model)
        scaler = pickle.dumps(self.scaler)
        self.db_helper.put_model(model, scaler)
