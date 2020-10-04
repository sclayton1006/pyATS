#Python
import time
import emoji
from rich.console import Console
from rich.table import Table
from genie.testbed import load

#Define the test bed file and connect to the device defined.
testbed = load('yaml/testbed.yaml')
device = testbed.devices['LAB-1841-R1']
print("Connecting...")
device.connect(log_stdout=False)

#Build out the table using Rich.table
table = Table(title="Show IP Interface Brief")
table.add_column("Interface", style="red", no_wrap=True)
table.add_column("IP Address", style="white")
table.add_column("Int Status")
table.add_column("Line Protocol")

preoutput = device.parse("show ip interface brief")
console = Console()

for k, v in preoutput['interface'].items():

    """define the values to get. In this case I want the address, status and line
    protocols for each interface. The loop will continue until there are no
    more ports to check. """

    ip = v.get('ip_address')
    stat = v.get('status')
    proto = v.get('protocol')

    """This piece of the code will check whether the interface is in an up state.
    There are a number of different interface states, not just up and down. Other
    examples can include "Admin down" and "err-disable"."""

    #if the interface is up and the line protocol is up...
    if stat == "up" and proto == "up":
        #Then add a 'Thumbs Up' Emoji to both the "Int Status" and "Line Protocol"
        #columns of the table
        table.add_row(k, ip, emoji.emojize(':thumbs_up:'), emoji.emojize(':thumbs_up:'))
    #Else, if the interface state is up and the protocol is down...
    elif stat == "up" and proto == "down":
        #Then add a 'Thumbs Up' Emoji to the "Int STatus" column of the table only.
        #leave the "Line Protocol" column blank
        table.add_row(k, ip, emoji.emojize(':thumbs_up:', ""))
    #Else if the interface state is NOT up
    elif proto != "up":
        #Leave the table columns for "Int Status and "Line Procool" blank.
        table.add_row(k, ip, "", "")
        #End of if statement
#Finally, print the table and a caveat explaining the Emojis
console.print(table, justify="left")
print(f"\nAn Emoji 'Thumbs Up' {emoji.emojize(':thumbs_up:')} denotes an interface that is only in the 'up' state.\nInterface states like 'Admin down' or 'err-disabled' will show as blank. \nPlease check if you think the state should be up.\n\n")
