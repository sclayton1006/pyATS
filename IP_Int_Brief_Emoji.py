#Python
import time
import emoji
from rich.console import Console
from rich.table import Table
from rich.emoji import Emoji
from genie.testbed import load

testbed = load('yaml/testbed.yaml')
device = testbed.devices['LAB-1841-R1']
print(f"Loading {testbed} and attempting to access {device}...")
device.connect(log_stdout=False)

table = Table(title="Show IP Interface Brief")
table.add_column("Interface", style="red", no_wrap=True)
table.add_column("IP Address", style="white")
table.add_column("Int Status")

preoutput = device.parse("show ip interface brief")
console = Console()
#thumbs_up = console.print(":+1:")
#thumbs_down = console.print(":-1:")

for k, v in preoutput['interface'].items():
    ip = v.get('ip_address')
    stat = v.get('status')
    if stat == "up":
        table.add_row(k, ip, emoji.emojize(':thumbs_up:'))
    else:
        table.add_row(k, ip, "")
    #table.add_row(k, ip, stat)
console.print(table, justify="center")
print("End of script")
