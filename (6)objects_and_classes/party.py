class Party:
    def __init__(self):
        self.going = []


party = Party()
line = input()

while line != 'End':
    party.going.append(line)
    line = input()

print(f'Going: {", ".join(party.going)}')
print(f'Total: {len(party.going)}')
