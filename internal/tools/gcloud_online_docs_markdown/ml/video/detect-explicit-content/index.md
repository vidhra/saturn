# gcloud ml video detect-explicit-content  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/video/detect-explicit-content](https://cloud.google.com/sdk/gcloud/reference/ml/video/detect-explicit-content)*

**NAME**

: **gcloud ml video detect-explicit-content - detect explicit content in videos**

**SYNOPSIS**

: **`gcloud ml video detect-explicit-content` `[INPUT_PATH](https://cloud.google.com/sdk/gcloud/reference/ml/video/detect-explicit-content#INPUT_PATH)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/ml/video/detect-explicit-content#--async)`] [`[--output-uri](https://cloud.google.com/sdk/gcloud/reference/ml/video/detect-explicit-content#--output-uri)`=`OUTPUT_URI`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/ml/video/detect-explicit-content#--region)`=`REGION`] [`[--segments](https://cloud.google.com/sdk/gcloud/reference/ml/video/detect-explicit-content#--segments)`=[`SEGMENTS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/video/detect-explicit-content#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Detect adult content within a video. Adult content is content generally
appropriate for 18 years of age and older, including but not limited to nudity,
sexual activities, and pornography (including cartoons or anime).
The response includes a bucketized likelihood value, from VERY_UNLIKELY to
VERY_LIKELY. When Explicit Content Detection evaluates a video, it does so on a
per-frame basis and considers visual content only (not audio).

**EXAMPLES**

: To detect explicit content in a video file named
'gs://my_bucket/input_file.mp4', run the following command.:

```
gcloud ml video detect-explicit-content gs://my_bucket/input_file.mp4
```

**POSITIONAL ARGUMENTS**

: **`INPUT_PATH`**:
Path to the video to be analyzed. Must be a local path or a Google Cloud Storage
URI.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--output-uri**:
Location to which the results should be written. Must be a Google Cloud Storage
URI.

**--region**:
Optional Cloud region where annotation should take place. If no region is
specified, a region will be determined based on video file location.
`REGION` must be one of: `asia-east1`,
`europe-west1`, `us-east1`, `us-west1`.

**--segments**:
Segments from the video which you want to analyze (by default, the entire video
will be treated as one segment). Must be in the format
START1:END1[,START2:END2,…] (inclusive). START and END of segments must
be a properly formatted duration string of the form `HhMmSs` where:

```
*  H is the number of hours from beginning of video
*  M is the number of minutes from the beginning of video
*  S is the number of seconds from the beginning of the video
```

H, M and S can be specified as ints or floats for fractional units (to
microsecond resolution). Unit chars (e.g. `h`, `m` or
`s`) are required. Microseconds can be specified using fractional
seconds e.g. 0.000569s == 569 microseconds.
Examples:
0s:23.554048s,24s:29.528064s
0:1m40s,3m50s:5m10.232265s

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

**API REFERENCE**

: This command uses the `videointelligence/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/video-intelligence/docs/](https://cloud.google.com/video-intelligence/docs/)

**NOTES**

: These variants are also available:

```
gcloud alpha ml video detect-explicit-content
```

```
gcloud beta ml video detect-explicit-content
```