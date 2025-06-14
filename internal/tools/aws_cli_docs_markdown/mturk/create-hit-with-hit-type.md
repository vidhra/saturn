# create-hit-with-hit-typeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/create-hit-with-hit-type.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/create-hit-with-hit-type.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mturk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/index.html#cli-aws-mturk) ]

# create-hit-with-hit-type

## Description

The `CreateHITWithHITType` operation creates a new Human Intelligence Task (HIT) using an existing HITTypeID generated by the `CreateHITType` operation.

This is an alternative way to create HITs from the `CreateHIT` operation. This is the recommended best practice for Requesters who are creating large numbers of HITs.

CreateHITWithHITType also supports several ways to provide question data: by providing a value for the `Question` parameter that fully specifies the contents of the HIT, or by providing a `HitLayoutId` and associated `HitLayoutParameters` .

### Note

If a HIT is created with 10 or more maximum assignments, there is an additional fee. For more information, see [Amazon Mechanical Turk Pricing](https://requester.mturk.com/pricing) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/CreateHITWithHITType)

## Synopsis

```
create-hit-with-hit-type
--hit-type-id <value>
[--max-assignments <value>]
--lifetime-in-seconds <value>
[--question <value>]
[--requester-annotation <value>]
[--unique-request-token <value>]
[--assignment-review-policy <value>]
[--hit-review-policy <value>]
[--hit-layout-id <value>]
[--hit-layout-parameters <value>]
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

`--hit-type-id` (string)

The HIT type ID you want to create this HIT with.

`--max-assignments` (integer)

The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

`--lifetime-in-seconds` (long)

An amount of time, in seconds, after which the HIT is no longer available for users to accept. After the lifetime of the HIT elapses, the HIT no longer appears in HIT searches, even if not all of the assignments for the HIT have been accepted.

`--question` (string)

The data the person completing the HIT uses to produce the results.

Constraints: Must be a QuestionForm data structure, an ExternalQuestion data structure, or an HTMLQuestion data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace.

Either a Question parameter or a HITLayoutId parameter must be provided.

`--requester-annotation` (string)

An arbitrary data field. The RequesterAnnotation parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, this parameter could be an identifier internal to the Requesterâs application that corresponds with the HIT.

The RequesterAnnotation parameter for a HIT is only visible to the Requester who created the HIT. It is not shown to the Worker, or any other Requester.

The RequesterAnnotation parameter may be different for each HIT you submit. It does not affect how your HITs are grouped.

`--unique-request-token` (string)

A unique identifier for this request which allows you to retry the call on error without creating duplicate HITs. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the HIT already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return a AWS.MechanicalTurk.HitAlreadyExists error with a message containing the HITId.

### Note

Note: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same UniqueRequestToken made after the 24 hour limit could create duplicate HITs.

`--assignment-review-policy` (structure)

The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for Mechanical Turk to take various actions based on the policy.

PolicyName -> (string)

Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

Parameters -> (list)

Name of the parameter from the Review policy.

(structure)

Name of the parameter from the Review policy.

Key -> (string)

Name of the parameter from the list of Review Polices.

Values -> (list)

The list of values of the Parameter

(string)

MapEntries -> (list)

List of ParameterMapEntry objects.

(structure)

This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

Key -> (string)

The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

Values -> (list)

The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.

(string)

JSON Syntax:

```
{
  "PolicyName": "string",
  "Parameters": [
    {
      "Key": "string",
      "Values": ["string", ...],
      "MapEntries": [
        {
          "Key": "string",
          "Values": ["string", ...]
        }
        ...
      ]
    }
    ...
  ]
}
```

`--hit-review-policy` (structure)

The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take various actions based on the policy.

PolicyName -> (string)

Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01

Parameters -> (list)

Name of the parameter from the Review policy.

(structure)

Name of the parameter from the Review policy.

Key -> (string)

Name of the parameter from the list of Review Polices.

Values -> (list)

The list of values of the Parameter

(string)

MapEntries -> (list)

List of ParameterMapEntry objects.

(structure)

This data structure is the data type for the AnswerKey parameter of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

Key -> (string)

The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy.

Values -> (list)

The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly.

(string)

JSON Syntax:

```
{
  "PolicyName": "string",
  "Parameters": [
    {
      "Key": "string",
      "Values": ["string", ...],
      "MapEntries": [
        {
          "Key": "string",
          "Values": ["string", ...]
        }
        ...
      ]
    }
    ...
  ]
}
```

`--hit-layout-id` (string)

The HITLayoutId allows you to use a pre-existing HIT design with placeholder values and create an additional HIT by providing those values as HITLayoutParameters.

Constraints: Either a Question parameter or a HITLayoutId parameter must be provided.

`--hit-layout-parameters` (list)

If the HITLayoutId is provided, any placeholder values must be filled in with values using the HITLayoutParameter structure. For more information, see HITLayout.

(structure)

The HITLayoutParameter data structure defines parameter values used with a HITLayout. A HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human Intelligence Task (HIT) question data for CreateHIT.

Name -> (string)

The name of the parameter in the HITLayout.

Value -> (string)

The value substituted for the parameter referenced in the HITLayout.

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
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

HIT -> (structure)

Contains the newly created HIT data. For a description of the HIT data structure as it appears in responses, see the HIT Data Structure documentation.

HITId -> (string)

A unique identifier for the HIT.

HITTypeId -> (string)

The ID of the HIT type of this HIT

HITGroupId -> (string)

The ID of the HIT Group of this HIT.

HITLayoutId -> (string)

The ID of the HIT Layout of this HIT.

CreationTime -> (timestamp)

The date and time the HIT was created.

Title -> (string)

The title of the HIT.

Description -> (string)

A general description of the HIT.

Question -> (string)

The data the Worker completing the HIT uses produce the results. This is either either a QuestionForm, HTMLQuestion or an ExternalQuestion data structure.

Keywords -> (string)

One or more words or phrases that describe the HIT, separated by commas. Search terms similar to the keywords of a HIT are more likely to have the HIT in the search results.

HITStatus -> (string)

The status of the HIT and its assignments. Valid Values are Assignable | Unassignable | Reviewable | Reviewing | Disposed.

MaxAssignments -> (integer)

The number of times the HIT can be accepted and completed before the HIT becomes unavailable.

Reward -> (string)

A string representing a currency amount.

AutoApprovalDelayInSeconds -> (long)

The amount of time, in seconds, after the Worker submits an assignment for the HIT that the results are automatically approved by Amazon Mechanical Turk. This is the amount of time the Requester has to reject an assignment submitted by a Worker before the assignment is auto-approved and the Worker is paid.

Expiration -> (timestamp)

The date and time the HIT expires.

AssignmentDurationInSeconds -> (long)

The length of time, in seconds, that a Worker has to complete the HIT after accepting it.

RequesterAnnotation -> (string)

An arbitrary data field the Requester who created the HIT can use. This field is visible only to the creator of the HIT.

QualificationRequirements -> (list)

Conditions that a Workerâs Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the `ActionsGuarded` field on each `QualificationRequirement` structure.

(structure)

The QualificationRequirement data structure describes a Qualification that a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification in order to preview the HIT, or see the HIT in search results.

QualificationTypeId -> (string)

The ID of the Qualification type for the requirement.

Comparator -> (string)

The kind of comparison to make against a Qualificationâs value. You can compare a Qualificationâs value to an IntegerValue to see if it is LessThan, LessThanOrEqualTo, GreaterThan, GreaterThanOrEqualTo, EqualTo, or NotEqualTo the IntegerValue. You can compare it to a LocaleValue to see if it is EqualTo, or NotEqualTo the LocaleValue. You can check to see if the value is In or NotIn a set of IntegerValue or LocaleValue values. Lastly, a Qualification requirement can also test if a Qualification Exists or DoesNotExist in the userâs profile, regardless of its value.

IntegerValues -> (list)

The integer value to compare against the Qualificationâs value. IntegerValue must not be present if Comparator is Exists or DoesNotExist. IntegerValue can only be used if the Qualification type has an integer value; it cannot be used with the Worker_Locale QualificationType ID. When performing a set comparison by using the In or the NotIn comparator, you can use up to 15 IntegerValue elements in a QualificationRequirement data structure.

(integer)

LocaleValues -> (list)

The locale value to compare against the Qualificationâs value. The local value must be a valid ISO 3166 country code or supports ISO 3166-2 subdivisions. LocaleValue can only be used with a Worker_Locale QualificationType ID. LocaleValue can only be used with the EqualTo, NotEqualTo, In, and NotIn comparators. You must only use a single LocaleValue element when using the EqualTo or NotEqualTo comparators. When performing a set comparison by using the In or the NotIn comparator, you can use up to 30 LocaleValue elements in a QualificationRequirement data structure.

(structure)

The Locale data structure represents a geographical region or location.

Country -> (string)

The country of the locale. Must be a valid ISO 3166 country code. For example, the code US refers to the United States of America.

Subdivision -> (string)

The state or subdivision of the locale. A valid ISO 3166-2 subdivision code. For example, the code WA refers to the state of Washington.

RequiredToPreview -> (boolean)

DEPRECATED: Use the `ActionsGuarded` field instead. If RequiredToPreview is true, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Workerâs Qualifications must meet all of the requirements for which RequiredToPreview is true in order to preview the HIT. If a Worker meets all of the requirements where RequiredToPreview is true (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HITâs question data, but will not be allowed to accept and complete the HIT. The default is false. This should not be used in combination with the `ActionsGuarded` field.

ActionsGuarded -> (string)

Setting this attribute prevents Workers whose Qualifications do not meet this QualificationRequirement from taking the specified action. Valid arguments include âAcceptâ (Worker cannot accept the HIT, but can preview the HIT and see it in their search results), âPreviewAndAcceptâ (Worker cannot accept or preview the HIT, but can see the HIT in their search results), and âDiscoverPreviewAndAcceptâ (Worker cannot accept, preview, or see the HIT in their search results). Itâs possible for you to create a HIT with multiple QualificationRequirements (which can have different values for the ActionGuarded attribute). In this case, the Worker is only permitted to perform an action when they have met all QualificationRequirements guarding the action. The actions in the order of least restrictive to most restrictive are Discover, Preview and Accept. For example, if a Worker meets all QualificationRequirements that are set to DiscoverPreviewAndAccept, but do not meet all requirements that are set with PreviewAndAccept, then the Worker will be able to Discover, i.e. see the HIT in their search result, but will not be able to Preview or Accept the HIT. ActionsGuarded should not be used in combination with the `RequiredToPreview` field.

HITReviewStatus -> (string)

Indicates the review status of the HIT. Valid Values are NotReviewed | MarkedForReview | ReviewedAppropriate | ReviewedInappropriate.

NumberOfAssignmentsPending -> (integer)

The number of assignments for this HIT that are being previewed or have been accepted by Workers, but have not yet been submitted, returned, or abandoned.

NumberOfAssignmentsAvailable -> (integer)

The number of assignments for this HIT that are available for Workers to accept.

NumberOfAssignmentsCompleted -> (integer)

The number of assignments for this HIT that have been approved or rejected.