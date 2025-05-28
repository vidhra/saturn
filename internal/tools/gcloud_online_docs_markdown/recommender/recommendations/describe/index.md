# gcloud recommender recommendations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/describe](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/describe)*

**NAME**

: **gcloud recommender recommendations describe - describe a recommendation for a Cloud project**

**SYNOPSIS**

: **`gcloud recommender recommendations describe` `[RECOMMENDATION](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/describe#RECOMMENDATION)` `[--location](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/describe#--location)`=`LOCATION` `[--recommender](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/describe#--recommender)`=`RECOMMENDER` (`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/describe#--billing-account)`=`BILLING_ACCOUNT`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/describe#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/describe#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/describe#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a recommendation. This currently supports the following parent
entities: project, billing account, folder, and organization.

**EXAMPLES**

: To describe a recommendation:

```
gcloud recommender recommendations describe RECOMMENDATION_ID --project=${PROJECT} --location=${LOCATION} --recommender=${RECOMMENDER}
```

**POSITIONAL ARGUMENTS**

: **`RECOMMENDATION`**:
Recommendation to describe

**REQUIRED FLAGS**

: **--location**:
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
gcloud alpha recommender recommendations describe
```

```
gcloud beta recommender recommendations describe
```