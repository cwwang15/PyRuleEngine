import argparse
import json
import sys
from collections import defaultdict


def read_log(log_file: str):
    d = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    with open(log_file, 'r') as fp:
        for line in fp:
            line = line.strip('\r\n')
            key, pos, char = line.split('\t')
            d[key][pos][char] += 1
    res = json.dumps(d)
    return res


def wrapper():
    cli = argparse.ArgumentParser("")
    cli.add_argument('-l', '--log', dest='log', required=True, help='log file generated by PyRuleEngineDelete.py')
    cli.add_argument('-s', '--save', dest='save', help='save result')
    args = cli.parse_args()
    log_file, save_file = args.log, args.save
    if save_file is not None:
        f_out = open(save_file, 'w')
    else:
        f_out = sys.stdout
    res = read_log(log_file)
    f_out.write(res)
    f_out.flush()
    f_out.close()
    pass


if __name__ == '__main__':
    wrapper()
    pass
