# gcloud vmware private-clouds delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/delete](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/delete)*

**NAME**

: **gcloud vmware private-clouds delete - delete a Google Cloud VMware Engine private cloud**

**SYNOPSIS**

: **`gcloud vmware private-clouds delete` (`[PRIVATE_CLOUD](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/delete#PRIVATE_CLOUD)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/delete#--async)`] [`[--delay-hours](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/delete#--delay-hours)`=`DELAY_HOURS`; default=3] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Marks a VMware Engine private cloud for deletion. The resource is deleted 3
hours after being marked for deletion. This process can be reversed by using
`[gcloud
vmware private-clouds undelete](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/undelete)`.

**EXAMPLES**

: To mark a private cloud called `my-private-cloud` for deletion, run:

```
gcloud vmware private-clouds delete my-private-cloud --location=us-west2-a --project=my-project
```

Or:

```
gcloud vmware private-clouds delete my-private-cloud
```

In the second example, the project and location are taken from gcloud properties
core/project and compute/zone.

**POSITIONAL ARGUMENTS**

: **Private cloud resource - private_cloud. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `private_cloud` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PRIVATE_CLOUD`**:
ID of the private cloud or fully qualified identifier for the private cloud.
To set the `private-cloud` attribute:

- provide the argument `private_cloud` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `private_cloud` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--delay-hours**:
Number of hours to wait before deleting the private cloud. Specifying a value of
`0` for this field begins the deletion process immediately.
`DELAY_HOURS` must be one of: `0`,
`1`, `2`, `3`, `4`, `5`,
`6`, `7`, `8`.

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