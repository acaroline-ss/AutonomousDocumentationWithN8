# async_tasks.py

## Summary
This module demonstrates the use of Python's `asyncio` for simulating asynchronous fetch and download operations. It includes functions to mimic network latency when fetching URLs, coordinating multiple asynchronous downloads concurrently, running these downloads synchronously via a helper function, and performing a periodic asynchronous task.

## Classes
No classes are defined in this module.

## Functions and Methods

### `async def fake_fetch(url, out_file)`
- Simulates fetching data asynchronously from a given URL.
- Parameters:
  - `url` (str): The URL to "fetch" from.
  - `out_file` (str or Path): The path where the fetched content should be written.
- Behavior:
  - Waits for 1 second to simulate network latency.
  - Writes a simple text indicating the content was downloaded from the given URL to the specified output file.
  - Returns the path of the output file.

---

### `async def fake_downloads(urls, out_dir="downloads")`
- Coordinates multiple asynchronous fetches concurrently.
- Parameters:
  - `urls` (iterable of str): A list or collection of URLs to "download".
  - `out_dir` (str, optional): Directory path where downloaded files will be saved. Defaults to `"downloads"`.
- Behavior:
  - Creates the output directory if it does not exist.
  - For each URL, schedules a `fake_fetch` task saving to a uniquely named file in `out_dir`.
  - Runs all fetch tasks concurrently using `asyncio.gather`.
  - Returns a list of paths to the downloaded files.

---

### `def run_fake_downloads(urls)`
- Synchronously runs the asynchronous `fake_downloads` function.
- Parameters:
  - `urls` (iterable of str): URLs to download.
- Behavior:
  - Records the start time.
  - Executes the asynchronous downloads using `asyncio.run` and waits for results.
  - Prints the total elapsed time for downloads.
  - Returns a list of downloaded file paths.

---

### `async def periodic_task(interval=2, count=3)`
- Performs a periodic asynchronous task multiple times.
- Parameters:
  - `interval` (int or float, optional): The number of seconds to wait between each task execution. Defaults to 2 seconds.
  - `count` (int, optional): How many times to repeat the task. Defaults to 3.
- Behavior:
  - Loops `count` times, printing a message each iteration.
  - Waits asynchronously for `interval` seconds between iterations.
  - Returns the string `"Finalizado"` after completion.

## Important Variables

- `urls` (function parameter): Input list or iterable of URLs to be processed.
- `out_dir` (function parameter, default `"downloads"`): Directory where downloaded files are stored.
- `tasks` (local variable in `fake_downloads`): A list holding all asynchronous fetch tasks to be run concurrently.
- `start` (local variable in `run_fake_downloads`): The timestamp marking the beginning of execution to compute total runtime.
- `interval` and `count` (parameters in `periodic_task`): Control timing and iteration count of the periodic asynchronous task.

---

This module is primarily an educational or demonstrative example on using `asyncio` for asynchronous I/O simulation and task scheduling.

# cli_interface.py

## Summary
This script provides a simple command-line interface (CLI) framework for user interaction. It includes functions to display menus, prompt for user input or confirmation, and print a banner and help menu. The code is organized to facilitate choices from a given set of options and to assist users in navigating different simulated commands related to repository and file management.

## Functions

### `ask_choice(options: dict)`
- **Purpose:**  
  Displays a list of options to the user and prompts them to select one.
- **Parameters:**  
  - `options` (dict): A dictionary where keys represent option identifiers and values are labels to display.
- **Returns:**  
  - The user's choice (key) if it exists in the options dictionary, otherwise `None`.

### `ask_input(prompt: str, default=None)`
- **Purpose:**  
  Prompts the user for input with a given message and returns their input or a default value if no input is provided.
- **Parameters:**  
  - `prompt` (str): The message displayed to the user when requesting input.  
  - `default` (optional): The value returned if the user inputs nothing.
- **Returns:**  
  - The user's input as a string or the default value if input is empty.

### `confirm(prompt: str) -> bool`
- **Purpose:**  
  Asks the user for a yes/no confirmation.
- **Parameters:**  
  - `prompt` (str): The confirmation message presented to the user.
- **Returns:**  
  - `True` if the user inputs "s" (indicating "sim" / yes), otherwise `False`.

### `banner()`
- **Purpose:**  
  Prints a decorative banner to the console to identify the program.

### `help_menu()`
- **Purpose:**  
  Prints a help menu listing available simulated commands and their brief descriptions.

## Variables

- No global or module-level variables are defined explicitly outside the functions in this script.

## Script Entry Point

- When executed directly, the script calls:
  - `banner()` to display the program banner.
  - `help_menu()` to show the list of command options and descriptions.

# file_utils.py

## Summary
This module provides utility functions for common file and directory operations. It includes functions to ensure directories exist, list Python files in a directory, compute file hashes, read from and save content to files, compare files based on their contents, and summarize basic statistics about a directory's files.

---

## Functions

### `ensure_dir(path: str)`
Creates the specified directory path if it doesn't already exist, including any necessary parent directories.

- **Parameters:**
  - `path` (str): The directory path to create.
- **Returns:**
  - The input `path` string.

---

### `list_python_files(directory: str)`
Recursively lists all Python files (`*.py`) in the given directory.

- **Parameters:**
  - `directory` (str): The directory path to search.
- **Returns:**
  - A list of absolute file paths (strings) to Python files found.

---

### `file_hash(filepath: str)`
Calculates the SHA-256 hash of a file's contents.

- **Parameters:**
  - `filepath` (str): The path to the file.
- **Returns:**
  - A hexadecimal string representing the SHA-256 hash of the file contents.

---

### `save_to_file(filepath: str, content: str)`
Saves a string `content` to a file at the given path, creating parent directories if necessary.

- **Parameters:**
  - `filepath` (str): The full file path where content should be saved.
  - `content` (str): The string content to write to the file.

---

### `read_file(filepath: str)`
Reads and returns the content of a file as a string. Returns an empty string if the file does not exist.

- **Parameters:**
  - `filepath` (str): The path to the file to read.
- **Returns:**
  - The file content as a string, or `""` if the file does not exist.

---

### `compare_files(file1: str, file2: str) -> bool`
Compares two files by computing and comparing their SHA-256 hashes. Returns `True` if the files are identical, `False` otherwise.

- **Parameters:**
  - `file1` (str): Path to the first file.
  - `file2` (str): Path to the second file.
- **Returns:**
  - Boolean indicating if the files are identical in contents.

---

### `summarize_directory(directory: str)`
Generates a summary of a directory's contents, counting the total number of files, lines, and characters across all files (ignoring unreadable files).

- **Parameters:**
  - `directory` (str): The directory path to summarize.
- **Returns:**
  - A dictionary with keys:
    - `"files"`: total number of files (int)
    - `"lines"`: total number of lines across all files (int)
    - `"chars"`: total number of characters across all files (int)

---

## Important Variables

- `summary` (dict): Used in `summarize_directory` to accumulate counts of files, lines, and characters in the target directory.
- `h` (hashlib.sha256 object): Used in `file_hash` to incrementally compute the SHA-256 hash of a file.
- `files` (list): Used in `list_python_files` to collect Python file paths found in the directory traversal.

---

## Classes

This module does not define any classes.

# main.py

## Summary
This script provides a command-line interface (CLI) tool to interact with GitHub repositories and Python files within directories. It allows users to simulate cloning and updating repositories, list Python files in a directory, perform asynchronous fake downloads, and generate a summary of a specified folder. The program runs in a loop until the user chooses to exit.

## Classes
This file does not define any classes explicitly. It utilizes the following imported class:

- **RepoHandler** (imported from `repo_handler`):
  - Purpose: Manage GitHub repository operations such as cloning and pulling updates.
  - Attributes and methods are not detailed in this file.

## Functions or Methods

### `main()`
- Purpose: Drives the CLI menu interface for interacting with repository operations, file listing, downloading, and directory summarization.
- Parameters: None
- Behavior:
  - Displays a banner.
  - Presents a menu with six options.
  - Based on user choices, it:
    - Simulates cloning a GitHub repository.
    - Simulates updating a local repository.
    - Lists all Python files in a given directory and optionally saves the list to a file.
    - Runs asynchronous fake downloads from user-provided URLs.
    - Summarizes contents of a specified directory.
  - Repeats until the user chooses to exit.
  - Handles invalid input by notifying the user.

## Important Variables

- `options` (dict):  
  A dictionary mapping string keys representing user choices to their corresponding descriptions in Portuguese. Used to display the menu and interpret user input.

- `choice` (str):  
  Stores the user input choice for menu selection.

- `repo_url` (str):  
  Holds the GitHub repository URL input by the user when cloning a repo.

- `branch` (str):  
  Stores the branch name input by the user or defaults to `"main"`.

- `repo_name` (str):  
  Name of the local folder containing the repository when updating (pulling).

- `path` (str):  
  Directory path input by the user for listing Python files or summarizing folder contents.

- `py_files` (list of str):  
  List of Python file paths found in the specified directory.

- `urls` (list of str):  
  List of URLs collected from user input for simulated asynchronous downloads.

- `results` (unknown):  
  Contains results returned from the asynchronous fake downloads. Format/value depends on the `run_fake_downloads` function implementation.

- `summary` (dict):  
  A dictionary summarizing folder contents (keys and values depending on `summarize_directory` function).

---

## External Imports and Their Roles

- `ask_choice`, `ask_input`, `confirm`, `banner` (from `cli_interface`):  
  Functions for CLI interactions such as presenting options, getting user input, confirmation prompts, and displaying banners.

- `RepoHandler` (from `repo_handler`):  
  Class to handle repository cloning and pulling operations.

- `list_python_files`, `save_to_file`, `summarize_directory` (from `file_utils`):  
  Utility functions to list Python files, save text to file, and generate directory summaries.

- `run_fake_downloads` (from `async_tasks`):  
  Function to simulate asynchronous downloads from user-provided URLs.

---

# End of documentation for `main.py`

# repo_handler.py

## Summary
This module provides the `RepoHandler` class, which simulates basic Git repository operations such as cloning and pulling updates. It is designed to handle repository URLs, branches, and local destination folders, creating or updating a placeholder `README.md` file to represent these operations.

## Classes

### `RepoHandler`
- **Purpose:**  
  Manages a simulated clone and pull operations for a Git repository given its URL, branch, and local destination folder.

- **Attributes:**  
  - `repo_url` (`str`): The URL of the repository.  
  - `branch` (`str`): The branch to operate on (default is `"main"`).  
  - `dest` (`str`): Local destination folder for the repository. Defaults to the repository name extracted from the URL if not explicitly provided.

- **Methods:**  
  - `__init__(self, repo_url: str, branch: str = "main", dest: str = None)`  
    Initializes the `RepoHandler` with the repository URL, branch, and destination folder.  
    - Parameters:  
      - `repo_url`: Repository URL string.  
      - `branch`: Branch name, default `"main"`.  
      - `dest`: Destination folder path; if `None`, set to repo name extracted from URL.
  
  - `get_repo_name(repo_url: str) -> str` (staticmethod)  
    Extracts the repository name from the given repository URL by parsing the URL path and stripping `.git` if present. Returns `"repo_demo"` if the name cannot be extracted.  
    - Parameters:  
      - `repo_url`: Repository URL string.  
    - Returns:  
      - Repository name as a string.

  - `clone(self)`  
    Simulates cloning the repository by checking if the destination exists; if not, it creates the destination folder and writes a `README.md` file indicating the source URL and branch.  
    - No parameters or return value.  
    - Prints messages indicating whether the repository was cloned or if it already exists.

  - `pull(self)`  
    Simulates pulling updates by appending a line to the existing `README.md` file in the destination folder. It will not attempt to pull if the folder does not exist.  
    - No parameters or return value.  
    - Prints messages indicating success or failure of the update.

## Functions / Methods

### `RepoHandler.__init__(repo_url: str, branch: str = "main", dest: str = None)`
- Initializes a repository handler object with the provided repository URL, branch, and destination.
- Parameters:  
  - `repo_url`: The URL of the git repository.  
  - `branch`: The branch to work on (default `"main"`).  
  - `dest`: The local directory to clone the repo into; if `None`, it is derived from the repository URL.

### `RepoHandler.get_repo_name(repo_url: str) -> str`
- Parses the repository name from a repository URL by extracting the last segment of the path and removing `.git`.
- Parameters:  
  - `repo_url`: The URL string of the repository.  
- Returns:  
  - A string containing the repository name or `"repo_demo"` if no name can be extracted.

### `RepoHandler.clone()`
- Simulates cloning the repository by creating a directory and `README.md` unless the destination directory already exists.
- No parameters.
- Prints status messages about cloning success or if the repo already exists locally.

### `RepoHandler.pull()`
- Simulates updating the repository by appending a line in the `README.md` file in the destination directory.
- No parameters.
- Prints status messages about update success or failure if the directory does not exist.

## Important Variables

- `repo_url`  
  Holds the repository URL passed to the handler; used as the source identifier.

- `branch`  
  Stores the branch name to simulate operations on, defaulting to `"main"`.

- `dest`  
  Destination folder path where repository files will be stored locally. If not provided, derived from the repository URL.

- `path` (in `get_repo_name` method)  
  Extracted path component of the URL used to determine the repository name.

---

This documentation covers all components explicitly present in `repo_handler.py` and explains their roles and parameters.

