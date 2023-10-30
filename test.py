import json

result = [[['clamav', 'comodo.py', ' OK']]]
result = result[0][0]
result = {
    "filename": result[1],
    "status": result[2]
}
json_out = json.dumps(result)

print(json_out)