import json
import random

with open('data.json', 'r+') as json_file:
    data = json.load(json_file)
    print(data)

    if data['index'] + 1 == len(data['choosenerList']): # Need to shuffle the lists
        new_choosener_list = data['choosenerList'].copy()
        new_food_list = data['foodList'].copy()
        isNotShuffledCorrectly = True
        while isNotShuffledCorrectly:
            random.shuffle(new_choosener_list)
            random.shuffle(new_food_list)
            print(new_choosener_list, new_food_list)

            isNotShuffledCorrectly = data['choosenerList'][data['index']] == new_choosener_list[0] or data['foodList'][data['index']] == new_food_list[0]
        data['index'] = 0
        data['choosenerList'] = new_choosener_list
        data['foodList'] = new_food_list
    else: # Increment the index
        data['index'] = data['index'] + 1

    print(data)
    json_file.seek(0)
    json_file.write(json.dumps(data))
    json_file.truncate()

    with open('index.html', 'w') as html_file:
        html_file.write("""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <style>
            h1 {
                text-align: center;
            }
        </style>
        <title>What we doing tonight!?</title>
    </head>
    <body>
        <h1>""" + data['choosenerList'][data['index']] + """</h1>
        <h1>""" + data['foodList'][data['index']] + """</h1>
    </body>
</html>""")
