import logging
import os

logger = logging.getLogger(__name__)


class Splitlib:
    def run(self, edam, work_root):
        for f in edam["files"]:
            if not "logical_name" in f:
                f["logical_name"] = (
                    str(f["core"]).lstrip(":").replace(":", "_").replace(".", "_")
                )
        return edam
