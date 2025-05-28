# gcloud compute interconnects groups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/create](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/create)*

**NAME**

: **gcloud compute interconnects groups create - create a Compute Engine interconnect group**

**SYNOPSIS**

: **`gcloud compute interconnects groups create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/create#NAME)` `[--intended-topology-capability](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/create#--intended-topology-capability)`=`INTENDED_TOPOLOGY_CAPABILITY` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/create#--description)`=`DESCRIPTION`] [`[--interconnects](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/create#--interconnects)`=[`INTERCONNECT`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/interconnects/groups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute interconnects groups create` is used to create
interconnect groups. An interconnect group connects a set of redundant
interconnects between Google and the customer.
For an example, refer to the `EXAMPLES` section below.

**EXAMPLES**

: To create an interconnect group capable of PRODUCTION_CRITICAL, run:

```
gcloud compute interconnects groups create example-interconnect-group --intended-topology-capability=PRODUCTION_CRITICAL --description="Example interconnect group"
```

It is easy to add members to an existing interconnect group after creation using
the `add-members` command.
To create an interconnect group capable of PRODUCTION_NON_CRITICAL, with two
members at creation time, run:

```
gcloud compute interconnects groups create example-interconnect-group --intended-topology-capability=PRODUCTION_NON_CRITICAL --interconnects=interconnect-1,interconnect-2
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the interconnect group to create.

**REQUIRED FLAGS**

: **--intended-topology-capability**:
The reliability the user intends this group to be capable of, in terms of the
Interconnect product SLAs.

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the interconnect group.

**--interconnects**:
Member interconnects to add to the interconnect group initially.

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

: These variants are also available:

```
gcloud alpha compute interconnects groups create
```

```
gcloud beta compute interconnects groups create
```