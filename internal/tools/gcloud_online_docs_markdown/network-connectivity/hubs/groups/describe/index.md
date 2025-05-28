# gcloud network-connectivity hubs groups describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/describe](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/describe)*

**NAME**

: **gcloud network-connectivity hubs groups describe - describe a group**

**SYNOPSIS**

: **`gcloud network-connectivity hubs groups describe` (`[GROUP](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/describe#GROUP)` : `[--hub](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/describe#--hub)`=`HUB`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieve and display details about a group.

**EXAMPLES**

: To display details about a group named
``my-group``, run:

```
gcloud network-connectivity hubs groups describe my-group
```

**POSITIONAL ARGUMENTS**

: **Group resource - Name of the group to describe. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `group` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`GROUP`**:
ID of the group or fully qualified identifier for the group.
To set the `group` attribute:

- provide the argument `group` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--hub**:
Id of the hub.
To set the `hub` attribute:

- provide the argument `group` on the command line with a fully
specified name;
- provide the argument `--hub` on the command line.**

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

**API REFERENCE**

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity hubs groups describe
```