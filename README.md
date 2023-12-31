
# README for Autoclicker Application

## Overview
This Autoclicker Application is a Python-based tool developed using PyQt5 and PyAutoGUI. It allows users to record and execute custom click patterns on their screen. Users can set up a sequence of clicks and then have the application automate the clicking process.

## Features
- **Click Pattern Recording**: Users can click on different parts of the screen to record a sequence of click positions.
- **Visual Feedback**: The application provides visual feedback for recorded clicks.
- **Execution of Click Patterns**: Once a click pattern is recorded, users can execute it, and the application will automatically perform the clicks.
- **Reset Functionality**: Users can reset their click pattern and start over if needed.

## Installation
To run this application, you need to have Python installed on your system along with the PyQt5 and PyAutoGUI libraries.

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install the required libraries using pip:

   ```
   pip install PyQt5 pyautogui pynput
   ```

## Usage
1. Start the application by running the Python script.
2. CD into the directory where the file is located and use "python3 autoclicker.py" to run the script
3. The application window will open. Click on the desired locations on your screen to record the click pattern.
4. Click on the "Done" button to execute the click pattern or "Reset" to clear the current pattern and start over.
5. The application will minimize and start executing the click pattern after a brief delay.

## Precautions
- **Supervision**: Always supervise the execution of the click pattern to avoid unintended clicks.
- **Delay Adjustment**: Adjust the delay between clicks in the code if needed (default is set to 0.5 seconds).
- **Minimization Delay**: There's a delay before the window minimizes to execute the click pattern. Ensure that the screen is set up as desired during this time.

## Contributing
Contributions to the project are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License
This project is open-source and is available under the [MIT License](https://opensource.org/licenses/MIT).

## Contact
For any queries or feedback, please contact the developer.
