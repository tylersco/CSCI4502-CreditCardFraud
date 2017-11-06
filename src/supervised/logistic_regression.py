import os
import pandas as pd
from sklearn import linear_model, metrics, model_selection
import matplotlib.pyplot as plt


class LogisticRegression:

    def plotROC(self, fpr, tpr, auc):
        plt.figure()
        lw = 2
        plt.plot(fpr, tpr, color='darkorange',
                 lw=lw, label='ROC curve (area = %0.2f)' % auc)
        plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Logistic Regression ROC')
        plt.legend(loc="lower right")
        plt.show()

    def logreg(self, X, y, test):

        # Associate higher weight (of 2) with the positive class:
        weights = {1: 5, 0: 1}

        '''
        The “balanced” mode uses the values of y to automatically adjust weights inversely proportional to class 
            frequencies in the input data as n_samples / (n_classes * np.bincount(y)).
        '''
        log_reg_model = linear_model.LogisticRegression(class_weight='balanced')
        log_reg_model.fit(X, y)
        results = log_reg_model.predict(test.drop("Class", axis=1).drop("Time", axis=1))
        accuracy = log_reg_model.score(test.drop("Class", axis=1).drop("Time", axis=1), test["Class"])
        confusion = metrics.confusion_matrix(test["Class"], results)

        # AUC and ROC measures
        fpr, tpr, thresholds = metrics.roc_curve(test["Class"], results)
        auc = metrics.auc(fpr, tpr)

        print(auc)

        # Plot ROC

        self.plotROC(fpr, tpr, auc)

        return results, accuracy, confusion


def main():
    # Create dataframe
    path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    path += '/data/creditcard.csv'
    df = pd.read_csv(path)

    #Create train and test groups
    train, test = model_selection.train_test_split(df)

    # X and Y used for sklearn logreg
    X = train.drop("Class", axis=1).drop("Time", axis=1)
    y = train["Class"]

    logistic_regression = LogisticRegression()

    total = logistic_regression.logreg(X, y, test)
    print(total[0])
    print(total[1])
    print(total[2])


if __name__ == '__main__':
    main()