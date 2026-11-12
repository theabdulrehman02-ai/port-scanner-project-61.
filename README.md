## Video Demonstration
https://drive.google.com/file/d/1_nWFTsup_u5lrJSY8U61WDQdI5eEuIXd/view?usp=sharing

# Port Scanner - Project #61

## Project Overview
This is a Python based Port Scanner that checks open ports on a target IP or website. It is useful for network security and ethical hacking.

## Features
- Scan any IP or website
- Scan custom port range
- Fast scanning using threading
- Save result in result.txt

## Technologies Used
- Python
- Socket Library
- Threading

## Installation
1. Install Python
2. Download port_scanner.py
3. Run: python port_scanner.py

## Usage
Enter target IP, starting port and ending port. Tool will show OPEN ports.

## Workflow
User input -> Resolve hostname -> Connect to each port -> Check result -> Display and save

## Testing
Tested on localhost (127.0.0.1). Successfully found open ports.

## Challenges
Slow scanning was challenge, solved using threading.

## Future Improvements
Add banner grabbing and GUI version.

## Conclusion
Project successfully scans ports and helps in understanding network security.

## References
- Python Socket Docs
- TryHackMe
