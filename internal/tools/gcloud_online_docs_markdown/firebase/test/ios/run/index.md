# gcloud firebase test ios run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run)*

**NAME**

: **gcloud firebase test ios run - invoke a test in Firebase Test Lab for iOS and view test results**

**SYNOPSIS**

: **`gcloud firebase test ios run` [`[ARGSPEC](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#ARGSPEC)`] [`[--device](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--device)`=`DIMENSION`=`VALUE`,[…]] [`[--test](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--test)`=`XCTEST_ZIP`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--timeout)`=`TIMEOUT`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--type)`=`TYPE`] [`[--xcode-version](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--xcode-version)`=`XCODE_VERSION`] [`[--xctestrun-file](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--xctestrun-file)`=`XCTESTRUN_FILE`] [`[--app](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--app)`=`APP`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--async)`] [`[--client-details](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--client-details)`=[`KEY`=`VALUE`,…]] [`[--num-flaky-test-attempts](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--num-flaky-test-attempts)`=`int`] [`[--record-video](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--record-video)`] [`[--results-bucket](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--results-bucket)`=`RESULTS_BUCKET`] [`[--results-dir](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--results-dir)`=`RESULTS_DIR`] [`[--results-history-name](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--results-history-name)`=`RESULTS_HISTORY_NAME`] [`[--test-special-entitlements](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--test-special-entitlements)`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud firebase test ios run` invokes and monitors tests in Firebase
Test Lab for iOS.
The currently supported iOS test frameworks are XCTest and XCUITest. Other iOS
testing frameworks which are built upon XCTest and XCUITest should also work.
The XCTEST_ZIP test package is a zip file built using Apple's Xcode and
supporting tools. For a detailed description of the process to create your
XCTEST_ZIP file, see [https://firebase.google.com/docs/test-lab/ios/command-line](https://firebase.google.com/docs/test-lab/ios/command-line).
All arguments for `gcloud firebase test ios run` may be specified on
the command line and/or within an argument file. Run `$ [gcloud topic arg-files](https://cloud.google.com/sdk/gcloud/reference/topic/arg-files)`
for more information about argument files.

**EXAMPLES**

: To invoke an XCTest lasting up to five minutes against the default device
environment, run:

```
gcloud firebase test ios run --test=XCTEST_ZIP --timeout=5m
```

To invoke an XCTest against an iPad 5 running iOS 11.2, run:

```
gcloud firebase test ios run --test=XCTEST_ZIP --device=model=ipad5,version=11.2
```

To run your tests against multiple iOS devices simultaneously, specify the
`--device` flag more than once:

```
gcloud firebase test ios run --test=XCTEST_ZIP --device=model=iphone7 --device=model=ipadmini4,version=11.2 --device=model=iphonese
```

To run your XCTest using a specific version of Xcode, say 9.4.1, run:

```
gcloud firebase test ios run --test=XCTEST_ZIP --xcode-version=9.4.1
```

To help you identify and locate your test matrix in the Firebase console, run:

```
gcloud firebase test ios run --test=XCTEST_ZIP --client-details=matrixLabel="Example matrix label"
```

All test arguments for a given test may alternatively be stored in an argument
group within a YAML-formatted argument file. The
`ARG_FILE` may contain one or more named argument groups,
and argument groups may be combined using the `include:` attribute
(Run `$ [gcloud topic](https://cloud.google.com/sdk/gcloud/reference/topic)
arg-files` for more information). The ARG_FILE can easily be shared with
colleagues or placed under source control to ensure consistent test executions.
To run a test using arguments loaded from an ARG_FILE named
`excelsior_app_args`, which contains an argument group named
`ios-args:`, use the following syntax:

```
gcloud firebase test ios run path/to/excelsior_app_args:ios-args
```

**POSITIONAL ARGUMENTS**

: **[`ARGSPEC`]**:
An ARG_FILE:ARG_GROUP_NAME pair, where ARG_FILE is the path to a file containing
groups of test arguments in yaml format, and ARG_GROUP_NAME is the particular
yaml object holding a group of arg:value pairs to use. Run `$ [gcloud topic arg-files](https://cloud.google.com/sdk/gcloud/reference/topic/arg-files)`
for more information and examples.

**COMMONLY USED FLAGS**

: **--device**:
A list of ``DIMENSION=VALUE`` pairs which
specify a target device to test against. This flag may be repeated to specify
multiple devices. The device dimensions are: `model`,
`version`, `locale`, and `orientation`. If any
dimensions are omitted, they will use a default value. The default value, and
all possible values, for each dimension can be found with the
``list`` command for that dimension, such as
`$ [gcloud firebase
test ios models](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/models) list`. Omitting this flag entirely will run tests
against a single device using defaults for every dimension.
Examples:

```
--device model=iphone8plus
--device version=11.2
--device model=ipadmini4,version=11.2,locale=zh_CN,orientation=landscape
```

**--test**:
The path to the test package (a zip file containing the iOS app and XCTest
files). The given path may be in the local filesystem or in Google Cloud Storage
using a URL beginning with `gs://`. Note: any .xctestrun file in this
zip file will be ignored if `--xctestrun-file` is specified.

**--timeout**:
The max time this test execution can run before it is cancelled (default: 15m).
It does not include any time necessary to prepare and clean up the target
device. The maximum possible testing time is 45m on physical devices and 60m on
virtual devices. The `TIMEOUT` units can be h, m, or s. If
no unit is given, seconds are assumed. Examples:

- `--timeout 1h` is 1 hour
- `--timeout 5m` is 5 minutes
- `--timeout 200s` is 200 seconds
- `--timeout 100` is 100 seconds

**--type**:
The type of iOS test to run. `TYPE` must be one of:
`xctest`, `game-loop`, `robo`.

**--xcode-version**:
The version of Xcode that should be used to run an XCTest. Defaults to the
latest Xcode version supported in Firebase Test Lab. This Xcode version must be
supported by all iOS versions selected in the test matrix. The list of Xcode
versions supported by each version of iOS can be viewed by running `$ [gcloud firebase
test ios versions list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/ios/versions/list)`.

**--xctestrun-file**:
The path to an .xctestrun file that will override any .xctestrun file contained
in the `--test` package. Because the .xctestrun file contains
environment variables along with test methods to run and/or ignore, this can be
useful for customizing or sharding test suites. The given path may be in the
local filesystem or in Google Cloud Storage using a URL beginning with
`gs://`.

**FLAGS**

: **--app**:
The path to the application archive (.ipa file) for game-loop testing. The path
may be in the local filesystem or in Google Cloud Storage using gs:// notation.
This flag is only valid when `--type` is `game-loop` or
`robo`.

**--async**:
Invoke a test asynchronously without waiting for test results.

**--client-details**:
Comma-separated, KEY=VALUE map of additional details to attach to the test
matrix. Arbitrary KEY=VALUE pairs may be attached to a test matrix to provide
additional context about the tests being run. When consuming the test results,
such as in Cloud Functions or a CI system, these details can add additional
context such as a link to the corresponding pull request.
Example:

```
--client-details=buildNumber=1234,pullRequest=https://example.com/link/to/pull-request
```

To help you identify and locate your test matrix in the Firebase console, use
the matrixLabel key.
Example:

```
--client-details=matrixLabel="Example matrix label"
```

**--num-flaky-test-attempts**:
Specifies the number of times a test execution should be reattempted if one or
more of its test cases fail for any reason. An execution that initially fails
but succeeds on any reattempt is reported as FLAKY.
The maximum number of reruns allowed is 10. (Default: 0, which implies no
reruns.) All additional attempts are executed in parallel.

**--record-video**:
Enable video recording during the test. Enabled by default, use
--no-record-video to disable.

**--results-bucket**:
The name of a Google Cloud Storage bucket where raw test results will be stored
(default: "test-lab-<random-UUID>"). Note that the bucket must be owned by
a billing-enabled project, and that using a non-default bucket will result in
billing charges for the storage used.

**--results-dir**:
The name of a `unique` Google Cloud Storage object within the results
bucket where raw test results will be stored (default: a timestamp with a random
suffix). Caution: if specified, this argument `must be unique` for
each test matrix you create, otherwise results from multiple test matrices will
be overwritten or intermingled.

**--results-history-name**:
The history name for your test results (an arbitrary string label; default: the
bundle ID for the iOS application). All tests which use the same history name
will have their results grouped together in the Firebase console in a
time-ordered test history list.

**--test-special-entitlements**:
Enables testing special app entitlements. Re-signs an app having special
entitlements with a new application-identifier. This currently supports testing
Push Notifications (aps-environment) entitlement for up to one app in a project.
Note: Because this changes the app's identifier, make sure none of the resources
in your zip file contain direct references to the test app's bundle id.

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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

: These variants are also available:

```
gcloud alpha firebase test ios run
```

```
gcloud beta firebase test ios run
```