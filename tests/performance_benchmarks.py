from context import hissdict
from hissdict import HissDict
from faker import Factory
from timing import timing
from time import sleep
from pprint import pprint

VALUE_SIZES = [100, 1000, 10000]#, 100000, 1000000, 10000000]


def create_test_data():
    fake = Factory.create()
    #generate some fake name values
    fake_names = list()
    for _ in range(100):
      fake_names.append(fake.name())

    return fake_names


@timing
def create_hissdict(input_data):
    hd = HissDict((key, value) for key, value in input_data)
    return hd

@timing
def create_dict(input_data):
    ex_dict = dict((key, value) for key, value in input_data)
    return ex_dict

@timing
def get_hissdict(hiss_dict):
    for key in hiss_dict.__iter__():
        val = hiss_dict.get(key)


def structure_timing(func_name, upper_bound, timed_result):
    times.append({
        "function": func_name,
        "upper_bound": upper_bound,
        "timed_result": timed_result
        })

        # "minimum_time": min(times),
        # "maximum_time": max(times),
        # "average_time": sum(times) / len(times)


fake_names = create_test_data()
global times
times = []
timing_results = []

for upper_bound in VALUE_SIZES:
    input_data = ((key, fake_names[key%100]) for key in range(upper_bound))

     #Todo: swap these functions in cleanly!
     #      randomize test runs
     #      cleaner recording of timing / repeated code

    #Dict
    for repeat in range(5):
        test_dict, func_name, timed_result = create_dict(input_data)
        structure_timing(func_name, upper_bound, timed_result)
        sleep(1)


    #Hissss

        test_hissdict, func_name, timed_result = create_hissdict(input_data)
        structure_timing(func_name, upper_bound, timed_result)
        sleep(1)

        _, func_name, timed_result = get_hissdict(test_hissdict)
        structure_timing(func_name, upper_bound, timed_result)
        sleep(1)




pprint(times)



#Get
