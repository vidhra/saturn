# gcloud emulators spanner start  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/emulators/spanner/start](https://cloud.google.com/sdk/gcloud/reference/emulators/spanner/start)*

**NAME**

: **gcloud emulators spanner start - start a local Cloud Spanner emulator**

**SYNOPSIS**

: **`gcloud emulators spanner start` [`[--enable-fault-injection](https://cloud.google.com/sdk/gcloud/reference/emulators/spanner/start#--enable-fault-injection)`=`ENABLE_FAULT_INJECTION`] [`[--host-port](https://cloud.google.com/sdk/gcloud/reference/emulators/spanner/start#--host-port)`=`HOST_PORT`] [`[--rest-port](https://cloud.google.com/sdk/gcloud/reference/emulators/spanner/start#--rest-port)`=`REST_PORT`] [`[--use-docker](https://cloud.google.com/sdk/gcloud/reference/emulators/spanner/start#--use-docker)`=`USE_DOCKER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/emulators/spanner/start#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command starts a local Cloud Spanner emulator.

**EXAMPLES**

: To start a local Cloud Spanner emulator, run:

```
gcloud emulators spanner start
```

**FLAGS**

: **--enable-fault-injection**:
If true, the emulator will randomly inject faults into transactions. This
facilitates application abort-retry testing.

**--host-port**:
The host:port to which the emulator should be bound. The default value is
localhost:9010. Note that this port serves gRPC requests. To override the
default port serving REST requests, use --rest-port. If using Docker to run the
emulator, the host must be specified as an ipaddress.

**--rest-port**:
The port at which REST requests are served. gcloud uses REST to communicate with
the emulator. The default value is 9020.

**--use-docker**:
Use the Cloud Spanner emulator docker image even if the platform has a native
binary available in the gcloud CLI. Currently we only provide a native binary
for Linux. For other systems, you must install Docker for your platform before
starting the emulator.

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
gcloud alpha emulators spanner start
```

```
gcloud beta emulators spanner start
```