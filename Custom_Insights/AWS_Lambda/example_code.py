import json

BitDecoder_function = {
    'id' : "bitDecoder",
    'name' : "Bit Decoder",
    'description' : "Decodes an integer value",
    'inlets' :
    [
        {
            'name': 'input_signal',
            'description': 'Input value',
            'primitive_type': 'NUMERIC'
        }
    ],
    'outlets':
    [
        {
            'name': 'output_signal',
            'description': 'Error string',
            'primitive_type': 'string'
        }
    ]
}

Insight = {
    'functions': 
    [
        BitDecoder_function
    ]
}

# Takes an integer value as an input value inside the event
#   Outputs "Error <n>" with 'n' being the MSB of the provided integer
#           "No Error" if there are no '1's in the binary representation
#
# Examples:
# Input '0' -> Binary '0000' -> Output 'No Error'
# Input '1' -> Binary '0001' -> Output 'Error 1'
# Input '2' -> Binary '0010' -> Output 'Error 2'
# Input '3' -> Binary '0011' -> Output 'Error 2'
def process_event(event):
    # Create the output object
    body = event["body"]
    body_obj = json.loads(body)
    print(json.dumps(body_obj))
    data = body_obj["data"][0]
    output = {}
    output["origin"] = data["origin"]
    output["generated"] = data["generated"]
    output["ts"] = data["ts"]
    output["tags"] = data["tags"]

    # Translate the data here
    max_bit_position = -1
    input_value = int(data["value"])
    for i in range(31): # 32 bits in an integer in python
        if ((1<<i) & input_value != 0):
            max_bit_position = i + 1
    if (max_bit_position == -1):
        output['value'] = "No Error "
    else:
        output['value'] = "Error " + str(max_bit_position)

    print(str(input_value) + " - " + output["value"])
    return json.dumps([[output]])

def lambda_handler(event, context):
    if event["requestContext"]["resourcePath"] == "/info":
        info = {
            'name': "BitDecoder",
            'description': "This is an example custom insight using an AWS Lambda function",
            'group_id_required': False,
            'wants_lifecycle_events': False
        }
        return {
            'statusCode': 200,
            'body': json.dumps(info)
        }
    elif event["requestContext"]["resourcePath"] == "/insight/BitDecoder":
        return {
            'statusCode': 200,
            'body': json.dumps(BitDecoder_function)
        }
    elif event["requestContext"]["resourcePath"] == "/insights":
        retobj = {
            'total' : len(Insight["functions"]),
            'count' : len(Insight["functions"]),
            'insights': Insight["functions"]
        }
        print(json.dumps(retobj))
        return {
            'statusCode': 200,
            'body': json.dumps(retobj)
        }
    elif (event["requestContext"]["resourcePath"] == "/process"):
        return {
            'statusCode': 200,
            'body': process_event(event)
        }

