To clone this repository locally, open your terminal, navigate to where you want to clone the repo and run:  
**git clone https://github.com/CMaxK/unittesting_examples**

Then run:  
**pip install -r requirements.txt**

You will find an Easy, Medium and Hard folder. Each folder contains 2 scripts. One is the actual script we are going to test.
The other is the script containing the tests.

Navigate to each of the Easy, Medium, Hard directories using **cd**

Once inside the directory run the following command to trigger the test script:  
**python -m unittest name_of_test_script.py**

For example if you are starting with the Easy tests, you would **cd** into Easy and run:  
**python -m unittest tests.py**

You can change the verbosity of the ouput by adding the **-v** argument. For example:  
**python -m unittest -v tests.py**

Increased verbosity potentially makes it easier to debug.

Feel free to play around with the scripts and tests to see if you can implement your own.
