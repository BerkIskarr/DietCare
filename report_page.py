from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QTextEdit,  QHeaderView
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSignal, QObject, QThread

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from numpy.polynomial.polynomial import Polynomial


import numpy as np

import sqlite3
from Food_data import Food_data
# Worker to handle functions inside of the report_page class(make it faster)
class Worker(QObject):
    finished = pyqtSignal()
    layoutCleared = pyqtSignal()
    update_layout_1 = pyqtSignal()
    update_layout_2 = pyqtSignal()
    update_layout_3 = pyqtSignal()
    requestClearLayout = pyqtSignal()
    # Gives the signal
    def run(self):
        self.requestClearLayout.emit()
        self.finished.emit()

class Report_Page(QWidget):
    def __init__(self, daily_tab, weekly_tab, monthly_tab, GoalClorieBMR, calculate_goal_dietary_goal,info=None, start_date=None, end_date=None, parent=None):
        super().__init__()


        self.info = info
        self.start_date = start_date
        self.end_date = end_date
        # Date difference between start and end dates
        self.date_difference = self.start_date.daysTo(self.end_date)
        self.food_data = Food_data()  # Create an instance of the Food_data class
        # List of food containing all the foods in csv
        self.food_list = self.food_data.foods_list
        self.GoalCalorieBMR = GoalClorieBMR
        # Dictionary storing all the saved user food selection data as (date:breakfast[{name:abc, carbohydrate: 12323}])
        self.food_dict = self.get_dict_from_data()
        # Calculates all the foods' nutrient inside of the food dict, and saves in meals
        self.total_daily_food_dict = self.calc_all_nutrient()

        # Goal for nutrients
        self.CarbGoal = self.calculate_goal_macro_nutrients()[0]
        self.ProtGoal = self.calculate_goal_macro_nutrients()[1]
        self.FatGoal = self.calculate_goal_macro_nutrients()[2]
        self.SugarGoal = calculate_goal_dietary_goal[0]
        self.PotassiumGoal = calculate_goal_dietary_goal[1]
        self.SaltGoal = calculate_goal_dietary_goal[2]

        # layouts for pages
        self.layout1 = QVBoxLayout()
        daily_tab.setLayout(self.layout1)
        self.layout2 = QVBoxLayout()
        weekly_tab.setLayout(self.layout2)
        self.layout3 = QVBoxLayout()
        monthly_tab.setLayout(self.layout3)


        self.worker = Worker()  # Instantiate the worker
        self.thread = QThread()  # Prepare the thread
        self.worker.moveToThread(self.thread)  # Move the worker to the thread


        # Connect signals to slots
        self.worker.requestClearLayout.connect(self.clearLayoutsSafe)
        self.worker.update_layout_1.connect(self.daily_tab_contents)
        self.worker.update_layout_2.connect(self.weekly_tab_contants)
        self.worker.update_layout_3.connect(self.monthly_tab_contents)
        self.worker.layoutCleared.connect(self.updateLayouts)

        # Start the worker's process
        self.thread.started.connect(self.worker.run)
        self.thread.start()



    def updateLayouts(self):
        # Now safe to update layouts
        self.worker.update_layout_1.emit()
        self.worker.update_layout_2.emit()
        self.worker.update_layout_3.emit()

    # refresh the content when time changed
    def refresh_content(self, start_date, end_date, GoalClorieBMR, calculate_goal_dietary_goal):
        self.start_date = start_date
        self.end_date = end_date
        self.date_difference = self.start_date.daysTo(self.end_date)

        # Recalculate these based on the new dates
        self.food_dict = self.get_dict_from_data()
        self.total_daily_food_dict = self.calc_all_nutrient()

        self.GoalCalorieBMR = GoalClorieBMR
        # Goal for nutrients
        self.CarbGoal = self.calculate_goal_macro_nutrients()[0]
        self.ProtGoal = self.calculate_goal_macro_nutrients()[1]
        self.FatGoal = self.calculate_goal_macro_nutrients()[2]
        self.SugarGoal = calculate_goal_dietary_goal[0]
        self.PotassiumGoal = calculate_goal_dietary_goal[1]
        self.SaltGoal = calculate_goal_dietary_goal[2]

        # Clear existing content from layouts
        self.worker.requestClearLayout.emit()

    # Clear layouts
    def clearLayoutsSafe(self):
        self.clearLayout(self.layout1)
        self.clearLayout(self.layout2)
        self.clearLayout(self.layout3)
        self.worker.layoutCleared.emit()  # Emit signal after clearing is done

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)  # Take the first item from the nested layout

            # If the child is a widget, delete it
            if child.widget():
                child.widget().deleteLater()

            # If the child is another layout, recursively clear it as well
            elif child.layout():
                self.clearLayout(child.layout())


    def get_dict_from_data(self):

        # Use a temporary variable to iterate from start to end date
        current_date = self.start_date

        # Initialize an empty list to hold all dates
        self.date_list = []

        # Loop through all dates from start to end, inclusive
        while current_date <= self.end_date:
            # Add the current date to the list, formatted as an ISO string
            self.date_list.append(current_date.toString(QtCore.Qt.ISODate))
            # Move to the next day
            current_date = current_date.addDays(1)

        # Connect to the database
        conn = sqlite3.connect('diet_tool.db')
        cursor = conn.cursor()

        # Format dates as strings for the SQL query
        formatted_start_date = self.start_date.toString(QtCore.Qt.ISODate)
        formatted_end_date = self.end_date.toString(QtCore.Qt.ISODate)
        # Execute the query to retrieve actions within the date range for the given user
        cursor.execute("""
            SELECT d.date, d.foodItems, d.meal, d.waterIntake
            FROM daily_intake d
            WHERE d.id = ? AND d.date BETWEEN ? AND ?
        """, (self.info[0], formatted_start_date, formatted_end_date))

        # Fetch all the results
        result = cursor.fetchall()

        # Close the connection to the database
        conn.close()

        # Initialize food_dict with all dates from date_list
        food_dict = {date: {"breakfast": [], "lunch": [], "dinner": [], "snack": [], "waterIntake": 0} for date in self.date_list}

        for date, food_items, meal, water_intake in result:
            if date not in food_dict:
                continue  # Skip dates not in our predefined list

            if food_items:  # If there are food items listed
                food_list = food_items.split(' - ')
                for food_item in food_list:
                    food_id = next((item["Nutrient Data Bank Number"] for item in self.food_data.foods_list if item["Description"] == food_item), None)
                    if food_id:
                        temp = self.food_data.get_specific_list(food_id)
                        food_dict[date][meal.lower()].append(*temp)  # Ensure this matches expected structure

            # Aggregate water intake for the day
            food_dict[date]["waterIntake"] += water_intake



        return food_dict


    def calc_all_nutrient(self):
        nutrient_totals_by_date = {}

        # Iterate through each date in the food_dict
        for date, meals in self.food_dict.items():

            if date not in nutrient_totals_by_date:
                nutrient_totals_by_date[date] = {}


            # Iterate through each meal type and sum the nutrients
            for meal_type in ["breakfast", "lunch", "dinner", "snack"]:
                # Initialize the nutrient sums for the day
                nutrient_sums = {
                    "Calorie":0,
                    "Carbohydrate": 0,
                    "Protein": 0,
                    "Total Fat": 0,
                    "Monounsaturated Fat": 0,
                    "Saturated Fat": 0,
                    "Cholesterol": 0,
                    "Fiber": 0,
                    "Sugar": 0,
                    "Water": meals["waterIntake"],  # Water intake is already summed for the day
                    "Calcium": 0,
                    "Iron": 0,
                    "Selenium": 0,
                    "Choline": 0,
                    "Potassium": 0,
                    "Sodium": 0,
                    "Vitamin A": 0,
                    "Vitamin B12": 0,
                    "Vitamin B6": 0,
                    "Vitamin C": 0,
                    "Vitamin E": 0,
                    "Vitamin K": 0,
                }
                for food in meals[meal_type]:
                    # Add nutrient values from the food item to the nutrient_sums
                    nutrient_sums["Calorie"] += float(food["Calories per 100g"])
                    nutrient_sums["Carbohydrate"] += float(food["Data.Carbohydrate"])
                    nutrient_sums["Protein"] += float(food["Data.Protein"])
                    nutrient_sums["Total Fat"] += float(food["Data.Fat.Total Lipid"])
                    nutrient_sums["Monounsaturated Fat"] += float(food["Data.Fat.Monosaturated Fat"])
                    nutrient_sums["Saturated Fat"] += float(food["Data.Fat.Saturated Fat"])
                    nutrient_sums["Cholesterol"] += float(food["Data.Cholesterol"])
                    nutrient_sums["Fiber"] += float(food["Data.Fiber"])
                    nutrient_sums["Sugar"] += float(food["Data.Sugar Total"])
                    nutrient_sums["Water"] += float(food["Data.Water"])
                    nutrient_sums["Calcium"] += float(food["Data.Major Minerals.Calcium"])
                    nutrient_sums["Iron"] += float(food["Data.Major Minerals.Iron"])
                    nutrient_sums["Selenium"] += float(food["Data.Selenium"])
                    nutrient_sums["Choline"] += float(food["Data.Choline"])
                    nutrient_sums["Potassium"] += float(food["Data.Major Minerals.Potassium"])
                    nutrient_sums["Sodium"] += float(food["Data.Major Minerals.Sodium"])
                    nutrient_sums["Vitamin A"] += float(food["Data.Vitamins.Vitamin A - RAE"])
                    nutrient_sums["Vitamin B6"] += float(food["Data.Vitamins.Vitamin B6"])
                    nutrient_sums["Vitamin B12"] += float(food["Data.Vitamins.Vitamin B12"])
                    nutrient_sums["Vitamin C"] += float(food["Data.Vitamins.Vitamin C"])
                    nutrient_sums["Vitamin E"] += float(food["Data.Vitamins.Vitamin E"])
                    nutrient_sums["Vitamin K"] += float(food["Data.Vitamins.Vitamin K"])
                # After summing all nutrients for the day, store them in the totals dict
                nutrient_totals_by_date[date][meal_type] = nutrient_sums

        return nutrient_totals_by_date



    def calc_average_nutrients(self, amount_of_days):
        # Initialize a dictionary to store sums of daily averages for each meal type
        total_nutrients_by_meal = {
            "breakfast": {},
            "lunch": {},
            "dinner": {},
            "snack": {}
        }

        # Initialize the structure to store the overall averages
        nutrient_averages_by_meal = {
            "breakfast": {},
            "lunch": {},
            "dinner": {},
            "snack": {}
        }

        # Aggregate the daily averages for each meal type
        for date, meals in self.total_daily_food_dict.items():
            for meal_type in ["breakfast", "lunch", "dinner", "snack"]:
                if meal_type in meals:  # Check if the meal type exists for the date
                    meal_data = meals[meal_type]
                    for nutrient, value in meal_data.items():
                        if nutrient not in total_nutrients_by_meal[meal_type]:
                            total_nutrients_by_meal[meal_type][nutrient] = value
                        else:
                            total_nutrients_by_meal[meal_type][nutrient] += value

        # Calculate the overall average for each nutrient in each meal type
        for meal_type, nutrients in total_nutrients_by_meal.items():
            for nutrient, total in nutrients.items():
                nutrient_averages_by_meal[meal_type][nutrient] = total / amount_of_days

        return nutrient_averages_by_meal

    def calc_average_nutrients_without_meals(self, amount_of_days):
        # Initialize a dictionary to store the sums of nutrients for each date
        total_nutrients_by_date = {}

        # Initialize the structure to store the overall averages for each date
        nutrient_averages_by_date = {}

        # Aggregate the nutrient values for each date, summing across all meal types
        for date, meals in self.total_daily_food_dict.items():
            if date not in total_nutrients_by_date:
                total_nutrients_by_date[date] = {}
            for meal_type in meals.values():  # Loop through each meal type for the date
                for nutrient, value in meal_type.items():
                    if nutrient not in total_nutrients_by_date[date]:
                        total_nutrients_by_date[date][nutrient] = value
                    else:
                        total_nutrients_by_date[date][nutrient] += value

        # Calculate the overall average for each nutrient on each date
        for date, nutrients in total_nutrients_by_date.items():
            nutrient_averages_by_date[date] = {}
            for nutrient, total in nutrients.items():
                nutrient_averages_by_date[date][nutrient] = total / amount_of_days

        return nutrient_averages_by_date



    # Returns calorie intake for each meal type on each day (dict{date: {meal_type: calorie}})
    def calc_overall_daily_nutrient_average(self,nutrient_averages_by_meal, amount_of_days):
        # Initialize a dictionary to store the sums of nutrient averages
        total_nutrients = {}

        # Sum up the averages for each nutrient across all meal types
        for meal_type, nutrients in nutrient_averages_by_meal.items():
            for nutrient, average in nutrients.items():
                if nutrient not in total_nutrients:
                    total_nutrients[nutrient] = average
                else:
                    total_nutrients[nutrient] += average

        # Calculate the overall daily average for each nutrient
        overall_daily_nutrient_average = {nutrient: total/amount_of_days for nutrient, total in total_nutrients.items()}

        return overall_daily_nutrient_average

    # creates table for all nutrients
    def show_all_nutrients(self, daily_nutrients, page):
        # Headers for the table
        headers = ["Nutrient", "Value"]

        # Create two instances of QTableWidget for splitting the table
        self.table1 = QTableWidget()
        self.table2 = QTableWidget()

        # Set up the tables with headers and font
        for table in (self.table1, self.table2):
            table.setColumnCount(len(headers))
            table.setHorizontalHeaderLabels(headers)
            font = QFont()
            font.setPointSize(8)  # Smaller font size
            table.setFont(font)
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Split the data into two halves
        rows = [(nutrient, f"{value:.2f}") for nutrient, value in daily_nutrients.items()]
        half_point = len(rows) // 2

        # Set row count for both tables
        self.table1.setRowCount(half_point)
        self.table2.setRowCount(len(rows) - half_point)

        # Define a row height for rows to be thinner
        row_height = 15

        # Fill the first table with the first half of rows and set row height
        for idx in range(half_point):
            nutrient, value = rows[idx]
            self.table1.setRowHeight(idx, row_height)
            self.table1.setItem(idx, 0, QTableWidgetItem(nutrient))
            self.table1.setItem(idx, 1, QTableWidgetItem(value))

        # Fill the second table with the second half of rows and set row height
        for idx in range(half_point, len(rows)):
            self.table2.setRowHeight(idx - half_point, row_height)
            nutrient, value = rows[idx]
            self.table2.setItem(idx - half_point, 0, QTableWidgetItem(nutrient))
            self.table2.setItem(idx - half_point, 1, QTableWidgetItem(value))

        # Create a horizontal layout to hold both tables
        tables_layout = QHBoxLayout()
        tables_layout.addWidget(self.table1)
        tables_layout.addWidget(self.table2)
        if(page == 'daily'):
            # Add the tables layout to the main layout
            self.layout1.addLayout(tables_layout)
        if(page == 'weekly'):
            # Add the tables layout to the main layout
            self.layout2.addLayout(tables_layout)
        if(page == 'monthly'):
            # Add the tables layout to the main layout
            self.layout3.addLayout(tables_layout)

    def daily_tab_contents(self):
        # Find the difference between the dates
        daily_nutrients_with_meal = self.calc_average_nutrients(self.date_difference)
        daily_nutrients = self.calc_overall_daily_nutrient_average(daily_nutrients_with_meal, self.date_difference)

        self.labels_for_pie = ["Breakfast", "Lunch", "Dinner", "Snack"]
        self.values = [daily_nutrients_with_meal["breakfast"]["Calorie"],daily_nutrients_with_meal["lunch"]["Calorie"], daily_nutrients_with_meal["dinner"]["Calorie"],daily_nutrients_with_meal["snack"]["Calorie"]]

        if(self.values[0]==0 and self.values[1]==0 and self.values[2]==0 and self.values[3]==0):
            self.values = [2,2,2,2]

        # Create the pie chart
        fig = Figure(figsize=(2, 2), dpi=70)
        plot1 = fig.add_subplot(111)
        plot1.pie(self.values, labels=self.labels_for_pie, autopct='%1.1f%%')
        plot1.set_title("Daily Calorie Intake")
        canvas = FigureCanvas(fig)

        values2 = [daily_nutrients_with_meal["breakfast"]["Water"],daily_nutrients_with_meal["lunch"]["Water"], daily_nutrients_with_meal["dinner"]["Water"],daily_nutrients_with_meal["snack"]["Water"]]
        if(values2[0]==0 and values2[1]==0 and values2[2]==0 and values2[3]==0):
            values2 = [2,2,2,2]

        fig2 = Figure(figsize=(3, 3), dpi=70)
        plot2 = fig2.add_subplot(111)
        plot2.pie(values2, labels=self.labels_for_pie, autopct='%1.1f%%')
        plot2.set_title("Daily Water Intake")
        canvas2 = FigureCanvas(fig2)


        # Create horizontal layout for pie charts
        self.horizontal_layout = QHBoxLayout()

        # Add pie chart canvases to the horizontal layout
        self.horizontal_layout.addWidget(canvas)
        self.horizontal_layout.addWidget(canvas2)


        carbs = [daily_nutrients_with_meal["breakfast"]["Carbohydrate"], daily_nutrients_with_meal["lunch"]["Carbohydrate"], daily_nutrients_with_meal["dinner"]["Carbohydrate"], daily_nutrients_with_meal["snack"]["Carbohydrate"]]  # Total carbs for each meal
        protein = [daily_nutrients_with_meal["breakfast"]["Protein"], daily_nutrients_with_meal["lunch"]["Protein"], daily_nutrients_with_meal["dinner"]["Protein"], daily_nutrients_with_meal["snack"]["Protein"]]  # Total protein for each meal
        fat = [daily_nutrients_with_meal["breakfast"]["Monounsaturated Fat"]+daily_nutrients_with_meal["breakfast"]["Saturated Fat"], daily_nutrients_with_meal["lunch"]["Monounsaturated Fat"]+daily_nutrients_with_meal["lunch"]["Saturated Fat"], daily_nutrients_with_meal["dinner"]["Monounsaturated Fat"]+daily_nutrients_with_meal["dinner"]["Saturated Fat"], daily_nutrients_with_meal["snack"]["Monounsaturated Fat"]+daily_nutrients_with_meal["snack"]["Saturated Fat"]]     # Total fat for each meal
        if (carbs ==[0,0,0,0]):
            carbs = [2,2,2,2]
        if (protein ==[0,0,0,0]):
            protein = [2,2,2,2]
        if (fat ==[0,0,0,0]):
            fat = [2,2,2,2]
        # Define the labels and colors for the macronutrients
        labels = ['Carbohydrates', 'Protein', 'Fat']
        colors = ['#ff9999','#66b3ff','#99ff99']

        # The position of the bars on the x-axis
        r = range(len(carbs))

        # Plotting the bars
        fig3, ax = plt.subplots(figsize=(2, 2), dpi=70)

        ax.bar(r, carbs, color=colors[0], edgecolor='white', width=0.85, label='Carbohydrates')
        ax.bar(r, protein, bottom=carbs, color=colors[1], edgecolor='white', width=0.85, label='Protein')
        ax.bar(r, fat, bottom=[i+j for i,j in zip(carbs, protein)], color=colors[2], edgecolor='white', width=0.85, label='Fat')

        # Add labels for the meals
        plt.xticks(r, ['Breakfast', 'Lunch', 'Dinner', 'Snack'])

        # Adding the legend and title
        plt.legend()
        plt.title('Macronutrient distribution per meal')
        # Add the matplotlib figure to a canvas and set it as the central widget
        canvas3 = FigureCanvas(fig3)

        self.horizontal_layout2 = QHBoxLayout()
        self.horizontal_layout2.addWidget(canvas3)


        # Calculate difference between consumed and goal

        text = f"<b>Overall Goal: {self.GoalCalorieBMR:.2f}  |  <b>Daily Average Calorie:{daily_nutrients['Calorie']:.2f}  |  <b>Daily Average Water: {daily_nutrients['Water']:.2f}<br>"
        text_edit = QTextEdit()

        text_edit.setReadOnly(True)  # Make the text edit read-only
        text_edit.setStyleSheet("""
            QTextEdit {
                font-size: 8px;
                color: black;
                background-color: #f0f0f0;
                font-family: Arial;
            }
        """)
        text_edit.setFixedSize(170,150)

        dict_without_meals = self.calc_average_nutrients_without_meals(self.date_difference)

        date_and_calorie = {}
        date_and_carb = {}
        date_and_prot = {}
        date_and_fat = {}
        date_and_sugar = {}
        date_and_potassium = {}
        date_and_salt_sodium = {}
        for date in dict_without_meals:
            date_and_calorie[date] = dict_without_meals[date]["Calorie"]
            date_and_carb[date] = dict_without_meals[date]["Carbohydrate"]
            date_and_prot[date] = dict_without_meals[date]["Protein"]
            date_and_fat[date] = dict_without_meals[date]["Monounsaturated Fat"] + dict_without_meals[date]["Saturated Fat"]
            date_and_sugar[date] = dict_without_meals[date]["Sugar"]
            date_and_potassium[date] = dict_without_meals[date]["Potassium"]
            date_and_salt_sodium[date] = dict_without_meals[date]["Sodium"]

        dates_numeric = np.array([i for i in range(len(date_and_calorie))])  # Example: range from 0 to len-1
        calories = np.array(list(date_and_calorie.values()))
        # Prepare arrays for other nutrients
        carbs = np.array(list(date_and_carb.values()))
        prot = np.array(list(date_and_prot.values()))
        fat = np.array(list(date_and_fat.values()))
        sugar = np.array(list(date_and_sugar.values()))
        potassium = np.array(list(date_and_potassium.values()))
        salt_sodium = np.array(list(date_and_salt_sodium.values()))

        for date in dict_without_meals:
            date_and_calorie[date] = dict_without_meals[date]["Calorie"]

        dates_numeric = np.array([i for i in range(len(date_and_calorie))])  # Example: range from 0 to len-1
        threshold_date_numeric = dates_numeric[-1] + 30 # checking 30 days beyond your current data

        # Create line of best fits to predict
        p_cal = Polynomial.fit(dates_numeric, calories, 2)
        p_carb = Polynomial.fit(dates_numeric, carbs, 2)
        p_protein = Polynomial.fit(dates_numeric, prot, 2)
        p_fat = Polynomial.fit(dates_numeric, fat, 2)


        p_sugar = Polynomial.fit(dates_numeric, sugar, 2)
        p_potassium = Polynomial.fit(dates_numeric, potassium, 2)
        p_salt_sodium = Polynomial.fit(dates_numeric, salt_sodium, 2)

        threshold_date_numeric = dates_numeric[-1] + 30 # checking 30 days beyond your current data
        # Generate the early warning message
        text = self.create_text_with_early_warning(p_cal,p_sugar,p_potassium,p_salt_sodium,1, dates_numeric[0], dates_numeric[-1]+30, threshold_date_numeric, 'day', 'Daily')

        text_edit.setHtml(text)
        self.horizontal_layout2.addWidget(text_edit)

        # Add the horizontal layout to
        self.layout1.addLayout(self.horizontal_layout)
        self.layout1.addLayout(self.horizontal_layout2)


        self.show_all_nutrients(daily_nutrients,'daily')

    # Returns total_daily_food_dict but without meal seperation
    def get_daily_food_without_meal(self):
        daily_without_meal = {}
        for date in self.total_daily_food_dict:
            total = 0
            for meal in self.total_daily_food_dict[date]:
                self.total_daily_food_dict[date][meal] += total
            daily_without_meal[date] = total

        return daily_without_meal

    # Manages weekly tab contents
    def weekly_tab_contants(self):
        dict_without_meals = self.calc_average_nutrients_without_meals(self.date_difference)
        weekly_cal={}

        # Split into pieces each is 7 days (each showing a week)
        for i in range(0, len(dict_without_meals), 7):
            week_dates = list(dict_without_meals)[i:i + 7]
            if week_dates:
                week_start = week_dates[0]
                week_end = week_dates[-1]

                # Initialize a dictionary to sum up nutrients for the current week
                weekly_nutrients_sum = {}

                for date in week_dates:
                    for nutrient, value in dict_without_meals[date].items():
                        if nutrient not in weekly_nutrients_sum:
                            weekly_nutrients_sum[nutrient] = 0
                        weekly_nutrients_sum[nutrient] += value

                weekly_cal[f"{week_start} to {week_end}"] = weekly_nutrients_sum
        # Calculate and save nutrients' values in another list since we need values list for plotting
        weekly_sugar_values = [nutrients.get('Sugar', 0) for week_range, nutrients in weekly_cal.items()]
        weekly_potassium_values = [nutrients.get('Potassium', 0) for week_range, nutrients in weekly_cal.items()]
        weekly_salt_sodium_values = [nutrients.get('Salt', 0) for week_range, nutrients in weekly_cal.items()]
        weekly_protein_values = [nutrients.get('Protein', 0) for week_range, nutrients in weekly_cal.items()]
        weekly_carb_values = [nutrients.get('Carbohydrate', 0) for week_range, nutrients in weekly_cal.items()]
        weekly_total_fat_values = [nutrients.get('Monounsaturated Fat', 0) + nutrients.get('Saturated Fat', 0) for week_range, nutrients in weekly_cal.items()]
        weekly_cal_values = [nutrients.get('Calorie', 0) for week_range, nutrients in weekly_cal.items()]  # Using .get() with a default of 0
        weeks = np.arange(len(weekly_cal_values))

        # Prepare the figure for plot
        fig, axs = plt.subplots(figsize=(6, 4), dpi =50)

        # Polynomial fit and plot for each nutrient
        # Calories
        p_cal = Polynomial.fit(weeks, weekly_cal_values, 2)
        axs.scatter(weeks, weekly_cal_values, color='blue', label='Weekly Calories')
        axs.plot(*p_cal.linspace(), color='#75E6DA', label='Polynomial Fit')
        axs.axhline(y=self.GoalCalorieBMR*7, color='red', linestyle='--', label='Goal Calorie BMR')

        axs.set_xlabel('Week Number')
        axs.set_ylabel('Calories')
        axs.legend()

        fig2, axs2 = plt.subplots(figsize=(3, 3), dpi =40)
        # Carbohydrates
        p_carb = Polynomial.fit(weeks, weekly_carb_values, 2)
        axs2.scatter(weeks, weekly_carb_values, color='green', label='Weekly Carbs')
        axs2.plot(*p_carb.linspace(), color='#81B622', label='Polynomial Fit')
        axs2.set_xlabel('Week Number')
        axs2.set_ylabel('Carbohydrates')
        axs2.legend()


        fig3, axs3 = plt.subplots(figsize=(3, 3), dpi =40)
        # Protein
        p_protein = Polynomial.fit(weeks, weekly_protein_values, 2)
        axs3.scatter(weeks, weekly_protein_values, color='#FF2E2E', label='Weekly Protein')
        axs3.plot(*p_protein.linspace(), color='#FF5C5C', label='Polynomial Fit')
        axs3.set_xlabel('Week Number')
        axs3.set_ylabel('Protein')
        axs3.legend()

        fig4, axs4 = plt.subplots(figsize=(3, 3), dpi =40)
        # Total Fat
        p_fat = Polynomial.fit(weeks, weekly_total_fat_values, 2)
        axs4.scatter(weeks, weekly_total_fat_values, color='#FFA500', label='Weekly Total Fat')
        axs4.plot(*p_fat.linspace(), color='#FFC55C', label='Polynomial Fit')
        axs4.set_xlabel('Week Number')
        axs4.set_ylabel('Total Fat')
        axs4.legend()

        # put into layouts
        self.layout_carb_weekly = QHBoxLayout()
        canvas = FigureCanvas(fig)
        self.layout_carb_weekly.addWidget(canvas)
        canvas_carb = FigureCanvas(fig2)
        canvas_prot = FigureCanvas(fig3)
        canvas4_fat = FigureCanvas(fig4)

        # Convert the figure to a canvas before adding it to the PyQt layout
        self.layout_macros_weekly = QHBoxLayout()
        self.layout_macros_weekly.addWidget(canvas_carb)
        self.layout_macros_weekly.addWidget(canvas_prot)
        self.layout_macros_weekly.addWidget(canvas4_fat)
        self.layout2.addLayout(self.layout_carb_weekly)
        self.layout2.addLayout(self.layout_macros_weekly)

        # calculates average weekly nutrient consumption
        weekly_average_nutrients=self.calc_overall_daily_nutrient_average(weekly_cal,int(self.date_difference)/7)

        text_edit = QTextEdit()

        text_edit.setReadOnly(True)  # Make the text edit read-only
        text_edit.setStyleSheet("""
            QTextEdit {
                font-size: 7px;
                color: black;
                background-color: #f0f0f0;
                font-family: Arial;
            }
        """)
        text_edit.setFixedSize(404,60)

        p_sugar = Polynomial.fit(weeks, weekly_sugar_values, 2)
        p_potassium = Polynomial.fit(weeks, weekly_potassium_values, 2)
        p_salt_sodium = Polynomial.fit(weeks, weekly_salt_sodium_values, 2)

        threshold_date_numeric = weeks[-1] + 3 # checking 3 week from the end date
        # Generate the early warning message

        text = self.create_text_with_early_warning(p_cal,p_sugar,p_potassium,p_salt_sodium,7, weeks[0],weeks[-1]+3, threshold_date_numeric, 'week', 'Weekly')

        text_edit.setHtml(text)
        self.layout2.addWidget(text_edit)

        # Create the table
        self.show_all_nutrients(weekly_average_nutrients,'weekly')

    # Manages the monthly tab's contents
    def monthly_tab_contents(self):
        dict_without_meals = self.calc_average_nutrients_without_meals(self.date_difference)
        # to store date and overall values of what's written in the name
        date_and_calorie = {}
        date_and_carb = {}
        date_and_prot = {}
        date_and_fat = {}
        date_and_sugar = {}
        date_and_potassium = {}
        date_and_salt_sodium = {}
        for date in dict_without_meals:
            date_and_calorie[date] = dict_without_meals[date]["Calorie"]
            date_and_carb[date] = dict_without_meals[date]["Carbohydrate"]
            date_and_prot[date] = dict_without_meals[date]["Protein"]
            date_and_fat[date] = dict_without_meals[date]["Monounsaturated Fat"] + dict_without_meals[date]["Saturated Fat"]
            date_and_sugar[date] = dict_without_meals[date]["Sugar"]
            date_and_potassium[date] = dict_without_meals[date]["Potassium"]
            date_and_salt_sodium[date] = dict_without_meals[date]["Sodium"]
        dates_numeric = np.array([i for i in range(len(date_and_calorie))])  # Example: range from 0 to len-1
        calories = np.array(list(date_and_calorie.values()))

        # Prepare the figure for plot
        fig, axs = plt.subplots(figsize=(6, 4), dpi =50)

        # Polynomial fit and plot for each nutrient
        # Calories
        p_cal = Polynomial.fit(dates_numeric, calories, 2)
        axs.scatter(dates_numeric, calories, color='blue', label='Weekly Calories')
        axs.plot(*p_cal.linspace(), color='#75E6DA', label='Polynomial Fit')
        axs.axhline(y=self.GoalCalorieBMR, color='red', linestyle='--', label='Goal Calorie BMR')

        axs.set_xlabel('Week Number')
        axs.set_ylabel('Calories')
        axs.legend()

        canvas = FigureCanvas(fig)
        self.layout3.addWidget(canvas)

        # Prepare arrays for other nutrients
        carbs = np.array(list(date_and_carb.values()))
        prot = np.array(list(date_and_prot.values()))
        fat = np.array(list(date_and_fat.values()))
        sugar = np.array(list(date_and_sugar.values()))
        potassium = np.array(list(date_and_potassium.values()))
        salt_sodium = np.array(list(date_and_salt_sodium.values()))
        # Polynomial fit and plot for Carbohydrates
        fig2, axs2 = plt.subplots(figsize=(3, 3), dpi=40)
        p_carb = Polynomial.fit(dates_numeric, carbs, 2)
        axs2.scatter(dates_numeric, carbs, color='green', label='Carbs')
        axs2.plot(*p_carb.linspace(), color='#81B622', label='Polynomial Fit')
        axs2.set_xlabel('Date')
        axs2.set_ylabel('Carbohydrates')
        axs2.legend()

        # Polynomial fit and plot for Protein
        fig3, axs3 = plt.subplots(figsize=(3, 3), dpi=40)
        p_protein = Polynomial.fit(dates_numeric, prot, 2)
        axs3.scatter(dates_numeric, prot, color='red', label='Protein')
        axs3.plot(*p_protein.linspace(), color='#FF5C5C', label='Polynomial Fit')
        axs3.set_xlabel('Date')
        axs3.set_ylabel('Protein')
        axs3.legend()

        # Polynomial fit and plot for Total Fat
        fig4, axs4 = plt.subplots(figsize=(3, 3), dpi=40)
        p_fat = Polynomial.fit(dates_numeric, fat, 2)
        axs4.scatter(dates_numeric, fat, color='orange', label='Total Fat')
        axs4.plot(*p_fat.linspace(), color='#FFC55C', label='Polynomial Fit')
        axs4.set_xlabel('Date')
        axs4.set_ylabel('Total Fat')
        axs4.legend()
        
        canvas2 = FigureCanvas(fig2)
        canvas3 = FigureCanvas(fig3)
        canvas4 = FigureCanvas(fig4)

        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(canvas2)
        horizontal_layout.addWidget(canvas3)
        horizontal_layout.addWidget(canvas4)

        self.layout3.addLayout(horizontal_layout)

        text_edit = QTextEdit()

        text_edit.setReadOnly(True)  # Make the text edit read-only
        text_edit.setStyleSheet("""
            QTextEdit {
                font-size: 8px;
                color: black;
                background-color: #f0f0f0;
                font-family: Arial;
            }
        """)

        p_sugar = Polynomial.fit(dates_numeric, sugar, 2)
        p_potassium = Polynomial.fit(dates_numeric, potassium, 2)
        p_salt_sodium = Polynomial.fit(dates_numeric, salt_sodium, 2)

        threshold_date_numeric = dates_numeric[-1] + 30 # checking 30 days beyond your current data
        # Generate the early warning message
        text = self.create_text_with_early_warning(p_cal,p_sugar,p_potassium,p_salt_sodium,1, dates_numeric[0], dates_numeric[-1]+30, threshold_date_numeric, 'day', 'Daily')

        text_edit.setFixedSize(404, 60)
        text_edit.setHtml(text)
        self.layout3.addWidget(text_edit)

        # Initialize a dictionary to sum up nutrients for the current week
        monthly_nutrients_sum = {}

        for date in dict_without_meals:
            for nutrient, value in dict_without_meals[date].items():
                if nutrient not in monthly_nutrients_sum:
                    monthly_nutrients_sum[nutrient] = 0
                monthly_nutrients_sum[nutrient] += value

        self.show_all_nutrients(monthly_nutrients_sum,"monthly")


    # Calculates the most appropriate goals for macro nutrients
    def calculate_goal_macro_nutrients(self):
        return [self.GoalCalorieBMR*0.5,self.GoalCalorieBMR*0.2,self.GoalCalorieBMR*0.3]


    # Call the function that creates the early warning for cal, carb, prot and fat
    def create_text_with_early_warning(self,p_cal,p_sugar,p_potassium,p_salt_sodium, multiplier, dates_numeric_start, dates_numeric_end, threshold_date_numeric, date_type, daily_weekly):
        # Generate the early warning message
        warning_message_cal = self.get_early_warning_message(p_cal, self.GoalCalorieBMR * multiplier, dates_numeric_start, dates_numeric_end + 30, threshold_date_numeric, 'Calorie', date_type, daily_weekly, "cal")
        warning_message_carb = self.get_early_warning_message(p_sugar, self.SugarGoal * multiplier, dates_numeric_start, dates_numeric_end + 30, threshold_date_numeric, 'Sugar', date_type, daily_weekly, "gr")
        warning_message_prot = self.get_early_warning_message(p_potassium, self.PotassiumGoal * multiplier, dates_numeric_start, dates_numeric_end + 30, threshold_date_numeric, 'Potassium', date_type, daily_weekly, "mg")
        warning_message_fat = self.get_early_warning_message(p_salt_sodium, self.SaltGoal * multiplier, dates_numeric_start, dates_numeric_end + 30, threshold_date_numeric, 'Salt', date_type, daily_weekly, "mg")

        text = warning_message_cal + warning_message_carb + warning_message_prot + warning_message_fat
        return text

    # Evaluates and creates early warning
    def get_early_warning_message(self, polynomial, goal_level, start_date_numeric, end_date_numeric, threshold_date_numeric, type, date_type, daily_weekly, metric):
        # Generate future dates and predict values using the polynomial model.
        future_dates = np.linspace(start_date_numeric, end_date_numeric, num=int(end_date_numeric-start_date_numeric+1))
        predicted_values = polynomial(future_dates)

        # Identify indices where predictions exceed or fall below the goal level.
        exceed_indices = np.where(predicted_values > goal_level)[0]
        below_indices = np.where(predicted_values < goal_level)[0]

        message = ""

        # Check for exceeding goal level before the threshold date and calculate the excess amount.
        if exceed_indices.size > 0 and future_dates[exceed_indices[0]] <= threshold_date_numeric:
            exceed_amount = predicted_values[exceed_indices[0]] - goal_level
            message += f"<b><font color='red'>Warning: {daily_weekly} {type} goal will be exceeded by {exceed_amount:.2f}{metric} from {start_date_numeric+exceed_indices[0]}th {date_type}. Consider corrective measures.<br>"

        # Check for falling below goal level before the threshold date and calculate the shortfall.
        if below_indices.size > 0 and future_dates[below_indices[0]] <= threshold_date_numeric:
            below_amount = goal_level - predicted_values[below_indices[0]]
            message += f"<b><font color='red'>Warning: {daily_weekly} {type} goal will be short by {below_amount:.2f}{metric} from {start_date_numeric+below_indices[0]}th {date_type}. Consider corrective measures.<br>"


        return message