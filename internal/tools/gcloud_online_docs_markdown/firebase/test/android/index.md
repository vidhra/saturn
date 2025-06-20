# gcloud firebase test android  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/android](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android)*

**NAME**

: **gcloud firebase test android - command group for Android application testing**

**SYNOPSIS**

: **`gcloud firebase test android` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Explore physical and virtual Android models, Android OS versions, and Android
locales which are available as test targets. Also run tests against your Android
app on these devices, monitor your test progress, and view detailed test results
in the Firebase console.

**EXAMPLES**

: To see a list of available Android devices, their form factors, and supported
Android OS versions, run:

```
gcloud firebase test android models list
```

To view more detailed information about a specific Android model, run:

```
gcloud firebase test android models describe MODEL_ID
```

To view details about available Android OS versions, such as their code names
and release dates, run:

```
gcloud firebase test android versions list
```

To view information about a specific Android OS version, run:

```
gcloud firebase test android versions describe VERSION_ID
```

To view the list of available Android locales which can be used for testing
internationalized applications, run:

```
gcloud firebase test android locales list
```

To view information about a specific locale, run:

```
gcloud firebase test android locales describe LOCALE
```

To view all options available for running Android tests, run:

```
gcloud firebase test android run --help
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[locales](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/locales)`**:
Explore Android locales available for testing.

**`[models](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models)`**:
Explore Android models available in the Test Environment catalog.

**`[versions](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions)`**:
Explore Android versions available for testing.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[list-device-capacities](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/list-device-capacities)`**:
List capacity information for Android models & versions.

**`[run](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run)`**:
Invoke a test in Firebase Test Lab for Android and view test results.

**NOTES**

: These variants are also available:

```
gcloud alpha firebase test android
```

```
gcloud beta firebase test android
```