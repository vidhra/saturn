# gcloud firebase test ios  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios)*

**NAME**

: **gcloud firebase test ios - command group for iOS application testing**

**SYNOPSIS**

: **`gcloud firebase test ios` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Explore physical iOS devices and iOS versions which are available as test
targets. Also run tests against your iOS app on these devices, monitor your test
progress, and view detailed test results in the Firebase console.

**EXAMPLES**

: To see a list of available iOS devices and supported iOS versions, run:

```
gcloud firebase test ios models list
```

To view information about a specific iOS model, run:

```
gcloud firebase test ios models describe MODEL_ID
```

To view details about all iOS versions, run:

```
gcloud firebase test ios versions list
```

To view information about a specific iOS version, run:

```
gcloud firebase test ios versions describe VERSION_ID
```

To view all options available for iOS tests, run:

```
gcloud firebase test ios run --help
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[locales](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/locales)`**:
Explore iOS locales available for testing.

**`[models](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models)`**:
Explore iOS models available in the Test Environment catalog.

**`[versions](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/versions)`**:
Explore iOS versions available for testing.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[list-device-capacities](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/list-device-capacities)`**:
List capacity information for iOS models & versions.

**`[run](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run)`**:
Invoke a test in Firebase Test Lab for iOS and view test results.

**NOTES**

: These variants are also available:

```
gcloud alpha firebase test ios
```

```
gcloud beta firebase test ios
```