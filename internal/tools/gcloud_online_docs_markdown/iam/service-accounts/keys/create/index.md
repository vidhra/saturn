# gcloud iam service-accounts keys create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/create](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/create)*

**NAME**

: **gcloud iam service-accounts keys create - create a service account key**

**SYNOPSIS**

: **`gcloud iam service-accounts keys create` `OUTPUT-FILE` `[--iam-account](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/create#--iam-account)`=`IAM_ACCOUNT` [`[--key-file-type](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/create#--key-file-type)`=`KEY_FILE_TYPE`; default="json"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.

**EXAMPLES**

: To create a new service account key and save the private portion of the key
locally, run:

```
gcloud iam service-accounts keys create key.json --iam-account=my-iam-account@my-project.iam.gserviceaccount.com
```

**POSITIONAL ARGUMENTS**

: **`OUTPUT-FILE`**:
The path where the resulting private key should be written. File system write
permission will be checked on the specified path prior to the key creation.

**REQUIRED FLAGS**

: **--iam-account**:
The service account for which to create a key.
To list all service accounts in the project, run:

```
gcloud iam service-accounts list
```

**OPTIONAL FLAGS**

: **--key-file-type**:
The type of key to create. `KEY_FILE_TYPE` must be one of:
`json`, `p12`.

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

: The option --key-file-type=p12 is available here only for legacy reasons; all
new use cases are encouraged to use the default 'json' format.
These variants are also available:

```
gcloud alpha iam service-accounts keys create
```

```
gcloud beta iam service-accounts keys create
```