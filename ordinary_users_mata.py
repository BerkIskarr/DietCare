import sys
import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, QRunnable, QUrl
from PyQt5.QtWidgets import QWidget, QApplication,QMessageBox, QTreeWidgetItem, QListWidgetItem

from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QPainter,  QDesktopServices
import random
from ui_py.ordinary_users import Ui_Form

from Food_data import Food_data
from report_page import Report_Page
import sqlite3

# Class responsible for creating pdf file
class PdfGenerator(QRunnable):
    def __init__(self, tabs, name):
        super().__init__()
        self.name = name
        self.tabs = tabs

    # Creates the pdf
    def run(self):
        # set file path as this directory
        pdf_file_name = "{}_report.pdf".format(self.name)
        pdf_file_path = os.path.join(os.getcwd(), pdf_file_name)  # Save in the current working directory
        try:
            # initiate the printer
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(pdf_file_path)
            printer.setFullPage(True)
            # initiate the painter
            painter = QPainter()
            # start painting
            if painter.begin(printer):
                # To export all the 3 pages
                for index, tab_widget in enumerate(self.tabs):
                    if index > 0:
                        printer.newPage()

                    # No dedicated header space; widget uses full page
                    page_width = printer.pageRect().width()
                    page_height = printer.pageRect().height()

                    tab_rect = tab_widget.rect()
                    scale_factor_width = page_width / tab_rect.width()
                    scale_factor_height = page_height / tab_rect.height()
                    scale_factor = min(scale_factor_width, scale_factor_height)

                    # Adjust scale factor to fill the page completely
                    fill_scale_width = page_width / tab_rect.width()
                    fill_scale_height = page_height / tab_rect.height()

                    painter.save()
                    painter.scale(fill_scale_width, fill_scale_height)  # Scale to fill the page
                    tab_widget.render(painter)
                    painter.restore()

                painter.end()

        except Exception as e:
            print(str(e))



class OrdinaryUsersMata(QWidget):

    def __init__(self, info, db_path, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.db_path = db_path
        self.info = info
        self.food_data = Food_data()
        self.init_info(info)
        self.init_lineEdit()
        self.fetch_and_display_recommendations()
        self.dietary_goal = self.get_dietary_goals_for_user()

        self.GoalCalorieBMR = self.BMRcalculate()
        # Goal for nutrients
        self.CarbGoal = self.calculate_goal_macro_nutrients()[0]
        self.ProtGoal = self.calculate_goal_macro_nutrients()[1]
        self.FatGoal = self.calculate_goal_macro_nutrients()[2]

        self.sugar_potassium_salt_goal = self.calculate_goal_dietary_goal()
        self.SugarGoal = self.sugar_potassium_salt_goal[0]
        self.PotassiumGoal = self.sugar_potassium_salt_goal[1]
        self.SaltGoal = self.sugar_potassium_salt_goal[2]

        self.tabs = [self.ui.tab_4,self.ui.tab_5, self.ui.tab_8]
        self.total_amount = 0

        # To show saved meal plan
        self.populate_meal_plan()

        # Connect signals and slots
        self.ui.searchBar_meal_selection.textChanged.connect(self.update_suggestions_meal_selection)
        self.ui.suggestionBox_meal_selection.itemClicked.connect(self.add_selected_food_meal_selection)
        self.ui.treeWidget_meal_breakfast.itemDoubleClicked.connect(self.remove_selected_food_meal)
        self.ui.treeWidget_lunch_meal.itemDoubleClicked.connect(self.remove_selected_food_meal)
        self.ui.treeWidget_dinner_meal.itemDoubleClicked.connect(self.remove_selected_food_meal)
        self.ui.treeWidget_snack_meal.itemDoubleClicked.connect(self.remove_selected_food_meal)


        # Connect signals and slots
        self.ui.searchBar.textChanged.connect(self.update_suggestions)
        self.ui.suggestionBox.itemClicked.connect(self.add_selected_food)
        self.ui.selectedItemsBox.itemDoubleClicked.connect(self.remove_selected_food)


    # Calculate daily basal calorie
    def BMRcalculate(self):
        gender = self.info[4]
        age = int(self.info[5])
        height = int(self.info[6])
        weight = int(self.info[7])
        BMR = 0
        # calculation
        if(gender== "male"):
            # Adapt to dietary goal
            if(len(self.dietary_goal)==0):
                BMR+= (10*weight+6.25*height-5*age+5)*1.375
            elif(self.dietary_goal[1]=='Not Active' ):
                BMR+= (10*weight+6.25*height-5*age+5)*1.2
            elif(self.dietary_goal[1]=="Active (1-4 days)"):
                BMR+= (10*weight+6.25*height-5*age+5)*1.375
            elif(self.dietary_goal[1]=='Very Active (5-7 days)'):
                BMR+= (10*weight+6.25*height-5*age+5)*1.725
            else:
                BMR+= (10*weight+6.25*height-5*age+5)*1.375
        else:
            # Adapt to dietary goal
            if(len(self.dietary_goal)==0):
                BMR+= (10*weight+6.25*height-5*age-161)*1.375
            elif(self.dietary_goal[1]=='Not Active'):
                BMR+= (10*weight+6.25*height-5*age-161)*1.2
            elif(self.dietary_goal[1]=="Active (1-4 days)"):
                BMR+= (10*weight+6.25*height-5*age-161)*1.375
            elif(self.dietary_goal[1]=='Very Active (5-7 days)'):
                BMR+= (10*weight+6.25*height-5*age-161)*1.725
            else:
                BMR+= (10*weight+6.25*height-5*age-161)*1.375
        if(len(self.dietary_goal)==0):
            return BMR
        elif(self.dietary_goal[2]=='Maintain Weigth' ):
            return BMR
        elif(self.dietary_goal[2]=='Lose Weight'):
            return BMR-200
        elif(self.dietary_goal[2]=='Gain Weight'):
            return BMR+200
        else:
            return BMR

    # Calculate nutrient goals according to dietary goal
    def calculate_goal_dietary_goal(self):
        dietary_goal = []
        if(len(self.dietary_goal) == 0):
            return [self.GoalCalorieBMR*0.1, 3510, 2300]

        if(self.dietary_goal[3]=='Low Sugar Intake' ):
            dietary_goal.append(self.GoalCalorieBMR*0.05)
        elif(self.dietary_goal[3]=='Normal Sugar Intake' or len(self.dietary_goal) == 0):
            dietary_goal.append(self.GoalCalorieBMR*0.1)
        elif(self.dietary_goal[3]=='High Sugar Intake'):
            dietary_goal.append(self.GoalCalorieBMR*0.20)
        else:
            dietary_goal.append(self.GoalCalorieBMR*0.1)
        if(self.dietary_goal[4]== 'Low Potassium Intake' ):
            dietary_goal.append(3100)
        elif(self.dietary_goal[4]=='Normal Potassium Intake' or len(self.dietary_goal) == 0):
            dietary_goal.append(3510)
        elif(self.dietary_goal[4]=='High Potassium Intake'):
            dietary_goal.append(3900)
        else:
            dietary_goal.append(3510)

        if(self.dietary_goal[5]== 'Low Salt Intake' ):
            dietary_goal.append(1900)
        elif(self.dietary_goal[5]=='Normal Salt Intake' or len(self.dietary_goal) == 0):
            dietary_goal.append(2300)
        elif(self.dietary_goal[5]=='High Salt Intake'):
            dietary_goal.append(2700)
        else:
            dietary_goal.append(2300)
        return dietary_goal

    # Calculates the most appropriate goals for macro nutrients
    def calculate_goal_macro_nutrients(self):
        return [self.GoalCalorieBMR*0.5,self.GoalCalorieBMR*0.2,self.GoalCalorieBMR*0.3]

    def init_info(self, info):
        self.ui.acc_l.setText(info[1])
        if not info[2] is None:
            self.ui.name_l.setText(info[2])
        if not info[4] is None:
            self.ui.sex_l.setText(info[4])
        if not info[5] is None:
            self.ui.age_l.setText(info[5])
        if not info[6] is None:
            self.ui.height_l.setText(info[6])
        if not info[7] is None:
            self.ui.weight_l.setText(info[7])
        if not info[8] is None:
            str_info = info[8].replace('-', '').replace('[', '').replace(']', '')
            l_info = str_info.split(',')
            for i in range(len(l_info)):
                str_info = l_info[i]
                t_info = str_info.replace('-', '').replace('[', '').replace(']', '')
                self.ui.textEdit.append(f'suggestion {i + 1}.{t_info}')
            self.ui.warn_num.setText(str(len(l_info)))

    def update_suggestions(self):
        # Update suggestions based on search text
        search_text = self.ui.searchBar.text()
        suggestions = self.get_suggestions(search_text)
        self.ui.suggestionBox.clear()
        self.ui.suggestionBox.addItems(suggestions)

    def get_suggestions(self, search_text):
        # Get filtered suggestions based on search text in descriptions
        food_items = [item["Category"] for item in self.food_data.foods_list]
        descriptions = [item["Description"] for item in self.food_data.foods_list]

        filtered_items = [item for item, desc in zip(food_items, descriptions) if search_text.lower() in desc.lower()]
        filtered_descs = [desc for item, desc in zip(food_items, descriptions) if search_text.lower() in desc.lower()]

        suggestions = [f"{item} - {desc}" for item, desc in zip(filtered_items, filtered_descs)]

        return suggestions

    def add_selected_food(self, event):
        # Add selected food to the selected items box
        selected_item = self.ui.suggestionBox.currentItem().text()
        food_name, food_desc = selected_item.split(" - ")
        food_id = next((item["Nutrient Data Bank Number"] for item in self.food_data.foods_list if item["Description"] == food_desc), None)
        if food_id:
            self.ui.selectedItemsBox.addItem(selected_item)


    def remove_selected_food(self, item):
        # Remove selected food from the selected items box
        self.ui.selectedItemsBox.takeItem(self.ui.selectedItemsBox.row(item))

    def updateTotalLabel(self):
        if self.total_amount >= 2000:
            QMessageBox.information(self, 'Success', 'You have reached your daily water intake goal!', QMessageBox.Ok)

    def updateWaterLevel(self, amount):
        self.total_amount += amount
        self.ui.progressBar.setValue(self.total_amount)
        self.updateTotalLabel()

    def clearWaterLevel(self):
        self.total_amount = 0
        self.ui.progressBar.setValue(0)
        self.updateTotalLabel()

    def init_lineEdit(self):
        self.ui.acc_l.setReadOnly(True)
        self.ui.name_l.setReadOnly(True)
        self.ui.sex_l.setReadOnly(True)
        self.ui.age_l.setReadOnly(True)
        self.ui.height_l.setReadOnly(True)
        self.ui.weight_l.setReadOnly(True)
        self.ui.textEdit.setReadOnly(True)

    @pyqtSlot()
    def on_add_btn_clicked(self):
        # Retrieve necessary information
        username = self.ui.acc_l.text()
        date = self.ui.dateEdit.date().toString(QtCore.Qt.ISODate)
        meal = self.ui.meal_cb.currentText()
        water_intake = self.total_amount

        # Get selected food items
        selected_items = [self.ui.selectedItemsBox.item(i).text() for i in range(self.ui.selectedItemsBox.count())]
        food_items = ', '.join(selected_items)

        # Connect to the database
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()

        try:
            # Get the user's ID from the account table
            cur.execute(f"SELECT id FROM account WHERE username = '{username}'")
            row = cur.fetchone()
            if row:
                user_id = row[0]

                # Insert the water intake record into the daily_intake table
                cur.execute("INSERT INTO daily_intake (id, foodItems, waterIntake, date, meal) VALUES (?, ?, ?, ?, ?)",
                            (user_id, food_items, water_intake, date, meal))
                con.commit()

                QMessageBox.information(self, 'Success', 'The food was saved successfully!',
                                        QMessageBox.Ok)
            else:
                QMessageBox.warning(self, 'Error', 'User not found!',
                                    QMessageBox.Ok)
        except Exception as e:
            QMessageBox.warning(self, 'Error', 'Failed to record the food!',
                                QMessageBox.Ok)
            con.rollback()
        finally:
            cur.close()
            con.close()

    @pyqtSlot()
    def on_add200_btn_clicked(self):
        self.updateWaterLevel(200)

    @pyqtSlot()
    def on_add400_btn_clicked(self):
        self.updateWaterLevel(400)

    @pyqtSlot()
    def on_add800_btn_clicked(self):
        self.updateWaterLevel(800)

    @pyqtSlot()
    def on_clearWater_btn_clicked(self):
        self.clearWaterLevel()

    @pyqtSlot()
    def on_record_btn_clicked(self):
        # First, get the selected food items for each meal from the UI
        breakfast_items = [self.ui.treeWidget_meal_breakfast.topLevelItem(i).text(0) for i in range(self.ui.treeWidget_meal_breakfast.topLevelItemCount())]
        lunch_items = [self.ui.treeWidget_lunch_meal.topLevelItem(i).text(0) for i in range(self.ui.treeWidget_lunch_meal.topLevelItemCount())]
        dinner_items = [self.ui.treeWidget_dinner_meal.topLevelItem(i).text(0) for i in range(self.ui.treeWidget_dinner_meal.topLevelItemCount())]
        snack_items = [self.ui.treeWidget_snack_meal.topLevelItem(i).text(0) for i in range(self.ui.treeWidget_snack_meal.topLevelItemCount())]

        # Convert the lists of items into a single string for each meal, new line look better
        breakfast = '\n'.join(breakfast_items)
        lunch = '\n'.join(lunch_items)
        dinner = '\n'.join(dinner_items)
        snack = '\n'.join(snack_items)


        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Prepare the SQL query
        query = '''INSERT OR REPLACE INTO custom_meal_plan (id, breakfast, lunch, dinner, snack)
                   VALUES (?, ?, ?, ?, ?)'''
        values = (self.info[0], breakfast, lunch, dinner, snack)

        # Execute the SQL query
        try:
            cursor.execute(query, values)
            conn.commit()
            QMessageBox.information(self, 'Success', 'The meal plan was saved successfully!',
                                    QMessageBox.Ok)
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'Error', 'An error occured while saving! Please try again.',
                                    QMessageBox.Ok)
        finally:
            # close the connection to the database
            conn.close()

    # Get suggestions over the entered chars
    def get_suggestions_meal(self, search_text):
        suggestions = []
        # Presuming self.food_data.foods_list is a list of dictionaries with food details
        for item in self.food_data.foods_list:
            if search_text.lower() in item["Description"].lower():
                desc = item["Description"]
                # To show nutrient infos
                nutrients = f"Calories: {item['Calories per 100g']:.2f}, Protein: {item['Data.Protein']:.2f}, Carbs: {item['Data.Carbohydrate']:.2f}, Fats: {(item['Data.Fat.Monosaturated Fat']+item['Data.Fat.Saturated Fat']):.2f}, Quantity: 1(100gr)"
                suggestions.append(f"{desc} - {nutrients}")
        return suggestions

    # Give suggestions
    def update_suggestions_meal_selection(self):
        search_text = self.ui.searchBar_meal_selection.text()
        suggestions = self.get_suggestions_meal(search_text)
        self.ui.suggestionBox_meal_selection.clear()
        for suggestion in suggestions:
            # Ensure each suggestion is added as a QListWidgetItem
            self.ui.suggestionBox_meal_selection.addItem(QListWidgetItem(suggestion))


    # Add into the treewidgets
    def add_selected_food_meal_selection(self, item):
        selected_item = item.text()
        meal = self.ui.meal_cb_2.currentText()
        food_name, food_desc = selected_item.split(" - ")
        # Assuming the Nutrient Data Bank Number is unique for each food item
        food_id = next((item["Nutrient Data Bank Number"] for item in self.food_data.foods_list if item["Description"] == food_name), None)

        if food_id:
            treeWidget = None
            if meal == "Breakfast":
                treeWidget = self.ui.treeWidget_meal_breakfast
            elif meal == 'Lunch':
                treeWidget = self.ui.treeWidget_lunch_meal
            elif meal == 'Dinner':
                treeWidget = self.ui.treeWidget_dinner_meal
            elif meal == "Snack":
                treeWidget = self.ui.treeWidget_snack_meal

            if treeWidget:
                # Create a QTreeWidgetItem using the selected item's text
                treeWidgetItem = QTreeWidgetItem([selected_item])
                # Add the new QTreeWidgetItem to the treeWidget
                treeWidget.addTopLevelItem(treeWidgetItem)

    # To be able to show the meals at the start
    def populate_meal_plan(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        query = '''SELECT breakfast, lunch, dinner, snack FROM custom_meal_plan WHERE id=?'''
        try:
            cursor.execute(query, (self.info[0],))
            meal_plan = cursor.fetchone()  # Fetch the meal plan for the user

            if meal_plan:
                # populate each treewidget
                breakfast, lunch, dinner, snack = meal_plan
                self.populate_tree_widget(self.ui.treeWidget_meal_breakfast, breakfast)
                self.populate_tree_widget(self.ui.treeWidget_lunch_meal, lunch)
                self.populate_tree_widget(self.ui.treeWidget_dinner_meal, dinner)
                self.populate_tree_widget(self.ui.treeWidget_snack_meal, snack)
        except sqlite3.Error as e:
            QMessageBox.warning(self, 'Error', 'An error occured while saving! Please try again.',
                                QMessageBox.Ok)
        finally:
            conn.close()

    # Populate each treewidget
    def populate_tree_widget(self, tree_widget, meal_items):
        if meal_items:
            items = meal_items.split('\n')
            for item in items:
                treeWidgetItem = QTreeWidgetItem([item])
                tree_widget.addTopLevelItem(treeWidgetItem)

    def remove_selected_food_meal(self, item, column):
        # Retrieve the parent (the tree widget) from the item
        parent_widget = item.treeWidget()

        # Check if the item has a parent node (if it is not a top-level item)
        if item.parent():
            # If the item has a parent, we need to remove it from its parent
            item.parent().removeChild(item)
        else:
            # If the item is a top-level item, we can remove it directly from the tree widget
            index = parent_widget.indexOfTopLevelItem(item)
            parent_widget.takeTopLevelItem(index)


    @pyqtSlot()
    def on_recommend_btn_clicked(self):
        # Get the meal recommendations
        recommendations = self.recommend_meals(self.GoalCalorieBMR, self.SugarGoal, self.PotassiumGoal, self.SaltGoal)

        # Save the recommendations to the database
        self.save_recommendations_to_db(recommendations)

        # Update the QTreeWidgets to display the recommendations
        self.fetch_and_display_recommendations()


    def recommend_meals(self, calorie_goal, sugar_goal, potassium_goal, salt_goal):
        # Define how to distribute calories among the meals
        meal_distribution = {'breakfast': 0.3, 'lunch': 0.3, 'dinner': 0.3, 'snack': 0.1}

        # Calculate meal-specific calorie goals
        meal_calorie_goals = {meal: calorie_goal * proportion for meal, proportion in meal_distribution.items()}

        # Initialize a dictionary to hold the recommended meals
        recommendations = {meal: [] for meal in meal_distribution.keys()}
        selected_categories = set()
        # Loop over each meal to select food items that fit within the calorie goal
        for meal in meal_distribution.keys():
            meal_calories = 0

            # Continue adding foods until the calorie goal for the meal is reached
            while meal_calories < meal_calorie_goals[meal]:
                # Filter the foods list for the specific meal
                meal_foods = [food for food in self.food_data.foods_list
                              if food['Calories per 100g'] + meal_calories <= meal_calorie_goals[meal]
                              and food['Data.Sugar Total'] <= sugar_goal
                              and food['Data.Major Minerals.Potassium'] <= potassium_goal
                              and food['Data.Major Minerals.Sodium'] <= salt_goal
                              and food['Category'] not in selected_categories]

                # Randomly select food from the filtered list
                if meal_foods:
                    selected_food = random.choice(meal_foods)
                    recommendations[meal].append(selected_food['Description'])
                    selected_category = selected_food['Category']
                    selected_categories.add(selected_category)
                    self.food_data.selected_foods.append(selected_food)  # Keep track of selected foods since no duplicates
                    meal_calories += selected_food['Calories per 100g']  # Update the calorie count for the meal
                else:
                    break  # If no foods fit the criteria, break out of the loop


        return recommendations


    def save_recommendations_to_db(self, recommendations):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()

        # Join the list into a string, separating each item with a newline
        breakfast_str = '\n'.join(recommendations['breakfast'])
        lunch_str = '\n'.join(recommendations['lunch'])
        dinner_str = '\n'.join(recommendations['dinner'])
        snack_str = '\n'.join(recommendations['snack'])

        # SQL query to insert the meal recommendations into the recommend_meal table
        insert_query = '''
        INSERT INTO recommend_meal (id, breakfast, lunch, dinner, snack) VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET 
        breakfast=excluded.breakfast, 
        lunch=excluded.lunch, 
        dinner=excluded.dinner, 
        snack=excluded.snack;
        '''
        cur.execute(insert_query, (self.info[0], breakfast_str, lunch_str, dinner_str, snack_str))

        con.commit()
        con.close()


    def fetch_and_display_recommendations(self):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()

        # Attempt to fetch the meal recommendations for the current user
        try:
            cur.execute("SELECT breakfast, lunch, dinner, snack FROM recommend_meal WHERE id=?", (self.info[0],))
            recommendations = cur.fetchone()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            recommendations = None

        con.close()


        # If we have recommendations, display them; otherwise, clear the tree widgets
        if recommendations:
            meals = ['breakfast', 'lunch', 'dinner', 'snack']
            tree_widgets = [self.ui.treeWidget_breakfast, self.ui.treeWidget_lunch, self.ui.treeWidget_dinner, self.ui.treeWidget_snack]

            for meal, recommendation, tree_widget in zip(meals, recommendations, tree_widgets):
                # Clear the tree widget before adding new items
                tree_widget.clear()
                if recommendation:  # There is a recommendation for this meal
                    # Split the recommendation by line breaks
                    food_items = recommendation.split('\n')
                    for food_item in food_items:
                        # Split each food item into name and description, if possible
                        parts = food_item.split(" - ", 1) if " - " in food_item else [food_item, "No description available"]
                        item = QTreeWidgetItem(parts)
                        tree_widget.addTopLevelItem(item)
                else:  # No recommendation, this wont happen but still just in case
                    item = QTreeWidgetItem(["No recommendation", ""])
                    tree_widget.addTopLevelItem(item)
        else:
            # Clear all tree widgets if there are no recommendations
            for tree_widget in [self.ui.treeWidget_breakfast, self.ui.treeWidget_lunch, self.ui.treeWidget_dinner, self.ui.treeWidget_snack]:
                tree_widget.clear()


    @pyqtSlot()
    def on_save_btn_clicked(self):
        self.start_pdf_generation_in_background()
        # Construct the file path
        file_name = f"{self.info[2]}_report.pdf"
        file_path = os.path.join(os.getcwd(), file_name)  # Assuming the file is saved in the current working directory

        # Check if the PDF file exists and inform the user
        if os.path.exists(file_path):
            # Open the PDF file with the default application
            QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))
        else:
            QMessageBox.information(self, "PDF Not Ready", "Please wait, the report PDF is still being prepared.", QMessageBox.Ok)

    @pyqtSlot()
    def on_save_btn_2_clicked(self):
        # Get the dates
        selected_start_date = self.ui.dateEdit_2.date()
        selected_end_date = self.ui.dateEdit_3.date()
        # Check if valid (it always will but still)
        if(selected_start_date.isValid() and selected_end_date.isValid()):
            # End date cannot be more than start date
            if(selected_end_date<= selected_start_date):
                QMessageBox.warning(self, "Date Error", "the start cannot be more than end date!")
            else:
                # Limit to max 30 days(a month)
                if(selected_start_date.daysTo(selected_end_date)>30):
                    QMessageBox.warning(self, "Date Range Error", "The difference between the start and end date cannot be more than 1 month!")
                else:
                    # Limit to min 7 days(a week)
                    if(selected_start_date.daysTo(selected_end_date)<7):
                        QMessageBox.warning(self, "Date Range Error", "The difference between the start and end date cannot be less than 7 days!")
                    else:
                        # If already exists (opened before)
                        if hasattr(self, 'report_page'):
                            self.report_page.refresh_content(selected_start_date,selected_end_date,self.GoalCalorieBMR, self.sugar_potassium_salt_goal)
                        else:
                            self.report_page = Report_Page(self.ui.tab_4,self.ui.tab_5, self.ui.tab_8, self.GoalCalorieBMR, self.sugar_potassium_salt_goal, self.info, selected_start_date, selected_end_date)


    @pyqtSlot()
    def on_clear_btn_clicked(self):
        self.ui.textEdit.setText('')
        self.ui.warn_num.setText('0')
        if self.remove_info(self.ui.acc_l.text()):
            QMessageBox.information(self, 'success', 'Clear Success!',
                                    QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.information(self, 'Error', 'Clear Fail!',
                                    QMessageBox.Ok, QMessageBox.Ok)

    # Creates the pdf and opens it
    def start_pdf_generation_in_background(self):
        pdfgenerator = PdfGenerator(self.tabs, self.info[2])
        pdfgenerator.run()

    def remove_info(self, username):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = f'UPDATE account SET infos = Null WHERE username=\'{username}\''
        try:

            cur.execute(sql)
            con.commit()
            return True
        except Exception as e:
            print(e)
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()

    @pyqtSlot()
    def on_re_btn_clicked(self):
        if self.ui.name_l.isReadOnly():
            self.ui.name_l.setReadOnly(False)
            self.ui.sex_l.setReadOnly(False)
            self.ui.age_l.setReadOnly(False)
            self.ui.height_l.setReadOnly(False)
            self.ui.weight_l.setReadOnly(False)
        else:
            self.ui.name_l.setReadOnly(True)
            self.ui.sex_l.setReadOnly(True)
            self.ui.age_l.setReadOnly(True)
            self.ui.height_l.setReadOnly(True)
            self.ui.weight_l.setReadOnly(True)
            is_suc = self.save_info(self.ui.acc_l.text(),
                                    self.ui.name_l.text(),
                                    self.ui.sex_l.text(),
                                    self.ui.age_l.text(),
                                    self.ui.height_l.text(),
                                    self.ui.weight_l.text()
                                    )
            if is_suc:
                QMessageBox.information(self, 'success', 'Modified successfully!',
                                        QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, 'Error', 'Modification failed!',
                                        QMessageBox.Ok, QMessageBox.Ok)

    def save_info(self, username, name, sex, height, age, weight):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        sql = f'UPDATE account SET name = \'{name}\',gender = \'{sex}\',age =  \'{age}\',height = \'{height}\',weight = \'{weight}\' WHERE username=\'{username}\''
        try:

            cur.execute(sql)
            con.commit()
            return True
        except Exception as e:
            print('save err')
            print(e)
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()

    @pyqtSlot()
    def on_save_dietargoal_btn_clicked(self):

        is_suc = self.save_dietary_goal(self.ui.comboBox_exercise.currentText(),
                                        self.ui.comboBox_calorie.currentText(),
                                        self.ui.comboBox_sugar.currentText(),
                                        self.ui.comboBox_potassium.currentText(),
                                        self.ui.comboBox_salt.currentText(),
                                        self.ui.comboBox_vegan.currentText()
                                        )
        # if saved recalculate everything with the new values
        if is_suc:
            self.dietary_goal = self.get_dietary_goals_for_user()
            self.GoalCalorieBMR = self.BMRcalculate()
            # Goal for nutrients
            self.CarbGoal = self.calculate_goal_macro_nutrients()[0]
            self.ProtGoal = self.calculate_goal_macro_nutrients()[1]
            self.FatGoal = self.calculate_goal_macro_nutrients()[2]

            self.sugar_potassium_salt_goal = self.calculate_goal_dietary_goal()
            self.SugarGoal = self.sugar_potassium_salt_goal[0]
            self.PotassiumGoal = self.sugar_potassium_salt_goal[1]
            self.SaltGoal = self.sugar_potassium_salt_goal[2]
            QMessageBox.information(self, 'success', 'Saved successfully!', QMessageBox.Ok, QMessageBox.Ok)

        else:
            QMessageBox.information(self, 'Error', 'Modification failed!', QMessageBox.Ok, QMessageBox.Ok)



    # Saves the dietary goal inputs
    def save_dietary_goal(self, exercise, calorie, sugar, potassium, salt, vegan):

        con = sqlite3.connect(self.db_path)
        cur = con.cursor()

        # Constructing SQL command Insert or if already exists update
        sql = ('INSERT OR REPLACE INTO dietary_goal '
               '(id, exercise_goal, calorie_goal, sugar_goal, '
               'potassium_goal, salt_goal, vegan) '
               'VALUES (?, ?, ?, ?, ?, ?, ?)')
        values = (self.info[0], exercise, calorie, sugar, potassium, salt, vegan)
        try:
            cur.execute(sql, values)
            con.commit()
            return True
        except Exception as e:
            QMessageBox.warning(self,"Error","An error occurred! Please try again.")
            con.rollback()
            return False
        finally:
            cur.close()
            con.close()

    def get_dietary_goals_for_user(self):
        con = sqlite3.connect('diet_tool.db')
        cur = con.cursor()

        user_id = self.info[0]  # Directly use the user ID stored in self.info[0]

        # Select the dietary goals for this user ID
        cur.execute("SELECT * FROM dietary_goal WHERE id = ?", (user_id,))
        goals = cur.fetchone()  # one row per user ID due to table's structure

        cur.close()
        con.close()

        if goals:
            return list(goals)  # Return the goals as a list
        else:
            return []  # Return an empty list if no goals found


    @pyqtSlot()
    def on_close_button_clicked(self):
        self.close()

    def mouseMoveEvent(self, e: QtGui.QMouseEvent):
        try:
            if (e.x() >= 10 and e.x() <= 451 and e.y() >= 0 and e.y() < 60):
                self._endPos = e.pos() - self._startPos
                self.move(self.pos() + self._endPos)
        except Exception as e:
            pass

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        try:
            if e.button() == QtCore.Qt.LeftButton:
                self._isTracking = True
                self._startPos = QtCore.QPoint(e.x(), e.y())
        except Exception as e:
            pass

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        try:
            if e.button() == QtCore.Qt.LeftButton:
                self._isTracking = False
                self._startPos = None
                self._endPos = None
        except Exception as e:
            pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = OrdinaryUsersMata()
    form.show()
    sys.exit(app.exec_())
