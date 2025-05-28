# gcloud dns policies describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/policies/describe](https://cloud.google.com/sdk/gcloud/reference/dns/policies/describe)*

**NAME**

: **gcloud dns policies describe - describes a Cloud DNS policy**

**SYNOPSIS**

: **`gcloud dns policies describe` `[POLICY](https://cloud.google.com/sdk/gcloud/reference/dns/policies/describe#POLICY)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/policies/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describes details of a Cloud DNS policy.

**EXAMPLES**

: To describe a policy, run:

```
gcloud dns policies describe mypolicy
```

**POSITIONAL ARGUMENTS**

: **Policy resource - The name of the policy you want to describe. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `policy` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`POLICY`**:
ID of the policy or fully qualified identifier for the policy.
To set the `policy` attribute:

- provide the argument `policy` on the command line.**

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

**API REFERENCE**

: This command uses the `dns/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/dns/docs](https://cloud.google.com/dns/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha dns policies describe
```

```
gcloud beta dns policies describe
```