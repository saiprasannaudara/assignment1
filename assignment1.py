# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:59:49 2023

@author: prasanna_udara
"""
# Import pandas and matplot library packages
import pandas as pd
import matplotlib.pyplot as plt


def line_plot(df, x_para, y_para):
    '''
    Function defined to illustrate lineplot using the following parameters:
    dataframe and axes. With the dataset, a lineplot between work year and
    salary based on the level of employment.
    '''
    # Defining the data
    df['experience_level'] = df['experience_level'].replace({
        'SE': 'Senior',
        'EN': 'Entry',
        'EX': 'Executive',
        'MI': 'Mid',
    })
    year = df.groupby(['experience_level', x_para])[y_para].mean()\
        .reset_index()
    grouped = year.groupby('experience_level')

    # Intialization of the figure
    plt.figure(figsize=(10, 6))

    # Calling the plot function to display lineplot
    for name, group in grouped:
        plt.plot(group[x_para], group[y_para], label=name)

    # Define the plot title
    plt.title("Data Job Salaries respective with year")

    # Axes labelling
    plt.xlabel("Year of work")
    plt.ylabel("Gross Salary")

    # Display grid
    plt.grid()

    # Removing whitespace surrounding the graph
    plt.xlim(group[x_para].min(), group[x_para].max())

    # Display legend
    plt.legend()

    # Save the figure
    plt.savefig("lineplot.png")


def bar_plot(df, x_para, y_para):
    '''
    Function defined to illustrate barplot using the following parameters:
    dataframe and axes. With the dataset, a barplot between level of experience
    and average salary.
    '''
    # Defining the data
    grouped = df.groupby(x_para)[y_para].mean().reset_index()

    # Intialization of the figure
    plt.figure(figsize=(10, 6))

    # Call the plot function to display barplot
    plt.bar(grouped[x_para], grouped[y_para], width=0.4)

    # Define the plot title
    plt.title("Average salary based on Experience level")

    # Axes labelling
    plt.xlabel("Level of Experience")
    plt.ylabel("Average Salary")

    # Save the figure
    plt.savefig("barplot.png")


def pie_plot(df, col_name, year):
    '''
    Function defined to illustrate piechart using the following parameters:
    dataframe and column name. A pieplot is displayed with the company size in
    the given year.
    '''
    # Defining the data
    year_2023 = df[df['work_year'] == year]
    data = year_2023[col_name].replace({'S': 'Small', 'M': 'Medium',
                                        'L': 'Large'})
    labels = data.unique()
    sizes = data.value_counts()

    # Intialization of the figure
    plt.figure(figsize=(10, 6))

    # Call the plot function to display piechart
    plt.pie(sizes, autopct='%1.1f%%')

    # Define the plot title
    plt.title("Size of the companies during " + str(year))

    # Axes labelling
    plt.legend(labels)

    # Save the figure
    plt.savefig("pieplot.png")


def main():
    # Creating a dataframe using pandas from CSV file
    df = pd.read_csv("salaries.csv")

    # Calling line_plot function with dataframe, x_axis and y_axis values
    line_plot(df, 'work_year', 'salary')

    # Calling bar_plot function with dataframe, x_axis and y_axis values
    bar_plot(df, 'experience_level', 'salary')

    # Calling pie_plot function with dataframe and column name as 'restecg'
    pie_plot(df, "company_size", 2023)


if __name__ == "__main__":
    # Calling main program
    main()
