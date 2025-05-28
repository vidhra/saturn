# gcloud network-connectivity hubs groups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update)*

**NAME**

: **gcloud network-connectivity hubs groups update - update a group**

**SYNOPSIS**

: **`gcloud network-connectivity hubs groups update` (`[GROUP](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#GROUP)` : `[--hub](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#--hub)`=`HUB`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#--description)`=`DESCRIPTION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--add-auto-accept-projects](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#--add-auto-accept-projects)`=[`AUTO-ACCEPT-PROJECTS`,…]     | `[--clear-auto-accept-projects](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#--clear-auto-accept-projects)`     | `[--remove-auto-accept-projects](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#--remove-auto-accept-projects)`=[`AUTO-ACCEPT-PROJECTS`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the details of a group.

**EXAMPLES**

: To update the description of a group named
``my-group``, in the hub
``my-hub``, run:

```
gcloud network-connectivity hubs groups update my-group --hub=my-hub --description="new group description"
```

To add the project ``my-project`` to the
auto-accept list of a group named ``my-group``
in the hub ``my-hub``, run:

```
gcloud network-connectivity hubs groups update my-group --hub=my-hub --add-auto-accept-projects=my-project
```

**POSITIONAL ARGUMENTS**

: **Group resource - Name of the group to update. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
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
The hub Id.
To set the `hub` attribute:

- provide the argument `group` on the command line with a fully
specified name;
- provide the argument `--hub` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
New description of the group.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--add-auto-accept-projects**

**--clear-labels**

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

: This command uses the networkconnectivity/v1 API. The full documentation for
this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity hubs groups update
```