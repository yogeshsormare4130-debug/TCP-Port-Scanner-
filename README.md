# Python Port Scanner

A multithreaded TCP Port Scanner built using Python that scans a specified range of ports on a target host and identifies whether ports are open, closed, or timed out.

## Features

* Multithreaded scanning for faster performance
* Hostname to IP address resolution
* Custom port range scanning
* Scan result logging to a text file
* Displays scan duration and statistics
* Simple command-line interface

## Technologies Used

* Python 3
* Socket Programming
* Threading
* Queue Module

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yogeshsormare4130-debug/TCP-Port-Scanner-
```

2. Navigate to the project directory:

```bash
cd Python-Port-Scanner
```

3. Run the scanner:

```bash
python scanner.py
```

## Usage

```text
Enter target host/IP: example.com
Start Port: 1
End Port: 1000
```

The scan results will be displayed on the terminal and saved to `scan_results.txt`.

## Project Structure

```text
Python-Port-Scanner/
│
├── scanner.py
├── scan_results.txt
└── README.md
```

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Always obtain permission before scanning systems or networks that you do not own.

## Author

Yogesh Sormare

Cybersecurity Enthusiast | MCA Student | Aspiring Security Professional
