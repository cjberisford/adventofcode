
report = []
with open("input/input.txt") as f:
    for line in f:
        report.append(line.strip())

gamma_rate = []
epsilon_rate = []

def most_common(lst):
    return max(set(lst), key=lst.count)

for i in range(12):
    bits = [str(x)[i] for x in report]
    bit = most_common(bits)
    gamma_rate.append(bit)
    epsilon_rate.append(str(1-int(bit)))

gamma_to_binary = int(''.join(gamma_rate), 2)
epsilon_to_binary = int(''.join(epsilon_rate), 2)

answer = gamma_to_binary * epsilon_to_binary
print(answer)
