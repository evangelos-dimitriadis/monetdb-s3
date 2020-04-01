def s3_loader(vars, line_buffer):

    from smart_open import open
    import json

    json_acceptable_string = vars.replace("'", '"')
    dictionary = json.loads(json_acceptable_string)
    keys = list(dictionary.keys())

    columns_dict = {}
    for i in range(1, len(keys)):
        columns_dict[keys[i]] = []

    num_lines = 0
    for line in open(keys[0]):
        row = line.rstrip('\n').split(",")
        num_lines += 1
        for i in range(1, len(keys)):
            if dictionary[keys[i]] == "INTEGER":
                columns_dict[keys[i]].append(int(row[i - 1]))
            elif dictionary[keys[i]] == "FLOAT":
                columns_dict[keys[i]].append(float(row[i - 1]))
            elif dictionary[keys[i]] == "STRING":
                columns_dict[keys[i]].append(float(row[i - 1]))

        if num_lines >= line_buffer:
            print(columns_dict)
            columns_dict = {}
            for i in range(1, len(keys)):
                columns_dict[keys[i]] = []
            num_lines = 0

    print(columns_dict)


s3_loader('{"/home/dameko/Documents/monetdb-s3/example2.csv": "STRING", "data": "INTEGER"}', 10000)
