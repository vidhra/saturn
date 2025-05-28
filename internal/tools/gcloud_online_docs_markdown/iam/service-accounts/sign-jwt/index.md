# gcloud iam service-accounts sign-jwt  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/sign-jwt](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/sign-jwt)*

**NAME**

: **gcloud iam service-accounts sign-jwt - sign a JWT with a managed service account key**

**SYNOPSIS**

: **`gcloud iam service-accounts sign-jwt` `INPUT-FILE` `OUTPUT-FILE` `[--iam-account](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/sign-jwt#--iam-account)`=`IAM_ACCOUNT` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/sign-jwt#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command signs a JWT using a system-managed service account key.
If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.

**EXAMPLES**

: To create a sign JWT with a system-managed service account key, run:

```
gcloud iam service-accounts sign-jwt --iam-account=my-iam-account@my-project.iam.gserviceaccount.com input.json output.jwt
```

**POSITIONAL ARGUMENTS**

: **`INPUT-FILE`**:
A path to the file containing the JSON JWT Claim set to be signed.

**`OUTPUT-FILE`**:
A path the resulting signed JWT will be written to.

**REQUIRED FLAGS**

: **--iam-account**:
The service account to sign as.

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

**SEE ALSO**

: For more information on how this command ties into the wider cloud
infrastructure, please see [https://cloud.google.com/appengine/docs/java/appidentity/](https://cloud.google.com/appengine/docs/java/appidentity/).

**NOTES**

: These variants are also available:

```
gcloud alpha iam service-accounts sign-jwt
```

```
gcloud beta iam service-accounts sign-jwt
```