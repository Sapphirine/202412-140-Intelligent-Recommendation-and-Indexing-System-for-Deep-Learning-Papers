request = {'resource': '/paper/nearbyPaper', 
           'path': '/paper/nearbyPaper',
        'httpMethod': 'POST',
         'headers': None, 
         'multiValueHeaders': None, 
         'queryStringParameters': None, 
         'multiValueQueryStringParameters': None, 
         'pathParameters': None, 
         'stageVariables': None, 
         'requestContext': {'resourceId': 'jz5upo', 'resourcePath': '/paper/nearbyPaper', 'httpMethod': 'POST', 'extendedRequestId': 'Ic3QiGDHoAMFyzQ=', 'requestTime': '22/Jul/2023:05:41:23 +0000', 'path': '/paper/nearbyPaper', 'accountId': '081094903724', 'protocol': 'HTTP/1.1', 'stage': 'test-invoke-stage', 'domainPrefix': 'testPrefix', 'requestTimeEpoch': 1690004483143, 'requestId': '5e4c4e47-40e5-4fc8-804d-8464af922eb2', 'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      'apiKey': 'test-invoke-api-key', 'principalOrgId': None, 'cognitoAuthenticationType': None, 'userArn': 'arn:aws:sts::081094903724:assumed-role/voclabs/user2643260=t0929940@u.nus.edu', 'apiKeyId': 'test-invoke-api-key-id', 'userAgent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0', 'accountId': '081094903724', 'caller': 'AROARFYNCA6WLPPZQLZVX:user2643260=t0929940@u.nus.edu', 'sourceIp': 'test-invoke-source-ip', 'accessKey': 'ASIARFYNCA6WFPNH7R7E', 'cognitoAuthenticationProvider': None, 'user': 'AROARFYNCA6WLPPZQLZVX:user2643260=t0929940@u.nus.edu'}, 'domainName': 'testPrefix.testDomainName', 'apiId': '3fvb4d3nc5'}, 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        'body': '{\n    query: ["1311.2524"]\n}', 'isBase64Encoded': False}
import json
print(request['body'].replace('\n', '').replace('\'', '\"'))