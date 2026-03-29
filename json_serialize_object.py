
from pydantic_class_example import SubSection
import sys

def serialize(obj):
    return subsection.model_dump_json()

def deserialize(json_str, class_name):
    cls = getattr(sys.modules[__name__], class_name)
    return cls.model_validate_json(json_str)

if __name__ == "__main__":
    subsection = SubSection(header="topic1", contentLines=["line1", "line2"])
    json = serialize(subsection)
    print(deserialize(json, "SubSection"))
