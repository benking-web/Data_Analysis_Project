# Steps to Resolve ModuleNotFoundError and Successfully Run Python Script

## **1. Identified the Python Version Being Used**
- Checked which Python executable was being used:
  ```powershell
  & "C:/Users/EMEKA BENKING UGWU/AppData/Local/Programs/Python/Python313/python.exe" --version

Confirmed that Python 3.13 was the active version.
2. Attempted to Run the Script
Initially ran the script:

& "C:/Users/EMEKA BENKING UGWU/AppData/Local/Programs/Python/Python313/python.exe" "c:/Users/EMEKA BENKING UGWU/Desktop/files/python folder/python_assignments/wk7_python_assignment/wk_7.py"

Encountered multiple ModuleNotFoundError messages for missing libraries.
3. Installed Missing Python Libraries
For each missing module, the following command was used:

Installed Pandas:
& "C:/Users/EMEKA BENKING UGWU/AppData/Local/Programs/Python/Python313/python.exe" -m pip install pandas

Installed Matplotlib:
& "C:/Users/EMEKA BENKING UGWU/AppData/Local/Programs/Python/Python313/python.exe" -m pip install matplotlib

Installed Seaborn:
& "C:/Users/EMEKA BENKING UGWU/AppData/Local/Programs/Python/Python313/python.exe" -m pip install seaborn

Installed Scikit-Learn:
& "C:/Users/EMEKA BENKING UGWU/AppData/Local/Programs/Python/Python313/python.exe" -m pip install scikit-learn

Alternatively, all required libraries were installed at once:
& "C:/Users/EMEKA BENKING UGWU/AppData/Local/Programs/Python/Python313/python.exe" -m pip install pandas matplotlib seaborn scikit-learn

4. Verified Installations
After installation, the modules were checked using:
& "C:/Users/EMEKA BENKING UGWU/AppData/Local/Programs/Python/Python313/python.exe" -c "import pandas, matplotlib, seaborn, sklearn; print('All modules loaded successfully!')"

If no errors appeared, it meant all required libraries were successfully installed.

5. Successfully Ran the Python Script
The script was then executed without issues:

& "C:/Users/EMEKA BENKING UGWU/AppData/Local/Programs/Python/Python313/python.exe" "c:/Users/EMEKA BENKING UGWU/Desktop/files/python folder/python_assignments/wk7_python_assignment/wk_7.py"

The script ran successfully without any ModuleNotFoundError.

Summary
The main issue was that Python 3.13 was being used, but required libraries were installed for Python 3.12. The solution was to:

Install the missing libraries for Python 3.13 using pip.
Verify installations to ensure modules loaded correctly.
Re-run the script, which then executed successfully.

