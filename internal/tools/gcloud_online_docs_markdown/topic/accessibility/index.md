# gcloud topic accessibility  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/topic/accessibility](https://cloud.google.com/sdk/gcloud/reference/topic/accessibility)*

**NAME**

: **gcloud topic accessibility - reference for `Accessibility` features**

**DESCRIPTION**

: The `accessibility/screen_reader` property when set to true will
change some behavior to make gcloud more screen reader friendly. Currently the
following changes are implemented:

- For progress trackers, instead of unicode spinners, the phrase 'working' is
displayed on stderr, every second while gcloud is working.
- For progress bars, progress is displayed as a percentage, outputted to stderr.
- For boxed tables, instead of the queried resources being displayed in tables
drawn in Unicode, results are rendered as a flattened list of items. Also
consider using the --format flag to define your own format.

To turn this on, run:

```
gcloud config set accessibility/screen_reader true
```

Accessibility support is still in early stages. Please report any issues that
you would like fixed using `[gcloud
feedback](https://cloud.google.com/sdk/gcloud/reference/feedback)`.

**NOTES**

: These variants are also available:

```
gcloud alpha topic accessibility
```

```
gcloud beta topic accessibility
```