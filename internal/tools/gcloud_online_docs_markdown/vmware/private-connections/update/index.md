# gcloud vmware private-connections update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update)*

**NAME**

: **gcloud vmware private-connections update - update a Google Cloud Private Connection**

**SYNOPSIS**

: **`gcloud vmware private-connections update` (`[PRIVATE_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update#PRIVATE_CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update#--description)`=`DESCRIPTION`] [`[--routing-mode](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update#--routing-mode)`=`ROUTING_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a VMware Engine private connection. Only description and routing-mode
can be updated.

**EXAMPLES**

: To update a private connection named `my-private-connection` in
project `my-project` and region `us-west1` by changing its
description to `Updated description for the private connection` and
routing-mode to `GLOBAL`, run:

```
gcloud vmware private-connections update my-private-connection --location=us-west1 --project=my-project --description="Updated description for the private connection" --routing-mode=GLOBAL
```

Or:

```
gcloud vmware private-connections update my-private-connection --description="Updated description for the private connection" --routing-mode=GLOBAL
```

In the second example, the project and location are taken from gcloud properties
core/project and compute/regions, respectively.

**POSITIONAL ARGUMENTS**

: **Private Connection resource - private_connection. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `private_connection` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PRIVATE_CONNECTION`**:
ID of the Private Connection or fully qualified identifier for the Private
Connection.
To set the `private-connection` attribute:

- provide the argument `private_connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The resource name of the location.
To set the `location` attribute:

- provide the argument `private_connection` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/region`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--description**:
Updated description for this Private Connection.

**--routing-mode**:
Updated routing mode for this Private Connection.
`ROUTING_MODE` must be one of: `GLOBAL`,
`REGIONAL`.

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