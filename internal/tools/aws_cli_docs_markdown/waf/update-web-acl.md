# update-web-aclÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-web-acl.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-web-acl.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [waf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/index.html#cli-aws-waf) ]

# update-web-acl

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Inserts or deletes  ActivatedRule objects in a `WebACL` . Each `Rule` identifies web requests that you want to allow, block, or count. When you update a `WebACL` , you specify the following values:

- A default action for the `WebACL` , either `ALLOW` or `BLOCK` . AWS WAF performs the default action if a request doesnât match the criteria in any of the `Rules` in a `WebACL` .
- The `Rules` that you want to add or delete. If you want to replace one `Rule` with another, you delete the existing `Rule` and add the new one.
- For each `Rule` , whether you want AWS WAF to allow requests, block requests, or count requests that match the conditions in the `Rule` .
- The order in which you want AWS WAF to evaluate the `Rules` in a `WebACL` . If you add more than one `Rule` to a `WebACL` , AWS WAF evaluates each request against the `Rules` in order based on the value of `Priority` . (The `Rule` that has the lowest value for `Priority` is evaluated first.) When a web request matches all the predicates (such as `ByteMatchSets` and `IPSets` ) in a `Rule` , AWS WAF immediately takes the corresponding action, allow or block, and doesnât evaluate the request against the remaining `Rules` in the `WebACL` , if any.

To create and configure a `WebACL` , perform the following steps:

- Create and update the predicates that you want to include in `Rules` . For more information, see  CreateByteMatchSet ,  UpdateByteMatchSet ,  CreateIPSet ,  UpdateIPSet ,  CreateSqlInjectionMatchSet , and  UpdateSqlInjectionMatchSet .
- Create and update the `Rules` that you want to include in the `WebACL` . For more information, see  CreateRule and  UpdateRule .
- Create a `WebACL` . See  CreateWebACL .
- Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an  UpdateWebACL request.
- Submit an `UpdateWebACL` request to specify the `Rules` that you want to include in the `WebACL` , to specify the default action, and to associate the `WebACL` with a CloudFront distribution.  The `ActivatedRule` can be a rule group. If you specify a rule group as your `ActivatedRule` , you can exclude specific rules from that rule group. If you already have a rule group associated with a web ACL and want to submit an `UpdateWebACL` request to exclude certain rules from that rule group, you must first remove the rule group from the web ACL, the re-insert it again, specifying the excluded rules. For details, see  ActivatedRule$ExcludedRules .

Be aware that if you try to add a RATE_BASED rule to a web ACL without setting the rule type when first creating the rule, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule (the default rule type) with the specified ID, which does not exist.

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/UpdateWebACL)

## Synopsis

```
update-web-acl
--web-acl-id <value>
--change-token <value>
[--updates <value>]
[--default-action <value>]
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

`--web-acl-id` (string)

The `WebACLId` of the  WebACL that you want to update. `WebACLId` is returned by  CreateWebACL and by  ListWebACLs .

`--change-token` (string)

The value returned by the most recent call to  GetChangeToken .

`--updates` (list)

An array of updates to make to the  WebACL .

An array of `WebACLUpdate` objects that you want to insert into or delete from a  WebACL . For more information, see the applicable data types:

- WebACLUpdate : Contains `Action` and `ActivatedRule`
- ActivatedRule : Contains `Action` , `OverrideAction` , `Priority` , `RuleId` , and `Type` . `ActivatedRule|OverrideAction` applies only when updating or adding a `RuleGroup` to a `WebACL` . In this case, you do not use `ActivatedRule|Action` . For all other update requests, `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction` .
- WafAction : Contains `Type`

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies whether to insert a `Rule` into or delete a `Rule` from a `WebACL` .

Action -> (string)

Specifies whether to insert a `Rule` into or delete a `Rule` from a `WebACL` .

ActivatedRule -> (structure)

The `ActivatedRule` object in an  UpdateWebACL request specifies a `Rule` that you want to insert or delete, the priority of the `Rule` in the `WebACL` , and the action that you want AWS WAF to take when a web request matches the `Rule` (`ALLOW` , `BLOCK` , or `COUNT` ).

Priority -> (integer)

Specifies the order in which the `Rules` in a `WebACL` are evaluated. Rules with a lower value for `Priority` are evaluated before `Rules` with a higher value. The value must be a unique integer. If you add multiple `Rules` to a `WebACL` , the values donât need to be consecutive.

RuleId -> (string)

The `RuleId` for a `Rule` . You use `RuleId` to get more information about a `Rule` (see  GetRule ), update a `Rule` (see  UpdateRule ), insert a `Rule` into a `WebACL` or delete a one from a `WebACL` (see  UpdateWebACL ), or delete a `Rule` from AWS WAF (see  DeleteRule ).

`RuleId` is returned by  CreateRule and by  ListRules .

Action -> (structure)

Specifies the action that CloudFront or AWS WAF takes when a web request matches the conditions in the `Rule` . Valid values for `Action` include the following:

- `ALLOW` : CloudFront responds with the requested object.
- `BLOCK` : CloudFront responds with an HTTP 403 (Forbidden) status code.
- `COUNT` : AWS WAF increments a counter of requests that match the conditions in the rule and then continues to inspect the web request based on the remaining rules in the web ACL.

`ActivatedRule|OverrideAction` applies only when updating or adding a `RuleGroup` to a `WebACL` . In this case, you do not use `ActivatedRule|Action` . For all other update requests, `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction` .

Type -> (string)

Specifies how you want AWS WAF to respond to requests that match the settings in a `Rule` . Valid settings include the following:

- `ALLOW` : AWS WAF allows requests
- `BLOCK` : AWS WAF blocks requests
- `COUNT` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You canât specify `COUNT` for the default action for a `WebACL` .

OverrideAction -> (structure)

Use the `OverrideAction` to test your `RuleGroup` .

Any rule in a `RuleGroup` can potentially block a request. If you set the `OverrideAction` to `None` , the `RuleGroup` will block a request if any individual rule in the `RuleGroup` matches the request and is configured to block that request. However if you first want to test the `RuleGroup` , set the `OverrideAction` to `Count` . The `RuleGroup` will then override any block action specified by individual rules contained within the group. Instead of blocking matching requests, those requests will be counted. You can view a record of counted requests using  GetSampledRequests .

`ActivatedRule|OverrideAction` applies only when updating or adding a `RuleGroup` to a `WebACL` . In this case you do not use `ActivatedRule|Action` . For all other update requests, `ActivatedRule|Action` is used instead of `ActivatedRule|OverrideAction` .

Type -> (string)

`COUNT` overrides the action specified by the individual rule within a `RuleGroup` . If set to `NONE` , the ruleâs action will take place.

Type -> (string)

The rule type, either `REGULAR` , as defined by  Rule , `RATE_BASED` , as defined by  RateBasedRule , or `GROUP` , as defined by  RuleGroup . The default is REGULAR. Although this field is optional, be aware that if you try to add a RATE_BASED rule to a web ACL without setting the type, the  UpdateWebACL request will fail because the request tries to add a REGULAR rule with the specified ID, which does not exist.

ExcludedRules -> (list)

An array of rules to exclude from a rule group. This is applicable only when the `ActivatedRule` refers to a `RuleGroup` .

Sometimes it is necessary to troubleshoot rule groups that are blocking traffic unexpectedly (false positives). One troubleshooting technique is to identify the specific rule within the rule group that is blocking the legitimate traffic and then disable (exclude) that particular rule. You can exclude rules from both your own rule groups and AWS Marketplace rule groups that have been associated with a web ACL.

Specifying `ExcludedRules` does not remove those rules from the rule group. Rather, it changes the action for the rules to `COUNT` . Therefore, requests that match an `ExcludedRule` are counted but not blocked. The `RuleGroup` owner will receive COUNT metrics for each `ExcludedRule` .

If you want to exclude rules from a rule group that is already associated with a web ACL, perform the following steps:

- Use the AWS WAF logs to identify the IDs of the rules that you want to exclude. For more information about the logs, see [Logging Web ACL Traffic Information](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) .
- Submit an  UpdateWebACL request that has two actions:
- The first action deletes the existing rule group from the web ACL. That is, in the  UpdateWebACL request, the first `Updates:Action` should be `DELETE` and `Updates:ActivatedRule:RuleId` should be the rule group that contains the rules that you want to exclude.
- The second action inserts the same rule group back in, but specifying the rules to exclude. That is, the second `Updates:Action` should be `INSERT` , `Updates:ActivatedRule:RuleId` should be the rule group that you just removed, and `ExcludedRules` should contain the rules that you want to exclude.

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The rule to exclude from a rule group. This is applicable only when the `ActivatedRule` refers to a `RuleGroup` . The rule must belong to the `RuleGroup` that is specified by the `ActivatedRule` .

RuleId -> (string)

The unique identifier for the rule to exclude from the rule group.

JSON Syntax:

```
[
  {
    "Action": "INSERT"|"DELETE",
    "ActivatedRule": {
      "Priority": integer,
      "RuleId": "string",
      "Action": {
        "Type": "BLOCK"|"ALLOW"|"COUNT"
      },
      "OverrideAction": {
        "Type": "NONE"|"COUNT"
      },
      "Type": "REGULAR"|"RATE_BASED"|"GROUP",
      "ExcludedRules": [
        {
          "RuleId": "string"
        }
        ...
      ]
    }
  }
  ...
]
```

`--default-action` (structure)

A default action for the web ACL, either ALLOW or BLOCK. AWS WAF performs the default action if a request doesnât match the criteria in any of the rules in a web ACL.

Type -> (string)

Specifies how you want AWS WAF to respond to requests that match the settings in a `Rule` . Valid settings include the following:

- `ALLOW` : AWS WAF allows requests
- `BLOCK` : AWS WAF blocks requests
- `COUNT` : AWS WAF increments a counter of the requests that match all of the conditions in the rule. AWS WAF then continues to inspect the web request based on the remaining rules in the web ACL. You canât specify `COUNT` for the default action for a `WebACL` .

Shorthand Syntax:

```
Type=string
```

JSON Syntax:

```
{
  "Type": "BLOCK"|"ALLOW"|"COUNT"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update a web ACL**

The following `update-web-acl` command deletes an `ActivatedRule` object in a WebACL.

**aws waf update-web-acl**:
âweb-acl-id a123fae4-b567-8e90-1234-5ab67ac8ca90 âchange-token 12cs345-67cd-890b-1cd2-c3a4567d89f1 âupdates Action=âDELETEâ,ActivatedRule=â{Priority=1,RuleId=âWAFRule-1-Exampleâ,Action={Type=âALLOWâ},Type=âREGULARâ}â

Output:

```
{
    "ChangeToken": "12cs345-67cd-890b-1cd2-c3a4567d89f1"
}
```

For more information, see [Working with Web ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-working-with.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

## Output

ChangeToken -> (string)

The `ChangeToken` that you used to submit the `UpdateWebACL` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .