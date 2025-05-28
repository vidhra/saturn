# gcloud storage sign-url  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/sign-url](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url)*

**NAME**

: **gcloud storage sign-url - generate a URL with embedded authentication that can be used by anyone**

**SYNOPSIS**

: **`gcloud storage sign-url` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#URL)` [`[URL](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#URL)` …] [`[--duration](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#--duration)`=`DURATION`, `[-d](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#-d)` `[DURATION](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#DURATION)`; default=3600] [`[--headers](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#--headers)`=[`KEY`=`VALUE`,…]] [`[--http-verb](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#--http-verb)`=`HTTP_VERB`, `[-m](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#-m)` `[HTTP_VERB](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#HTTP_VERB)`; default="GET"] [`[--private-key-file](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#--private-key-file)`=`PRIVATE_KEY_FILE`] [`[--private-key-password](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#--private-key-password)`=`PRIVATE_KEY_PASSWORD`, `[-p](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#-p)` `[PRIVATE_KEY_PASSWORD](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#PRIVATE_KEY_PASSWORD)`] [`[--query-params](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#--query-params)`=[`KEY`=`VALUE`,…]] [`[--region](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#--region)`=`REGION`, `[-r](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#-r)` `[REGION](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#REGION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/sign-url#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud storage sign-url` will generate a signed URL that embeds
authentication data so the URL can be used by someone who does not have a Google
account. Use the global
``--impersonate-service-account`` flag to
specify the service account that will be used to sign the specified URL or
authenticate with a service account directly. Otherwise, a service account key
is required. Please see the [Signed
URLs documentation](https://cloud.google.com/storage/docs/access-control/signed-urls) for background about signed URLs.
Note, `gcloud storage sign-url` does not support operations on
sub-directories. For example, unless you have an object named
`some-directory/` stored inside the bucket `some-bucket`,
the following command returns an error: `gcloud storage sign-url
gs://some-bucket/some-directory/`.

**EXAMPLES**

: To create a signed url for downloading an object valid for 10 minutes with the
credentials of an impersonated service account:

```
gcloud storage sign-url gs://my-bucket/file.txt --duration=10m --impersonate-service-account=sa@my-project.iam.gserviceaccount.com
```

To create a signed url that will bill to my-billing-project when already
authenticated as a service account:

```
gcloud storage sign-url gs://my-bucket/file.txt --query-params=userProject=my-billing-project
```

To create a signed url, valid for one hour, for uploading a plain text file via
HTTP PUT:

```
gcloud storage sign-url gs://my-bucket/file.txt --http-verb=PUT --duration=1h --headers=content-type=text/plain --impersonate-service-account=sa@my-project.iam.gserviceaccount.com
```

To create a signed URL that initiates a resumable upload for a plain text file
using a private key file:

```
gcloud storage sign-url gs://my-bucket/file.txt --http-verb=POST --headers=x-goog-resumable=start,content-type=text/plain --private-key-file=key.json
```

**POSITIONAL ARGUMENTS**

: **`URL` [`URL` …]**:
The URLs to be signed. May contain wildcards.

**FLAGS**

: **--duration**:
Specifies the duration that the signed url should be valid for, default duration
is 1 hour. For example 10s for 10 seconds. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.
The max duration allowed is 12 hours. This limitation exists because the
system-managed key used to sign the URL may not remain valid after 12 hours.
Alternatively, the max duration allowed is 7 days when signing with either the
``--private-key-file`` flag or an account that
authorized with ``gcloud auth
activate-service-account``.

**--headers**:
Specifies the headers to be used in the signed request. Possible headers are
listed in the XML API's documentation: [https://cloud.google.com/storage/docs/xml-api/reference-headers#headers](https://cloud.google.com/storage/docs/xml-api/reference-headers#headers)

**--http-verb**:
Specifies the HTTP verb to be authorized for use with the signed URL, default is
GET. When using a signed URL to start a resumable upload session, you will need
to specify the ``x-goog-resumable:start``
header in the request or else signature validation will fail.

**--private-key-file**:
The service account private key used to generate the cryptographic signature for
the generated URL. Must be in PKCS12 or JSON format. If encrypted, will prompt
for the passphrase used to protect the private key file (default
``notasecret``).
Note: Service account keys are a security risk if not managed correctly. Review
[best
practices for managing service account keys](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys) before using this option.

**--private-key-password**:
Specifies the PRIVATE_KEY_FILE password instead of prompting.

**--query-params**:
Specifies the query parameters to be used in the signed request. Possible query
parameters are listed in the XML API's documentation: [https://cloud.google.com/storage/docs/xml-api/reference-headers#query](https://cloud.google.com/storage/docs/xml-api/reference-headers#query)

**--region**:
Specifies the region in which the resources for which you are creating signed
URLs are stored.
Default value is ``auto`` which will cause
gcloud storage sign-url to fetch the region for the resource. When
auto-detecting the region, the current user's credentials, not the credentials
from PRIVATE_KEY_FILE, are used to fetch the bucket's metadata.

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
gcloud alpha storage sign-url
```