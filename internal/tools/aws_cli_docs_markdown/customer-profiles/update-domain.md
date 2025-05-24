# update-domainÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/update-domain.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/update-domain.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [customer-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/index.html#cli-aws-customer-profiles) ]

# update-domain

## Description

Updates the properties of a domain, including creating or selecting a dead letter queue or an encryption key.

After a domain is created, the name canât be changed.

Use this API or [CreateDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html) to enable [identity resolution](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html) : set `Matching` to true.

To prevent cross-service impersonation when you call this API, see [Cross-service confused deputy prevention](https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html) for sample policies that you should apply.

To add or remove tags on an existing Domain, see [TagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html) /[UntagResource](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/customer-profiles-2020-08-15/UpdateDomain)

## Synopsis

```
update-domain
--domain-name <value>
[--default-expiration-days <value>]
[--default-encryption-key <value>]
[--dead-letter-queue-url <value>]
[--matching <value>]
[--rule-based-matching <value>]
[--tags <value>]
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

`--domain-name` (string)

The unique name of the domain.

`--default-expiration-days` (integer)

The default number of days until the data within the domain expires.

`--default-encryption-key` (string)

The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage. If specified as an empty string, it will clear any existing value.

`--dead-letter-queue-url` (string)

The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. If specified as an empty string, it will clear any existing value. You must set up a policy on the DeadLetterQueue for the SendMessage operation to enable Amazon Connect Customer Profiles to send messages to the DeadLetterQueue.

`--matching` (structure)

The process of matching duplicate profiles. If `Matching` = `true` , Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains.

After the Identity Resolution Job completes, use the [GetMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html) API to return and review the results. Or, if you have configured `ExportingConfig` in the `MatchingRequest` , you can download the results from S3.

Enabled -> (boolean)

The flag that enables the matching process of duplicate profiles.

JobSchedule -> (structure)

The day and time when do you want to start the Identity Resolution Job every week.

DayOfTheWeek -> (string)

The day when the Identity Resolution Job should run every week.

Time -> (string)

The time when the Identity Resolution Job should run every week.

AutoMerging -> (structure)

Configuration information about the auto-merging process.

Enabled -> (boolean)

The flag that enables the auto-merging of duplicate profiles.

Consolidation -> (structure)

A list of matching attributes that represent matching criteria. If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.

MatchingAttributesList -> (list)

A list of matching criteria.

(list)

(string)

ConflictResolution -> (structure)

How the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same `FirstName` and `LastName` (and that is the matching criteria), which `EmailAddress` should be used?

ConflictResolvingModel -> (string)

How the auto-merging process should resolve conflicts between different profiles.

- `RECENCY` : Uses the data that was most recently updated.
- `SOURCE` : Uses the data from a specific source. For example, if a company has been aquired or two departments have merged, data from the specified source is used. If two duplicate profiles are from the same source, then `RECENCY` is used again.

SourceName -> (string)

The `ObjectType` name that is used to resolve profile merging conflicts when choosing `SOURCE` as the `ConflictResolvingModel` .

MinAllowedConfidenceScoreForMerging -> (double)

A number between 0 and 1 that represents the minimum confidence score required for profiles within a matching group to be merged during the auto-merge process. A higher score means higher similarity required to merge profiles.

ExportingConfig -> (structure)

Configuration information for exporting Identity Resolution results, for example, to an S3 bucket.

S3Exporting -> (structure)

The S3 location where Identity Resolution Jobs write result files.

S3BucketName -> (string)

The name of the S3 bucket where Identity Resolution Jobs write result files.

S3KeyName -> (string)

The S3 key name of the location where Identity Resolution Jobs write result files.

JSON Syntax:

```
{
  "Enabled": true|false,
  "JobSchedule": {
    "DayOfTheWeek": "SUNDAY"|"MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"SATURDAY",
    "Time": "string"
  },
  "AutoMerging": {
    "Enabled": true|false,
    "Consolidation": {
      "MatchingAttributesList": [
        ["string", ...]
        ...
      ]
    },
    "ConflictResolution": {
      "ConflictResolvingModel": "RECENCY"|"SOURCE",
      "SourceName": "string"
    },
    "MinAllowedConfidenceScoreForMerging": double
  },
  "ExportingConfig": {
    "S3Exporting": {
      "S3BucketName": "string",
      "S3KeyName": "string"
    }
  }
}
```

`--rule-based-matching` (structure)

The process of matching duplicate profiles using the rule-Based matching. If `RuleBasedMatching` = true, Amazon Connect Customer Profiles will start to match and merge your profiles according to your configuration in the `RuleBasedMatchingRequest` . You can use the `ListRuleBasedMatches` and `GetSimilarProfiles` API to return and review the results. Also, if you have configured `ExportingConfig` in the `RuleBasedMatchingRequest` , you can download the results from S3.

Enabled -> (boolean)

The flag that enables the rule-based matching process of duplicate profiles.

MatchingRules -> (list)

Configures how the rule-based matching process should match profiles. You can have up to 15 `MatchingRule` in the `MatchingRules` .

(structure)

Specifies how does the rule-based matching process should match profiles. You can choose from the following attributes to build the matching Rule:

- AccountNumber
- Address.Address
- Address.City
- Address.Country
- Address.County
- Address.PostalCode
- Address.State
- Address.Province
- BirthDate
- BusinessName
- EmailAddress
- FirstName
- Gender
- LastName
- MiddleName
- PhoneNumber
- Any customized profile attributes that start with the `Attributes`

Rule -> (list)

A single rule level of the `MatchRules` . Configures how the rule-based matching process should match profiles.

(string)

MaxAllowedRuleLevelForMerging -> (integer)

[MatchingRule](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_MatchingRule.html)

MaxAllowedRuleLevelForMatching -> (integer)

Indicates the maximum allowed rule level.

AttributeTypesSelector -> (structure)

Configures information about the `AttributeTypesSelector` where the rule-based identity resolution uses to match profiles.

AttributeMatchingModel -> (string)

Configures the `AttributeMatchingModel` , you can either choose `ONE_TO_ONE` or `MANY_TO_MANY` .

Address -> (list)

The `Address` type. You can choose from `Address` , `BusinessAddress` , `MaillingAddress` , and `ShippingAddress` .

You only can use the Address type in the `MatchingRule` . For example, if you want to match profile based on `BusinessAddress.City` or `MaillingAddress.City` , you need to choose the `BusinessAddress` and the `MaillingAddress` to represent the Address type and specify the `Address.City` on the matching rule.

(string)

PhoneNumber -> (list)

The `PhoneNumber` type. You can choose from `PhoneNumber` , `HomePhoneNumber` , and `MobilePhoneNumber` .

You only can use the `PhoneNumber` type in the `MatchingRule` . For example, if you want to match a profile based on `Phone` or `HomePhone` , you need to choose the `Phone` and the `HomePhone` to represent the `PhoneNumber` type and only specify the `PhoneNumber` on the matching rule.

(string)

EmailAddress -> (list)

The `Email` type. You can choose from `EmailAddress` , `BusinessEmailAddress` and `PersonalEmailAddress` .

You only can use the `EmailAddress` type in the `MatchingRule` . For example, if you want to match profile based on `PersonalEmailAddress` or `BusinessEmailAddress` , you need to choose the `PersonalEmailAddress` and the `BusinessEmailAddress` to represent the `EmailAddress` type and only specify the `EmailAddress` on the matching rule.

(string)

ConflictResolution -> (structure)

How the auto-merging process should resolve conflicts between different profiles.

ConflictResolvingModel -> (string)

How the auto-merging process should resolve conflicts between different profiles.

- `RECENCY` : Uses the data that was most recently updated.
- `SOURCE` : Uses the data from a specific source. For example, if a company has been aquired or two departments have merged, data from the specified source is used. If two duplicate profiles are from the same source, then `RECENCY` is used again.

SourceName -> (string)

The `ObjectType` name that is used to resolve profile merging conflicts when choosing `SOURCE` as the `ConflictResolvingModel` .

ExportingConfig -> (structure)

Configuration information about the S3 bucket where Identity Resolution Jobs writes result files.

### Note

You need to give Customer Profiles service principal write permission to your S3 bucket. Otherwise, youâll get an exception in the API response. For an example policy, see [Amazon Connect Customer Profiles cross-service confused deputy prevention](https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html#customer-profiles-cross-service) .

S3Exporting -> (structure)

The S3 location where Identity Resolution Jobs write result files.

S3BucketName -> (string)

The name of the S3 bucket where Identity Resolution Jobs write result files.

S3KeyName -> (string)

The S3 key name of the location where Identity Resolution Jobs write result files.

JSON Syntax:

```
{
  "Enabled": true|false,
  "MatchingRules": [
    {
      "Rule": ["string", ...]
    }
    ...
  ],
  "MaxAllowedRuleLevelForMerging": integer,
  "MaxAllowedRuleLevelForMatching": integer,
  "AttributeTypesSelector": {
    "AttributeMatchingModel": "ONE_TO_ONE"|"MANY_TO_MANY",
    "Address": ["string", ...],
    "PhoneNumber": ["string", ...],
    "EmailAddress": ["string", ...]
  },
  "ConflictResolution": {
    "ConflictResolvingModel": "RECENCY"|"SOURCE",
    "SourceName": "string"
  },
  "ExportingConfig": {
    "S3Exporting": {
      "S3BucketName": "string",
      "S3KeyName": "string"
    }
  }
}
```

`--tags` (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

DomainName -> (string)

The unique name of the domain.

DefaultExpirationDays -> (integer)

The default number of days until the data within the domain expires.

DefaultEncryptionKey -> (string)

The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage.

DeadLetterQueueUrl -> (string)

The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications.

Matching -> (structure)

The process of matching duplicate profiles. If `Matching` = `true` , Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains.

After the Identity Resolution Job completes, use the [GetMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html) API to return and review the results. Or, if you have configured `ExportingConfig` in the `MatchingRequest` , you can download the results from S3.

Enabled -> (boolean)

The flag that enables the matching process of duplicate profiles.

JobSchedule -> (structure)

The day and time when do you want to start the Identity Resolution Job every week.

DayOfTheWeek -> (string)

The day when the Identity Resolution Job should run every week.

Time -> (string)

The time when the Identity Resolution Job should run every week.

AutoMerging -> (structure)

Configuration information about the auto-merging process.

Enabled -> (boolean)

The flag that enables the auto-merging of duplicate profiles.

Consolidation -> (structure)

A list of matching attributes that represent matching criteria. If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.

MatchingAttributesList -> (list)

A list of matching criteria.

(list)

(string)

ConflictResolution -> (structure)

How the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same `FirstName` and `LastName` (and that is the matching criteria), which `EmailAddress` should be used?

ConflictResolvingModel -> (string)

How the auto-merging process should resolve conflicts between different profiles.

- `RECENCY` : Uses the data that was most recently updated.
- `SOURCE` : Uses the data from a specific source. For example, if a company has been aquired or two departments have merged, data from the specified source is used. If two duplicate profiles are from the same source, then `RECENCY` is used again.

SourceName -> (string)

The `ObjectType` name that is used to resolve profile merging conflicts when choosing `SOURCE` as the `ConflictResolvingModel` .

MinAllowedConfidenceScoreForMerging -> (double)

A number between 0 and 1 that represents the minimum confidence score required for profiles within a matching group to be merged during the auto-merge process. A higher score means higher similarity required to merge profiles.

ExportingConfig -> (structure)

Configuration information for exporting Identity Resolution results, for example, to an S3 bucket.

S3Exporting -> (structure)

The S3 location where Identity Resolution Jobs write result files.

S3BucketName -> (string)

The name of the S3 bucket where Identity Resolution Jobs write result files.

S3KeyName -> (string)

The S3 key name of the location where Identity Resolution Jobs write result files.

RuleBasedMatching -> (structure)

The process of matching duplicate profiles using the rule-Based matching. If `RuleBasedMatching` = true, Amazon Connect Customer Profiles will start to match and merge your profiles according to your configuration in the `RuleBasedMatchingRequest` . You can use the `ListRuleBasedMatches` and `GetSimilarProfiles` API to return and review the results. Also, if you have configured `ExportingConfig` in the `RuleBasedMatchingRequest` , you can download the results from S3.

Enabled -> (boolean)

The flag that enables the rule-based matching process of duplicate profiles.

MatchingRules -> (list)

Configures how the rule-based matching process should match profiles. You can have up to 15 `MatchingRule` in the `MatchingRules` .

(structure)

Specifies how does the rule-based matching process should match profiles. You can choose from the following attributes to build the matching Rule:

- AccountNumber
- Address.Address
- Address.City
- Address.Country
- Address.County
- Address.PostalCode
- Address.State
- Address.Province
- BirthDate
- BusinessName
- EmailAddress
- FirstName
- Gender
- LastName
- MiddleName
- PhoneNumber
- Any customized profile attributes that start with the `Attributes`

Rule -> (list)

A single rule level of the `MatchRules` . Configures how the rule-based matching process should match profiles.

(string)

Status -> (string)

PENDING

- The first status after configuration a rule-based matching rule. If it is an existing domain, the rule-based Identity Resolution waits one hour before creating the matching rule. If it is a new domain, the system will skip the `PENDING` stage.

IN_PROGRESS

- The system is creating the rule-based matching rule. Under this status, the system is evaluating the existing data and you can no longer change the Rule-based matching configuration.

ACTIVE

- The rule is ready to use. You can change the rule a day after the status is in `ACTIVE` .

MaxAllowedRuleLevelForMerging -> (integer)

[MatchingRule](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_MatchingRule.html)

MaxAllowedRuleLevelForMatching -> (integer)

Indicates the maximum allowed rule level.

AttributeTypesSelector -> (structure)

Configures information about the `AttributeTypesSelector` where the rule-based identity resolution uses to match profiles.

AttributeMatchingModel -> (string)

Configures the `AttributeMatchingModel` , you can either choose `ONE_TO_ONE` or `MANY_TO_MANY` .

Address -> (list)

The `Address` type. You can choose from `Address` , `BusinessAddress` , `MaillingAddress` , and `ShippingAddress` .

You only can use the Address type in the `MatchingRule` . For example, if you want to match profile based on `BusinessAddress.City` or `MaillingAddress.City` , you need to choose the `BusinessAddress` and the `MaillingAddress` to represent the Address type and specify the `Address.City` on the matching rule.

(string)

PhoneNumber -> (list)

The `PhoneNumber` type. You can choose from `PhoneNumber` , `HomePhoneNumber` , and `MobilePhoneNumber` .

You only can use the `PhoneNumber` type in the `MatchingRule` . For example, if you want to match a profile based on `Phone` or `HomePhone` , you need to choose the `Phone` and the `HomePhone` to represent the `PhoneNumber` type and only specify the `PhoneNumber` on the matching rule.

(string)

EmailAddress -> (list)

The `Email` type. You can choose from `EmailAddress` , `BusinessEmailAddress` and `PersonalEmailAddress` .

You only can use the `EmailAddress` type in the `MatchingRule` . For example, if you want to match profile based on `PersonalEmailAddress` or `BusinessEmailAddress` , you need to choose the `PersonalEmailAddress` and the `BusinessEmailAddress` to represent the `EmailAddress` type and only specify the `EmailAddress` on the matching rule.

(string)

ConflictResolution -> (structure)

How the auto-merging process should resolve conflicts between different profiles.

ConflictResolvingModel -> (string)

How the auto-merging process should resolve conflicts between different profiles.

- `RECENCY` : Uses the data that was most recently updated.
- `SOURCE` : Uses the data from a specific source. For example, if a company has been aquired or two departments have merged, data from the specified source is used. If two duplicate profiles are from the same source, then `RECENCY` is used again.

SourceName -> (string)

The `ObjectType` name that is used to resolve profile merging conflicts when choosing `SOURCE` as the `ConflictResolvingModel` .

ExportingConfig -> (structure)

Configuration information about the S3 bucket where Identity Resolution Jobs writes result files.

### Note

You need to give Customer Profiles service principal write permission to your S3 bucket. Otherwise, youâll get an exception in the API response. For an example policy, see [Amazon Connect Customer Profiles cross-service confused deputy prevention](https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html#customer-profiles-cross-service) .

S3Exporting -> (structure)

The S3 location where Identity Resolution Jobs write result files.

S3BucketName -> (string)

The name of the S3 bucket where Identity Resolution Jobs write result files.

S3KeyName -> (string)

The S3 key name of the location where Identity Resolution Jobs write result files.

CreatedAt -> (timestamp)

The timestamp of when the domain was created.

LastUpdatedAt -> (timestamp)

The timestamp of when the domain was most recently edited.

Tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)