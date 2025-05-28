# gcloud iam workforce-pools create-cred-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config)*

**NAME**

: **gcloud iam workforce-pools create-cred-config - create a configuration file for generated credentials**

**SYNOPSIS**

: **`gcloud iam workforce-pools create-cred-config` `[AUDIENCE](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#AUDIENCE)` `[--output-file](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--output-file)`=`OUTPUT_FILE` `[--workforce-pool-user-project](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--workforce-pool-user-project)`=`WORKFORCE_POOL_USER_PROJECT` (`[--credential-source-file](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--credential-source-file)`=`CREDENTIAL_SOURCE_FILE`     | `[--credential-source-url](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--credential-source-url)`=`CREDENTIAL_SOURCE_URL`     | `[--executable-command](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--executable-command)`=`EXECUTABLE_COMMAND`) [`[--credential-source-field-name](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--credential-source-field-name)`=`CREDENTIAL_SOURCE_FIELD_NAME`] [`[--credential-source-headers](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--credential-source-headers)`=[`key`=`value`,…]] [`[--credential-source-type](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--credential-source-type)`=`CREDENTIAL_SOURCE_TYPE`] [`[--subject-token-type](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--subject-token-type)`=`SUBJECT_TOKEN_TYPE`] [`[--executable-interactive-timeout-millis](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--executable-interactive-timeout-millis)`=`EXECUTABLE_INTERACTIVE_TIMEOUT_MILLIS` `[--executable-output-file](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--executable-output-file)`=`EXECUTABLE_OUTPUT_FILE` `[--executable-timeout-millis](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--executable-timeout-millis)`=`EXECUTABLE_TIMEOUT_MILLIS`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--service-account)`=`SERVICE_ACCOUNT` : `[--service-account-token-lifetime-seconds](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#--service-account-token-lifetime-seconds)`=`SERVICE_ACCOUNT_TOKEN_LIFETIME_SECONDS`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-cred-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command creates a configuration file to allow access to authenticated
Google Cloud actions from a variety of external user accounts.

**EXAMPLES**

: To create a file-sourced credential configuration for your project, run:

```
gcloud iam workforce-pools create-cred-config locations/$REGION/workforcePools/$WORKFORCE_POOL_ID/providers/$PROVIDER_ID --credential-source-file=$PATH_TO_OIDC_ID_TOKEN --workforce-pool-user-project=$PROJECT_NUMBER --output-file=credentials.json
```

To create a URL-sourced credential configuration for your project, run:

```
gcloud iam workforce-pools create-cred-config locations/$REGION/workforcePools/$WORKFORCE_POOL_ID/providers/$PROVIDER_ID --credential-source-url=$URL_FOR_OIDC_TOKEN --credential-source-headers=Key=Value --workforce-pool-user-project=$PROJECT_NUMBER --output-file=credentials.json
```

To create an executable-source credential configuration for your project, run
the following command:

```
gcloud iam workforce-pools create-cred-config locations/$REGION/workforcePools/$WORKFORCE_POOL_ID/providers/$PROVIDER_ID --executable-command=$EXECUTABLE_COMMAND --executable-timeout-millis=30000 --executable-output-file=$CACHE_FILE --workforce-pool-user-project=$PROJECT_NUMBER --output-file=credentials.json
```

To use the resulting file for any of these commands, set the
GOOGLE_APPLICATION_CREDENTIALS environment variable to point to the generated
file.

**POSITIONAL ARGUMENTS**

: **`AUDIENCE`**:
The workforce pool provider resource name.

**REQUIRED FLAGS**

: **--output-file**:
Location to store the generated credential configuration file.

**--workforce-pool-user-project**:
The client project number used to identify the application (client project) to
the server when calling Google APIs. The user principal must have
serviceusage.services.use IAM permission to use the specified project.

**--credential-source-file**

**OPTIONAL FLAGS**

: **--credential-source-field-name**:
Subject token field name (key) in a JSON credential source.

**--credential-source-headers**:
Headers to use when querying the credential-source-url.

**--credential-source-type**:
Format of the credential source (JSON or text).

**--subject-token-type**:
The type of token being used for authorization. This defaults to
urn:ietf:params:oauth:token-type:id_token.

**--executable-interactive-timeout-millis**

**--service-account**

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
gcloud alpha iam workforce-pools create-cred-config
```

```
gcloud beta iam workforce-pools create-cred-config
```