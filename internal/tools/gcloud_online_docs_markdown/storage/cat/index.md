# gcloud storage cat  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/storage/cat](https://cloud.google.com/sdk/gcloud/reference/storage/cat)*

**NAME**

: **gcloud storage cat - outputs the contents of one or more URLs to stdout**

**SYNOPSIS**

: **`gcloud storage cat` `[URL](https://cloud.google.com/sdk/gcloud/reference/storage/cat#URL)` [`[URL](https://cloud.google.com/sdk/gcloud/reference/storage/cat#URL)` …] [`[--additional-headers](https://cloud.google.com/sdk/gcloud/reference/storage/cat#--additional-headers)`=`HEADER`=`VALUE`] [`[--display-url](https://cloud.google.com/sdk/gcloud/reference/storage/cat#--display-url)`, `[-d](https://cloud.google.com/sdk/gcloud/reference/storage/cat#-d)`] [`[--range](https://cloud.google.com/sdk/gcloud/reference/storage/cat#--range)`=`RANGE`, `[-r](https://cloud.google.com/sdk/gcloud/reference/storage/cat#-r)` `[RANGE](https://cloud.google.com/sdk/gcloud/reference/storage/cat#RANGE)`] [`[--decryption-keys](https://cloud.google.com/sdk/gcloud/reference/storage/cat#--decryption-keys)`=[`DECRYPTION_KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/storage/cat#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The cat command outputs the contents of one or more URLs to stdout. While the
cat command does not compute a checksum, it is otherwise equivalent to doing:

```
gcloud storage cp url… -
```

(The final '-' causes gcloud to stream the output to stdout.)

**EXAMPLES**

: The following command writes all text files in a bucket to stdout:

```
gcloud storage cat gs://bucket/*.txt
```

The following command outputs a short header describing file.txt, along with its
contents:

```
gcloud storage cat -d gs://my-bucket/file.txt
```

The following command outputs bytes 256-939 of file.txt:

```
gcloud storage cat -r 256-939 gs://my-bucket/file.txt
```

The following command outputs the last 5 bytes of file.txt:

```
gcloud storage cat -r -5 gs://my-bucket/file.txt
```

**POSITIONAL ARGUMENTS**

: **`URL` [`URL` …]**:
The url of objects to list.

**FLAGS**

: **--additional-headers**:
Includes arbitrary headers in storage API calls. Accepts a comma separated list
of key=value pairs, e.g. `header1=value1,header2=value2`. Overrides
the default `storage/additional_headers` property value for this
command invocation.

**--display-url**:
Prints the header before each object.

**--range**:
Causes gcloud storage to output just the specified byte range of the object. In
a case where "start" = 'x', and "end" = 'y', ranges take the form:
`x-y` (e.g., `-r 256-5939`), `x-` (e.g.,
`-r 256-`), `-y` (e.g., `-r -5`)
When offsets start at 0, x-y means to return bytes x through y (inclusive), x-
means to return bytes x through the end of the object, and -y changes the role
of y. If -y is present, then it returns the last y bytes of the object.
If the bytes are out of range of the object, then nothing is printed

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
gcloud alpha storage cat
```