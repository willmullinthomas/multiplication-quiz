# multiplication-quiz
A simple python multiplication table quiz with a UI created in PyQt5. Users can configure their quiz based on the number of questions they want to try and what the largest factor in each equation can be (eg 9x9, 12x12).

The app can be run locally by running ```python main.py``` in the command line from the root directory.

Unit tests are in the ```test``` directory. They can be run from the root directory with ```python -m unittest```.

To build, run ```pyinstaller main.spec``` from the root directory. This creates the executable ```dist/main/main.exe``` which runs as a desktop application.

Underlying game logic can be found in ```src/model``.

gui is in ```src/view```.
