# gcloud compute sign-url  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/sign-url](https://cloud.google.com/sdk/gcloud/reference/compute/sign-url)*

**NAME**

: **gcloud compute sign-url - sign specified URL for use with Cloud CDN Signed URLs**

**SYNOPSIS**

: **`gcloud compute sign-url` `[URL](https://cloud.google.com/sdk/gcloud/reference/compute/sign-url#URL)` `[--expires-in](https://cloud.google.com/sdk/gcloud/reference/compute/sign-url#--expires-in)`=`EXPIRES_IN` `[--key-file](https://cloud.google.com/sdk/gcloud/reference/compute/sign-url#--key-file)`=`LOCAL_FILE_PATH` `[--key-name](https://cloud.google.com/sdk/gcloud/reference/compute/sign-url#--key-name)`=`KEY_NAME` [`[--validate](https://cloud.google.com/sdk/gcloud/reference/compute/sign-url#--validate)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/sign-url#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute sign-url` generates a signed URL for the specified
URL and optionally validates the response by sending a request to the signed
URL.
Cloud CDN Signed URLs give you a way to serve responses from the globally
distributed CDN cache, even if the request needs to be authorized.
Signed URLs are a mechanism to temporarily give a client access to a private
resource without requiring additional authorization. To achieve this, the full
request URL that should be allowed is hashed and cryptographically signed. By
using the signed URL you give it, that one request will be considered authorized
to receive the requested content.
Generally, a signed URL can be used by anyone who has it. However, it is usually
only intended to be used by the client that was directly given the URL. To
mitigate this, they expire at a time chosen by the issuer. To minimize the risk
of a signed URL being shared, it is recommended that the signed URL be set to
expire as soon as possible.
A 128-bit secret key is used for signing the URLs.
The URLs to sign have the following restrictions:

- The URL scheme must be either HTTP or HTTPS.
- The URLs must not contain the query parameters: `Expires`,
`KeyName` or `Signature`, since they are used for signing.
- The URL must not have a fragment.

**POSITIONAL ARGUMENTS**

: **`URL`**:
The URL to sign.

**REQUIRED FLAGS**

: **--expires-in**:
The duration for which the signed URL will be valid. For example, specifying
`12h` will cause the signed URL to be valid up to 12 hours. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--key-file**:
The file containing the RFC 4648 Section 5 base64url encoded 128-bit secret key
for Cloud CDN Signed URL. It is vital that the key is strongly random. One way
to generate such a key is with the following command:

```
head -c 16 /dev/random | base64 | tr +/ -_ > [KEY_FILE_NAME]
```

**--key-name**:
Name of the Cloud CDN Signed URL key.

**OPTIONAL FLAGS**

: **--validate**:
If provided, validates the generated signed URL by sending a HEAD request and
prints out the HTTP response code.
If the signed URL is valid, the result should be the same as the response code
sent by the backend. If it isn't, recheck the key name and the contents of the
key file, and ensure that expires-in is set to at least several seconds and that
the clock on the computer running this command is accurate.
If not provided, the generated signed URL is not verified.

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
gcloud alpha compute sign-url
```

```
gcloud beta compute sign-url
```