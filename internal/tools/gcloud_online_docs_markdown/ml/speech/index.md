# gcloud ml speech  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/speech](https://cloud.google.com/sdk/gcloud/reference/ml/speech)*

**NAME**

: **gcloud ml speech - use Google Cloud Speech to get transcripts of audio**

**SYNOPSIS**

: **`gcloud ml speech` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/ml/speech#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/ml/speech#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/speech#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Use Google Cloud Speech to get transcripts of recorded audio, and to get
information about long-running speech recognition operations. For audio under 60
seconds, use:

```
gcloud ml speech recognize
```

For audio 60 seconds or longer, use:

```
gcloud ml speech recognize-long-running
```

For more information about the Google Cloud Speech API, refer to this guide: [https://cloud.google.com/speech/docs/](https://cloud.google.com/speech/docs/)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[operations](https://cloud.google.com/sdk/gcloud/reference/ml/speech/operations)`**:
Interact with Google Cloud Speech operations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[recognize](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize)`**:
Get transcripts of short (less than 60 seconds) audio from an audio file.

**`[recognize-long-running](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running)`**:
Get transcripts of longer audio from an audio file.

**NOTES**

: These variants are also available:

```
gcloud alpha ml speech
```

```
gcloud beta ml speech
```