#!/usr/bin/env python3

import re


class Methods:

    def rearrage_name(self, name):
        result = re.search(r"^([\w .]*), ([\w .]*)$", name)
        return "{} {}".format(result[2], result[1])

