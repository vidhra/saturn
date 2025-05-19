# gcloud alpha compute interconnects groups update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/update](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/update)*

**NAME**

: **gcloud alpha compute interconnects groups update - update a Compute Engine interconnect group**

**SYNOPSIS**

: **`gcloud alpha compute interconnects groups update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/update#NAME)` [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/update#--description)`=`DESCRIPTION`] [`[--intended-topology-capability](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/update#--intended-topology-capability)`=`INTENDED_TOPOLOGY_CAPABILITY`] [`[--interconnects](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/update#--interconnects)`=[`INTERCONNECT`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/interconnects/groups/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute interconnects groups
update` is used to update interconnect groups.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To update an interconnect group example-interconnect-group's intended topology
capability to PRODUCTION_CRITICAL, run:

```
gcloud alpha compute interconnects groups update example-interconnect-group --intended-topology-capability=PRODUCTION_CRITICAL
```

To update an interconnect group example-interconnect-group's description to
"example interconnect group description", run:

```
gcloud alpha compute interconnects groups update example-interconnect-group --description="example interconnect group description"
```

To update an interconnect group example-interconnect-group's member
interconnects to interconnect-1 and interconnect-2, run:

```
gcloud alpha compute interconnects groups update example-interconnect-group --interconnects=interconnect-1,interconnect-2
```

Although you can add or remove member interconnects using this command, it is
recommended to add or remove member interconnects using the
`add-members` and `remove-members` commands.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect group to update.

**FLAGS**

: **--description**:
An optional, textual description for the interconnect group.

**--intended-topology-capability**:
The reliability the user intends this group to be capable of, in terms of the
Interconnect product SLAs.

**--interconnects**:
Member interconnects to set the interconnect group to contain.

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

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute interconnects groups update
```

```
gcloud beta compute interconnects groups update
```