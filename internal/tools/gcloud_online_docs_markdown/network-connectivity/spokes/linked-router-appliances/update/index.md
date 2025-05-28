# gcloud network-connectivity spokes linked-router-appliances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update)*

**NAME**

: **gcloud network-connectivity spokes linked-router-appliances update - update a Router appliance spoke**

**SYNOPSIS**

: **`gcloud network-connectivity spokes linked-router-appliances update` (`[SPOKE](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#SPOKE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#--description)`=`DESCRIPTION`] [`[--include-import-ranges](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#--include-import-ranges)`=[`INCLUDE_IMPORT_RANGES`,…]] [`[--router-appliance](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#--router-appliance)`=[`instance`=`INSTANCE`],[`ip`=`IP`]] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the details of a Router appliance spoke.

**EXAMPLES**

: To update the description of a Router appliance spoke named
``my-spoke``, run:

```
gcloud network-connectivity spokes linked-router-appliances update my-spoke --region=us-central1 --description="new spoke description"
```

To replace the router appliance instances linked to a spoke with two new
instances, run:

```
gcloud network-connectivity spokes linked-router-appliances update my-spoke --region=us-central1 --router-appliance=instance=https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/vm1,ip=10.10.0.1 --router-appliance=instance=https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/vm2,ip=10.10.0.2
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

**--router-appliance**:
Router appliance instance(s) with which to replace the set of instances already
linked to this spoke. Pass this flag multiple times to replace with multiple
instances. For example, use
`--router-appliance=instance=new_ins_uri,ip=10.10.0.1` for a single
router appliance instance, or
`--router-appliance=instance=new_ins_uri_1,ip=10.10.0.1
--router-appliance=instance=new_ins_uri_2,ip=10.10.0.2 …` for
multiple instances.

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
gcloud beta network-connectivity spokes linked-router-appliances update
```