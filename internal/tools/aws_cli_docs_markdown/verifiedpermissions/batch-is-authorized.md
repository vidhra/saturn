# batch-is-authorizedÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/batch-is-authorized.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/batch-is-authorized.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [verifiedpermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/verifiedpermissions/index.html#cli-aws-verifiedpermissions) ]

# batch-is-authorized

## Description

Makes a series of decisions about multiple authorization requests for one principal or resource. Each request contains the equivalent content of an `IsAuthorized` request: principal, action, resource, and context. Either the `principal` or the `resource` parameter must be identical across all requests. For example, Verified Permissions wonât evaluate a pair of requests where `bob` views `photo1` and `alice` views `photo2` . Authorization of `bob` to view `photo1` and `photo2` , or `bob` and `alice` to view `photo1` , are valid batches.

The request is evaluated against all policies in the specified policy store that match the entities that you declare. The result of the decisions is a series of `Allow` or `Deny` responses, along with the IDs of the policies that produced each decision.

The `entities` of a `BatchIsAuthorized` API request can contain up to 100 principals and up to 100 resources. The `requests` of a `BatchIsAuthorized` API request can contain up to 30 requests.

### Note

The `BatchIsAuthorized` operation doesnât have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission `verifiedpermissions:IsAuthorized` in their IAM policies.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/verifiedpermissions-2021-12-01/BatchIsAuthorized)

## Synopsis

```
batch-is-authorized
--policy-store-id <value>
[--entities <value>]
--requests <value>
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--policy-store-id` (string)

Specifies the ID of the policy store. Policies in this policy store will be used to make the authorization decisions for the input.

`--entities` (tagged union structure)

(Optional) Specifies the list of resources and principals and their associated attributes that Verified Permissions can examine when evaluating the policies. These additional entities and their attributes can be referenced and checked by conditional elements in the policies in the specified policy store.

### Note

You can include only principal and resource entities in this parameter; you canât include actions. You must specify actions in the schema.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `entityList`, `cedarJson`.

entityList -> (list)

An array of entities that are needed to successfully evaluate an authorization request. Each entity in this array must include an identifier for the entity, the attributes of the entity, and a list of any parent entities.

### Note

If you include multiple entities with the same `identifier` , only the last one is processed in the request.

(structure)

Contains information about an entity that can be referenced in a Cedar policy.

This data type is used as one of the fields in the [EntitiesDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntitiesDefinition.html) structure.

`{ "identifier": { "entityType": "Photo", "entityId": "VacationPhoto94.jpg" }, "attributes": {}, "parents": [ { "entityType": "Album", "entityId": "alice_folder" } ] }`

identifier -> (structure)

The identifier of the entity.

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

attributes -> (map)

A list of attributes for the entity.

key -> (string)

value -> (tagged union structure)

The value of an attribute.

Contains information about the runtime context for a request for which an authorization decision is made.

This data type is used as a member of the [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html) structure which is uses as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `boolean`, `entityIdentifier`, `long`, `string`, `set`, `record`, `ipaddr`, `decimal`.

boolean -> (boolean)

An attribute value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#boolean) type.

Example: `{"boolean": true}`

entityIdentifier -> (structure)

An attribute value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html) .

Example: `"entityIdentifier": { "entityId": "<id>", "entityType": "<entity type>"}`

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

long -> (long)

An attribute value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#long) type.

Example: `{"long": 0}`

string -> (string)

An attribute value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#string) type.

Example: `{"string": "abc"}`

set -> (list)

An attribute value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#set) type.

Example: `{"set": [ {} ] }`

(tagged union structure)

The value of an attribute.

Contains information about the runtime context for a request for which an authorization decision is made.

This data type is used as a member of the [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html) structure which is uses as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `boolean`, `entityIdentifier`, `long`, `string`, `set`, `record`, `ipaddr`, `decimal`.

boolean -> (boolean)

An attribute value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#boolean) type.

Example: `{"boolean": true}`

entityIdentifier -> (structure)

An attribute value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html) .

Example: `"entityIdentifier": { "entityId": "<id>", "entityType": "<entity type>"}`

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

long -> (long)

An attribute value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#long) type.

Example: `{"long": 0}`

string -> (string)

An attribute value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#string) type.

Example: `{"string": "abc"}`

set -> (list)

An attribute value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#set) type.

Example: `{"set": [ {} ] }`

( â¦ recursive â¦ )

record -> (map)

An attribute value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#record) type.

Example: `{"record": { "keyName": {} } }`

key -> (string)

( â¦ recursive â¦ )

ipaddr -> (string)

An attribute value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.

Example: `{"ip": "192.168.1.100"}`

decimal -> (string)

An attribute value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.

Example: `{"decimal": "1.1"}`

record -> (map)

An attribute value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#record) type.

Example: `{"record": { "keyName": {} } }`

key -> (string)

value -> (tagged union structure)

The value of an attribute.

Contains information about the runtime context for a request for which an authorization decision is made.

This data type is used as a member of the [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html) structure which is uses as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `boolean`, `entityIdentifier`, `long`, `string`, `set`, `record`, `ipaddr`, `decimal`.

boolean -> (boolean)

An attribute value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#boolean) type.

Example: `{"boolean": true}`

entityIdentifier -> (structure)

An attribute value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html) .

Example: `"entityIdentifier": { "entityId": "<id>", "entityType": "<entity type>"}`

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

long -> (long)

An attribute value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#long) type.

Example: `{"long": 0}`

string -> (string)

An attribute value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#string) type.

Example: `{"string": "abc"}`

set -> (list)

An attribute value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#set) type.

Example: `{"set": [ {} ] }`

( â¦ recursive â¦ )

record -> (map)

An attribute value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#record) type.

Example: `{"record": { "keyName": {} } }`

key -> (string)

( â¦ recursive â¦ )

ipaddr -> (string)

An attribute value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.

Example: `{"ip": "192.168.1.100"}`

decimal -> (string)

An attribute value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.

Example: `{"decimal": "1.1"}`

ipaddr -> (string)

An attribute value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.

Example: `{"ip": "192.168.1.100"}`

decimal -> (string)

An attribute value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.

Example: `{"decimal": "1.1"}`

parents -> (list)

The parent entities in the hierarchy that contains the entity. A principal or resource entity can be defined with at most 99 *transitive parents* per authorization request.

A transitive parent is an entity in the hierarchy of entities including all direct parents, and parents of parents. For example, a user can be a member of 91 groups if one of those groups is a member of eight groups, for a total of 100: one entity, 91 entity parents, and eight parents of parents.

(structure)

Contains the identifier of an entity, including its ID and type.

This data type is used as a request parameter for [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) operation, and as a response parameter for the [CreatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html) , [GetPolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_GetPolicy.html) , and [UpdatePolicy](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicy.html) operations.

Example: `{"entityId":"*string* ","entityType":"*string* "}`

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

cedarJson -> (string)

A Cedar JSON string representation of the entities needed to successfully evaluate an authorization request.

Example: `{"cedarJson": "[{\"uid\":{\"type\":\"Photo\",\"id\":\"VacationPhoto94.jpg\"},\"attrs\":{\"accessLevel\":\"public\"},\"parents\":[]}]"}`

JSON Syntax:

```
{
  "entityList": [
    {
      "identifier": {
        "entityType": "string",
        "entityId": "string"
      },
      "attributes": {"string": {
            "boolean": true|false,
            "entityIdentifier": {
              "entityType": "string",
              "entityId": "string"
            },
            "long": long,
            "string": "string",
            "set": [
              {
                "boolean": true|false,
                "entityIdentifier": {
                  "entityType": "string",
                  "entityId": "string"
                },
                "long": long,
                "string": "string",
                "set": [
                  { ... recursive ... }
                  ...
                ],
                "record": {"string": { ... recursive ... }
                  ...},
                "ipaddr": "string",
                "decimal": "string"
              }
              ...
            ],
            "record": {"string": {
                  "boolean": true|false,
                  "entityIdentifier": {
                    "entityType": "string",
                    "entityId": "string"
                  },
                  "long": long,
                  "string": "string",
                  "set": [
                    { ... recursive ... }
                    ...
                  ],
                  "record": {"string": { ... recursive ... }
                    ...},
                  "ipaddr": "string",
                  "decimal": "string"
                }
              ...},
            "ipaddr": "string",
            "decimal": "string"
          }
        ...},
      "parents": [
        {
          "entityType": "string",
          "entityId": "string"
        }
        ...
      ]
    }
    ...
  ],
  "cedarJson": "string"
}
```

`--requests` (list)

An array of up to 30 requests that you want Verified Permissions to evaluate.

(structure)

An authorization request that you include in a `BatchIsAuthorized` API request.

principal -> (structure)

Specifies the principal for which the authorization decision is to be made.

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

action -> (structure)

Specifies the requested action to be authorized. For example, `PhotoFlash::ReadPhoto` .

actionType -> (string)

The type of an action.

actionId -> (string)

The ID of an action.

resource -> (structure)

Specifies the resource that you want an authorization decision for. For example, `PhotoFlash::Photo` .

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

context -> (tagged union structure)

Specifies additional context that can be used to make more granular authorization decisions.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `contextMap`, `cedarJson`.

contextMap -> (map)

An list of attributes that are needed to successfully evaluate an authorization request. Each attribute in this array must include a map of a data type and its value.

Example: `"contextMap":{"<KeyName1>":{"boolean":true},"<KeyName2>":{"long":1234}}`

key -> (string)

value -> (tagged union structure)

The value of an attribute.

Contains information about the runtime context for a request for which an authorization decision is made.

This data type is used as a member of the [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html) structure which is uses as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `boolean`, `entityIdentifier`, `long`, `string`, `set`, `record`, `ipaddr`, `decimal`.

boolean -> (boolean)

An attribute value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#boolean) type.

Example: `{"boolean": true}`

entityIdentifier -> (structure)

An attribute value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html) .

Example: `"entityIdentifier": { "entityId": "<id>", "entityType": "<entity type>"}`

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

long -> (long)

An attribute value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#long) type.

Example: `{"long": 0}`

string -> (string)

An attribute value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#string) type.

Example: `{"string": "abc"}`

set -> (list)

An attribute value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#set) type.

Example: `{"set": [ {} ] }`

(tagged union structure)

The value of an attribute.

Contains information about the runtime context for a request for which an authorization decision is made.

This data type is used as a member of the [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html) structure which is uses as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `boolean`, `entityIdentifier`, `long`, `string`, `set`, `record`, `ipaddr`, `decimal`.

boolean -> (boolean)

An attribute value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#boolean) type.

Example: `{"boolean": true}`

entityIdentifier -> (structure)

An attribute value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html) .

Example: `"entityIdentifier": { "entityId": "<id>", "entityType": "<entity type>"}`

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

long -> (long)

An attribute value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#long) type.

Example: `{"long": 0}`

string -> (string)

An attribute value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#string) type.

Example: `{"string": "abc"}`

set -> (list)

An attribute value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#set) type.

Example: `{"set": [ {} ] }`

( â¦ recursive â¦ )

record -> (map)

An attribute value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#record) type.

Example: `{"record": { "keyName": {} } }`

key -> (string)

( â¦ recursive â¦ )

ipaddr -> (string)

An attribute value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.

Example: `{"ip": "192.168.1.100"}`

decimal -> (string)

An attribute value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.

Example: `{"decimal": "1.1"}`

record -> (map)

An attribute value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#record) type.

Example: `{"record": { "keyName": {} } }`

key -> (string)

value -> (tagged union structure)

The value of an attribute.

Contains information about the runtime context for a request for which an authorization decision is made.

This data type is used as a member of the [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html) structure which is uses as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `boolean`, `entityIdentifier`, `long`, `string`, `set`, `record`, `ipaddr`, `decimal`.

boolean -> (boolean)

An attribute value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#boolean) type.

Example: `{"boolean": true}`

entityIdentifier -> (structure)

An attribute value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html) .

Example: `"entityIdentifier": { "entityId": "<id>", "entityType": "<entity type>"}`

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

long -> (long)

An attribute value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#long) type.

Example: `{"long": 0}`

string -> (string)

An attribute value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#string) type.

Example: `{"string": "abc"}`

set -> (list)

An attribute value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#set) type.

Example: `{"set": [ {} ] }`

( â¦ recursive â¦ )

record -> (map)

An attribute value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#record) type.

Example: `{"record": { "keyName": {} } }`

key -> (string)

( â¦ recursive â¦ )

ipaddr -> (string)

An attribute value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.

Example: `{"ip": "192.168.1.100"}`

decimal -> (string)

An attribute value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.

Example: `{"decimal": "1.1"}`

ipaddr -> (string)

An attribute value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.

Example: `{"ip": "192.168.1.100"}`

decimal -> (string)

An attribute value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.

Example: `{"decimal": "1.1"}`

cedarJson -> (string)

A Cedar JSON string representation of the context needed to successfully evaluate an authorization request.

Example: `{"cedarJson":"{\"<KeyName1>\": true, \"<KeyName2>\": 1234}" }`

JSON Syntax:

```
[
  {
    "principal": {
      "entityType": "string",
      "entityId": "string"
    },
    "action": {
      "actionType": "string",
      "actionId": "string"
    },
    "resource": {
      "entityType": "string",
      "entityId": "string"
    },
    "context": {
      "contextMap": {"string": {
            "boolean": true|false,
            "entityIdentifier": {
              "entityType": "string",
              "entityId": "string"
            },
            "long": long,
            "string": "string",
            "set": [
              {
                "boolean": true|false,
                "entityIdentifier": {
                  "entityType": "string",
                  "entityId": "string"
                },
                "long": long,
                "string": "string",
                "set": [
                  { ... recursive ... }
                  ...
                ],
                "record": {"string": { ... recursive ... }
                  ...},
                "ipaddr": "string",
                "decimal": "string"
              }
              ...
            ],
            "record": {"string": {
                  "boolean": true|false,
                  "entityIdentifier": {
                    "entityType": "string",
                    "entityId": "string"
                  },
                  "long": long,
                  "string": "string",
                  "set": [
                    { ... recursive ... }
                    ...
                  ],
                  "record": {"string": { ... recursive ... }
                    ...},
                  "ipaddr": "string",
                  "decimal": "string"
                }
              ...},
            "ipaddr": "string",
            "decimal": "string"
          }
        ...},
      "cedarJson": "string"
    }
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Output

results -> (list)

A series of `Allow` or `Deny` decisions for each request, and the policies that produced them. These results are returned in the order they were requested.

(structure)

The decision, based on policy evaluation, from an individual authorization request in a `BatchIsAuthorized` API request.

request -> (structure)

The authorization request that initiated the decision.

principal -> (structure)

Specifies the principal for which the authorization decision is to be made.

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

action -> (structure)

Specifies the requested action to be authorized. For example, `PhotoFlash::ReadPhoto` .

actionType -> (string)

The type of an action.

actionId -> (string)

The ID of an action.

resource -> (structure)

Specifies the resource that you want an authorization decision for. For example, `PhotoFlash::Photo` .

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

context -> (tagged union structure)

Specifies additional context that can be used to make more granular authorization decisions.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `contextMap`, `cedarJson`.

contextMap -> (map)

An list of attributes that are needed to successfully evaluate an authorization request. Each attribute in this array must include a map of a data type and its value.

Example: `"contextMap":{"<KeyName1>":{"boolean":true},"<KeyName2>":{"long":1234}}`

key -> (string)

value -> (tagged union structure)

The value of an attribute.

Contains information about the runtime context for a request for which an authorization decision is made.

This data type is used as a member of the [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html) structure which is uses as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `boolean`, `entityIdentifier`, `long`, `string`, `set`, `record`, `ipaddr`, `decimal`.

boolean -> (boolean)

An attribute value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#boolean) type.

Example: `{"boolean": true}`

entityIdentifier -> (structure)

An attribute value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html) .

Example: `"entityIdentifier": { "entityId": "<id>", "entityType": "<entity type>"}`

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

long -> (long)

An attribute value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#long) type.

Example: `{"long": 0}`

string -> (string)

An attribute value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#string) type.

Example: `{"string": "abc"}`

set -> (list)

An attribute value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#set) type.

Example: `{"set": [ {} ] }`

(tagged union structure)

The value of an attribute.

Contains information about the runtime context for a request for which an authorization decision is made.

This data type is used as a member of the [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html) structure which is uses as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `boolean`, `entityIdentifier`, `long`, `string`, `set`, `record`, `ipaddr`, `decimal`.

boolean -> (boolean)

An attribute value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#boolean) type.

Example: `{"boolean": true}`

entityIdentifier -> (structure)

An attribute value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html) .

Example: `"entityIdentifier": { "entityId": "<id>", "entityType": "<entity type>"}`

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

long -> (long)

An attribute value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#long) type.

Example: `{"long": 0}`

string -> (string)

An attribute value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#string) type.

Example: `{"string": "abc"}`

set -> (list)

An attribute value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#set) type.

Example: `{"set": [ {} ] }`

( â¦ recursive â¦ )

record -> (map)

An attribute value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#record) type.

Example: `{"record": { "keyName": {} } }`

key -> (string)

( â¦ recursive â¦ )

ipaddr -> (string)

An attribute value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.

Example: `{"ip": "192.168.1.100"}`

decimal -> (string)

An attribute value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.

Example: `{"decimal": "1.1"}`

record -> (map)

An attribute value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#record) type.

Example: `{"record": { "keyName": {} } }`

key -> (string)

value -> (tagged union structure)

The value of an attribute.

Contains information about the runtime context for a request for which an authorization decision is made.

This data type is used as a member of the [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html) structure which is uses as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `boolean`, `entityIdentifier`, `long`, `string`, `set`, `record`, `ipaddr`, `decimal`.

boolean -> (boolean)

An attribute value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#boolean) type.

Example: `{"boolean": true}`

entityIdentifier -> (structure)

An attribute value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html) .

Example: `"entityIdentifier": { "entityId": "<id>", "entityType": "<entity type>"}`

entityType -> (string)

The type of an entity.

Example: `"entityType":"*typeName* "`

entityId -> (string)

The identifier of an entity.

`"entityId":"*identifier* "`

long -> (long)

An attribute value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#long) type.

Example: `{"long": 0}`

string -> (string)

An attribute value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#string) type.

Example: `{"string": "abc"}`

set -> (list)

An attribute value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#set) type.

Example: `{"set": [ {} ] }`

( â¦ recursive â¦ )

record -> (map)

An attribute value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#record) type.

Example: `{"record": { "keyName": {} } }`

key -> (string)

( â¦ recursive â¦ )

ipaddr -> (string)

An attribute value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.

Example: `{"ip": "192.168.1.100"}`

decimal -> (string)

An attribute value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.

Example: `{"decimal": "1.1"}`

ipaddr -> (string)

An attribute value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.

Example: `{"ip": "192.168.1.100"}`

decimal -> (string)

An attribute value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.

Example: `{"decimal": "1.1"}`

cedarJson -> (string)

A Cedar JSON string representation of the context needed to successfully evaluate an authorization request.

Example: `{"cedarJson":"{\"<KeyName1>\": true, \"<KeyName2>\": 1234}" }`

decision -> (string)

An authorization decision that indicates if the authorization request should be allowed or denied.

determiningPolicies -> (list)

The list of determining policies used to make the authorization decision. For example, if there are two matching policies, where one is a forbid and the other is a permit, then the forbid policy will be the determining policy. In the case of multiple matching permit policies then there would be multiple determining policies. In the case that no policies match, and hence the response is DENY, there would be no determining policies.

(structure)

Contains information about one of the policies that determined an authorization decision.

This data type is used as an element in a response parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

Example: `"determiningPolicies":[{"policyId":"SPEXAMPLEabcdefg111111"}]`

policyId -> (string)

The Id of a policy that determined to an authorization decision.

Example: `"policyId":"SPEXAMPLEabcdefg111111"`

errors -> (list)

Errors that occurred while making an authorization decision. For example, a policy might reference an entity or attribute that doesnât exist in the request.

(structure)

Contains a description of an evaluation error.

This data type is a response parameter of the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) , [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html) , and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

errorDescription -> (string)

The error description.