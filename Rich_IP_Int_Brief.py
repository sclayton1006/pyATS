#Python
import time

from rich.console import Console
from rich.table import Table

from genie.testbed import load

testbed = load('yaml/testbed.yaml')
device = testbed.devices['LAB-1841-R1']
print(f"Loading {testbed} and attempting to access {device}...")
device.connect(log_stdout=False)

table = Table(title="Show IP Interface Brief")
table.add_column("Interface", style="red", no_wrap=True)
table.add_column("IP Address", style="white")

preoutput = device.parse("show ip interface brief")

for k, v in preoutput['interface'].items():
    table.add_row(k, v.get('ip_address'))

console = Console()
console.print(table, justify="center")
