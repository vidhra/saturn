# gcloud transcoder jobs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create)*

**NAME**

: **gcloud transcoder jobs create - create Transcoder jobs**

**SYNOPSIS**

: **`gcloud transcoder jobs create` [`[--batch-mode-priority](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#--batch-mode-priority)`=`BATCH_MODE_PRIORITY`] [`[--input-uri](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#--input-uri)`=`INPUT_URI`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#--location)`=`LOCATION`] [`[--mode](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#--mode)`=`MODE`] [`[--optimization](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#--optimization)`=`OPTIMIZATION`] [`[--output-uri](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#--output-uri)`=`OUTPUT_URI`] [`[--file](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#--file)`=`FILE`     | `[--json](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#--json)`=`JSON`     | `[--template-id](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#--template-id)`=`TEMPLATE_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transcoder/jobs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create Transcoder jobs.

**EXAMPLES**

: To create a transcoder job with default template, input URI, and output URI:

```
gcloud transcoder jobs create --location=us-central1 --input-uri="gs://bucket/input.mp4" --output-uri="gs://bucket/output/"
```

To create a transcoder job with template id, input URI, and output URI:

```
gcloud transcoder jobs create --location=us-central1 --input-uri="gs://bucket/input.mp4" --output-uri="gs://bucket/output/" --template-id=my-template
```

To create a transcoder job with json format configuration:

```
gcloud transcoder jobs create --location=us-central1 --json="config: json-format"
```

To create a transcoder job with json format configuration file:

```
gcloud transcoder jobs create --location=us-central1 --file="config.json"
```

To create a transcoder job with labels:

```
gcloud transcoder jobs create --location=us-central1 --file="config.json" --labels=key=value
```

To create a transcoder job in batch mode:

```
gcloud transcoder jobs create --location=us-central1 --file="config.json" --mode=PROCESSING_MODE_BATCH
```

To create a transcoder job in batch mode with priority:

```
gcloud transcoder jobs create --location=us-central1 --file="config.json" --mode=PROCESSING_MODE_BATCH --batch-mode-priority=3
```

To create a transcoder job with optimizations disabled:

```
gcloud transcoder jobs create --location=us-central1 --file="config.json" --optimization=DISABLED
```

**FLAGS**

: **--batch-mode-priority**:
Processing priority of a batch mode transcoder job. This value will override
batch mode priority in job config.

**--input-uri**:
Google Cloud Storage URI. This value will override input URI in job config.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**Location resource - Transcoder location This represents a Cloud resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- set the property `transcoder/location` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line;
- set the property `transcoder/location`.**

**--mode**:
Processing mode of transcode job. This value will override mode in job config.
`MODE` must be one of:
`PROCESSING_MODE_INTERACTIVE`, `PROCESSING_MODE_BATCH`.

**--optimization**:
Optimization strategy of transcode job. This value will override optimization in
job config. `OPTIMIZATION` must be one of:
`AUTODETECT`, `DISABLED`.

**--output-uri**:
Google Cloud Storage directory URI (followed by a trailing forward slash). This
value will override output URI in job config.

**--file**

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