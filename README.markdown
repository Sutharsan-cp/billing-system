# Billing System

A Python-based billing system with a Tkinter GUI, featuring a login page and a billing interface for managing purchases in Medical, Grocery, and Cold Drinks categories.

## Overview
This project is a desktop application developed using Python and Tkinter. It includes a login system to authenticate users and a billing system to calculate the cost of items, apply taxes, generate bills, and save them locally. The application supports three categories of items: Medical, Grocery, and Cold Drinks, with predefined prices and tax rates.

## Features
- **Login System**: Authenticate users with predefined employee credentials.
- **Billing Interface**: Add items from Medical, Grocery, and Cold Drinks categories with quantity inputs.
- **Price and Tax Calculation**: Automatically calculate total price and taxes (Medical: 5%, Grocery: 5%, Cold Drinks: 10%).
- **Bill Generation**: Generate a detailed bill with customer details, items, quantities, prices, and taxes.
- **Bill Saving**: Save bills to a local directory (`bills/`).
- **Bill Search**: Search for existing bills by bill number.
- **Clear and Exit Options**: Reset the form or exit the application with confirmation prompts.

## Screenshots
(Add a screenshot of the login page and billing interface here after uploading them to your repository)

## Installation
Follow these steps to set up and run the project on your local machine.

### Prerequisites
- Python 3.6 or higher (Tkinter is included in the standard library)
- Git (to clone the repository)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/billing-system.git
   cd billing-system
   ```

2. **Create the Bills Directory** (if not already present):
   - The application saves bills in a `bills/` directory. Create this folder manually in the project root:
     ```bash
     mkdir bills
     ```

3. **Run the Application**:
   - Start with the login page:
     ```bash
     python login.py
     ```
   - Use the following credentials to log in:
     - Username: `Meena`, Password: `0606`
     - Username: `sutharsan`, Password: `7373`
     - Username: `barath`, Password: `2005`

4. **Usage**:
   - After logging in, the billing interface opens.
   - Enter customer details (name and phone number).
   - Add items by entering quantities in the Medical, Grocery, or Cold Drinks sections.
   - Click "Total" to calculate prices and taxes.
   - Click "Generate Bill" to display the bill in the Bill Area.
   - Save the bill to the `bills/` directory by confirming the prompt.
   - Search for a bill using the bill number, clear the form, or exit as needed.

## Project Structure
- `__init__.py`: Package initialization file.
- `login.py`: Login interface to authenticate users.
- `billing_system.py`: Main billing application with GUI.
- `bills/`: Directory where generated bills are saved (created manually or automatically).
- `requirements.txt`: Lists dependencies (Python standard library).
- `.gitignore`: Excludes unnecessary files (e.g., `__pycache__`, `bills/`).
- `README.md`: Project documentation.

## Known Issues
- The bill save path in `billing_system.py` is hardcoded (`D:/BARATH/...`). This should be updated to a relative path (e.g., `bills/`) for portability.
- Some labels in the bill area are incorrect (e.g., "Sanitizer" is used for multiple items). This needs to be fixed for accurate billing.
- The grocery tax calculation uses an incorrect multiplier (`*5` instead of `*0.05`).

## Future Improvements
- Update the bill save path to use a relative directory for better portability.
- Fix incorrect labels in the bill area and ensure proper variable usage.
- Add a database (e.g., SQLite) to store employee credentials and bills.
- Implement user registration and password reset features.
- Enhance the UI with modern styling using Tkinter's `ttk` themes.
- Add support for printing bills directly from the application.

## License
MIT License