# check notebook random_forest_label2_with_detritus.ipynb

plt.rcParams['figure.dpi'] = 100

plt.rcParams['figure.figsize'] = [10, 8]

my_plot = metrics.plot_confusion_matrix(clf, X_test, y_test, display_labels = LE.classes_,cmap='rocket')

fig = my_plot.figure_

plt.xlabel('Predicted label', fontsize=12)

plt.ylabel('True label', fontsize=12)

plt.show()

fig.savefig('/output/report_figs/confusion_matrix_label2_with_detritus_RF.png')
