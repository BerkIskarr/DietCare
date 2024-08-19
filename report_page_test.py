import pytest
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QDate
from report_page import Report_Page, Worker

@pytest.fixture(scope='module')
def app():
    """Fixture to initialize QApplication."""
    return QApplication([])

@pytest.fixture
def report_page(app):
    """Fixture to create a Report_Page instance before each test."""
    daily_tab = QWidget()
    weekly_tab = QWidget()
    monthly_tab = QWidget()
    return Report_Page(daily_tab, weekly_tab, monthly_tab, 2000, [50, 30, 20], info=["1", "Test User", "Test", None, "male", "10", "11", "13", "Bye", "Balcon"], start_date=QDate.currentDate(), end_date=QDate.currentDate().addDays(1))

def test_init(report_page):
    assert report_page.food_dict is not None
    assert report_page.date_difference == 1
    assert isinstance(report_page.worker, Worker)

# Here, we use the report_page fixture directly in our test functions
def test_clear_layouts_safe(report_page):
    layout = report_page.daily_tab.layout()
    widget = QWidget()
    layout.addWidget(widget)
    assert layout.count() > 0
    report_page.clearLayoutsSafe(layout)
    assert layout.count() == 0

def test_calc_all_nutrient_updates_correctly(report_page):
    report_page.food_dict = {'apple': {"Calories per 100g": 1.0,'calories': 95.0, 'sugar': 19, "waterIntake": 12, 'protein': 0.5, "breakfast": {"Calorie": 1} }}
    report_page.calc_all_nutrient()
    assert report_page.TotalCalorie == 95
    assert report_page.TotalSugar == 19
    assert report_page.TotalProtein == 0.5


def test_calc_average_nutrients(report_page):
    # Setup: Assuming total_daily_food_dict is structured as {date: {meal_type: {nutrient: value}}}
    report_page.total_daily_food_dict = {
        "2023-01-01": {
            "breakfast": {"Calorie": 300, "Protein": 10},
            "lunch": {"Calorie": 500, "Protein": 15},
            "dinner": {"Calorie": 700, "Protein": 20}
        },
        "2023-01-02": {
            "breakfast": {"Calorie": 350, "Protein": 11},
            "lunch": {"Calorie": 450, "Protein": 14},
            "dinner": {"Calorie": 600, "Protein": 18}
        }
    }
    expected_avg = {
        "breakfast": {"Calorie": 325, "Protein": 10.5},
        "lunch": {"Calorie": 475, "Protein": 14.5},
        "dinner": {"Calorie": 650, "Protein": 19}
    }
    assert report_page.calc_average_nutrients(2) == expected_avg


def test_calc_average_nutrients_without_meals(report_page):
    # Similar setup as above, but the test validates the aggregation without meal separation
    report_page.total_daily_food_dict = {...}  # Use the same or similar structure as the previous test
    expected_avg_without_meals = {...}  # Expected result based on your actual implementation logic
    assert report_page.calc_average_nutrients_without_meals(2) == expected_avg_without_meals


def test_refresh_content_updates_attributes(report_page):
    # Setup: New start and end dates, and new dietary goals
    new_start_date = QDate(2023, 1, 1)
    new_end_date = QDate(2023, 1, 3)
    new_goal_calorie_bmr = 2200
    new_calculate_goal_dietary_goal = [60, 3500, 2300]  # Example: [SugarGoal, PotassiumGoal, SaltGoal]

    report_page.refresh_content(new_start_date, new_end_date, new_goal_calorie_bmr, new_calculate_goal_dietary_goal)

    assert report_page.start_date == new_start_date
    assert report_page.end_date == new_end_date
    assert report_page.GoalCalorieBMR == new_goal_calorie_bmr
    # Validate the nutrient goals have been updated appropriately
    assert report_page.SugarGoal == new_calculate_goal_dietary_goal[0]
    assert report_page.PotassiumGoal == new_calculate_goal_dietary_goal[1]
    assert report_page.SaltGoal == new_calculate_goal_dietary_goal[2]
