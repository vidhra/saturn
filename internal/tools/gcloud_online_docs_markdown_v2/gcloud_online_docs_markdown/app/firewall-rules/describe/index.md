# gcloud app firewall-rules describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/firewall-rules/describe](https://cloud.google.com/sdk/gcloud/reference/app/firewall-rules/describe)*

**NAME**

: **gcloud app firewall-rules describe - prints the fields of a specified firewall rule**

**SYNOPSIS**

: **`gcloud app firewall-rules describe` `[PRIORITY](https://cloud.google.com/sdk/gcloud/reference/app/firewall-rules/describe#PRIORITY)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/firewall-rules/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Prints the fields of a specified firewall rule.

**EXAMPLES**

: To describe an App Engine firewall rule, run:

```
gcloud app firewall-rules describe 1234
```

**POSITIONAL ARGUMENTS**

: **`PRIORITY`**:
An integer between 1 and 2^32-1 which indicates the evaluation order of rules.
Lowest priority rules are evaluated first. The handle `default` may
also be used to refer to the final rule at priority 2^32-1 which is always
present in a set of rules.

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

: This variant is also available:

```
gcloud beta app firewall-rules describe
```