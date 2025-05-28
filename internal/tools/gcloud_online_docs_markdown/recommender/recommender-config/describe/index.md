# gcloud recommender recommender-config describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/describe](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/describe)*

**NAME**

: **gcloud recommender recommender-config describe - describe a recommender configuration**

**SYNOPSIS**

: **`gcloud recommender recommender-config describe` `[RECOMMENDER](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/describe#RECOMMENDER)` `[--location](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/describe#--location)`=`LOCATION` (`[--billing-account](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/describe#--billing-account)`=`BILLING_ACCOUNT`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/describe#--organization)`=`ORGANIZATION_ID`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/describe#--project)`=`PROJECT_ID`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recommender/recommender-config/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a recommender configuration based on a given entity (project,
organization, billing account), location, and recommender.

**EXAMPLES**

: To describe a recommender configuration, run:

```
gcloud recommender recommender-config describe ${RECOMMENDER} --project=${PROJECT} --location=${LOCATION}
```

**POSITIONAL ARGUMENTS**

: **`RECOMMENDER`**:
Recommender to use for this invocation.

**REQUIRED FLAGS**

: **--location**:
Location to use for this invocation.

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

: This variant is also available:

```
gcloud beta recommender recommender-config describe
```