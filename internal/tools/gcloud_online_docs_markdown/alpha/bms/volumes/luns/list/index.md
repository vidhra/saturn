# gcloud alpha bms volumes luns list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/luns/list](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/luns/list)*

**NAME**

: **gcloud alpha bms volumes luns list - list Bare Metal Solution LUNs in a project**

**SYNOPSIS**

: **`gcloud alpha bms volumes luns list` (`[--volume](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/luns/list#--volume)`=`VOLUME` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/luns/list#--region)`=`REGION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/luns/list#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/luns/list#--limit)`=`LIMIT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/luns/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` List Bare Metal Solution logical unit numbers (LUNs) for a
volume.

**EXAMPLES**

: To list all LUNs on volume ``my-volume`` in
region ``us-central1``, run:

```
gcloud alpha bms volumes luns list --region=us-central1 --volume=my-volume
```

**REQUIRED FLAGS**

: **Volume resource - volume. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--volume**:
ID of the volume or fully qualified identifier for the volume.
To set the `volume` attribute:

- provide the argument `--volume` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--region**:
Region of the resource.
To set the `region` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--filter`, `--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--filter`, `--limit`.

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
gcloud bms volumes luns list
```