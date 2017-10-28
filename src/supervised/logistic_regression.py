import os
import pandas as pd
from sklearn import linear_model


class LogisticRegression:

    def logreg(self, X, y):

        results = {}

        # According to online sources, LogisticRegression can handle multiple classes ootb
        log_reg_model = linear_model.LogisticRegression()

        log_reg_model.fit(X, y)

        results = log_reg_model.predict(X)

        accuracy = log_reg_model.score(X,y)

        # for output in results:
        #     if output != 0:
        #         print(output)

        return (results, accuracy)





def main():
    # Create dataframe
    path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    path += '/data/creditcard.csv'
    df = pd.read_csv(path)

    # X and Y used for sklearn logreg
    X = df.drop("Class", axis=1).drop("Time", axis=1)
    y = df["Class"]

    logistic_regression = LogisticRegression()

    total = logistic_regression.logreg(X,y)
    print(total[0])
    print(total[1])

    # print("Number of positives = " + str(len(results)))
    # print(logistic_regression.accuracy())



if __name__ == '__main__':
    main()