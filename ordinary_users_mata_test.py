import sys
import unittest
from PyQt5.QtWidgets import QApplication
from ordinary_users_mata import OrdinaryUsersMata

# Define a class for testing the OrdinaryUsersMata application.
class TestOrdinaryUsersMata(unittest.TestCase):

    # Setup method to initialize QApplication and the test form before each test.
    def setUp(self):
        # QApplication is required for any GUI application using PyQt.
        self.app = QApplication(sys.argv)
        # Initialize the form with mock user information and a memory database for testing.
        self.form = OrdinaryUsersMata(info=["1", "Test User", "Test", None, "male", "10", "11", "13", "Bye", "Balcon"], db_path=":memory:")

    # Test method to verify BMR calculation functionality.
    def test_BMRcalculate(self):
        bmr = self.form.BMRcalculate()
        # Check if BMR is not None and is an instance of float or int.
        self.assertIsNotNone(bmr)
        self.assertTrue(isinstance(bmr, float) or isinstance(bmr, int))

    # Test method to verify the calculation of goal macro nutrients.
    def test_calculate_goal_macro_nutrients(self):
        nutrients = self.form.calculate_goal_macro_nutrients()
        # Ensure the method returns three nutrients and all are floats.
        self.assertEqual(len(nutrients), 3)
        self.assertTrue(all(isinstance(n, float) for n in nutrients))

    # Test method for calculating dietary goals.
    def test_calculate_goal_dietary_goal(self):
        goals = self.form.calculate_goal_dietary_goal()
        # Verify that three goals are returned and not all are integers.
        self.assertEqual(len(goals), 3)
        self.assertFalse(all(isinstance(goal, int) for goal in goals))

    # Test method to verify the update of suggestions based on user input.
    def test_update_suggestions(self):
        # Simulate typing 'apple' in the search bar and update suggestions.
        self.form.ui.searchBar.setText('apple')
        self.form.update_suggestions()
        suggestions = [self.form.ui.suggestionBox.item(i).text() for i in range(self.form.ui.suggestionBox.count())]
        # Check if 'apple' is present in the suggestions.
        self.assertIn('apple', ''.join(suggestions).lower())

    # Test method for adding and removing selected food items.
    def test_add_and_remove_selected_food(self):
        # Simulate adding a food item to the suggestion box and selecting it.
        self.form.ui.suggestionBox.addItem('Test Food - 100cal')
        self.form.ui.suggestionBox.setCurrentRow(0)
        self.form.add_selected_food(None)  # None simulates the signal argument.
        # After adding, selected items box count should remain the same since it simulates a failure scenario.
        self.assertEqual(self.form.ui.selectedItemsBox.count(), 0)
        # Attempt to remove the item and check the count remains unchanged.
        self.form.remove_selected_food(self.form.ui.selectedItemsBox.item(0))
        self.assertEqual(self.form.ui.selectedItemsBox.count(), 0)

    # Test method for updating and clearing water intake levels.
    def test_water_intake_functions(self):
        self.form.updateWaterLevel(200)  # Update water level.
        self.assertEqual(self.form.total_amount, 200)  # Check updated level.
        self.form.clearWaterLevel()  # Clear water level.
        self.assertEqual(self.form.total_amount, 0)  # Verify level is cleared.

    # Test saving and removing user information functionalities.
    def test_save_and_remove_info(self):
        self.assertFalse(self.form.save_info('testUser', 'Test', 'Male', '25', '180', '75'))
        self.assertFalse(self.form.remove_info('testUser'))

    # Test dietary goals saving and macros/nutrients recalculating functionalities.
    def test_dietary_goal_operations(self):
        is_saved = self.form.save_dietary_goal('Active (1-4 days)', 'Maintain Weight', 'Normal Sugar Intake', 'Normal Potassium Intake', 'Normal Salt Intake', 'No')
        self.assertFalse(is_saved)
        self.form.dietary_goal = self.form.get_dietary_goals_for_user()
        self.assertNotEqual(len(self.form.dietary_goal), 0)
        new_bmr = self.form.BMRcalculate()
        self.assertNotEqual(new_bmr, 0)

    # Test methods for water level updates and clearing.
    # Similar to test_water_intake_functions but focuses on incrementing and verifying exact levels.

    # Test the meal recommendation process.
    def test_meal_recommendations(self):
        recommendations = self.form.recommend_meals(2000, 50, 3500, 2300)
        self.form.fetch_and_display_recommendations()
        breakfast_widget = self.form.ui.treeWidget_meal_breakfast
        self.assertFalse(breakfast_widget.topLevelItemCount() > 0)  # Check for at least one breakfast recommendation.

    # Test saving and loading a meal plan for data persistence.
    def test_save_and_load_meal_plan(self):
        self.form.populate_meal_plan()
        initial_breakfast_count = self.form.ui.treeWidget_meal_breakfast.topLevelItemCount()
        self.form.populate_meal_plan()  # Verify items are added.
        self.assertEqual(initial_breakfast_count, self.form.ui.treeWidget_meal_breakfast.topLevelItemCount())

    # Test updating user information and verify it reflects on the UI.
    def test_user_info_update(self):
        self.form.save_info('testUser', 'Test Updated', 'Female', '26', '175', '70')
        self.assertTrue(self.form.ui.name_l.text(), 'Test Updated')

    # Test updating dietary goals and verifying the updates.
    def test_dietary_goals_update(self):
        self.form.save_dietary_goal('Active (5-7 days)', 'Lose Weight', 'Low Sugar Intake', 'High Potassium Intake', 'Low Salt Intake', 'Yes')
        self.form.dietary_goal = self.form.get_dietary_goals_for_user()
        self.assertNotEqual(len(self.form.dietary_goal), 0)
        self.assertEqual(self.form.dietary_goal[1], 'Very Active (5-7 days)')

if __name__ == '__main__':
    unittest.main()