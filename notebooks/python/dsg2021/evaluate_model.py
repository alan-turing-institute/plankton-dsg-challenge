# evaluate_model.py>

# this file contains three functions:
# 1. model_metrics: calculate accuracy, precision, recall and f1_score using precomputed confusion matrix
# 2. plot_precision_recall: plot precision-recall curve for two-class problem
# 3. plot_roc: plot ROC curve for two-class problem

# import libraries
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt

# function
def model_metrics(confusion_matrix):
    true_pos = np.diag(confusion_matrix)
    false_pos = np.sum(confusion_matrix, axis=0) - true_pos
    false_neg = np.sum(confusion_matrix, axis=1) - true_pos

    precision = (true_pos / (true_pos + false_pos))
    recall = (true_pos / (true_pos + false_neg))
    f1 = 2*precision*recall / (precision + recall)
    accuracy = np.sum(confusion_matrix.diagonal())/np.sum(confusion_matrix)

    precision = np.mean(precision)
    recall = np.mean(recall)
    f1 = np.mean(f1)

    return accuracy, precision, recall, f1

# function
# reference: https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/
def plot_precision_recall(clf, X_test, y_test, y_pred):
    # predict class probabilities for X_test
    probs = clf.predict_proba(X_test)
    
    # keep probabilities for the positive class only
    probs = probs[:,1]
    precision, recall, _ = metrics.precision_recall_curve(y_test, probs)
    f1 = metrics.f1_score(y_test, y_pred)
    auc = metrics.auc(recall, precision)
    
    # summarize scores
    print('RndomForest: f1=%.3f AUC=%.3f' % (f1, auc))
    
    # plot the precision-recall curves
    no_skill = len(y_test[y_test==1]) / len(y_test)
    fig = plt.figure()
    plt.plot([0, 1], [no_skill, no_skill], linestyle = "--", label = "No-Skill")
    plt.plot(recall, precision, marker = ".", label = "RandomForest")
    
    # axis labels
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    # show legend
    plt.legend()
    
    return fig

# function
def plot_roc(clf, X_test, y_test):
    # predict class probabilities for X_test
    probs = clf.predict_proba(X_test)
    
    # keep probabilities for the positive class only
    probs = probs[:, 1]
    # calculate scores
    auc = metrics.roc_auc_score(y_test, probs)
    # summarize scores
    print('ROC AUC=%.3f' % (auc))
    
    fig = plt.figure()
    # calculate roc curves
    fpr, tpr, _ = metrics.roc_curve(y_test, probs)
    # plot the roc curve for the model
    plt.plot([0, 1], [0, 1], linestyle='--', label = 'No-Skill')
    plt.plot(fpr, tpr, marker='.', label='RandomForest')
    
    # axis labels
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    # show the legend
    plt.legend()

    return fig
