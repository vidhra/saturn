# gcloud storage objects describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/objects/describe](https://cloud.google.com/sdk/gcloud/reference/storage/objects/describe)*

**NAME**

: **gcloud storage objects describe - describe a Cloud Storage object**

**SYNOPSIS**

: **`gcloud storage objects describe` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/objects/describe#URL)` [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/objects/describe#--additional-headers)`=`HEADER`=`VALUE`] [`[--fetch-encrypted-object-hashes](https://cloud.google.com/sdk/gcloud/reference/storage/objects/describe#--fetch-encrypted-object-hashes)`] [`[--raw](https://cloud.google.com/sdk/gcloud/reference/storage/objects/describe#--raw)`] [`[--soft-deleted](https://cloud.google.com/sdk/gcloud/reference/storage/objects/describe#--soft-deleted)`] [`[--decryption-keys](https://cloud.google.com/sdk/gcloud/reference/storage/objects/describe#--decryption-keys)`=[`DECRYPTION_KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/objects/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Cloud Storage object.

**EXAMPLES**

: Describe a Google Cloud Storage object with the url "gs://bucket/my-object":

```
gcloud storage objects describe gs://bucket/my-object
```

Describe object with JSON formatting, only returning the "name" key:

```
gcloud storage objects describe gs://bucket/my-object --format="json(name)"
```

**POSITIONAL ARGUMENTS**

: **`URL`**:
Specifies URL of object to describe.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--fetch-encrypted-object-hashes**:
If the initial GET request returns an object encrypted with a customer-supplied
encryption key, the hash fields will be null. If the matching decryption key is
present on the system, this flag retries the GET request with the key.

**--raw**:
Shows metadata in the format returned by the API instead of standardizing it.

**--soft-deleted**:
Displays soft-deleted resources only. For objects, it will exclude live and
noncurrent ones.

**ENCRYPTION FLAGS**

: **--decryption-keys**:
A comma-separated list of customer-supplied encryption keys (RFC 4648 section 4
base64-encoded AES256 strings) that will be used to decrypt Cloud Storage
objects. Data encrypted with a customer-managed encryption key (CMEK) is
decrypted automatically, so CMEKs do not need to be listed here.

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
gcloud alpha storage objects describe
```