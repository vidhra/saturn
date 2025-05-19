# gcloud container fleet memberships delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete)*

**NAME**

: **gcloud container fleet memberships delete - delete a membership**

**SYNOPSIS**

: **`gcloud container fleet memberships delete` (`[MEMBERSHIP](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete#MEMBERSHIP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command deletes the Fleet Membership resource corresponding to the cluster.
This command is intended to delete stale Fleet Membership resources as doing so
on a fully registered cluster will skip uninstalling the Connect Agent and and
orphan in-cluster resources and agent connections to Google. To completely
unregister the cluster, consider using the command: `[gcloud
container fleet memberships unregister](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/unregister)`.

**EXAMPLES**

: First retrieve the ID of the membership using the command below. The output of
this command lists all the fleet's members, with their unique IDs in the Names
column:

```
gcloud container fleet memberships list
```

Delete a membership from the active project's fleet:

```
gcloud container fleet memberships delete MEMBERSHIP_NAME
```

**POSITIONAL ARGUMENTS**

: **Membership resource - The cluster membership to delete. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `membership` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MEMBERSHIP`**:
ID of the membership or fully qualified identifier for the membership.
To set the `membership` attribute:

- provide the argument `membership` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `membership` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- global is the only supported location.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `gkehub/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster](https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster)

**NOTES**

: These variants are also available:

```
gcloud alpha container fleet memberships delete
```

```
gcloud beta container fleet memberships delete
```