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
    #if parsed_voc["latin"].startswith("b"):
    #    break
    parsed_vocabulary.append(parsed_voc)
import json

voc_indecies = [info["latin"] for info in parsed_vocabulary]
print(voc_indecies)

pages = {
    4: ("a, ab", "atque, ac"),
    5: ("attingere", "concilium"),
    6: ("concurrere", "de"),
    7: ("debere", "evocare"),
    8: ("e, ex", "huc"),
    9: ("iam", "item"),
    10: ("iter", "munire"),
    11: ("munitio", "ostendere"),
    12: ("pabulum", "praesens"),
    13: ("praesidium", "quo"),
    14: ("quod", "spes"),
    15: ("statuere", "uti"),
    16: ("vadum", "vulnus"),
}

content = {
    "vocs": parsed_vocabulary,
    "pages": {page_idx: (voc_indecies.index(page[0]), voc_indecies.index(page[1])) for page_idx, page in pages.items()}
}
print(content)
with open("vocabulary.json", "w") as file:
    json.dump(content, file)

