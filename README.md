GEDCOM project for SSW 555.

# Description

Parses a given GEDCOM file and outputs a tabular view of the provided data
along with various errors that are present in the file. These errors are
problems with the logic of the information, like a death occurring before a
birth. The GEDCOM file provided to the program is expected to be syntactically
correct.

# Usage

```
pip install -r requirements.txt
```

```
python ged.py <gedcom_file>
```

Output to a file:

```
python ged.py <gedcom_file> -o <output_file>
```

Additional usage information:

```
python ged.py - h
```

# Development

# Development environment

Python 3 is used for this project. All commands assume that the `python`
executable defaults to Python 3.

After cloning, navigate to the project directory.

```
python -m venv .venv
```

This creates a virtual environment so you don't install dependencies to your
system directories. This keeps your system clean while you work on the project.

(Linux and MacOS)

```
source .venv/bin/activate
```

(Windows) In the command prompt or Powershell:

```
.venv\Scripts\activate.bat
```

While inside the virtual environment:

```
pip install -r requirements.txt
```

That will install the required packages for the project to your virtual
environment. When you leave the virtual environment, you lose access to the
packages until you activate the environment again.

# Running tests

While in the root of the project directory:

```
python -m nose
```

# Adding a new required package

While in the root of the project directory:

```
pip freeze > requirements.txt
```
