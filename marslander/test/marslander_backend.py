""" Mars lander backend function"""

import re

OUTPUT_FORMAT = re.compile('(?P<rotation>-?[0-9]{1,2}) (?P<power>[01234])')

def check_output(output):
    matching = OUTPUT_FORMAT.match(output)
    assert matching
    rotation = int(matching.group('rotation'))
    power = int(matching.group('power'))

    assert abs(rotation) <= 90
    assert power <= 4


