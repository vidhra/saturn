# gcloud dataproc autoscaling-policies describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/describe](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/describe)*

**NAME**

: **gcloud dataproc autoscaling-policies describe - describe an autoscaling policy**

**SYNOPSIS**

: **`gcloud dataproc autoscaling-policies describe` (`[AUTOSCALING_POLICY](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/describe#AUTOSCALING_POLICY)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/describe#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/describe#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: The following command prints out the autoscaling policy
`example-autoscaling-policy`:

```
gcloud dataproc autoscaling-policies describe example-autoscaling-policy
```

**POSITIONAL ARGUMENTS**

: **Autoscaling policy resource - The autoscaling policy to describe. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `autoscaling_policy` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`AUTOSCALING_POLICY`**:
ID of the autoscaling policy or fully qualified identifier for the autoscaling
policy.
To set the `autoscaling_policy` attribute:

- provide the argument `autoscaling_policy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Dataproc region for the autoscaling policy. Each Dataproc region constitutes an
independent resource namespace constrained to deploying instances into Compute
Engine zones inside the region. Overrides the default
`dataproc/region` property value for this command invocation.
To set the `region` attribute:

- provide the argument `autoscaling_policy` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

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
gcloud alpha dataproc autoscaling-policies describe
```

```
gcloud beta dataproc autoscaling-policies describe
```