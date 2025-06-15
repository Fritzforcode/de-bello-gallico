from vocabulary import vocabulary as raw_vocabulary

def parse_voc(voc):
    if isinstance(voc[-1], list):
        sub_vocabulary = [parse_voc(sub_voc) for sub_voc in voc[-1]]
        voc = voc[:-1]
    else:
        sub_vocabulary = []
    sub_voc_one = sub_vocabulary[0] if len(sub_vocabulary) >= 1 else None
    sub_voc_two = sub_vocabulary[1] if len(sub_vocabulary) >= 2 else None
    latin  = voc[0]
    if len(voc) == 2:
        grammar_info = None
        german       = voc[1]
        note         = None
    elif len(voc) == 3:
        grammar_info = voc[1]
        german       = voc[2]
        note         = None
    elif len(voc) == 4:
        grammar_info = voc[1]
        german       = voc[2]
        note         = voc[3]
    else: raise Exception()
    assert isinstance(latin       , str            ), f"invalid latin: {repr(latin)}"
    assert isinstance(grammar_info, str |type(None)), f"invalid grammar info: {repr(grammar_info)}"
    assert isinstance(german      , str            ), f"invalid german: {repr(german)}"
    assert isinstance(note        , str |type(None)), f"invalid note: {repr(note)}"
    assert isinstance(sub_voc_one , dict|type(None)), f"invalid sub voc one: {repr(sub_voc_one)}"
    assert isinstance(sub_voc_two , dict|type(None)), f"invalid sub voc two: {repr(sub_voc_two)}"
    parsed_voc = {
        "latin"       : latin,
        "grammar_info": grammar_info,
        "german"      : german,
    }
    if note        != None: parsed_voc["note"       ] = note
    if sub_voc_one != None: parsed_voc["sub_voc_one"] = sub_voc_one
    if sub_voc_two != None: parsed_voc["sub_voc_two"] = sub_voc_two
    for name, attr in [("latin", latin), ("grammar_info", grammar_info), ("german", german), ("note", note), ("sub_voc_one", sub_voc_one), ("sub_voc_two", sub_voc_two)]:
        if isinstance(attr, str) and ("\n" in attr):
            print("**", name, attr)
    return parsed_voc  

    
    

parsed_vocabulary = []
for i, voc in enumerate(raw_vocabulary):
    parsed_voc = parse_voc(voc)
    #print("-", voc)
    #print("-", parsed_voc)
    #if i % 3 == 3-1:
    #    print()
    #if parsed_voc["latin"].startswith("f"):
    parsed_vocabulary.append(parsed_voc)
    if parsed_voc["latin"] == "de":
        break
import json
#print(json.dumps(parsed_vocabulary))
print(len(parsed_vocabulary))
with open("vocabulary.json", "w") as file:
    json.dump(parsed_vocabulary, file)

