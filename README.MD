# Setting Up a Python Virtual Environment and Installing Requirements

This guide walks you through the steps to set up a Python virtual environment and install dependencies from a `requirements.txt` file.

## Steps

### 1. Create a Virtual Environment

1. Open a terminal or command prompt.
2. Navigate to your project directory:
   ```bash
   cd /path/to/your/project
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
   - Replace `python` with `python3` if your default Python version is Python 2.
   - The `venv` folder will contain the virtual environment.

### 2. Activate the Virtual Environment

- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **On macOS and Linux**:
  ```bash
  source venv/bin/activate
  ```

Once activated, your terminal prompt will show the virtual environment's name, e.g., `(venv)`.

### 3. Install Dependencies

Ensure you have a `requirements.txt` file in your project directory. Then, run the following command to install the dependencies:
```bash
pip install -r requirements.txt
```

### 4. Verify Installation

To confirm the dependencies were installed correctly, run:
```bash
pip list
```
This will display all installed packages in the virtual environment.

### 5. Deactivate the Virtual Environment

When you are done working, deactivate the virtual environment:
```bash
deactivate
```
This will return your terminal to the global Python environment.

---

## Additional Notes

- If you don’t have `pip` installed, follow the official Python documentation to install it: [pip Installation Guide](https://pip.pypa.io/en/stable/installation/).
- Use `python --version` to check your Python version before creating the virtual environment.
- You can update `pip` to the latest version using:
  ```bash
  pip install --upgrade pip
  
