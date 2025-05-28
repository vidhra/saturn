# gcloud network-connectivity hubs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create)*

**NAME**

: **gcloud network-connectivity hubs create - create a new hub**

**SYNOPSIS**

: **`gcloud network-connectivity hubs create` `[HUB](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create#HUB)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create#--description)`=`DESCRIPTION`] [`[--export-psc](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create#--export-psc)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--policy-mode](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create#--policy-mode)`=`POLICY_MODE`] [`[--preset-topology](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create#--preset-topology)`=`PRESET_TOPOLOGY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new hub with the given name.

**EXAMPLES**

: To create a hub with the name ``my-hub`` and
the description ``optional description``, run:

```
gcloud network-connectivity hubs create my-hub --description="optional description"
```

**POSITIONAL ARGUMENTS**

: **Hub resource - Name of the hub to be created. This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `hub` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`HUB`**:
ID of the hub or fully qualified identifier for the hub.
To set the `hub` attribute:

- provide the argument `hub` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the hub.

**--export-psc**:
This boolean controls whether Private Service Connect transitivity is enabled
for the hub.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--policy-mode**:
Policy mode of the hub. `POLICY_MODE` must be one of:
`policy-mode-unspecified`, `preset`.

**--preset-topology**:
Topology of the hub. Only applicable when
``--policy-mode=PRESET``.
`PRESET_TOPOLOGY` must be one of:
`hybrid-inspection`, `mesh`,
`preset-topology-unspecified`, `star`.

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

: These variants are also available:

```
gcloud alpha network-connectivity hubs create
```

```
gcloud beta network-connectivity hubs create
```