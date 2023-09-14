pytest -s -v --capture=tee-sys .\test_001_AccountRegistration.py --browser chrome

pytest -s -v -m "sanity or regression" --html="reports\report.html" .\testCases --browser chrome