import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df=pd.read_csv(r"C:\Users\Python\Project Python\Data-Analysis-with-Python-Projects-FreeCodeCamp\Page_View_Time_Series_Visualizer\fcc-forum-pageviews.csv",
               index_col='date')

# Clean the data by filtering out days when the page 
# views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
clean_data = df[(df["value"] >= df["value"].quantile(0.025)) & 
                (df["value"] <= df["value"].quantile(0.097))]


# Create a 'draw_line_plot' function that uses Matplotlib to draw a line chart. The title should 
# be 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019'. 
# The label on the x axis should be 'Date' and the label on the y axis should be 'Page Views'.
def draw_line_plot(data):
    data = data.reset_index()
    fig =data.plot(kind="line", x="date", y="value")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.savefig(r"C:\Users\Python\Project Python\Data-Analysis-with-Python-Projects-FreeCodeCamp\Page_View_Time_Series_Visualizer\Figure1.png")
    return fig


