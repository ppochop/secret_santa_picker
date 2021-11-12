import csv
from os import stat
from os.path import exists

REGISTER_PATH = 'register_file.csv'

def norun_on_empty(func):
    def wrapper(*args, **kwargs):
        if (not exists(REGISTER_PATH)) or stat(REGISTER_PATH).st_size == 0:
            print('No participants registered yet.')
            return
        return func(*args, **kwargs)
    return wrapper


def register_new(new_entries, method='a'):
    with open(REGISTER_PATH, method, newline='') as reg:
        writer = csv.writer(reg)
        writer.writerows(new_entries)


@norun_on_empty
def read(print=False):
    with open(REGISTER_PATH, 'r', newline='') as reg:
        reader = csv.reader(reg)
        if print:
            for entry in reader:
                print(', '.join(entry))
        else:
            return list(reader)

@norun_on_empty
def update(old, new, dlt=False):
    updated = []
    with open(REGISTER_PATH, 'r', newline='') as reg:
        matches_found = 0
        reader = csv.reader(reg)
        for entry in reader:
            skip = False
            for i in [0, 1]:
                if entry[i] == old:
                    matches_found += 1
                    entry[i] = new
                    if dlt:
                        skip = True
            if not skip:
                updated.append(entry)
        if matches_found == 0:
            print("No matches found for {}.".format(old))
            return

    register_new(updated, method='w')


def delete(delete_this):
    update(delete_this, 'x', dlt=True)


def get():
    with open(REGISTER_PATH, 'r') as reg:
        reader = csv.reader(reg, newline='')
        return list(reader)


def _parse_participants(entries):
    return map(lambda entry: entry.split(':'), entries)


def participant_list(args):
    if args.show:
        read(print=True)
    if args.delete:
        for reject in args.delete:
            delete(reject)
    if args.register:
        register_new(_parse_participants(args.register))
