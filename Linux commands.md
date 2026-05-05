**Software & Package Management**

- **`dpkg`**: The low-level tool for managing Debian (`.deb`) packages.
- **`apt`**: A high-level wrapper for `dpkg` that handles downloading and dependencies.
- **`snap` / `AppImage`**: Alternative software formats that live outside the `dpkg` database.

**Reading & Viewing Files**

- **`cat`** (Concatenate): Outputs the entire contents of a file (or joins multiple files).
- **`tac`**: The reverse of `cat`; prints lines from bottom to top.
- **`head`**: Shows the beginning (default top 10 lines) of a file.
- **`tail`**: Shows the end of a file. Use **`tail -f`** to follow live updates (logs).
- **`less`**: An interactive pager to scroll through large files without loading them all at once.

**Writing & Modifying Text**

- **`echo`**: Prints text or variables directly to the terminal.
- **`cat > file.txt`**: Creates a file and lets you type content into it from the keyboard.
- **`<< EOF` (Here Doc)**: A way to write multi-line blocks of text inside scripts.
- **`sed`**: A "stream editor" used to find and replace text (e.g., `s/old/new/g`).
- **`awk`**: A powerful tool for extracting and processing specific **columns** of data.

**Command "Glue" & Flow**

- **`|` (Pipe)**: Takes the output of one command and sends it to the next.
- **`>` / `>>`**: Redirects output to a file (overwrites or appends).
- **`xargs`**: Converts text into arguments for another command.
- **`{}`**: A placeholder used in `xargs -I` to specify where a filename should be placed in a command.