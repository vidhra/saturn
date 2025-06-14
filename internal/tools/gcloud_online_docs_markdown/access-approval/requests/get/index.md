# gcloud access-approval requests get  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/access-approval/requests/get](https://cloud.google.com/sdk/gcloud/reference/access-approval/requests/get)*

**NAME**

: **gcloud access-approval requests get - get an Access Approval request**

**SYNOPSIS**

: **`gcloud access-approval requests get` `[NAME](https://cloud.google.com/sdk/gcloud/reference/access-approval/requests/get#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/access-approval/requests/get#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get an Access Approval Request. Raise error if the request does not exist.

**EXAMPLES**

: To get an approval request using its name (e.g.
projects/my-project-123/approvalRequests/abc123), run:

```
gcloud access-approval requests get projects/my-project-123/approvalRequests/abc123
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
gcloud alpha access-approval requests get
```

```
gcloud beta access-approval requests get
```