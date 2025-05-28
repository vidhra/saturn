# gcloud vmware private-connections describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/describe](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/describe)*

**NAME**

: **gcloud vmware private-connections describe - describe a Google Cloud Private Connection**

**SYNOPSIS**

: **`gcloud vmware private-connections describe` (`[PRIVATE_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/describe#PRIVATE_CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-connections/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Private Connection by its resource name. It contains details of the
private connection, such as service_network, vmware_engine_network, routing_mode
and state.

**EXAMPLES**

: To get the information about a private connection resource called
`my-private-connection` in project `my-project` and region
`us-west1`, run:

```
gcloud vmware private-connections describe my-private-connection --location=us-west1 --project=my-project
```

Or:

```
gcloud vmware private-connections describe my-private-connection
```

In the second example, the project and location are taken from gcloud properties
core/project and compute/region, respectively.

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