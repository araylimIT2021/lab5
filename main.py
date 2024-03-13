from functools import reduce


def map_operation(line):
    phone_number_1, phone_number_2, call_duration, _, _ = line.split(" ")
    call_duration = int(call_duration)
    yield phone_number_1, (call_duration, 1)
    yield phone_number_2, (call_duration, 1)

def reduce_operation(mapped_data):
    reduced_data = dict()
    for phone_number, (call_duration, count) in mapped_data:
        if phone_number not in reduced_data:
            reduced_data[phone_number] = (call_duration, count)
        else:
            existing_call_duration, existing_count = reduced_data[phone_number]
            reduced_data[phone_number] = (existing_call_duration + call_duration, existing_count + count)
    return reduced_data

with open('lab5_data.txt', 'r') as file:
    data = file.readlines()
# 2 Compose a Map part code, which presents how long each phone number were talking in each call
mapped_data = map(map_operation, data)
mapped_data = map(lambda x: list(x), mapped_data)
data = []
for i in mapped_data:
    for j in i:
        data.append(j)
mapped_data = data

reduced_data = reduce_operation(mapped_data)
with open('output.txt', 'w') as file:
    for phone_number, (call_duration, count) in reduced_data.items():
        file.write(str(f'{phone_number} total call duration {call_duration} and count of calls {count} \n'))


# for obj in mapped_data:
# for item in obj:
# print(item)
