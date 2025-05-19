# gcloud alloydb clusters  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters)*

**NAME**

: **gcloud alloydb clusters - provide commands for managing AlloyDB clusters**

**SYNOPSIS**

: **`gcloud alloydb clusters` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Provide commands for managing AlloyDB clusters including creating, configuring,
restarting, and deleting clusters.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create)`**:
Create a new AlloyDB cluster within a given project.

**`[create-secondary](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create-secondary)`**:
Create a new AlloyDB SECONDARY cluster within a given project.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/delete)`**:
Delete an AlloyDB cluster in a given region.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/describe)`**:
Describe an AlloyDB cluster in a given project and region.

**`[export](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/export)`**:
Export data from an AlloyDB cluster to Google Cloud Storage.

**`[import](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/import)`**:
Import data into an AlloyDB cluster from Google Cloud Storage.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/list)`**:
List AlloyDB clusters in a given project and region.

**`[promote](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/promote)`**:
Promote an AlloyDB SECONDARY cluster in a given project and region.

**`[restore](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/restore)`**:
Restore an AlloyDB cluster from a given backup or a source cluster and a
timestamp.

**`[switchover](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/switchover)`**:
Switchover an AlloyDB SECONDARY cluster in a given project and region.

**`[update](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/update)`**:
Update an AlloyDB cluster within a given project and region.

**`[upgrade](https://cloud.google.com/sdk/gcloud/reference/alloydb/clusters/upgrade)`**:
Upgrade an AlloyDB cluster within a given project and region.

**NOTES**

: These variants are also available:

```
gcloud alpha alloydb clusters
```

```
gcloud beta alloydb clusters
```