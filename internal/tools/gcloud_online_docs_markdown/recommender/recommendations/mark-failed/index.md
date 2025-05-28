# gcloud recommender recommendations mark-failed  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed)*

**NAME**

: **gcloud recommender recommendations mark-failed - mark a recommendation's state as FAILED**

**SYNOPSIS**

: **`gcloud recommender recommendations mark-failed` `[RECOMMENDATION](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#RECOMMENDATION)` `[--etag](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#--etag)`=`ETAG` `[--location](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#--location)`=`LOCATION` `[--recommender](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#--recommender)`=`RECOMMENDER` (`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#--billing-account)`=`BILLING_ACCOUNT`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#--project)`=`PROJECT_ID`) [`[--state-metadata](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#--state-metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#KEY)`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-failed#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Mark a recommendation's state as FAILED. Can be applied to recommendations in
ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

**EXAMPLES**

: To mark a recommendation as FAILED:

```
gcloud recommender recommendations mark-failed abcd-1234 --project=project-id --location=global --recommender=google.compute.instance.MachineTypeRecommender --etag=abc123 --state-metadata=key1=value1,key2=value2
```

**POSITIONAL ARGUMENTS**

: **`RECOMMENDATION`**:
Recommendation id which will be marked as FAILED.

**REQUIRED FLAGS**

: **--etag**:
Etag of a recommendation.

**--location**:
Location.

**--recommender**:
Recommender of recommendation.

**--billing-account**

**OPTIONAL FLAGS**

: **--state-metadata**:
State metadata for recommendation, in format of
--state-metadata=key1=value1,key2=value2

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
gcloud alpha recommender recommendations mark-failed
```

```
gcloud beta recommender recommendations mark-failed
```