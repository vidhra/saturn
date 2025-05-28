# gcloud dns response-policies describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/describe](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/describe)*

**NAME**

: **gcloud dns response-policies describe - describes a Cloud DNS response policy**

**SYNOPSIS**

: **`gcloud dns response-policies describe` `[RESPONSE_POLICIES](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/describe#RESPONSE_POLICIES)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/describe#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/response-policies/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command describes details of a Cloud DNS response policy.

**EXAMPLES**

: To describe a global response policy (default), run:

```
gcloud dns response-policies describe myresponsepolicy
```

**POSITIONAL ARGUMENTS**

: **Response policy resource - The response policy to describe. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `response_policies` on the command line with a
fully specified name;
- set the property `core/project`.

This must be specified.

**`RESPONSE_POLICIES`**:
ID of the response_policy or fully qualified identifier for the response_policy.
To set the `response-policy` attribute:

- provide the argument `response_policies` on the command line.**

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
gcloud alpha dns response-policies describe
```

```
gcloud beta dns response-policies describe
```