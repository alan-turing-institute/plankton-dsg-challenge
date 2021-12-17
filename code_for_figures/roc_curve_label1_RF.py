# check notebook random_forest_label1.ipynb
from evaluate_model import plot_roc
plt.rcParams['figure.figsize'] = [5, 5]
plt.rcParams['figure.dpi'] = 100
fig = plot_roc(clf, X_test, y_test)
plt.xlabel('False Positive Rate', fontsize=14)
plt.ylabel('True Positive Rate', fontsize=14)
plt.legend(prop={'size': 12})
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('/output/report_figs/roc_curve_label1_RF.png')
