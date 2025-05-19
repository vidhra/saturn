# gcloud alpha asset  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/asset](https://cloud.google.com/sdk/gcloud/reference/alpha/asset)*

**NAME**

: **gcloud alpha asset - manage the Cloud Asset Inventory**

**SYNOPSIS**

: **`gcloud alpha asset` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha/asset#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha/asset#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/asset#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Manage the Cloud Asset Inventory.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[feeds](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/feeds)`**:
`(ALPHA)` Manage Cloud Asset Inventory feeds.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/operations)`**:
`(ALPHA)` Manage Cloud Asset Inventory operations.

**`[saved-queries](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/saved-queries)`**:
`(ALPHA)` Manage Cloud Asset Inventory saved queries.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[analyze-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/analyze-iam-policy)`**:
`(ALPHA)` ALPHA version, Analyzes IAM policies that match a request.

**`[analyze-iam-policy-longrunning](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/analyze-iam-policy-longrunning)`**:
`(ALPHA)` Analyzes IAM policies that match a request asynchronously
and writes the results to Google Cloud Storage or BigQuery destination.

**`[analyze-org-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/analyze-org-policies)`**:
`(ALPHA)` Analyze organization policies under a scope.

**`[analyze-org-policy-governed-containers](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/analyze-org-policy-governed-containers)`**:
`(ALPHA)` Analyze organization policies governed containers under a
scope.

**`[export](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/export)`**:
`(ALPHA)` Export the cloud assets to Google Cloud Storage/BigQuery.

**`[get-history](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/get-history)`**:
`(ALPHA)` Get the update history of assets that overlaps a time
window.

**`[list](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/list)`**:
`(ALPHA)` List the Cloud assets.

**`[query](https://cloud.google.com/sdk/gcloud/reference/alpha/asset/query)`**:
`(ALPHA)` Query the Cloud assets.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud asset
```

```
gcloud beta asset
```