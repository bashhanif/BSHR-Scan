








______  _____ _   _ ______       _____ _____   ___   _   _ 
| ___ \/  ___| | | || ___ \     /  ___/  __ \ / _ \ | \ | |
| |_/ /\ `--.| |_| || |_/ /_____\ `--.| /  \// /_\ \|  \| |
| ___ \ `--. \  _  ||    /______|`--. \ |    |  _  || . ` |
| |_/ //\__/ / | | || |\ \      /\__/ / \__/\| | | || |\  |
\____/ \____/\_| |_/\_| \_|     \____/ \____/\_| |_/\_| \_/

Welcome to BSHR-SCAN, 

A simple Port scanning tool made with the socket Python library. 
This tool is currently only available for Windows.
BSHR-SCAN is fairly new and has basic features as of now, features include 

Single port scanning: Scan a specific port on a given IP Address 
Range port scanning: Scan a range of ports on a given IP Address


Download and Installaition
1. Download the Executable:
  Go to the Releases page on our GitHub repository.
  Download the BSHR-SCAN.exe file

2. Locate the file:
  the file will be saved in your default downloads directory

Usage 

To use BSHR-SCAN, you need to run it from the command line with the appropriate arguments:
NOTE: BSHR-SCAN will only work if the command line is in the correct directory, make sure you are in the correct folder!

  1. Open the command prompt
  2. Navigate to the folder in which BSHR-SCAN is located

     To use BSHR-SCAN, run it from the command line with the appropriate arguments:

     Single port scan e.g.

     BSHR-SCAN -p 135 190.000.00.0

     This is an example of a single port scan, -p specifies we are scanning a single port, 135 is our port and we end with our IP Address


     Range port scan e.g.

     BSHR-SCAN -r 100-200 190.000.00.0

     This is an example of a range port scan, -r specifies that we are scanning a range of ports, 100-200 are our ports to scan and we end with our IP Address(for ranges please remember to add a - in between port numbers).

     Always include BSHR-SCAN before commands!


  

Disclaimer 

BSHR-SCAN is intended solely for educational purposes and should be used responsibly. Unauthorized use of this tool to scan networks or systems without permission may be illegal and is against the ethical guidelines of responsible computing. Use this tool only on systems and networks for which you have explicit authorization.

The developers of BSHR-SCAN are not liable for any damage or legal consequences resulting from the misuse of this tool. Always obtain proper consent before performing any network scanning activities.









     
     
