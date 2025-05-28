# gcloud recommender recommendations mark-succeeded  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded)*

**NAME**

: **gcloud recommender recommendations mark-succeeded - mark a recommendation's state as SUCCEEDED**

**SYNOPSIS**

: **`gcloud recommender recommendations mark-succeeded` `[RECOMMENDATION](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#RECOMMENDATION)` `[--etag](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#--etag)`=`ETAG` `[--location](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#--location)`=`LOCATION` `[--recommender](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#--recommender)`=`RECOMMENDER` (`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#--billing-account)`=`BILLING_ACCOUNT`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#--project)`=`PROJECT_ID`) [`[--state-metadata](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#--state-metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#KEY)`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender/recommendations/mark-succeeded#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Mark a recommendation's state as SUCCEEDED. Can be applied to recommendations in
ACTIVE, CLAIMED, SUCCEEDED, or FAILED state.

**EXAMPLES**

: To mark a recommendation as SUCCEEDED:

```
gcloud recommender recommendations mark-succeeded abcd-1234 --project=project-id --location=global --recommender=google.compute.instance.MachineTypeRecommender --etag=abc123 --state-metadata=key1=value1,key2=value2
```

**POSITIONAL ARGUMENTS**

: **`RECOMMENDATION`**:
Recommendation id which will be marked as succeeded

**REQUIRED FLAGS**

: **--etag**:
Etag of a recommendation

**--location**:
Location

**--recommender**:
Recommender of recommendation

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
gcloud alpha recommender recommendations mark-succeeded
```

```
gcloud beta recommender recommendations mark-succeeded
```