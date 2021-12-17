# check notebook random_forest_label1.ipynb
from evaluate_model import plot_precision_recall
plt.rcParams['figure.figsize'] = [5, 5]
plt.rcParams['figure.dpi'] = 100
fig = plot_precision_recall(clf, X_test, y_test, y_pred)
plt.xlabel('Recall', fontsize=14)
plt.ylabel('Precision', fontsize=14)
plt.legend(prop={'size': 12})
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('/output/report_figs/precision_recall_label1_RF.png')
