# list-review-policy-results-for-hitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-review-policy-results-for-hit.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/list-review-policy-results-for-hit.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mturk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mturk/index.html#cli-aws-mturk) ]

# list-review-policy-results-for-hit

## Description

The `ListReviewPolicyResultsForHIT` operation retrieves the computed results and the actions taken in the course of executing your Review Policies for a given HIT. For information about how to specify Review Policies when you call CreateHIT, see Review Policies. The ListReviewPolicyResultsForHIT operation can return results for both Assignment-level and HIT-level review results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mturk-requester-2017-01-17/ListReviewPolicyResultsForHIT)

## Synopsis

```
list-review-policy-results-for-hit
--hit-id <value>
[--policy-levels <value>]
[--retrieve-actions | --no-retrieve-actions]
[--retrieve-results | --no-retrieve-results]
[--next-token <value>]
[--max-results <value>]
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

`--hit-id` (string)

The unique identifier of the HIT to retrieve review results for.

`--policy-levels` (list)

The Policy Level(s) to retrieve review results for - HIT or Assignment. If omitted, the default behavior is to retrieve all data for both policy levels. For a list of all the described policies, see Review Policies.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Assignment
  HIT
```

`--retrieve-actions` | `--no-retrieve-actions` (boolean)

Specify if the operation should retrieve a list of the actions taken executing the Review Policies and their outcomes.

`--retrieve-results` | `--no-retrieve-results` (boolean)

Specify if the operation should retrieve a list of the results computed by the Review Policies.

`--next-token` (string)

Pagination token

`--max-results` (integer)

Limit the number of results returned.

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

HITId -> (string)

The HITId of the HIT for which results have been returned.

AssignmentReviewPolicy -> (structure)

The name of the Assignment-level Review Policy. This contains only the PolicyName element.

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

HITReviewPolicy -> (structure)

The name of the HIT-level Review Policy. This contains only the PolicyName element.

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

AssignmentReviewReport -> (structure)

Contains both ReviewResult and ReviewAction elements for an Assignment.

ReviewResults -> (list)

A list of ReviewResults objects for each action specified in the Review Policy.

(structure)

This data structure is returned multiple times for each result specified in the Review Policy.

ActionId -> (string)

A unique identifier of the Review action result.

SubjectId -> (string)

The HITID or AssignmentId about which this result was taken. Note that HIT-level Review Policies will often emit results about both the HIT itself and its Assignments, while Assignment-level review policies generally only emit results about the Assignment itself.

SubjectType -> (string)

The type of the object from the SubjectId field.

QuestionId -> (string)

Specifies the QuestionId the result is describing. Depending on whether the TargetType is a HIT or Assignment this results could specify multiple values. If TargetType is HIT and QuestionId is absent, then the result describes results of the HIT, including the HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the result describes the Workerâs performance on the HIT.

Key -> (string)

Key identifies the particular piece of reviewed information.

Value -> (string)

The values of Key provided by the review policies you have selected.

ReviewActions -> (list)

A list of ReviewAction objects for each action specified in the Review Policy.

(structure)

Both the AssignmentReviewReport and the HITReviewReport elements contains the ReviewActionDetail data structure. This structure is returned multiple times for each action specified in the Review Policy.

ActionId -> (string)

The unique identifier for the action.

ActionName -> (string)

The nature of the action itself. The Review Policy is responsible for examining the HIT and Assignments, emitting results, and deciding which other actions will be necessary.

TargetId -> (string)

The specific HITId or AssignmentID targeted by the action.

TargetType -> (string)

The type of object in TargetId.

Status -> (string)

The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED.

CompleteTime -> (timestamp)

The date when the action was completed.

Result -> (string)

A description of the outcome of the review.

ErrorCode -> (string)

Present only when the Results have a FAILED Status.

HITReviewReport -> (structure)

Contains both ReviewResult and ReviewAction elements for a particular HIT.

ReviewResults -> (list)

A list of ReviewResults objects for each action specified in the Review Policy.

(structure)

This data structure is returned multiple times for each result specified in the Review Policy.

ActionId -> (string)

A unique identifier of the Review action result.

SubjectId -> (string)

The HITID or AssignmentId about which this result was taken. Note that HIT-level Review Policies will often emit results about both the HIT itself and its Assignments, while Assignment-level review policies generally only emit results about the Assignment itself.

SubjectType -> (string)

The type of the object from the SubjectId field.

QuestionId -> (string)

Specifies the QuestionId the result is describing. Depending on whether the TargetType is a HIT or Assignment this results could specify multiple values. If TargetType is HIT and QuestionId is absent, then the result describes results of the HIT, including the HIT agreement score. If ObjectType is Assignment and QuestionId is absent, then the result describes the Workerâs performance on the HIT.

Key -> (string)

Key identifies the particular piece of reviewed information.

Value -> (string)

The values of Key provided by the review policies you have selected.

ReviewActions -> (list)

A list of ReviewAction objects for each action specified in the Review Policy.

(structure)

Both the AssignmentReviewReport and the HITReviewReport elements contains the ReviewActionDetail data structure. This structure is returned multiple times for each action specified in the Review Policy.

ActionId -> (string)

The unique identifier for the action.

ActionName -> (string)

The nature of the action itself. The Review Policy is responsible for examining the HIT and Assignments, emitting results, and deciding which other actions will be necessary.

TargetId -> (string)

The specific HITId or AssignmentID targeted by the action.

TargetType -> (string)

The type of object in TargetId.

Status -> (string)

The current disposition of the action: INTENDED, SUCCEEDED, FAILED, or CANCELLED.

CompleteTime -> (timestamp)

The date when the action was completed.

Result -> (string)

A description of the outcome of the review.

ErrorCode -> (string)

Present only when the Results have a FAILED Status.

NextToken -> (string)

If the previous response was incomplete (because there is more data to retrieve), Amazon Mechanical Turk returns a pagination token in the response. You can use this pagination token to retrieve the next set of results.