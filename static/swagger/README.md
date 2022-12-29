---
title: Legal Entity Search v2.0.0
language_tabs:
  - python: Python
language_clients:
  - python: ""
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="legal-entity-search">Legal Entity Search v2.0.0</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="legal-entity-search-default">Default</h1>

## post__v2_search

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/v2/search', headers = headers)

print(r.json())

```

`POST /v2/search`

*This service allows searching a company in all internal systems by name, address, and other input fields.*

> Body parameter

```json
{
  "config": {
    "matching-method": "exact",
    "ignore": ""
  },
  "data": [
    {
      "entity_key": "",
      "entity_class": "",
      "legal_name": "Stellabella Toys*",
      "street_address": "1360 cambridge st",
      "city": "Cambridge",
      "state": "MA",
      "country": "US",
      "zip_code": "02139"
    },
    {
      "entity_key": "",
      "entity_class": "",
      "legal_name": "Stellabella Toys",
      "street_address": "1366 cambridge st",
      "city": "Cambridge",
      "state": "MA",
      "country": "US",
      "zip_code": "02139"
    }
  ]
}
```

<h3 id="post__v2_search-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|The company that we want to search.|
|» config|body|object|false|none|
|»» matching-method|body|string|false|Enter the matching method to use in the searching process. The allowed values are: exact, fuzzy|
|»» ignore|body|string|false|Enter a field that is going to be excluded from the search. Use this only in combination with the exact matching method.|
|» data|body|object|false|Data of the company to be search.|
|»» entity_key|body|string|false|Optional input if we are doing an internal search. This refers to where the internal entity record is coming from. Omit this field for external searching.|
|»» entity_class|body|string|false|Optional input if we are doing an internal search. This is the type of records (what database or entity type?) i.e. SFC, AR, Buyer, Seller. Omit this field for external searching.|
|»» legal_name|body|string|false|Name of the company.|
|»» street_address|body|string|false|Address of the company.|
|»» city|body|string|false|City of the company.|
|»» state|body|string|false|State of the company.|
|»» country|body|string|false|Country of the company.|
|»» zip_code|body|string|false|Zip code of the company address.|

> Example responses

> 200 Response

```json
{
  "ok": true,
  "message": "string",
  "data": [
    {
      "address_number": "1360",
      "address_number_ratio_score": 100,
      "city": "cambridge",
      "cleaned_entity_name": "stellabella toys",
      "country": "us",
      "entity_class": "",
      "entity_id": 0,
      "entity_key": "",
      "entity_name": "Stellabella Toys*",
      "full_address": "1360 cambridge st cambridge ma 02139 us",
      "is_exact_address_match": true,
      "is_exact_match": true,
      "is_exact_name_match": true,
      "legal_name": "Stellabella Toys*",
      "matched_address_number": "1360",
      "matched_city": "cambridge",
      "matched_cleaned_entity_name": "stellabella toys",
      "matched_country": "united states",
      "matched_entity_class": "ar_buyer",
      "matched_entity_id": 22204,
      "matched_entity_key": "99984",
      "matched_entity_name": "Stellabella Toys*",
      "matched_full_address": "1360 cambridge st cambridge ma 02139 united states",
      "matched_legal_name": "Stellabella Toys*",
      "matched_processed_name": "stellabella toys",
      "matched_state": "ma",
      "matched_street_address": "1360 cambridge st",
      "matched_street_address_split": "1360 cambridge st",
      "matched_street_name": "None",
      "matched_tagged_addresses": {
        "AddressNumber": "1360",
        "CountryName": "states",
        "PlaceName": "cambridge",
        "StateName": "ma",
        "StreetNamePostType": "st",
        "ZipCode": "02139"
      },
      "matched_zip_code": "02139",
      "matched_zip_code_abv": "02139",
      "name_partial_ratio_score": 100,
      "name_ratio_score": 100,
      "name_token_set_ratio_score": 100,
      "name_token_sort_ratio_score": 100,
      "processed_name": "stellabella toys",
      "state": "ma",
      "street_address": "1360 cambridge st",
      "street_address_split": "1360 cambridge st",
      "street_name": "None",
      "street_name_ratio_score": 100,
      "tagged_addresses": {
        "AddressNumber": "1360",
        "CountryName": "us",
        "PlaceName": "cambridge",
        "StateName": "ma",
        "StreetNamePostType": "st",
        "ZipCode": "02139"
      },
      "zip_code": "02139",
      "zip_code_abv": "02139",
      "zip_code_ratio_score": 100
    },
    {
      "address_number": "1360",
      "address_number_ratio_score": 100,
      "city": "cambridge",
      "cleaned_entity_name": "stellabella toys",
      "country": "us",
      "entity_class": "",
      "entity_id": 0,
      "entity_key": "",
      "entity_name": "Stellabella Toys*",
      "full_address": "1360 cambridge st cambridge ma 02139 us",
      "is_exact_address_match": true,
      "is_exact_match": true,
      "is_exact_name_match": true,
      "legal_name": "Stellabella Toys*",
      "matched_address_number": "1360",
      "matched_city": "cambridge",
      "matched_cleaned_entity_name": "stellabella toys",
      "matched_country": "united states",
      "matched_entity_class": "ar_buyer",
      "matched_entity_id": 22205,
      "matched_entity_key": "131228",
      "matched_entity_name": "Stellabella Toys",
      "matched_full_address": "1360 cambridge street cambridge ma 02139 united states",
      "matched_legal_name": "Stellabella Toys",
      "matched_processed_name": "stellabella toys",
      "matched_state": "ma",
      "matched_street_address": "1360 cambridge street",
      "matched_street_address_split": "1360 cambridge street",
      "matched_street_name": "None",
      "matched_tagged_addresses": {
        "AddressNumber": "1360",
        "CountryName": "states",
        "PlaceName": "cambridge",
        "StateName": "ma",
        "StreetNamePostType": "street",
        "ZipCode": "02139"
      },
      "matched_zip_code": "02139",
      "matched_zip_code_abv": "02139",
      "name_partial_ratio_score": 100,
      "name_ratio_score": 100,
      "name_token_set_ratio_score": 100,
      "name_token_sort_ratio_score": 100,
      "processed_name": "stellabella toys",
      "state": "ma",
      "street_address": "1360 cambridge st",
      "street_address_split": "1360 cambridge st",
      "street_name": "None",
      "street_name_ratio_score": 100,
      "tagged_addresses": {
        "AddressNumber": "1360",
        "CountryName": "us",
        "PlaceName": "cambridge",
        "StateName": "ma",
        "StreetNamePostType": "st",
        "ZipCode": "02139"
      },
      "zip_code": "02139",
      "zip_code_abv": "02139",
      "zip_code_ratio_score": 100
    }
  ]
}
```

<h3 id="post__v2_search-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Success|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Error|Inline|

<h3 id="post__v2_search-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» ok|boolean|false|none|Success confirmation|
|» message|string|false|none|Success confirmation|
|» data|object|false|none|Company data|
|»» address_number|string|false|none|none|
|»» address_number_ratio_score|integer|false|none|none|
|»» city|string|false|none|none|
|»» cleaned_entity_name|string|false|none|none|
|»» country|string|false|none|none|
|»» entity_class|string|false|none|none|
|»» entity_id|integer|false|none|none|
|»» entity_key|string|false|none|none|
|»» entity_name|string|false|none|none|
|»» full_address|string|false|none|none|
|»» is_exact_address_match|boolean|false|none|none|
|»» is_exact_match|boolean|false|none|none|
|»» is_exact_name_match|boolean|false|none|none|
|»» legal_name|string|false|none|none|
|»» matched_address_number|string|false|none|none|
|»» matched_city|string|false|none|none|
|»» matched_cleaned_entity_name|string|false|none|none|
|»» matched_country|string|false|none|none|
|»» matched_entity_class|string|false|none|none|
|»» matched_entity_id|string|false|none|none|
|»» matched_entity_key|string|false|none|none|
|»» matched_entity_name|string|false|none|none|
|»» matched_full_address|string|false|none|none|
|»» matched_legal_name|string|false|none|none|
|»» matched_processed_name|string|false|none|none|
|»» matched_state|string|false|none|none|
|»» matched_street_address|string|false|none|none|
|»» matched_street_address_split|string|false|none|none|
|»» matched_street_name|string|false|none|none|
|»» matched_tagged_addresses|object|false|none|none|
|»»» AddressNumber|string|false|none|none|
|»»» CountryName|string|false|none|none|
|»»» PlaceName|string|false|none|none|
|»»» StateName|string|false|none|none|
|»»» StreetNamePostType|string|false|none|none|
|»»» ZipCode|string|false|none|none|
|»» matched_zip_code|string|false|none|none|
|»» matched_zip_code_abv|string|false|none|none|
|»» name_partial_ratio_score|integer|false|none|none|
|»» name_ratio_score|integer|false|none|none|
|»» name_token_set_ratio_score|integer|false|none|none|
|»» name_token_sort_ratio_score|integer|false|none|none|
|»» processed_name|string|false|none|none|
|»» state|string|false|none|none|
|»» street_address|string|false|none|none|
|»» street_address_split|string|false|none|none|
|»» street_name|string|false|none|none|
|»» street_name_ratio_score|integer|false|none|none|
|»» tagged_addresses|object|false|none|none|
|»»» AddressNumber|string|false|none|none|
|»»» CountryName|string|false|none|none|
|»»» PlaceName|string|false|none|none|
|»»» StateName|string|false|none|none|
|»»» StreetNamePostType|string|false|none|none|
|»»» ZipCode|string|false|none|none|
|»» zip_code|string|false|none|none|
|»» zip_code_abv|string|false|none|none|
|»» zip_code_ratio_score|integer|false|none|none|

Status Code **404**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» body|string|false|none|Not found|

<aside class="success">
This operation does not require authentication
</aside>

