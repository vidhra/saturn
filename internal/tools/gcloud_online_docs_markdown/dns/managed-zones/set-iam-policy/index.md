# gcloud dns managed-zones set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/set-iam-policy)*

**NAME**

: **gcloud dns managed-zones set-iam-policy - set the IAM policy for a Cloud DNS managed-zone**

**SYNOPSIS**

: **`gcloud dns managed-zones set-iam-policy` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/set-iam-policy#ZONE)` `[--policy-file](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/set-iam-policy#--policy-file)`=`POLICY_FILE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dns/managed-zones/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command sets the IAM policy of the specified managed-zone.

**EXAMPLES**

: To set the IAM policy of your managed-zone , run:

```
gcloud dns managed-zones set-iam-policy my-zone --policy-file=policy.json
```

**POSITIONAL ARGUMENTS**

: **Zone resource - The name of the managed-zone to set the IAM policy for. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ZONE`**:
ID of the zone or fully qualified identifier for the zone.
To set the `zone` attribute:

- provide the argument `zone` on the command line.**

**REQUIRED FLAGS**

: **--policy-file**:
JSON or YAML file with the IAM policy

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
gcloud alpha dns managed-zones set-iam-policy
```

```
gcloud beta dns managed-zones set-iam-policy
```