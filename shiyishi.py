from tuning import PARAMETERS

avai_commands = set()
for k in PARAMETERS.keys():
    avai_commands.add(k)
print(sorted(list(avai_commands)))
