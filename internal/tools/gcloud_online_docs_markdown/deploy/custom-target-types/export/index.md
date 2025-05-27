# gcloud deploy custom-target-types export  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/deploy/custom-target-types/export](https://cloud.google.com/sdk/gcloud/reference/deploy/custom-target-types/export)*

**NAME**

: **gcloud deploy custom-target-types export - returns the .yaml definition of the specified custom target type**

**SYNOPSIS**

: **`gcloud deploy custom-target-types export` (`[CUSTOM_TARGET_TYPE](https://cloud.google.com/sdk/gcloud/reference/deploy/custom-target-types/export#CUSTOM_TARGET_TYPE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/deploy/custom-target-types/export#--region)`=`REGION`) [`[--destination](https://cloud.google.com/sdk/gcloud/reference/deploy/custom-target-types/export#--destination)`=`DESTINATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/deploy/custom-target-types/export#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The exported yaml definition can be applied by `deploy apply`
command.

**EXAMPLES**

: To return the .yaml definition of the custom target type
`test-custom-target-type`, in region `us-central1`, run:

```
gcloud deploy custom-target-types export test-custom-target-type --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **Custom target type resource - The name of the Custom Target Type. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `custom_target_type` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CUSTOM_TARGET_TYPE`**:
ID of the custom_target_type or fully qualified identifier for the
custom_target_type.
To set the `custom_target_type` attribute:

- provide the argument `custom_target_type` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud region for the custom_target_type. Alternatively, set the property
[deploy/region].
To set the `region` attribute:

- provide the argument `custom_target_type` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- set the property `deploy/region`.**

**FLAGS**

: **--destination**:
Path to a YAML file where the configuration will be exported. Alternatively, you
may omit this flag to write to standard output.

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
gcloud alpha deploy custom-target-types export
```

```
gcloud beta deploy custom-target-types export
```