# gcloud dns response-policies rules delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/delete](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/delete)*

**NAME**

: **gcloud dns response-policies rules delete - deletes a Cloud DNS response policy rule**

**SYNOPSIS**

: **`gcloud dns response-policies rules delete` (`[RESPONSE_POLICY_RULE](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/delete#RESPONSE_POLICY_RULE)` : `[--response-policy](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/delete#--response-policy)`=`RESPONSE_POLICY`) [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/delete#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/rules/delete#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To delete a response policy rule, run:

```
gcloud dns response-policies rules delete --response-policy=myresponsepolicy rulename
```

**POSITIONAL ARGUMENTS**

: **Response policy rule resource - The response policy rule to delete. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `response_policy_rule` on the command line with
a fully specified name;
- set the property `core/project`.

This must be specified.

**`RESPONSE_POLICY_RULE`**:
ID of the response_policy_rule or fully qualified identifier for the
response_policy_rule.
To set the `response-policy-rule` attribute:

- provide the argument `response_policy_rule` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--response-policy**:
The Cloud DNS response policy name response_policy_rule.
To set the `response-policy` attribute:

- provide the argument `response_policy_rule` on the command line with
a fully specified name;
- provide the argument `--response-policy` on the command line.**

**FLAGS**

: **--location**:
Specifies the desired service location the request is sent to. Defaults to Cloud
DNS global service. Use --location=global if you want to target the global
service.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**NOTES**

: These variants are also available:

```
gcloud alpha dns response-policies rules delete
```

```
gcloud beta dns response-policies rules delete
```