# gcloud alpha alloydb clusters  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters)*

**NAME**

: **gcloud alpha alloydb clusters - provide commands for managing AlloyDB clusters**

**SYNOPSIS**

: **`gcloud alpha alloydb clusters` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Provide commands for managing AlloyDB clusters including
creating, configuring, restarting, and deleting clusters.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/create)`**:
`(ALPHA)` Create a new AlloyDB cluster within a given project.

**`[create-secondary](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/create-secondary)`**:
`(ALPHA)` Create a new AlloyDB SECONDARY cluster within a given
project.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/delete)`**:
`(ALPHA)` Delete an AlloyDB cluster in a given region.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/describe)`**:
`(ALPHA)` Describe an AlloyDB cluster in a given project and region.

**`[export](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/export)`**:
`(ALPHA)` Export data from an AlloyDB cluster to Google Cloud
Storage.

**`[import](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/import)`**:
`(ALPHA)` Import data to an AlloyDB cluster from Google Cloud
Storage.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/list)`**:
`(ALPHA)` List AlloyDB clusters in a given project and region.

**`[migrate-cloud-sql](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/migrate-cloud-sql)`**:
`(ALPHA)` Migrate Cloud SQL instance to an AlloyDB cluster using an
existing Cloud SQL backup.

**`[promote](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/promote)`**:
`(ALPHA)` Promote an AlloyDB SECONDARY cluster in a given project and
region.

**`[restore](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/restore)`**:
`(ALPHA)` Restore an AlloyDB cluster from a given backup or a source
cluster and a timestamp.

**`[switchover](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/switchover)`**:
`(ALPHA)` Switchover an AlloyDB SECONDARY cluster in a given project
and region.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/update)`**:
`(ALPHA)` Update an AlloyDB cluster within a given project and
region.

**`[upgrade](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/clusters/upgrade)`**:
`(ALPHA)` Upgrade an AlloyDB cluster within a given project and
region.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud alloydb clusters
```

```
gcloud beta alloydb clusters
```