# gcloud access-approval requests invalidate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-approval/requests/invalidate](https://cloud.google.com/sdk/gcloud/reference/access-approval/requests/invalidate)*

**NAME**

: **gcloud access-approval requests invalidate - invalidate an Access Approval request**

**SYNOPSIS**

: **`gcloud access-approval requests invalidate` `[NAME](https://cloud.google.com/sdk/gcloud/reference/access-approval/requests/invalidate#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-approval/requests/invalidate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Invalidate an Access Approval request. This will raise an error if the request
does not exist or is not in an approved state.

**EXAMPLES**

: To invalidate an approval request using its name (e.g.
projects/12345/approvalRequests/abc123), run:

```
gcloud access-approval requests invalidate projects/12345/approvalRequests/abc123
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the Access Approval request to invalidate

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
gcloud alpha access-approval requests invalidate
```

```
gcloud beta access-approval requests invalidate
```