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
                'primitive_type': 'numeric'
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
    input_value = data["value"]
    output['value'] = "Error " + str(input_value)

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
        return {
            'statusCode': 200,
            'body': json.dumps(retobj)
        }
    elif (event["requestContext"]["resourcePath"] == "/process"):
        return {
            'statusCode': 200,
            'body': process_event(event)
        }
