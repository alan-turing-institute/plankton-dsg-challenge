# see notebook random_forest_label2.ipynb

# Creating a bar plot

my_barplot = sns.barplot(x=feature_imp, y=feature_imp.index)

fig = my_barplot.get_figure()

plt.rcParams['figure.figsize'] = [6, 10]

#plt.rcParams['figure.dpi'] = 100

# Add labels to your graph

plt.xlabel('Feature Importance Score', fontsize = 16)

plt.ylabel('Features', fontsize = 16)

plt.xticks(fontsize=12)

plt.tight_layout()

plt.show()

fig.savefig('/output/report_figs/feature_importance_label2_RF.png')
