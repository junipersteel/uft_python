# ============================================================================
# Python Library Functions
#
# Purpose:
#   This file contains reusable functions and classes that can be imported
#   into UFT One Python tests.
#
# Why use a library?
#   Rather than duplicating code across multiple test scripts, common
#   functionality can be placed into a library and reused wherever needed.
#
# Typical examples:
#   - Logging utilities
#   - Timing utilities
#   - Database helpers
#   - API wrappers
#   - Test data functions
#   - Application-specific helper methods
#
# UFT Best Practice:
#   Store reusable code in libraries and keep test actions focused on
#   business-process automation.
# ============================================================================


# ----------------------------------------------------------------------------
# Import Required Modules
# ----------------------------------------------------------------------------

# Import Python's built-in datetime module.
#
# This module provides classes and functions for working
# with dates and times.
#
# Common uses:
#   - Logging timestamps
#   - Measuring execution times
#   - Creating date-based filenames
#   - Recording test execution information
import datetime


# ----------------------------------------------------------------------------
# Simple Function Example
# ----------------------------------------------------------------------------

def g():
    """
    A very simple function.

    Functions allow a block of code to be executed whenever needed.
    Instead of copying the same code repeatedly, we place it inside
    a function and call it as required.

    Example:
        g()
    """

    # Print text to the console.
    #
    # print() is one of Python's most fundamental functions.
    print("This is a function call !")

    # Print a second message.
    print("And another line.")


# ----------------------------------------------------------------------------
# Dog Class Example
# ----------------------------------------------------------------------------

class Dog:
    """
    Simple demonstration of a Python class.

    A class acts as a blueprint for creating objects.

    Example:
        my_dog = Dog("Buddy", 3)

    The object contains:
        name = "Buddy"
        age = 3
    """

    # ------------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------------

    def __init__(self, name, age):
        """
        Constructor method.

        __init__() is automatically called whenever a new
        instance of the class is created.

        Parameters:
            name - the dog's name
            age  - the dog's age
        """

        # self represents the current instance (object).
        #
        # These values are stored inside the object and
        # can be accessed from other methods.
        self.name = name
        self.age = age

    # ------------------------------------------------------------------------
    # Object Method
    # ------------------------------------------------------------------------

    def bark(self):
        """
        Example instance method.

        Methods define behavior for an object.
        """

        # f-strings provide an easy way to insert variables
        # into strings.
        #
        # Example result:
        #   Buddy says woof!
        return f"{self.name} says woof!"

    # ------------------------------------------------------------------------
    # Special Python Method
    # ------------------------------------------------------------------------

    def __str__(self):
        """
        String representation method.

        This method is automatically called when:
            print(my_dog)

        is executed.
        """

        # Example result:
        #   Buddy is 3 years old.
        return f"{self.name} is {self.age} years old."


# ----------------------------------------------------------------------------
# Logger Class
# ----------------------------------------------------------------------------

class Logger:
    """
    Simple logging utility.

    Logging is commonly used in automation frameworks to:
        - Track test execution
        - Record failures
        - Capture diagnostics
        - Aid troubleshooting

    UFT projects often include logging helpers similar to this.
    """

    def __init__(self):
        """
        Constructor.

        Currently no initialization logic is needed.

        'pass' is Python's placeholder statement used when
        a block is required syntactically but no code is
        needed yet.
        """
        pass

    def output(self, severity, message):
        """
        Output a timestamped log message.

        Parameters:
            severity - INFO, WARNING, ERROR, etc.
            message  - text to log

        Example:
            logger.output("INFO", "Login successful")
        """

        # Retrieve the current date and time.
        #
        # Example:
        #   2026-09-14 10:15:32.123456
        date_stamp = datetime.datetime.now()

        # Convert the datetime object into a string and combine
        # it with the message and severity.
        #
        # Example output:
        #
        # 2026-09-14 10:15:32.123456
        #     Login successful
        #     INFO
        print(str(date_stamp) + "     " + message + "    " + severity)


# ----------------------------------------------------------------------------
# Timer Class
# ----------------------------------------------------------------------------

class Timer:
    """
    Placeholder timer utility.

    This class will likely be expanded in future versions
    to support transaction timing or elapsed-time measurements.

    In larger UFT automation frameworks, timer classes are often
    used to measure:
        - Login duration
        - Search response times
        - Transaction completion times
        - API response times
    """

    def __init__(self):
        """
        Constructor.

        No initialization code currently required.
        """
        pass

    def out(self):
        """
        Placeholder method.

        Currently returns a fixed value.

        Future versions might:
            - Return elapsed time
            - Calculate duration
            - Generate performance statistics
            - Start or stop timers
        """

        # Return a simple integer value.
        #
        # The 'return' statement sends a value back
        # to the code that called the function.
        return 0
    
