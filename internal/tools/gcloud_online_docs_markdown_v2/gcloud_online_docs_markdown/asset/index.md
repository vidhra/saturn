# gcloud asset  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/asset](https://cloud.google.com/sdk/gcloud/reference/asset)*

**NAME**

: **gcloud asset - manage the Cloud Asset Inventory**

**SYNOPSIS**

: **`gcloud asset` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/asset#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/asset#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/asset#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage the Cloud Asset Inventory.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[feeds](https://cloud.google.com/sdk/gcloud/reference/asset/feeds)`**:
Manage Cloud Asset Inventory feeds.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/asset/operations)`**:
Manage Cloud Asset Inventory operations.

**`[saved-queries](https://cloud.google.com/sdk/gcloud/reference/asset/saved-queries)`**:
Manage Cloud Asset Inventory saved queries.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[analyze-iam-policy](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy)`**:
Analyzes IAM policies that match a request.

**`[analyze-iam-policy-longrunning](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning)`**:
Analyzes IAM policies that match a request asynchronously and writes the results
to Google Cloud Storage or BigQuery destination.

**`[analyze-move](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-move)`**:
Analyzes resource move.

**`[analyze-org-policies](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policies)`**:
Analyze organization policies under a scope.

**`[analyze-org-policy-governed-assets](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-assets)`**:
Analyze organization policies governed assets under a scope.

**`[analyze-org-policy-governed-containers](https://cloud.google.com/sdk/gcloud/reference/asset/analyze-org-policy-governed-containers)`**:
Analyze organization policies governed containers under a scope.

**`[export](https://cloud.google.com/sdk/gcloud/reference/asset/export)`**:
Export the cloud assets to Google Cloud Storage/BigQuery.

**`[get-effective-iam-policy](https://cloud.google.com/sdk/gcloud/reference/asset/get-effective-iam-policy)`**:
Get effective IAM policies for a specified list of resources within accessible
scope, such as a project, folder or organization.

**`[get-history](https://cloud.google.com/sdk/gcloud/reference/asset/get-history)`**:
Get the update history of assets that overlaps a time window.

**`[list](https://cloud.google.com/sdk/gcloud/reference/asset/list)`**:
List the Cloud assets.

**`[query](https://cloud.google.com/sdk/gcloud/reference/asset/query)`**:
Query the Cloud assets.

**`[search-all-iam-policies](https://cloud.google.com/sdk/gcloud/reference/asset/search-all-iam-policies)`**:
Searches all IAM policies within the specified accessible scope, such as a
project, folder or organization.

**`[search-all-resources](https://cloud.google.com/sdk/gcloud/reference/asset/search-all-resources)`**:
Searches all Cloud resources within the specified accessible scope, such as a
project, folder or organization.

**NOTES**

: These variants are also available:

```
gcloud alpha asset
```

```
gcloud beta asset
```