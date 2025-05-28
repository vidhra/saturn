# gcloud firebase test android run  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run)*

**NAME**

: **gcloud firebase test android run - invoke a test in Firebase Test Lab for Android and view test results**

**SYNOPSIS**

: **`gcloud firebase test android run` [`[ARGSPEC](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#ARGSPEC)`] [`[--app](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--app)`=`APP`] [`[--device](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--device)`=`DIMENSION`=`VALUE`,[…]] [`[--test](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--test)`=`TEST`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--timeout)`=`TIMEOUT`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--type)`=`TYPE`] [`[--additional-apks](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--additional-apks)`=`APK`,[`[APK](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#APK)`,…]] [`[--app-package](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--app-package)`=`APP_PACKAGE`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--async)`] [`[--auto-google-login](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--auto-google-login)`] [`[--client-details](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--client-details)`=[`KEY`=`VALUE`,…]] [`[--directories-to-pull](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--directories-to-pull)`=[`DIR_TO_PULL`,…]] [`[--environment-variables](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--environment-variables)`=[`KEY`=`VALUE`,…]] [`[--network-profile](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--network-profile)`=`PROFILE_ID`] [`[--num-flaky-test-attempts](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--num-flaky-test-attempts)`=`int`] [`[--obb-files](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--obb-files)`=`OBB_FILE`,[`[OBB_FILE](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#OBB_FILE)`]] [`[--other-files](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--other-files)`=`DEVICE_PATH`=`FILE_PATH`,[…]] [`[--performance-metrics](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--performance-metrics)`] [`[--record-video](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--record-video)`] [`[--results-bucket](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--results-bucket)`=`RESULTS_BUCKET`] [`[--results-dir](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--results-dir)`=`RESULTS_DIR`] [`[--results-history-name](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--results-history-name)`=`RESULTS_HISTORY_NAME`] [`[--scenario-labels](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--scenario-labels)`=`LABEL`,[`[LABEL](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#LABEL)`,…]] [`[--scenario-numbers](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--scenario-numbers)`=`int`,[`int`,…]] [`[--test-package](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--test-package)`=`TEST_PACKAGE`] [`[--test-runner-class](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--test-runner-class)`=`TEST_RUNNER_CLASS`] [`[--test-targets](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--test-targets)`=`TEST_TARGET`,[`[TEST_TARGET](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#TEST_TARGET)`,…]] [`[--use-orchestrator](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--use-orchestrator)`] [`[--resign](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--resign)`] [`[--robo-directives](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--robo-directives)`=[`TYPE`:`[RESOURCE_NAME](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#RESOURCE_NAME)`=`INPUT`,…]] [`[--robo-script](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--robo-script)`=`ROBO_SCRIPT`] [`[--device-ids](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--device-ids)`=`MODEL_ID`,[`[MODEL_ID](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#MODEL_ID)`,…], `[-d](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#-d)` `[MODEL_ID](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#MODEL_ID)`,[`[MODEL_ID](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#MODEL_ID)`,…]] [`[--locales](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--locales)`=`LOCALE`,[`[LOCALE](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#LOCALE)`,…], `[-l](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#-l)` `[LOCALE](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#LOCALE)`,[`[LOCALE](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#LOCALE)`,…]] [`[--orientations](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--orientations)`=`ORIENTATION`,[`[ORIENTATION](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#ORIENTATION)`], `[-o](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#-o)` `[ORIENTATION](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#ORIENTATION)`,[`[ORIENTATION](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#ORIENTATION)`]] [`[--os-version-ids](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--os-version-ids)`=`OS_VERSION_ID`,[…], `[-v](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#-v)` `[OS_VERSION_ID](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#OS_VERSION_ID)`,[…]] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/run#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud firebase test android run` invokes and monitors tests in
Firebase Test Lab for Android.
Three main types of Android tests are currently supported:

- `robo`: runs a smart, automated exploration of the activities in your
Android app which records any installation failures or crashes and builds an
activity map with associated screenshots and video.
- `instrumentation`: runs automated unit or integration tests written
using a testing framework. Firebase Test Lab for Android currently supports the
Espresso and UI Automator 2.0 testing frameworks.
- `game-loop`: executes a special intent built into the game app (a
"demo mode") that simulates the actions of a real player. This test type can
include multiple game loops (also called "scenarios"), which can be logically
organized using scenario labels so that you can run related loops together.
Refer to [https://firebase.google.com/docs/test-lab/android/game-loop](https://firebase.google.com/docs/test-lab/android/game-loop)
for more information about how to build and run Game Loop tests.

The type of test to run can be specified with the `--type` flag,
although the type can often be inferred from other flags. Specifically, if the
`--test` flag is present, the test `--type` defaults to
`instrumentation`. If `--test` is not present, then
`--type` defaults to `robo`.
All arguments for `gcloud firebase test android run` may be specified
on the command line and/or within an argument file. Run `$ [gcloud topic arg-files](https://cloud.google.com/sdk/gcloud/reference/topic/arg-files)`
for more information about argument files.

**EXAMPLES**

: To invoke a robo test lasting 100 seconds against the default device
environment, run:

```
gcloud firebase test android run --app=APP_APK --timeout=100s
```

When specifying devices to test against, the preferred method is to use the
--device flag. For example, to invoke a robo test against a virtual, generic
MDPI Nexus device in landscape orientation, run:

```
gcloud firebase test android run --app=APP_APK --device=model=NexusLowRes,orientation=landscape
```

To invoke an instrumentation test against a physical Nexus 6 device (MODEL_ID:
shamu) which is running Android API level 21 in French, run:

```
gcloud firebase test android run --app=APP_APK --test=TEST_APK --device=model=shamu,version=21,locale=fr
```

To test against multiple devices, specify --device more than once:

```
gcloud firebase test android run --app=APP_APK --test=TEST_APK --device=model=Nexus4,version=19 --device=model=Nexus4,version=21 --device=model=NexusLowRes,version=25
```

To invoke a robo test on an Android App Bundle, pass the .aab file using the
--app flag.

```
gcloud firebase test android run --app=bundle.aab
```

You may also use the legacy dimension flags (deprecated) to specify which
devices to use. Firebase Test Lab will run tests against every possible
combination of the listed device dimensions. Note that some combinations of
device models and OS versions may not be valid or available in Test Lab. Any
unsupported combinations of dimensions in the test matrix will be skipped.
For example, to execute a series of 5-minute robo tests against a very
comprehensive matrix of virtual and physical devices, OS versions, locales and
orientations, run:

```
gcloud firebase test android run --app=APP_APK --timeout=5m --device-ids=shamu,NexusLowRes,Nexus5,g3,zeroflte --os-version-ids=19,21,22,23,24,25 --locales=en_GB,es,fr,ru,zh --orientations=portrait,landscape
```

The above command will generate a test matrix with a total of 300 test
executions, but only the subset of executions with valid dimension combinations
will actually run your tests.
To help you identify and locate your test matrix in the Firebase console, run:

```
gcloud firebase test android run --app=APP_APK --client-details=matrixLabel="Example matrix label"
```

Controlling Results Storage
By default, Firebase Test Lab stores detailed test results for a limited time in
a Google Cloud Storage bucket provided for you at no charge. If you wish to use
a storage bucket that you control, or if you need to retain detailed test
results for a longer period, use the `--results-bucket` option. See
[https://firebase.google.com/docs/test-lab/analyzing-results#detailed](https://firebase.google.com/docs/test-lab/analyzing-results#detailed)
for more information.
Detailed test result files are prefixed by default with a timestamp and a random
character string. If you require a predictable path where detailed test results
are stored within the results bucket (say, if you have a Continuous Integration
system which does custom post-processing of test result artifacts), use the
`--results-dir` option. `Note that each test invocation
`must` have a unique storage location, so never reuse the same value
for `--results-dir` between different test runs`.
Possible strategies could include using a UUID or sequence number for
`--results-dir`.
For example, to run a robo test using a specific Google Cloud Storage location
to hold the raw test results, run:

```
gcloud firebase test android run --app=APP_APK --results-bucket=gs://my-bucket --results-dir=my/test/results/<unique-value>
```

To run an instrumentation test and specify a custom name under which the history
of your tests will be collected and displayed in the Firebase console, run:

```
gcloud firebase test android run --app=APP_APK --test=TEST_APK --results-history-name='Excelsior App Test History'
```

Argument Files
All test arguments for a given test may alternatively be stored in an argument
group within a YAML-formatted argument file. The
`ARG_FILE` may contain one or more named argument groups,
and argument groups may be combined using the `include:` attribute
(Run `$ [gcloud topic](https://cloud.google.com/sdk/gcloud/reference/topic)
arg-files` for more information). The ARG_FILE can easily be shared with
colleagues or placed under source control to ensure consistent test executions.
To run a test using arguments loaded from an ARG_FILE named
`excelsior_args`, which contains an argument group named
`robo-args:`, use the following syntax:

```
gcloud firebase test android run path/to/excelsior_args:robo-args
```

**POSITIONAL ARGUMENTS**

: **[`ARGSPEC`]**:
An ARG_FILE:ARG_GROUP_NAME pair, where ARG_FILE is the path to a file containing
groups of test arguments in yaml format, and ARG_GROUP_NAME is the particular
yaml object holding a group of arg:value pairs to use. Run `$ [gcloud topic arg-files](https://cloud.google.com/sdk/gcloud/reference/topic/arg-files)`
for more information and examples.

**COMMONLY USED FLAGS**

: **--app**:
The path to the application binary file. The path may be in the local filesystem
or in Google Cloud Storage using gs:// notation. Android App Bundles are
specified as .aab, all other files are assumed to be APKs.

**--device**:
A list of ``DIMENSION=VALUE`` pairs which
specify a target device to test against. This flag may be repeated to specify
multiple devices. The four device dimensions are: `model`,
`version`, `locale`, and `orientation`. If any
dimensions are omitted, they will use a default value. The default value, and
all possible values, for each dimension can be found with the
``list`` command for that dimension, such as
`$ [gcloud
firebase test android models](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models) list`. `--device` is now the
preferred way to specify test devices and may not be used in conjunction with
`--devices-ids`, `--os-version-ids`,
`--locales`, or `--orientations`. Omitting all of the
preceding dimension-related flags will run tests against a single device using
defaults for all four device dimensions.
Examples:

```
--device model=Nexus6
--device version=23,orientation=portrait
--device model=shamu,version=22,locale=zh_CN,orientation=default
```

**--test**:
The path to the binary file containing instrumentation tests. The given path may
be in the local filesystem or in Google Cloud Storage using a URL beginning with
`gs://`.

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
The type of test to run. `TYPE` must be one of:
`instrumentation`, `robo`, `game-loop`.

**FLAGS**

: **--additional-apks**:
A list of up to 100 additional APKs to install, in addition to those being
directly tested. The path may be in the local filesystem or in Google Cloud
Storage using gs:// notation.

**--app-package**:
(REMOVED) The Java package of the application under test. By default, the
application package name is parsed from the APK manifest.
Flag --app-package has been removed.

**--async**:
Invoke a test asynchronously without waiting for test results.

**--auto-google-login**:
Automatically log into the test device using a preconfigured Google account
before beginning the test. Enabled by default, use --no-auto-google-login to
disable.

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

**--directories-to-pull**:
A list of paths that will be copied from the device's storage to the designated
results bucket after the test is complete. These must be absolute paths under
`/sdcard`, `/storage`, or `/data/local/tmp`
(for example, `--directories-to-pull
/sdcard/tempDir1,/data/local/tmp/tempDir2`). Path names are restricted to
the characters `a-zA-Z0-9_-./+`. The paths `/sdcard` and
`/data` will be made available and treated as implicit path
substitutions. E.g. if `/sdcard` on a particular device does not map
to external storage, the system will replace it with the external storage path
prefix for that device. Note that access to some directories on API levels 29
and later may also be limited by scoped storage rules.

**--environment-variables**:
A comma-separated, key=value map of environment variables and their desired
values. The environment variables are mirrored as extra options to the `am
instrument -e KEY1 VALUE1 …` command and passed to your test runner
(typically AndroidJUnitRunner). Examples:
Enable code coverage and provide a directory to store the coverage results when
using Android Test Orchestrator (`--use-orchestrator`):

```
--environment-variables clearPackageData=true,coverage=true,coverageFilePath=/sdcard/Download/
```

Enable code coverage and provide a file path to store the coverage results when
`not` using Android Test Orchestrator
(`--no-use-orchestrator`):

```
--environment-variables coverage=true,coverageFile=/sdcard/Download/coverage.ec
```

Note: If you need to embed a comma into a `VALUE` string, please
refer to `[gcloud topic
escaping](https://cloud.google.com/sdk/gcloud/reference/topic/escaping)` for ways to change the default list delimiter.

**--network-profile**:
The name of the network traffic profile, for example
`--network-profile=LTE`, which consists of a set of parameters to
emulate network conditions when running the test (default: no network shaping;
see available profiles listed by the $ [gcloud firebase
test network-profiles list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles/list) command). This feature only works on physical
devices.

**--num-flaky-test-attempts**:
Specifies the number of times a test execution should be reattempted if one or
more of its test cases fail for any reason. An execution that initially fails
but succeeds on any reattempt is reported as FLAKY.
The maximum number of reruns allowed is 10. (Default: 0, which implies no
reruns.) All additional attempts are executed in parallel.

**--obb-files**:
A list of one or two Android OBB file names which will be copied to each test
device before the tests will run (default: None). Each OBB file name must
conform to the format as specified by Android (e.g.
[main|patch].0300110.com.example.android.obb) and will be installed into
<shared-storage>/Android/obb/<package-name>/ on the test device.

**--other-files**:
A list of device-path=file-path pairs that indicate the device paths to push
files to the device before starting tests, and the paths of files to push.
Device paths must be under absolute, approved paths (${EXTERNAL_STORAGE}, or
${ANDROID_DATA}/local/tmp). Source file paths may be in the local filesystem or
in Google Cloud Storage (gs://…).
Examples:

```
--other-files /sdcard/dir1/file1.txt=local/file.txt,/storage/dir2/file2.jpg=gs://bucket/file.jpg
```

This flag only copies files to the device. To install files, like OBB or APK
files, see --obb-files and --additional-apks.

**--performance-metrics**:
Monitor and record performance metrics: CPU, memory, network usage, and FPS
(game-loop only). Enabled by default, use --no-performance-metrics to disable.

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
application's label from the APK manifest). All tests which use the same history
name will have their results grouped together in the Firebase console in a
time-ordered test history list.

**ANDROID GAME-LOOP TEST FLAGS**

: **--scenario-labels**:
A list of game-loop scenario labels (default: None). Each game-loop scenario may
be labeled in the APK manifest file with one or more arbitrary strings, creating
logical groupings (e.g. GPU_COMPATIBILITY_TESTS). If
`--scenario-numbers` and `--scenario-labels` are specified
together, Firebase Test Lab will first execute each scenario from
`--scenario-numbers`. It will then expand each given scenario label
into a list of scenario numbers marked with that label, and execute those
scenarios.

**--scenario-numbers**:
A list of game-loop scenario numbers which will be run as part of the test
(default: all scenarios). A maximum of 1024 scenarios may be specified in one
test matrix, but the maximum number may also be limited by the overall test
`--timeout` setting.

**ANDROID INSTRUMENTATION TEST FLAGS**

: **--test-package**:
(REMOVED) The Java package name of the instrumentation test. By default, the
test package name is parsed from the APK manifest.
Flag --test-package has been removed.

**--test-runner-class**:
The fully-qualified Java class name of the instrumentation test runner (default:
the last name extracted from the APK manifest).

**--test-targets**:
A list of one or more test target filters to apply (default: run all test
targets). Each target filter must be fully qualified with the package name,
class name, or test annotation desired. Any test filter supported by `am
instrument -e …` is supported. See [https://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner](https://developer.android.com/reference/android/support/test/runner/AndroidJUnitRunner)
for more information. Examples:

- `--test-targets "package com.my.package.name"`
- `--test-targets "notPackage com.package.to.skip"`
- `--test-targets "class com.foo.ClassName"`
- `--test-targets "notClass com.foo.ClassName#testMethodToSkip"`
- `--test-targets "annotation com.foo.AnnotationToRun"`
- `--test-targets "size large notAnnotation com.foo.AnnotationToSkip"`

**--use-orchestrator**:
Whether each test runs in its own Instrumentation instance with the Android Test
Orchestrator (default: Orchestrator is not used, same as specifying
--no-use-orchestrator). Orchestrator is only compatible with AndroidJUnitRunner
v1.1 or higher. See [https://developer.android.com/training/testing/junit-runner.html#using-android-test-orchestrator](https://developer.android.com/training/testing/junit-runner.html#using-android-test-orchestrator)
for more information about Android Test Orchestrator.

**ANDROID ROBO TEST FLAGS**

: **--resign**:
Make Robo re-sign the app-under-test APK for a higher quality crawl. If your app
cannot properly function when re-signed, disable this feature. When an
app-under-test APK is not re-signed, Robo crawl is slower and Robo has access to
less information about the state of the crawled app, which reduces crawl
quality. Consequently, if your Roboscript has actions on elements of
RecyclerView or AdapterView, and you disable APK re-signing, those actions might
require manual tweaking because Robo does not identify RecyclerView and
AdapterView in this mode. Enabled by default, use `--no-resign` to
disable.

**--robo-directives**:
A comma-separated (`<type>:<key>=<value>`) map of
`robo_directives` that you can use to customize the behavior of Robo
test. The `type` specifies the action type of the directive, which
may take on values `click`, `text` or `ignore`.
If no `type` is provided, `text` will be used by default.
Each key should be the Android resource name of a target UI element and each
value should be the text input for that element. Values are only permitted for
`text` type elements, so no value should be specified for
`click` and `ignore` type elements. No more than one
`click` element is allowed.
To provide custom login credentials for your app, use

```
--robo-directives text:username_resource=username,text:password_resource=password
```

To instruct Robo to click on the sign-in button, use

```
--robo-directives click:sign_in_button=
```

To instruct Robo to ignore any UI elements with resource names which equal or
start with the user-defined value, use

```
--robo-directives ignore:ignored_ui_element_resource_name=
```

To learn more about Robo test and robo_directives, see [https://firebase.google.com/docs/test-lab/android/command-line#custom_login_and_text_input_with_robo_test](https://firebase.google.com/docs/test-lab/android/command-line#custom_login_and_text_input_with_robo_test).
Caution: You should only use credentials for test accounts that are not
associated with real users.

**--robo-script**:
The path to a Robo Script JSON file. The path may be in the local filesystem or
in Google Cloud Storage using gs:// notation. You can guide the Robo test to
perform specific actions by recording a Robo Script in Android Studio and then
specifying this argument. Learn more at [https://firebase.google.com/docs/test-lab/robo-ux-test#scripting](https://firebase.google.com/docs/test-lab/robo-ux-test#scripting).

**DEPRECATED DEVICE DIMENSIONS FLAGS**

: **--device-ids**:
The list of MODEL_IDs to test against (default: one device model determined by
the Firebase Test Lab device catalog; see TAGS listed by the `$ [gcloud firebase
test android models list](https://cloud.google.com/sdk/gcloud/reference/firebase/test/android/models/list)` command).

**--locales**:
The list of LOCALEs to test against (default: a single locale determined by the
Firebase Test Lab device catalog).

**--orientations**:
The device orientation(s) to test against (default: portrait). Specifying
'default' will pick the preferred orientation for the app.
`ORIENTATION` must be one of: `portrait`,
`landscape`, `default`.

**--os-version-ids**:
The list of OS_VERSION_IDs to test against (default: a version ID determined by
the Firebase Test Lab device catalog).

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
gcloud alpha firebase test android run
```

```
gcloud beta firebase test android run
```