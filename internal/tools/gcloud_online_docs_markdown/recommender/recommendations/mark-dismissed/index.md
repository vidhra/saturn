# gcloud recommender recommendations mark-dismissed  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed)*

**NAME**

: **gcloud recommender recommendations mark-dismissed - mark recommendation's state as DISMISSED**

**SYNOPSIS**

: **`gcloud recommender recommendations mark-dismissed` `[RECOMMENDATION](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed#RECOMMENDATION)` `[--etag](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed#--etag)`=`ETAG` `[--location](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed#--location)`=`LOCATION` `[--recommender](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed#--recommender)`=`RECOMMENDER` (`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed#--billing-account)`=`BILLING_ACCOUNT`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-dismissed#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Mark recommendation's state as DISMISSED. Can be applied to recommendations in
ACTIVE state. The following parent resources are supported: project, billing
account, folder, and organization as parent resources for recommendations.

**EXAMPLES**

: To mark a recommendation as DISMISSED:

```
gcloud recommender recommendations mark-dismissed abcd-1234 --project=project-id --location=global --recommender=google.compute.instance.MachineTypeRecommender --etag=abc123
```

**POSITIONAL ARGUMENTS**

: **`RECOMMENDATION`**:
Recommendation ID which will be marked as dismissed

**REQUIRED FLAGS**

: **--etag**:
Etag of a recommendation

**--location**:
Location

**--recommender**:
Recommender of the recommendations

**--billing-account**

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
gcloud alpha recommender recommendations mark-dismissed
```

```
gcloud beta recommender recommendations mark-dismissed
```