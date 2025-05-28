# gcloud ml speech recognize-long-running  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running)*

**NAME**

: **gcloud ml speech recognize-long-running - get transcripts of longer audio from an audio file**

**SYNOPSIS**

: **`gcloud ml speech recognize-long-running` `[AUDIO](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#AUDIO)` `[--language-code](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--language-code)`=`LANGUAGE_CODE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--async)`] [`[--enable-automatic-punctuation](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--enable-automatic-punctuation)`] [`[--encoding](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--encoding)`=`ENCODING`; default="encoding-unspecified"] [`[--filter-profanity](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--filter-profanity)`] [`[--hints](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--hints)`=[`HINT`,…]] [`[--include-word-time-offsets](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--include-word-time-offsets)`] [`[--max-alternatives](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--max-alternatives)`=`MAX_ALTERNATIVES`; default=1] [`[--model](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--model)`=`MODEL`] [`[--output-uri](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--output-uri)`=`OUTPUT_URI`] [`[--sample-rate](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--sample-rate)`=`SAMPLE_RATE`] [`[--audio-channel-count](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--audio-channel-count)`=`AUDIO_CHANNEL_COUNT` `[--separate-channel-recognition](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#--separate-channel-recognition)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get a transcript of audio up to 80 minutes in length. If the audio is under 60
seconds, you may also use `[gcloud ml speech
recognize](https://cloud.google.com/sdk/gcloud/reference/ml/speech/recognize)` to analyze it.

**EXAMPLES**

: To block the command from completing until analysis is finished, run:

```
gcloud ml speech recognize-long-running AUDIO_FILE --language-code=LANGUAGE_CODE --sample-rate=SAMPLE_RATE
```

You can also receive an operation as the result of the command by running:

```
gcloud ml speech recognize-long-running AUDIO_FILE --language-code=LANGUAGE_CODE --sample-rate=SAMPLE_RATE --async
```

This will return information about an operation. To get information about the
operation, run:

```
gcloud ml speech operations describe OPERATION_ID
```

To poll the operation until it's complete, run:

```
gcloud ml speech operations wait OPERATION_ID
```

**POSITIONAL ARGUMENTS**

: **`AUDIO`**:
The location of the audio file to transcribe. Must be a local path or a Google
Cloud Storage URL (in the format gs://bucket/object).

**REQUIRED FLAGS**

: **--language-code**:
The language of the supplied audio as a BCP-47
(https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US".
See [https://cloud.google.com/speech/docs/languages](https://cloud.google.com/speech/docs/languages)
for a list of the currently supported language codes.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--enable-automatic-punctuation**:
Adds punctuation to recognition result hypotheses.

**--encoding**:
The type of encoding of the file. Required if the file format is not WAV or
FLAC. `ENCODING` must be one of: `alaw`,
`amr`, `amr-wb`, `encoding-unspecified`,
`flac`, `linear16`, `mp3`, `mulaw`,
`ogg-opus`, `speex-with-header-byte`,
`webm-opus`.

**--filter-profanity**:
If True, the server will attempt to filter out profanities, replacing all but
the initial character in each filtered word with asterisks, e.g.
`f***`.

**--hints**:
A list of strings containing word and phrase "hints" so that the speech
recognition is more likely to recognize them. This can be used to improve the
accuracy for specific words and phrases, for example, if specific commands are
typically spoken by the user. This can also be used to add additional words to
the vocabulary of the recognizer. See [https://cloud.google.com/speech/limits#content](https://cloud.google.com/speech/limits#content).

**--include-word-time-offsets**:
If True, the top result includes a list of words with the start and end time
offsets (timestamps) for those words. If False, no word-level time offset
information is returned.

**--max-alternatives**:
Maximum number of recognition hypotheses to be returned. The server may return
fewer than max_alternatives. Valid values are 0-30. A value of 0 or 1 will
return a maximum of one.

**--model**:
Select the model best suited to your domain to get best results. If you do not
explicitly specify a model, Speech-to-Text will auto-select a model based on
your other specified parameters. Some models are premium and cost more than
standard models (although you can reduce the price by opting into
https://cloud.google.com/speech-to-text/docs/data-logging).
`MODEL` must be one of:

**`command_and_search`**:
short queries such as voice commands or voice search.

**`default`**:
audio that is not one of the specific audio models. For example, long-form
audio. Ideally the audio is high-fidelity, recorded at a 16khz or greater
sampling rate.

**`latest_long`**:
Use this model for any kind of long form content such as media or spontaneous
speech and conversations. Consider using this model in place of the video model,
especially if the video model is not available in your target language. You can
also use this in place of the default model.

**`latest_short`**:
Use this model for short utterances that are a few seconds in length. It is
useful for trying to capture commands or other single shot directed speech use
cases. Consider using this model instead of the command and search model.

**`medical_conversation`**:
Best for audio that originated from a conversation between a medical provider
and patient.

**`medical_dictation`**:
Best for audio that originated from dictation notes by a medical provider.

**`phone_call`**:
audio that originated from a phone call (typically recorded at an 8khz sampling
rate).

**`phone_call_enhanced`**:
audio that originated from a phone call (typically recorded at an 8khz sampling
rate). This is a premium model and can produce better results but costs more
than the standard rate.

**`telephony`**:
Improved version of the "phone_call" model, best for audio that originated from
a phone call, typically recorded at an 8kHz sampling rate.

**`telephony_short`**:
Dedicated version of the modern "telephony" model for short or even single-word
utterances for audio that originated from a phone call, typically recorded at an
8kHz sampling rate.

**`video_enhanced`**:
audio that originated from video or includes multiple speakers. Ideally the
audio is recorded at a 16khz or greater sampling rate. This is a premium model
that costs more than the standard rate.

**--output-uri**:
Location to which the results should be written. Must be a Google Cloud Storage
URI.

**--sample-rate**:
The sample rate in Hertz. For best results, set the sampling rate of the audio
source to 16000 Hz. If that's not possible, use the native sample rate of the
audio source (instead of re-sampling).

**--audio-channel-count**

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

: This command uses the speech/v1 API. The full documentation for this API can be
found at: [https://cloud.google.com/speech-to-text/docs/quickstart-protocol](https://cloud.google.com/speech-to-text/docs/quickstart-protocol)

**NOTES**

: These variants are also available:

```
gcloud alpha ml speech recognize-long-running
```

```
gcloud beta ml speech recognize-long-running
```