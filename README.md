# BBOS - Basic Build Operating Software

A Python-based mini operating system running in the terminal, featuring a custom file system, a 3D flight simulator, utilities, and more.

## Overview

BBOS (Basic Build Operating Software) is a complete operating system simulation built entirely in Python. It features:
- **Custom Virtual File System**: In-memory file system using Python dictionaries
- **3D Flight Simulator**: Terminal-based raycasting game with physics
- **Command Shell**: Unix-like command interface
- **Multiple Programs**: Fibonacci calculator, wisdom generator, file system utilities
- **Global Shutdown**: System-wide shutdown mechanism accessible from any program

## Features

### Core System
- **Virtual File System (VFS)**: Navigate directories, manage files stored as strings ("Dash files")
- **Command Parser**: Flexible command execution (e.g., `%pr home` or `home %pr`)
- **System Context**: Persistent state management across programs
- **Boot Sequence**: Animated boot with scrollart visualizations

### Built-in Programs
- **Flight Simulator (`fsys`)**: 3D raycasting game with music, scoring, and crash detection
- **Fibonacci Calculator (`fibc`)**: High-performance calculator with memoization (up to 400,400th number)
- **God (`god`)**: Random wisdom generator with Stoic and Bhagavad Gita quotes
- **Real File System (`realfs`)**: Interface to actual file system for text file operations
- **Random Sound Generator (`rsg`)**: Audio experimentation tool

## Requirements
- **OS**: Windows (Required for `msvcrt`, `winsound`, and `ctypes.windll`)
- **Python**: 3.x
- **Dependencies**: See `requirements.txt`

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sswatdash-design/bb0s.git
   cd bb0s
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run BBOS:
```bash
python scripts/fsys_dynamic.py
```

Watch the boot animation, then interact with the command prompt:
```
/$ >> help
```

## Available Commands

| Command | Description |
| --- | --- |
| `help` | Show help menu (commands or general info) |
| `%sw` | Show files/folders in current directory |
| `%pr [dir]` | Change priority/directory (no argument returns to root) |
| `realfs` | Open real file system interface |
| `fibc` | Launch Fibonacci calculator |
| `god` | Launch wisdom generator |
| `fsys` | Launch 3D flight simulator game |
| `rsg` | Random sound generator |
| `shutdown` or `z` | Shutdown BBOS |

## Flight Simulator Controls

| Key | Action |
| --- | --- |
| **W** | Increase Speed |
| **S** | Decrease Speed |
| **A** | Turn Left |
| **D** | Turn Right |
| **Q** | Increase Altitude |
| **E** | Decrease Altitude |
| **I** | Pitch Up |
| **K** | Pitch Down |
| **R** | Radio (Next Song) |
| **X** | Exit Flight Simulator |
| **Z** | Shutdown Entire System |

## Global Shutdown

Press **Z** or type `shutdown` anywhere in BBOS to trigger a graceful system shutdown. This works from:
- Command prompt
- Inside any running program (flight sim, fibonacci calculator, god, etc.)
- Any input prompt

## Architecture

BBOS implements a simplified operating system architecture:

- **Kernel Layer**: System context initialization, virtual file system management
- **Shell Layer**: Command parser, main execution loop
- **Application Layer**: All programs (fsys, fibc, god, realfs, etc.)

The entire OS runs in a single Python process with shared state managed through the system context dictionary.

## Music Files

The flight simulator supports background music, but music files are not included in this repository due to size constraints. Place your own `.mp3` or `.wav` files in the `music/` directory to enable the radio feature. The system will handle missing music files gracefully.

## Developer

Created by Saswat Dash

## Troubleshooting

- **No Sound**: Ensure system volume is up (uses Windows `winsound` and MCI)
- **Console Display Issues**: Use a monospaced font terminal with sufficient window size
- **Import Errors**: Ensure you're using the virtual environment with dependencies installed
- **Module Not Found**: Verify you're running from the project root directory
