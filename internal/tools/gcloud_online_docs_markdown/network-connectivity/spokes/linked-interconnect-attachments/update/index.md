# gcloud network-connectivity spokes linked-interconnect-attachments update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update)*

**NAME**

: **gcloud network-connectivity spokes linked-interconnect-attachments update - update a VLAN attachment spoke**

**SYNOPSIS**

: **`gcloud network-connectivity spokes linked-interconnect-attachments update` (`[SPOKE](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update#SPOKE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update#--description)`=`DESCRIPTION`] [`[--include-import-ranges](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update#--include-import-ranges)`=[`INCLUDE_IMPORT_RANGES`,…]] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the details of a VLAN attachment spoke.

**EXAMPLES**

: To update the description of a VLAN attachment spoke named
``my-spoke``, run:

```
gcloud network-connectivity spokes linked-interconnect-attachments update my-spoke --region=us-central1 --description="new spoke description"
```

**POSITIONAL ARGUMENTS**

: **Spoke resource - Name of the spoke to update. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `spoke` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SPOKE`**:
ID of the spoke or fully qualified identifier for the spoke.
To set the `spoke` attribute:

- provide the argument `spoke` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The location Id.
To set the `region` attribute:

- provide the argument `spoke` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
New description of the spoke.

**--include-import-ranges**:
IP address range(s) allowed to be imported from hub subnets. Only
``ALL_IPV4_RANGES`` can be added to the list. If it's empty, the spoke does not
import any subnets from the hub.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity spokes linked-interconnect-attachments update
```