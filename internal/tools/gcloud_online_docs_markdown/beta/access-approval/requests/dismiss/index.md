# gcloud beta access-approval requests dismiss  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/access-approval/requests/dismiss](https://cloud.google.com/sdk/gcloud/reference/beta/access-approval/requests/dismiss)*

**NAME**

: **gcloud beta access-approval requests dismiss - dismiss an Access Approval request**

**SYNOPSIS**

: **`gcloud beta access-approval requests dismiss` `[NAME](https://cloud.google.com/sdk/gcloud/reference/beta/access-approval/requests/dismiss#NAME)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/access-approval/requests/dismiss#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` Dismiss an Access Approval request. Note: this does not deny
access to the resource if another request has been made and approved for the
same resource. This will raise an error if the request does not exist.

**EXAMPLES**

: To dismiss an approval request using its name (e.g.
projects/12345/approvalRequests/abc123), run:

```
gcloud beta access-approval requests dismiss projects/12345/approvalRequests/abc123
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

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud access-approval requests dismiss
```

```
gcloud alpha access-approval requests dismiss
```