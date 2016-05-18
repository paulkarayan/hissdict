from context import hissdict
from hissdict import HissDict
from faker import Factory
from timing import timing
from time import sleep
from pprint import pprint
import matplotlib.pyplot as plt
import csv

VALUE_SIZES = [100, 1000, 10000, 100000, 1000000, 10000000]
CSV_FILENAME = "performance_hiss_dict_mini.csv"
HEADERS = ["function", "upper_bound", 'maximum_time', 'minimum_time', 'average_time']


INT_CSV_FILENAME = "performance_hiss_dict_int.csv"
INT_HEADERS = ["function", "upper_bound", 'timed_result']

def main():

    fake_names = create_test_data()
    global times
    times = []

    for upper_bound in VALUE_SIZES:
        input_data = ((key, fake_names[key%100]) for key in range(upper_bound))

         #Todo: swap these functions in cleanly!
         #      randomize test runs
         #      cleaner recording of timing / repeated code
         #      write unit tests for the timing aggregator and others
         #      write itermediate data to file, then process it. decouples the two processes...
         #      move CSV to a utils file
         #     figure out how to clean setup (somehow advantageous to second type)

        #Dict
        for repeat in range(5):
            test_dict, func_name, timed_result = create_dict(input_data)
            structure_timing(func_name, upper_bound, timed_result)
            sleep(1)

            _, func_name, timed_result = get_dict(test_dict)
            structure_timing(func_name, upper_bound, timed_result)
            sleep(1)

            _, func_name, timed_result = iter_dict(test_dict)
            structure_timing(func_name, upper_bound, timed_result)
            sleep(1)

            _, func_name, timed_result = del_dict(test_dict)
            structure_timing(func_name, upper_bound, timed_result)
            sleep(1)

    times = []
    for upper_bound in VALUE_SIZES:
        input_data = ((key, fake_names[key%100]) for key in range(upper_bound))

        for repeat in range(5):
        #Hissss

            test_hissdict, func_name, timed_result = create_hissdict(input_data)
            structure_timing(func_name, upper_bound, timed_result)
            sleep(1)

            _, func_name, timed_result = get_hissdict(test_hissdict)
            structure_timing(func_name, upper_bound, timed_result)
            sleep(1)

            _, func_name, timed_result = iter_hissdict(test_hissdict)
            structure_timing(func_name, upper_bound, timed_result)
            sleep(1)

            _, func_name, timed_result = del_hissdict(test_hissdict)
            structure_timing(func_name, upper_bound, timed_result)
            sleep(1)

    pprint(times)
    timing_results = aggregate_timing(times)
    pprint(timing_results)

    #write dict to CSV
    write_to_csv(CSV_FILENAME, timing_results, HEADERS)


def write_to_csv(csv_filename, dataset, fieldnames=None):
    with open(csv_filename, 'a') as fptr:
        if fieldnames:
            writer = csv.DictWriter(fptr, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dataset)
        else:
            writer = csv.writer(fptr)
            for row in dataset:
                print(row)
                writer.writerow([row])

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
def get_hissdict(hiss_dict):
    for key in hiss_dict.__iter__():
        val = hiss_dict.get(key)

@timing
def del_hissdict(hiss_dict):
    #Prepared list avoids this error: RuntimeError: dictionary changed size during iteration
    keys = [key for key in hiss_dict.__iter__()]
    for key in keys:
        del hiss_dict[key]

@timing
def iter_hissdict(hiss_dict):
    for key in hiss_dict.__iter__():
        pass

@timing
def create_dict(input_data):
    ex_dict = dict((key, value) for key, value in input_data)
    return ex_dict

@timing
def get_dict(test_dict):
    for key in test_dict.__iter__():
        val = test_dict.get(key)

@timing
def del_dict(test_dict):
    #Prepared list avoids this error: RuntimeError: dictionary changed size during iteration
    keys = [key for key in test_dict.__iter__()]
    for key in keys:
        del test_dict[key]

@timing
def iter_dict(test_dict):
    for key in test_dict.__iter__():
        pass

def structure_timing(func_name, upper_bound, timed_result):
    times.append({
        "function": func_name,
        "upper_bound": upper_bound,
        "timed_result": timed_result
        })

def aggregate_timing(times):
    timing_results = []
    test_types = list(set(
                    tuple((item["function"], item["upper_bound"]) for item in times)
                ))
    print test_types

    for test in test_types:
        func_name, upper_bound = test
        trial_times = [item["timed_result"] for item in times if item["function"] == func_name and item["upper_bound"] == upper_bound]

        print trial_times, "<---"

        timing_results.append({
            "function": func_name,
            "upper_bound": upper_bound,
            "minimum_time": min(trial_times),
            "maximum_time": max(trial_times),
            "average_time": sum(trial_times) / len(trial_times)
            })

    return timing_results

if __name__ == main():
    main()
