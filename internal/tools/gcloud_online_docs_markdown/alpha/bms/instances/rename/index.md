# gcloud alpha bms instances rename  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/rename](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/rename)*

**NAME**

: **gcloud alpha bms instances rename - rename a Bare Metal Solution instance**

**SYNOPSIS**

: **`gcloud alpha bms instances rename` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/rename#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/rename#--region)`=`REGION`) `[--new-name](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/rename#--new-name)`=`NEW_NAME` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/instances/rename#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Rename a Bare Metal Solution instance.

**EXAMPLES**

: To rename an instance ``my-instance`` to
``my-new-instance-name`` in region
``us-central1``, run:

```
gcloud alpha bms instances rename my-instance --new-name=my-new-instance-name --region=us-central1 --project=bms-example-project
```

**POSITIONAL ARGUMENTS**

: **Instance resource - instance. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Region of the resource.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

**REQUIRED FLAGS**

: **--new-name**:
New instance name for renaming an already existing instance.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud bms instances rename
```