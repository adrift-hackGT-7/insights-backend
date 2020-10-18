import requests
from typing import Optional, Dict, Any

# We want a header like 'Authorization': 'Basic {base64({username}:{password})}'
USERNAME = 'c96e4d9e-5930-4eff-8586-0d2d2925a0d3'
PASSWORD = 'T2ru%w!0!kJ&jQGh'

headers = {
    'content-type': 'application/json',
    'nep-organization': '747eb48be123491387ccea5d921ab6c8',
    'nep-enterprise-unit': '747eb48be123491387ccea5d921ab6c8',  # for put_pricecode
    'nep-correlation-id': 'sdfjisdofjfisdjodsof',
    'nep-site-id': '452753b037dc4f32bf25c4232c2f3fbd',
    'nep-shared-key': '4ec364c1a645473eb68eff4f290f0d27',
    'nep-secret-key': '31868425672543c18ee5018752fd3451',
}

id = '66979a6495414081ae5930389b1c60ff'
url = f'https://gateway-staging.ncrcloud.com/order/3/orders/1/{id}'
# request = requests.get(url, headers=headers, auth=(USERNAME, PASSWORD))
# print(request.json())

DEFAULT_PUT_ITEM_DATA = """{
                                "version": 111,
                               "packageIdentifiers": [
                                   {
                                       "type": "sampleaaaaaaaaaaaaaa",
                                       "value": "5043"
                                   }
                               ],
                               "longDescription": {
                                   "values": [
                                       {
                                           "locale": "en-us",
                                           "value": "String long description in American English"
                                       },
                                       {
                                           "locale": "fr-ca",
                                           "value": "String long description in American English"
                                       },
                                       {
                                           "locale": "en-br",
                                           "value": "String long description in American English"
                                       }
                                   ]
                               },
                               "shortDescription": {
                                   "values": [
                                       {
                                           "locale": "fr-ca",
                                           "value": "Short descritpion of type string in Canadian FrenchsShort desSho"
                                       },
                                       {
                                           "locale": "en-us",
                                           "value": "Short descritpion of type string in Canadian FrenchsShort desSho"
                                       }
                                   ]
                               },
                               "departmentId": "Short descritpion of type string in Canadian FrenchsShort desShoShortShort descritpiondescritpiondes",
                               "merchandiseCategory": {
                                   "nodeId": "ShortStringStringStringStringStringStringStringStringStringStringStringStringStringStringStringStringStringStringStringS"
                               },
                               "status": "INACTIVE",
                               "familyCode": " String",
                               "manufacturerCode": "manufacturer T",
                               "nonMerchandise": "false",
                               "dynamicAttributes": [
                                   {

                                       "type": "ab1",
                                       "attributes": [
                                           {
                                               "localizedValue": {
                                                   "values": [
                                                       {
                                                           "locale": "en-US",
                                                           "value": "Attribute Value"
                                                       }
                                                   ]
                                               },
                                               "key": "Dynamic1",
                                               "value": " Dynamic Attribute value"
                                           }
                                       ]
                                   }
                               ]
                           }"""


def put_item(item_code: str = 'itemCodeTest', data=DEFAULT_PUT_ITEM_DATA):
    """
    https://developer.ncrcloud.com/portals/dev-portal/api-explorer/details/8849/documentation?proxy=bsp-items-catalog-v2&path=put_items_itemCode 
    """
    request = requests.put(f'https://gateway-staging.ncrcloud.com/catalog/items/{item_code}',
                           headers=headers, auth=(
                               USERNAME, PASSWORD), data=data
                           )
    print(request)


def put_pricecode(item_code: str = 'itemCodeTest', price_code: str = '234343', data: str = '{"version":88,"price":17.5,"currency":"US Dollar","effectiveDate":"2020-04-18T00:13:16.594Z","endDate":"2021-04-03T11:06:48.463Z","status":"INACTIVE","basePrice":false,"linkGroupId":{"linkGroupCode":"29837289"},"itemPriceType":"SELF_SERVICE_CASH","tareWeightUom":"NOT_KNOWN","tareWeight":1.5,"precision":2,"includesContainer":true,"quantityPricedItem":true,"dynamicAttributes":[{"type":"String","attributes":[]}]}'):
    """
    https://developer.ncrcloud.com/portals/dev-portal/api-explorer/details/8849/documentation?proxy=bsp-items-catalog-v2&path=put_item-prices_itemCode_priceCode
    """
    request = requests.put(f'https://gateway-staging.ncrcloud.com/catalog/item-prices/{item_code}/{price_code}',
                           headers=headers, auth=(USERNAME, PASSWORD), data=data)
    if request.status_code == 204:
        print(request)
        return request
    else:
        print(request.json())
        return request.json()


def get_items(params: Optional[Dict[str, Any]] = None):
    """
    https://developer.ncrcloud.com/portals/dev-portal/api-explorer/details/8849/documentation?proxy=bsp-items-catalog-v2&path=get_items
    """
    request = requests.get(f'https://gateway-staging.ncrcloud.com/catalog/items',
                           headers=headers, auth=(USERNAME, PASSWORD), params=params)
    res = request.json()
    print(res)
    return res


def put_groups(data: str = '{"groups":[{"version":112,"tag":"food","status":"INACTIVE","title":{"values":[{"locale":"en-US","value":"sample text"}]},"groupId":{"groupCode":"7389289"}}]}'):
    """
    If we get an error like follows, we should increment the `version`. {'details': ['groups', '/747eb48be123491387ccea5d921ab6c8/!7389289', 'identifier', 'Object version should be greater than current version.', 'INVALID_OBJECT_VERSION'], 'errorType': 'com.ncr.nep.common.exception.InvalidResourceStateException', 'message': "The state of the groups with the identifier '/747eb48be123491387ccea5d921ab6c8/!7389289' is invalid for the requested operation. Object version should be greater than current version.", 'statusCode': 409}

    https://developer.ncrcloud.com/portals/dev-portal/api-explorer/details/8849/documentation?proxy=bsp-items-catalog-v2&path=put_groups
    """
    request = requests.put(f'https://gateway-staging.ncrcloud.com/catalog/groups',
                           headers=headers, auth=(USERNAME, PASSWORD), data=data)
    print(request.json())
    return request


def get_category_nodes():
    request = requests.get(f'https://gateway-staging.ncrcloud.com/catalog/category-nodes',
                           headers=headers, auth=(USERNAME, PASSWORD))
    print(request.json())
    return request


def put_category_nodes():
    """
    This error means that the parentNode that you want doesn't exist: {'details': ['NodeId', '1-846-188-450', 'identifier', 'Invalid node hierarchy detected in the request.', 'INVALID_NODE_HIERARCHY'], 'errorType': 'com.ncr.nep.common.exception.InvalidResourceStateException', 'message': "The state of the NodeId with the identifier '1-846-188-450' is invalid for the requested operation. Invalid node hierarchy detected in the request.", 'statusCode': 409}

    https://developer.ncrcloud.com/portals/dev-portal/api-explorer/details/8849/documentation?proxy=bsp-items-catalog-v2&path=put_item-prices_itemCode_priceCode
    """
    request = requests.put(f'https://gateway-staging.ncrcloud.com/catalog/category-nodes',
                           headers=headers, auth=(USERNAME, PASSWORD), data='{"nodes":[{"version":6,"nodeCode":"3278392","tag":"clothes","departmentNode":false,"departmentSale":false,"status":"INACTIVE","title":{"values":[{"locale":"en-US","value":"sample text"}]},"nodeId":{"nodeId":"1-846-188-450"},"parentId":{"nodeId":"1-846-188-450"}}]}')
    print(request.json())
    return request


put_category_nodes()


"""
const calculateSignature = function() {
    const date = new Date();
    postman.setEnvironmentVariable('date', date.toGMTString());
    const key = uniqueKey(date);
    const sc = signableContent();
    const hmac = CryptoJS.HmacSHA512(sc, key);
    return CryptoJS.enc.Base64.stringify(hmac);
}
"""

"""
const axios = require('axios')

function btoa(str) {
    return Buffer.from(str, 'binary').toString('base64')
}

axios.get('https://gateway-staging.ncrcloud.com/transaction-document/v2/transaction-documents/find', {
    headers: {
        'Authorization': `Basic ${btoa('michaelchen:T2ru%w!0!kJ&jQGh')}`
    }
})
.then(res => console.log(res))
.catch(err => console.log(err.response.data))
"""
