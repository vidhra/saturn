# gcloud dataproc autoscaling-policies import  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/import](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/import)*

**NAME**

: **gcloud dataproc autoscaling-policies import - import an autoscaling policy**

**SYNOPSIS**

: **`gcloud dataproc autoscaling-policies import` (`[AUTOSCALING_POLICY](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/import#AUTOSCALING_POLICY)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/import#--region)`=`REGION`) [`[--source](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/import#--source)`=`SOURCE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/autoscaling-policies/import#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If the specified autoscaling policy already exists, it will be overwritten.
Otherwise, a new autoscaling policy will be created. To edit an existing
autoscaling policy, you can export the autoscaling policy to a file, edit its
configuration, and then import the new configuration.
This command does not allow output only fields, such as policy id and resource
name. It populates the id field based on the resource name specified as the
first command line argument.

**EXAMPLES**

: The following command creates or updates the contents of autoscaling policy
`example-autoscaling-policy` based on a yaml file:

```
gcloud dataproc autoscaling-policies import example-autoscaling-policy --source=saved-policy.yaml
```

**POSITIONAL ARGUMENTS**

: **Autoscaling policy resource - The autoscaling policy to import. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**FLAGS**

: **--source**:
Path to a YAML file containing configuration export data. Alternatively, you may
omit this flag to read from standard input.

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
gcloud alpha dataproc autoscaling-policies import
```

```
gcloud beta dataproc autoscaling-policies import
```