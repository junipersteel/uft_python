# ============================================================================
# Advantage Online Shopping Utility Library
#
# Purpose:
#   This library contains reusable helper functions that can be loaded
#   into UFT Python tests using:
#
#       LoadFunctionLibrary(...)
#
# Functions Included:
#   GetComments()
#       Calls a REST API and retrieves customer comments.
#
#   show_info_dialog()
#       Displays a graphical information dialog using Tkinter.
#
#
# Why Create Libraries?
#
# Instead of duplicating code throughout many test scripts,
# reusable functionality can be centralized into a library.
#
# Benefits:
#   - Easier maintenance
#   - Less duplicate code
#   - Better readability
#   - Encourages framework design
#
# Python Concepts:
#   - Imports
#   - Functions
#   - HTTP requests
#   - JSON processing
#   - GUI programming with Tkinter
#
# UFT Concepts:
#   - Function libraries
#   - API testing
#   - Reusable automation utilities
# ============================================================================


# ----------------------------------------------------------------------------
# Import Required Libraries
# ----------------------------------------------------------------------------

# Requests is a popular third-party package used for
# interacting with REST APIs.
#
# Typical uses:
#   - Login APIs
#   - Order APIs
#   - Search APIs
#   - Backend validation
import requests


# Tkinter is Python's standard GUI framework.
#
# It allows Python programs to create native desktop windows,
# buttons, labels, dialogs, and other user interface components.
#
# The alias "tk" is commonly used by Python developers.
import tkinter as tk


# ttk (Themed Tk Widgets) provides more modern controls
# with improved appearance and platform integration.
#
# Most newer Tkinter applications prefer ttk controls
# rather than older standard widgets.
from tkinter import ttk


# ============================================================================
# REST API Helper Function
# ============================================================================

def GetComments(base_url):
    """
    Retrieve the most popular comments from
    Advantage Online Shopping.

    Parameters:
        base_url

    Example:
        https://www.advantageonlineshopping.com

    Returns:
        Dictionary containing API response data.
    """

    # ------------------------------------------------------------------------
    # Build Endpoint URL
    # ------------------------------------------------------------------------

    # rstrip('/') removes a trailing slash if present.
    #
    # Example:
    #
    # Before:
    #   https://site.com/
    #
    # After:
    #   https://site.com
    #
    # This prevents accidental double slashes.
    url = (
        f"{base_url.rstrip('/')}"
        "/catalog/api/v1/MostPopularComments"
    )


    # ------------------------------------------------------------------------
    # HTTP Headers
    # ------------------------------------------------------------------------

    # Headers provide metadata about an HTTP request.
    #
    # Content-Type indicates the type of data being exchanged.
    #
    # Although this GET request does not send JSON,
    # including headers is a common REST API practice.
    headers = {
        "Content-Type": "application/json"
    }


    # ------------------------------------------------------------------------
    # Send HTTP Request
    # ------------------------------------------------------------------------

    # Execute a GET request.
    #
    # GET is used to retrieve information without modifying
    # server-side data.
    response = requests.get(url)


    # ------------------------------------------------------------------------
    # Validate HTTP Response
    # ------------------------------------------------------------------------

    # Raises an exception if the server returns an error.
    #
    # Examples:
    #   400 Bad Request
    #   401 Unauthorized
    #   404 Not Found
    #   500 Internal Server Error
    response.raise_for_status()


    # ------------------------------------------------------------------------
    # Convert JSON into Python Objects
    # ------------------------------------------------------------------------

    # Most REST services return JSON.
    #
    # response.json() converts JSON into native Python
    # dictionaries and lists.
    data = response.json()


    # ------------------------------------------------------------------------
    # Return Result
    # ------------------------------------------------------------------------

    # Wrap the API response inside a Python dictionary.
    #
    # This allows future expansion by adding additional
    # properties without changing calling code.
    return {
        "response": data,
    }


# ============================================================================
# GUI Dialog Helper
# ============================================================================

def show_info_dialog(title, message):
    """
    Display a graphical information window.

    Parameters:
        title
            Window title.

        message
            Text displayed inside the dialog.

    Example:
        show_info_dialog(
            "Assessment Complete",
            "No harmful comments detected."
        )
    """

    # ------------------------------------------------------------------------
    # Create Main Window
    # ------------------------------------------------------------------------

    # Tk() creates the application's main window.
    #
    # Everything displayed will exist inside this window.
    dialog = tk.Tk()


    # Display title text in the window title bar.
    dialog.title(title)


    # Allow the user to resize the window.
    #
    # True, True means:
    #   Width can change
    #   Height can change
    dialog.resizable(True, True)


    # ------------------------------------------------------------------------
    # Set Default Window Size
    # ------------------------------------------------------------------------

    # Geometry uses:
    #
    # "width x height"
    #
    # Example:
    #   650 pixels wide
    #   800 pixels high
    dialog.geometry("650x800")


    # ------------------------------------------------------------------------
    # Main Container Frame
    # ------------------------------------------------------------------------

    # Frames are containers used to organize controls.
    #
    # Padding adds spacing between controls
    # and window borders.
    frame = ttk.Frame(dialog, padding=20)


    # Pack positions the frame within the window.
    #
    # fill="both"
    #   Expand horizontally and vertically.
    #
    # expand=True
    #   Grow when the window is resized.
    frame.pack(
        fill="both",
        expand=True
    )


    # ------------------------------------------------------------------------
    # Information Icon
    # ------------------------------------------------------------------------

    # Create a large information symbol.
    #
    # Unicode character:
    #   ℹ
    #
    # Used to visually indicate informational content.
    icon_label = tk.Label(
        frame,

        text="ℹ",

        # Font settings:
        #
        # Segoe UI
        # 32 pt
        font=("Segoe UI", 32),

        # Blue color
        fg="#0078D7"
    )


    # Position the icon within a grid layout.
    #
    # row=0
    # column=0
    #
    # rowspan=2 means the icon spans two rows.
    icon_label.grid(
        row=0,
        column=0,
        rowspan=2,
        padx=(0, 15),
        sticky="n"
    )


    # ------------------------------------------------------------------------
    # Header Label
    # ------------------------------------------------------------------------

    header_label = ttk.Label(
        frame,

        text=title,

        font=(
            "Segoe UI",
            16,
            "bold"
        )
    )

    header_label.grid(
        row=0,
        column=1,
        sticky="w"
    )


    # ------------------------------------------------------------------------
    # Message Area
    # ------------------------------------------------------------------------

    # Display the message passed into the function.
    #
    # wraplength=500
    #   Automatically wraps long text.
    #
    # justify="left"
 
