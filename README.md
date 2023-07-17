# Training Plan Generator

## Tech Stack

- Python 3.9

## Setup

1. Install Python 3.9
2. CD into the project directory

    ```bash
    cd training-plan-generator
    ```

3. Install virtualenv

    ```bash
    pip install virtualenv
    ```

4. Create a virtual environment

    ```bash
    python -m venv venv
    ```

5. Activate the virtual environment

    ```bash
    ./venv/Script/activate
    ```

6. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

7. Run the app

    ```bash
    python src/main.py
    ```

If you would like to test the app manually, you can disable the GUI by setting `GUI_ENABLED` to `False` in `src/main.py`, then
modify the start and end dates as required.

## Assumptions

I have made the following assumptions:

- The start date is flexible, but the race date is fixed.
- Therefore, the start date will be modified to make the period divisible by 7.

## Project Structure and Design

The project follows MVC pattern. The model is in `src/model`, the view is in `src/gui`, and the controller is in `src/main.py`.

The data flows only from the controller to the view. The view is not allowed to modify the data. The view is only allowed to display the data.

The model receives the data from the controller and processes it.

### Project structure:

```plaintext
src\
    gui\
        __init__.py
        gui.py
    model\
        __init__.py
        plan.py
        week.py
    main.py
```
