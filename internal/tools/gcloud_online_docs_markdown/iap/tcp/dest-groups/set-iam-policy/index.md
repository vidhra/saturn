# gcloud iap tcp dest-groups set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/set-iam-policy)*

**NAME**

: **gcloud iap tcp dest-groups set-iam-policy - set the IAM policy for an IAP TCP Destination Group resource**

**SYNOPSIS**

: **`gcloud iap tcp dest-groups set-iam-policy` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/set-iam-policy#POLICY_FILE)` `[--dest-group](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/set-iam-policy#--dest-group)`=`DEST_GROUP` `[--region](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/set-iam-policy#--region)`=`REGION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command replaces the existing IAM policy for an IAP TCP Destination Group
resource, given a file encoded in JSON or YAML that contains the IAM policy. If
the given policy file specifies an "etag" value, then the replacement will
succeed only if the policy already in place matches that etag. (An etag obtained
via $ [gcloud
iap tcp dest-groups get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iap/tcp/dest-groups/get-iam-policy) will prevent the replacement if the
policy for the resource has been subsequently updated.) A policy file that does
not contain an etag value will replace any existing policy for the resource.

**EXAMPLES**

: To set the IAM policy for the TCP Destination Group resource within the active
project in the group 'my-group' located in the region 'us-west1', run:

```
gcloud iap tcp dest-groups set-iam-policy POLICY_FILE --dest-group=='my-group' --region='us-west1'
```

To set the IAM policy for the TCP Destination Group resource within project
PROJECT_ID in the group 'my-group' located in the region 'us-west1', run:

```
gcloud iap tcp dest-groups set-iam-policy POLICY_FILE --project=PROJECT_ID --dest-group=='my-group' --region='us-west1'
```

**POSITIONAL ARGUMENTS**

: **`POLICY_FILE`**:
JSON or YAML file containing the IAM policy.

**REQUIRED FLAGS**

: **--dest-group**:
Name of the Destination Group.

**--region**:
Region of the Destination Group.

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
gcloud alpha iap tcp dest-groups set-iam-policy
```

```
gcloud beta iap tcp dest-groups set-iam-policy
```