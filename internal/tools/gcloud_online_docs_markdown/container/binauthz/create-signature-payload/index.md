# gcloud container binauthz create-signature-payload  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/binauthz/create-signature-payload](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/create-signature-payload)*

**NAME**

: **gcloud container binauthz create-signature-payload - create a JSON container image signature object**

**SYNOPSIS**

: **`gcloud container binauthz create-signature-payload` `[--artifact-url](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/create-signature-payload#--artifact-url)`=`ARTIFACT_URL` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/binauthz/create-signature-payload#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Given a container image URL specified by the manifest digest, this command will
produce a JSON object whose signature is expected by Cloud Binary Authorization.

**EXAMPLES**

: To output serialized JSON to sign, run:

```
gcloud container binauthz create-signature-payload --artifact-url="gcr.io/example-project/example-image@sha256:abcd"
```

**REQUIRED FLAGS**

: **--artifact-url**:
Container URL. May be in the `gcr.io/repository/image` format, or may
optionally contain the `http` or `https` scheme

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
gcloud alpha container binauthz create-signature-payload
```

```
gcloud beta container binauthz create-signature-payload
```