# add-policy-grantÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/add-policy-grant.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/add-policy-grant.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datazone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/index.html#cli-aws-datazone) ]

# add-policy-grant

## Description

Adds a policy grant (an authorization policy) to a specified entity, including domain units, environment blueprint configurations, or environment profiles.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/AddPolicyGrant)

## Synopsis

```
add-policy-grant
[--client-token <value>]
--detail <value>
--domain-identifier <value>
--entity-identifier <value>
--entity-type <value>
--policy-type <value>
--principal <value>
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

`--client-token` (string)

A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.

`--detail` (tagged union structure)

The details of the policy grant.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `addToProjectMemberPool`, `createAssetType`, `createDomainUnit`, `createEnvironment`, `createEnvironmentFromBlueprint`, `createEnvironmentProfile`, `createFormType`, `createGlossary`, `createProject`, `createProjectFromProjectProfile`, `delegateCreateEnvironmentProfile`, `overrideDomainUnitOwners`, `overrideProjectOwners`, `useAssetType`.

addToProjectMemberPool -> (structure)

Specifies that the policy grant is to be added to the members of the project.

includeChildDomainUnits -> (boolean)

Specifies whether the policy grant is applied to child domain units.

createAssetType -> (structure)

Specifies that this is a create asset type policy.

includeChildDomainUnits -> (boolean)

Specifies whether the policy grant is applied to child domain units.

createDomainUnit -> (structure)

Specifies that this is a create domain unit policy.

includeChildDomainUnits -> (boolean)

Specifies whether the policy grant is applied to child domain units.

createEnvironment -> (structure)

Specifies that this is a create environment policy.

createEnvironmentFromBlueprint -> (structure)

The details of the policy of creating an environment.

createEnvironmentProfile -> (structure)

Specifies that this is a create environment profile policy.

domainUnitId -> (string)

The ID of the domain unit.

createFormType -> (structure)

Specifies that this is a create form type policy.

includeChildDomainUnits -> (boolean)

Specifies whether the policy grant is applied to child domain units.

createGlossary -> (structure)

Specifies that this is a create glossary policy.

includeChildDomainUnits -> (boolean)

Specifies whether the policy grant is applied to child domain units.

createProject -> (structure)

Specifies that this is a create project policy.

includeChildDomainUnits -> (boolean)

Specifies whether the policy grant is applied to child domain units.

createProjectFromProjectProfile -> (structure)

Specifies whether to create a project from project profile.

includeChildDomainUnits -> (boolean)

Specifies whether to include child domain units when creating a project from project profile policy grant details

projectProfiles -> (list)

Specifies project profiles when creating a project from project profile policy grant details

(string)

delegateCreateEnvironmentProfile -> (structure)

Specifies that this is the delegation of the create environment profile policy.

overrideDomainUnitOwners -> (structure)

Specifies whether to override domain unit owners.

includeChildDomainUnits -> (boolean)

Specifies whether the policy is inherited by child domain units.

overrideProjectOwners -> (structure)

Specifies whether to override project owners.

includeChildDomainUnits -> (boolean)

Specifies whether the policy is inherited by child domain units.

useAssetType -> (structure)

Specifies the domain unit(s) whose projects can use this asset type while creating asset or asset revisions.

domainUnitId -> (string)

The ID of the domain unit.

Shorthand Syntax:

```
addToProjectMemberPool={includeChildDomainUnits=boolean},createAssetType={includeChildDomainUnits=boolean},createDomainUnit={includeChildDomainUnits=boolean},createEnvironment={},createEnvironmentFromBlueprint={},createEnvironmentProfile={domainUnitId=string},createFormType={includeChildDomainUnits=boolean},createGlossary={includeChildDomainUnits=boolean},createProject={includeChildDomainUnits=boolean},createProjectFromProjectProfile={includeChildDomainUnits=boolean,projectProfiles=[string,string]},delegateCreateEnvironmentProfile={},overrideDomainUnitOwners={includeChildDomainUnits=boolean},overrideProjectOwners={includeChildDomainUnits=boolean},useAssetType={domainUnitId=string}
```

JSON Syntax:

```
{
  "addToProjectMemberPool": {
    "includeChildDomainUnits": true|false
  },
  "createAssetType": {
    "includeChildDomainUnits": true|false
  },
  "createDomainUnit": {
    "includeChildDomainUnits": true|false
  },
  "createEnvironment": {

  },
  "createEnvironmentFromBlueprint": {

  },
  "createEnvironmentProfile": {
    "domainUnitId": "string"
  },
  "createFormType": {
    "includeChildDomainUnits": true|false
  },
  "createGlossary": {
    "includeChildDomainUnits": true|false
  },
  "createProject": {
    "includeChildDomainUnits": true|false
  },
  "createProjectFromProjectProfile": {
    "includeChildDomainUnits": true|false,
    "projectProfiles": ["string", ...]
  },
  "delegateCreateEnvironmentProfile": {

  },
  "overrideDomainUnitOwners": {
    "includeChildDomainUnits": true|false
  },
  "overrideProjectOwners": {
    "includeChildDomainUnits": true|false
  },
  "useAssetType": {
    "domainUnitId": "string"
  }
}
```

`--domain-identifier` (string)

The ID of the domain where you want to add a policy grant.

`--entity-identifier` (string)

The ID of the entity (resource) to which you want to add a policy grant.

`--entity-type` (string)

The type of entity (resource) to which the grant is added.

Possible values:

- `DOMAIN_UNIT`
- `ENVIRONMENT_BLUEPRINT_CONFIGURATION`
- `ENVIRONMENT_PROFILE`
- `ASSET_TYPE`

`--policy-type` (string)

The type of policy that you want to grant.

Possible values:

- `CREATE_DOMAIN_UNIT`
- `OVERRIDE_DOMAIN_UNIT_OWNERS`
- `ADD_TO_PROJECT_MEMBER_POOL`
- `OVERRIDE_PROJECT_OWNERS`
- `CREATE_GLOSSARY`
- `CREATE_FORM_TYPE`
- `CREATE_ASSET_TYPE`
- `CREATE_PROJECT`
- `CREATE_ENVIRONMENT_PROFILE`
- `DELEGATE_CREATE_ENVIRONMENT_PROFILE`
- `CREATE_ENVIRONMENT`
- `CREATE_ENVIRONMENT_FROM_BLUEPRINT`
- `CREATE_PROJECT_FROM_PROJECT_PROFILE`
- `USE_ASSET_TYPE`

`--principal` (tagged union structure)

The principal to whom the permissions are granted.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `domainUnit`, `group`, `project`, `user`.

domainUnit -> (structure)

The domain unit of the policy grant principal.

domainUnitDesignation -> (string)

Specifes the designation of the domain unit users.

domainUnitGrantFilter -> (tagged union structure)

The grant filter for the domain unit.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `allDomainUnitsGrantFilter`.

allDomainUnitsGrantFilter -> (structure)

Specifies a grant filter containing all domain units.

domainUnitIdentifier -> (string)

The ID of the domain unit.

group -> (tagged union structure)

The group of the policy grant principal.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `groupIdentifier`.

groupIdentifier -> (string)

The ID Of the group of the group principal.

project -> (structure)

The project of the policy grant principal.

projectDesignation -> (string)

The project designation of the project policy grant principal.

projectGrantFilter -> (tagged union structure)

The project grant filter of the project policy grant principal.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `domainUnitFilter`.

domainUnitFilter -> (structure)

The domain unit filter of the project grant filter.

domainUnit -> (string)

The domain unit ID to use in the filter.

includeChildDomainUnits -> (boolean)

Specifies whether to include child domain units.

projectIdentifier -> (string)

The project ID of the project policy grant principal.

user -> (tagged union structure)

The user of the policy grant principal.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `allUsersGrantFilter`, `userIdentifier`.

allUsersGrantFilter -> (structure)

The all users grant filter of the user policy grant principal.

userIdentifier -> (string)

The user ID of the user policy grant principal.

JSON Syntax:

```
{
  "domainUnit": {
    "domainUnitDesignation": "OWNER",
    "domainUnitGrantFilter": {
      "allDomainUnitsGrantFilter": {

      }
    },
    "domainUnitIdentifier": "string"
  },
  "group": {
    "groupIdentifier": "string"
  },
  "project": {
    "projectDesignation": "OWNER"|"CONTRIBUTOR"|"PROJECT_CATALOG_STEWARD",
    "projectGrantFilter": {
      "domainUnitFilter": {
        "domainUnit": "string",
        "includeChildDomainUnits": true|false
      }
    },
    "projectIdentifier": "string"
  },
  "user": {
    "allUsersGrantFilter": {

    },
    "userIdentifier": "string"
  }
}
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

None