# gcloud network-connectivity spokes linked-interconnect-attachments create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create)*

**NAME**

: **gcloud network-connectivity spokes linked-interconnect-attachments create - create a new VLAN attachment spoke**

**SYNOPSIS**

: **`gcloud network-connectivity spokes linked-interconnect-attachments create` (`[SPOKE](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#SPOKE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#--region)`=`REGION`) `[--hub](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#--hub)`=`HUB` `[--interconnect-attachments](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#--interconnect-attachments)`=[`INTERCONNECT_ATTACHMENTS`,…] [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#--description)`=`DESCRIPTION`] [`[--group](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#--group)`=`GROUP`] [`[--include-import-ranges](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#--include-import-ranges)`=[`INCLUDE_IMPORT_RANGES`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--site-to-site-data-transfer](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#--site-to-site-data-transfer)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new [VLAN
attachment spoke](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vlan-spoke).

**EXAMPLES**

: To create a spoke in region ``us-central1``
that uses data transfer and has two VLAN attachments, run:

```
gcloud network-connectivity spokes linked-interconnect-attachments create my-spoke --hub="https://www.googleapis.com/networkconnectivity/v1/project\
s/my-project/locations/global/hubs/my-hub" --region=us-central1 \
    --interconnect-attachments=https://www.googleapis.com/compute/\
v1/projects/my-project/regions/us-central1/interconnectAttachments/\
ic1,https://www.googleapis.com/compute/v1/projects/my-project/\
regions/us-central1/interconnectAttachments/ic2 \
    --site-to-site-data-transfer
```

**POSITIONAL ARGUMENTS**

: **Spoke resource - Name of the spoke to be created. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
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

**REQUIRED FLAGS**

: **--hub**:
Hub that the spoke will attach to. The hub must already exist.

**--interconnect-attachments**:
VLAN attachments that the spoke provides connectivity to. The resources must
already exist.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the spoke to create.

**--group**:
The group that the spoke will be added to. The group must already exist. If
unset, the spoke will be added to the ``default`` group.

**--include-import-ranges**:
IP address range(s) allowed to be imported from hub subnets. Only
``ALL_IPV4_RANGES`` can be added to the list. If it's empty, the spoke does not
import any subnets from the hub.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--site-to-site-data-transfer**:
Whether to enable site-to-site data transfer for this spoke. Data transfer is
available only in [supported
locations](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations).

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
gcloud beta network-connectivity spokes linked-interconnect-attachments create
```