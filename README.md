# String Calculator

A simple string calculator implemented using **Test-Driven Development (TDD)** principles. The calculator supports basic addition of numbers in a string with various delimiters, including custom ones, and handles edge cases like negative numbers and empty strings.

---

## Features
- Add numbers provided in a string.
- Handle empty strings (returns `0`).
- Support multiple numbers separated by commas or newlines.
- Allow custom delimiters (e.g., `//[delimiter]\n[numbers]`).
- Throw exceptions for negative numbers with a detailed message.
- TDD approach with comprehensive unit tests.

---

## Examples

### Input & Output Examples:

| Input                  | Output |
|------------------------|--------|
| ""                    | `0`    |
| "1"                   | `1`    |
| "1,2"                 | `3`    |
| "1,2,3,4"             | `10`   |
| "1\n2,3"             | `6`    |
| "//;\n1;2"           | `3`    |
| "1,-2,-3"             | Exception: `negative numbers not allowed -2, -3` |

---

## Requirements
- Python 3.7+
- [PyTest](https://pytest.org/) for running tests

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shivyas10/incubyte_tdd_assessment.git
   cd calculator
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   .\venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install pytest
   ```

---

## How to Use

### Running the Calculator:
Edit `calculator.py` and run the `add` method directly in your IDE or a script:
```python
from calculator import Calculator

result = Calculator.add("1,2,3")
print(result)  # Output: 6
```

---

## Running Tests

1. Run all tests using PyTest:
   ```bash
   pytest
   ```

2. Run a specific test:
   ```bash
   pytest test_string_calculator.py::test_empty_string
   ```

---

## Project Structure
```
string-calculator/
├── calculator.py          # Main implementation of the String Calculator
├── test_string_calculator.py # Unit tests for the String Calculator
├── README.md              # Project documentation

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---
