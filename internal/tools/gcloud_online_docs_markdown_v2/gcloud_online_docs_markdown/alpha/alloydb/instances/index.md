# gcloud alpha alloydb instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances)*

**NAME**

: **gcloud alpha alloydb instances - provide commands for managing AlloyDB instances**

**SYNOPSIS**

: **`gcloud alpha alloydb instances` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Provide commands for managing AlloyDB clusters including
creating, configuring, restarting, and deleting instances.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/create)`**:
`(ALPHA)` Creates a new AlloyDB instance within a given cluster.

**`[create-secondary](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/create-secondary)`**:
`(ALPHA)` Creates a new AlloyDB SECONDARY instance within a given
cluster.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/delete)`**:
`(ALPHA)` Deletes an AlloyDB instance within a given cluster.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/describe)`**:
`(ALPHA)` Describes an AlloyDB instance within a given cluster.

**`[failover](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/failover)`**:
`(ALPHA)` Failover an AlloyDB instance within a given cluster.

**`[inject-fault](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/inject-fault)`**:
`(ALPHA)` Inject fault on an AlloyDB instance within a given cluster.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/list)`**:
`(ALPHA)` Lists AlloyDB instances in a given cluster.

**`[restart](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/restart)`**:
`(ALPHA)` Restarts an AlloyDB instance within a given cluster.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update)`**:
`(ALPHA)` Updates an AlloyDB instance within a given cluster.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud alloydb instances
```

```
gcloud beta alloydb instances
```