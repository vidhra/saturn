# gcloud beta ai endpoints stream-raw-predict  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-raw-predict](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-raw-predict)*

**NAME**

: **gcloud beta ai endpoints stream-raw-predict - run Vertex AI online stream raw prediction**

**SYNOPSIS**

: **`gcloud beta ai endpoints stream-raw-predict` (`[ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-raw-predict#ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-raw-predict#--region)`=`REGION`) `[--request](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-raw-predict#--request)`=`REQUEST` [`[--http-headers](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-raw-predict#--http-headers)`=[`HEADER`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-raw-predict#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` `gcloud beta ai endpoints stream-raw-predict`
sends a stream raw prediction request to a Vertex AI endpoint. The request can
be given on the command line or read from a file or stdin.

**EXAMPLES**

: To predict against an endpoint ``123`` under
project ``example`` in region
``us-central1``, reading the request from the
command line, run:

```
gcloud beta ai endpoints stream-raw-predict 123 --project=example --region=us-central1 --request='{
    "instances": [
      { "values": [1, 2, 3, 4], "key": 1 },
      { "values": [5, 6, 7, 8], "key": 2 }
    ]
  }'
```

If the request body was in the file
``input.json``, run:

```
gcloud beta ai endpoints stream-raw-predict 123 --project=example --region=us-central1 --request=@input.json
```

To send the image file ``image.jpeg`` and set
the `content type`, run:

```
gcloud beta ai endpoints stream-raw-predict 123 --project=example --region=us-central1 --http-headers=Content-Type=image/jpeg --request=@image.jpeg
```

**POSITIONAL ARGUMENTS**

: **Endpoint resource - The endpoint to do online stream raw prediction. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENDPOINT`**:
ID of the endpoint or fully qualified identifier for the endpoint.
To set the `name` attribute:

- provide the argument `endpoint` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the endpoint.
To set the `region` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**REQUIRED FLAGS**

: **--request**:
The request to send to the endpoint.
If the request starts with the letter '`@`', the rest should be a
file name to read the request from, or '`@-`' to read from
`stdin`. If the request body actually starts with '`@`',
it must be placed in a file.
If required, the `Content-Type` header should also be set
appropriately, particularly for binary data.

**OPTIONAL FLAGS**

: **--http-headers**:
List of header and value pairs to send as part of the request. For example, to
set the `Content-Type` and `X-Header`:

```
--http-headers=Content-Type="application/json",X-Header=Value
```

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
gcloud ai endpoints stream-raw-predict
```

```
gcloud alpha ai endpoints stream-raw-predict
```