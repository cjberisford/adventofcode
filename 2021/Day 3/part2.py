report = []
with open("input/input.txt") as f:
    for line in f:
        report.append(line.strip())

oxygen_generator_rating = []
co2_scrubber_rating = []

def most_common_v2(lst, compliment):
    zeros = lst.count('0')
    ones = lst.count('1')

    if compliment:
        if zeros <= ones:
            return 0
        else:
            return 1
    else:
        return int(ones >= zeros)


def filter_list(list, compliment):
    print("")
    filtered_list = list
    for i in range(12):
        # ith character in output
        bits = [str(x)[i] for x in filtered_list]
        # list of ith characters in input
        bit = most_common_v2(bits, compliment)
        # dominant bit in input
        filtered_list = [x for x in filtered_list if x[i] == str(bit)]
        # new list created from instances with dominant bit in position
        
        if len(filtered_list) == 1:
            break

    return filtered_list

oxygen_generator_rating = int(''.join(filter_list(report, 0)), 2)
c02_scrubber_rating = int(''.join(filter_list(report, 1)), 2)
print(oxygen_generator_rating)
print(c02_scrubber_rating)


print(oxygen_generator_rating * c02_scrubber_rating)

