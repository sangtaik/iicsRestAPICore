import json

def jsonMerge(jsonA, jsonB):

    if jsonA is None:
        return jsonB
    elif jsonB is None:
        return jsonA

    jsonA.extend(jsonB)

    return jsonA