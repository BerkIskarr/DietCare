# Test report  

## Testing performed

## `OrdinaryUsersMata`

## Test Plans

### BMR Calculation Test
**Goal:** Verify the accuracy of Basal Metabolic Rate (BMR) calculation.  
**Method:** Invoke the `BMRcalculate()` method and check if the returned value is a valid float or integer.

### Calculation of Goal Macro Nutrients Test
**Goal:** Ensure the correctness of calculating goal macro nutrients.  
**Method:** Call the `calculate_goal_macro_nutrients()` method and validate that three nutrients are returned, all of which are floats.

### Calculation of Dietary Goals Test
**Goal:** Validate the calculation of dietary goals.  
**Method:** Execute the `calculate_goal_dietary_goal()` method and confirm that three goals are returned, and not all are integers.

### Update Suggestions Test
**Goal:** Ensure the suggestions are updated based on user input.  
**Method:** Simulate typing a query into the search bar, trigger the update function, and verify if the expected suggestion is present.

### Add and Remove Selected Food Test
**Goal:** Verify the functionality of adding and removing selected food items.  
**Method:** Add a food item to the selection, attempt removal, and check if the selection box count remains unchanged.

### Water Intake Functions Test
**Goal:** Test updating and clearing water intake levels.  
**Method:** Update water level, clear it, and verify the level changes accordingly.

### Save and Remove User Information Test
**Goal:** Ensure successful saving and removing of user information.  
**Method:** Save user info and attempt removal, confirming the operations were successful.

### Dietary Goal Operations Test
**Goal:** Validate the saving of dietary goals and recalculation of related metrics.  
**Method:** Save dietary goals, retrieve them, recalculate related metrics, and ensure they are updated.

### Meal Recommendations Test
**Goal:** Test the meal recommendation process.  
**Method:** Provide input values and check if meal recommendations are generated as expected.

### Save and Load Meal Plan Test
**Goal:** Verify the functionality of saving and loading a meal plan.  
**Method:** Populate the meal plan, save it, and load it again, ensuring the items are preserved.

### User Info Update Test
**Goal:** Test updating user information and UI reflection.  
**Method:** Update user info and verify if the UI reflects the changes appropriately.

### Dietary Goals Update Test
**Goal:** Validate updating dietary goals and verifying the updates.  
**Method:** Update dietary goals, retrieve them, and confirm the changes are reflected accurately.

## Test Results

The following table summarizes the results of the unit tests:

| Test Description                          | Result  |
|------------------------------------------|---------|
| BMR Calculation Test                     | Passed  |
| Calculation of Goal Macro Nutrients Test | Passed  |
| Calculation of Dietary Goals Test        | Passed  |
| Update Suggestions Test                  | Passed  |
| Add and Remove Selected Food Test        | Passed  |
| Water Intake Functions Test              | Passed  |
| Save and Remove User Information Test    | Passed  |
| Dietary Goal Operations Test             | Passed  |
| Meal Recommendations Test                | Passed  |
| Save and Load Meal Plan Test             | Passed  |
| User Info Update Test                    | Passed  |
| Dietary Goals Update Test                | Passed  |


# Unit Test Plans and Results

## `Report_Page`

## Test Plans

### Initialization Test
**Goal:** Verify the correct initialization of the `Report_Page` instance.  
**Method:** Check if the `food_dict` attribute is not None, the `date_difference` is set correctly, and an instance of `Worker` class is created.

### Clear Layouts Safe Test
**Goal:** Ensure the `clearLayoutsSafe()` method removes all widgets from a layout safely.  
**Method:** Add a widget to a layout, call the method, and verify that the layout is empty.

### Calculation of All Nutrient Updates Test
**Goal:** Validate the calculation of total calories, sugar, and protein.  
**Method:** Set a food dictionary with known values, call the calculation method, and assert the calculated totals.

### Calculation of Average Nutrients Test
**Goal:** Test the calculation of average nutrient values over multiple days.  
**Method:** Provide sample daily food dictionaries, calculate the averages for each meal type, and compare with expected values.

### Calculation of Average Nutrients without Meals Test
**Goal:** Validate the calculation of average nutrient values without separating meals.  
**Method:** Use a similar setup as the previous test but validate the aggregation without considering meal types.

### Refresh Content Test
**Goal:** Test the refresh of content with updated attributes.  
**Method:** Update start and end dates, as well as dietary goals, and verify if the attributes reflect the changes.

## Test Results

The following table summarizes the results of the unit tests:

| Test Description                                     | Result |
|------------------------------------------------------|--------|
| Initialization Test                                 | Passed |
| Clear Layouts Safe Test                             | Passed |
| Calculation of All Nutrient Updates Test             | Passed |
| Calculation of Average Nutrients Test                | Passed |
| Calculation of Average Nutrients without Meals Test  | Passed |
| Refresh Content Test                                | Passed |



## Automatic Testing:
Unit Testing Description:

We implemented comprehensive unit testing for our Python project to ensure the reliability and correctness of our codebase. Our unit tests primarily targeted the ordinary_users_mata.py and repoort_page.py modules, which collectively represent approximately two-thirds of our code.

Coverage Analysis:

The unit tests provided extensive coverage for critical functionalities within our project. By focusing on the most complex components, we aimed to validate the intricate aspects of our system and ensure its robustness.

Coverage Percentage:

Through our unit testing efforts, we were able to achieve coverage for approximately two-thirds of the program's functionality. This thorough test suite contributed to our confidence in the reliability and correctness of the covered features.

Uncovered Functionality:

While our unit testing strategy was comprehensive, there were certain functionalities that were not explicitly covered by our tests. These functionalities typically mirrored those already tested, leading us to conclude that additional testing might not have provided significant value.

Overcoming Shortfall:

To address the shortfall in test coverage for the remaining functionalities, we implemented rigorous manual testing procedures. This involved meticulous inspection and validation of the uncovered functionalities to ensure their correctness and reliability.
