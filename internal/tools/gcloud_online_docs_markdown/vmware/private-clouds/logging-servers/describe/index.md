# gcloud vmware private-clouds logging-servers describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/describe](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/describe)*

**NAME**

: **gcloud vmware private-clouds logging-servers describe - describe a Google Cloud VMware Engine logging-server**

**SYNOPSIS**

: **`gcloud vmware private-clouds logging-servers describe` (`[LOGGING_SERVER](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/describe#LOGGING_SERVER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/describe#--location)`=`LOCATION` `[--private-cloud](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/describe#--private-cloud)`=`PRIVATE_CLOUD`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/vmware/private-clouds/logging-servers/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display data associated with a VMware Engine logging-server, such as its host
name, port, protocol, and source type.

**EXAMPLES**

: To describe a logging-server called `my-logging-server` in private
cloud `my-private-cloud` and zone `us-west2-a`, run:

```
gcloud vmware private-clouds logging-servers describe my-logging-server --location=us-west2-a --project=my-project --private-cloud=my-private-cloud
```

```
Or:
```

```
gcloud vmware private-clouds logging-servers describe my-logging-server --private-cloud=my-private-cloud
```

```
In the second example, the project and location are taken from gcloud properties core/project and compute/zone.
```

**POSITIONAL ARGUMENTS**

: **Logging Server resource - logging_server. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `logging_server` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`LOGGING_SERVER`**:
ID of the Logging Server or fully qualified identifier for the Logging Server.
To set the `logging-server` attribute:

- provide the argument `logging_server` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the private cloud or cluster.
To set the `location` attribute:

- provide the argument `logging_server` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `compute/zone`.

**--private-cloud**:
VMware Engine private cloud.
To set the `private-cloud` attribute:

- provide the argument `logging_server` on the command line with a
fully specified name;
- provide the argument `--private-cloud` on the command line.**

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