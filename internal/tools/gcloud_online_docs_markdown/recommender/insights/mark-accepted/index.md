# gcloud recommender insights mark-accepted  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted)*

**NAME**

: **gcloud recommender insights mark-accepted - mark an insight's state as ACCEPTED**

**SYNOPSIS**

: **`gcloud recommender insights mark-accepted` `[INSIGHT](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#INSIGHT)` `[--etag](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#--etag)`=`etag` `[--insight-type](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#--insight-type)`=`INSIGHT_TYPE` `[--location](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#--location)`=`LOCATION` (`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#--billing-account)`=`BILLING_ACCOUNT`     | `[--folder](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#--project)`=`PROJECT_ID`) [`[--state-metadata](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#--state-metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#KEY)`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender/insights/mark-accepted#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Mark an insight's state as ACCEPTED. Can be applied to insights in ACTIVE or
ACCEPTED state. The following are currently supported: project, billing_account,
folder, and organization.

**EXAMPLES**

: To mark an insight as ACCEPTED:

```
gcloud recommender insights mark-accepted abcd-1234 --project=project-id --location=global --insight-type=google.compute.firewall.Insight --etag=abc123
```

**POSITIONAL ARGUMENTS**

: **`INSIGHT`**:
Insight id which will be marked as accepted

**REQUIRED FLAGS**

: **--etag**:
Etag of a insight

**--insight-type**:
Insight Type of the insights

**--location**:
Location

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
gcloud alpha recommender insights mark-accepted
```

```
gcloud beta recommender insights mark-accepted
```