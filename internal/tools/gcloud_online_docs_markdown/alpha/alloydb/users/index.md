# gcloud alpha alloydb users  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users)*

**NAME**

: **gcloud alpha alloydb users - provide commands for managing AlloyDB users**

**SYNOPSIS**

: **`gcloud alpha alloydb users` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Provide commands for managing AlloyDB users including
creating, configuring, getting, listing, and deleting users.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[create](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/create)`**:
`(ALPHA)` Creates a user in a given cluster.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/delete)`**:
`(ALPHA)` Deletes an AlloyDB user in a given cluster.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/list)`**:
`(ALPHA)` Lists AlloyDB users in a given cluster.

**`[set-password](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/set-password)`**:
`(ALPHA)` Update an AlloyDB user's password within a given cluster
and region.

**`[set-roles](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/set-roles)`**:
`(ALPHA)` Update an AlloyDB user's database roles within a given
cluster and region.

**`[set-superuser](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/users/set-superuser)`**:
`(ALPHA)` Update an AlloyDB user's superuser role within a given
cluster and region.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud alloydb users
```

```
gcloud beta alloydb users
```