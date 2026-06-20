# Python Workflow Examples

A lightweight, clean reference library demonstrating common python development workflows, including date/time formatting with system timezones, string format validations, and built-in unit testing.

## Features

* **Date Formatting & Timezone Parsing**: Uses the modern standard library `zoneinfo` to convert local datetime strings to UTC.
* **String Validations**: Validates common string formats (e.g., email addresses) using standard expressions.
* **Unit Testing**: Tests are structured using the built-in `unittest` module.

## Setup & Testing

To run the test suite:

```bash
python3 -m unittest discover -s tests
```
