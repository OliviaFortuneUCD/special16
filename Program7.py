import seaborn as sns
sns.set_theme()

# Load the penguins dataset
mpg = sns.load_dataset("mpg")

# Plot sepal width as a function of sepal_length across days
g = sns.lmplot(
    data=mpg,
    x="horsepower", y="mpg", hue="origin",
    height=5
)

# Use more informative axis labels than are provided by default
g.set_axis_labels("horsepower", "mpg")