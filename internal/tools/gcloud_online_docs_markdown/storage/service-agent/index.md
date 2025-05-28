# gcloud storage service-agent  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/service-agent](https://cloud.google.com/sdk/gcloud/reference/storage/service-agent)*

**NAME**

: **gcloud storage service-agent - manage a project's Cloud Storage service agent, which is used to perform Cloud KMS operations**

**SYNOPSIS**

: **`gcloud storage service-agent` [`[--authorize-cmek](https://cloud.google.com/sdk/gcloud/reference/storage/service-agent#--authorize-cmek)`=`AUTHORIZE_CMEK`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/service-agent#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage service-agent` displays the Cloud Storage service
agent, which is used to perform Cloud KMS operations against your a default or
supplied project. If the project does not yet have a service agent, `gcloud
storage service-agent` creates one.

**EXAMPLES**

: To show the service agent for your default project:

```
gcloud storage service-agent
```

To show the service account for ``my-project``:

```
gcloud storage service-agent --project=my-project
```

To authorize your default project to use a Cloud KMS key:

```
gcloud storage service-agent --authorize-cmek=projects/key-project/locations/us-east1/keyRings/key-ring/cryptoKeys/my-key
```

**FLAGS**

: **--authorize-cmek**:
Adds appropriate encrypt/decrypt permissions to the specified Cloud KMS key.
This allows the Cloud Storage service agent to write and read Cloud
KMS-encrypted objects in buckets associated with the service agent's project.

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
gcloud alpha storage service-agent
```