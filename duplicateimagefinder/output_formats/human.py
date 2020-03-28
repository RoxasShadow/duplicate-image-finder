from types import *
import sys
import os

import base


class HumanFormat(base.BaseFormatter):
    def output(self, data):
        assert type(data) is ListType, "data is not a list"

        if not len(data):
            print "No results."
            return

        # List the images that are similar to each other
        for similar in data:
            assert isinstance(similar, base.OutputRecord), "record is not instance of OutputRecord"

            image1_is_bigger = os.path.getsize(similar.image1) > os.path.getsize(similar.image2)

            sys.stdout.old_write("'%s' is %d%% similar to '%s' (the %s one is bigger)\n" % (
                os.path.basename(similar.image1), similar.similarity_pct, os.path.basename(similar.image2),
                "first" if image1_is_bigger else "second"
            ))

            os.remove(similar.image1) if image1_is_bigger else os.remove(similar.image2)

            sys.stdout.flush()
