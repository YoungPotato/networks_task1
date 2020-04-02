import subprocess
import re
from prettytable import PrettyTable


class Program:
    def get_statistics(self, dst):
        table = PrettyTable()
        table.field_names = ["№ по порядку", "IP", "AS"]
        traceroute = subprocess.Popen(["traceroute", dst],
                                      stdout=subprocess.PIPE)
        regex = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        i = 1
        for line in iter(traceroute.stdout.readline, ""):
            line = line.decode()
            if "* * *" in line:
                print(table)
                break
            else:
                ip = re.search(regex, line)[0]
                code_value = subprocess.Popen(
                    "whois -h whois.radb.net {} | grep '^origin'".format(ip),
                    shell=True, stdout=subprocess.PIPE)
                code = re.search('(\d+)', code_value.stdout.readline().decode())
                if code is None:
                    as_code = ""
                else:
                    as_code = code[0]
                table.add_row([i, ip, as_code])
                i += 1