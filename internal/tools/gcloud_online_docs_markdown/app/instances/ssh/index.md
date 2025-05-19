# gcloud app instances ssh  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh](https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh)*

**NAME**

: **gcloud app instances ssh - SSH into the VM of an App Engine Flexible instance**

**SYNOPSIS**

: **`gcloud app instances ssh` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh#INSTANCE)` [`[--container](https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh#--container)`=`CONTAINER`] [`[--service](https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh#--service)`=`SERVICE`] [`[--tunnel-through-iap](https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh#--tunnel-through-iap)`] [`[--version](https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh#GCLOUD-WIDE-FLAGS) …`] [-- `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh#COMMAND)` …]**

**DESCRIPTION**

: `gcloud app instances ssh` lets you remotely log in to your running
App Engine Flexible instances under two conditions:

- The instance is running.
- The instance has an external IP address. To check from the Cloud Console, go to
the Instances page and confirm that there is an IP address listed in the VM IP
column. To check from your app.yaml, open your app.yaml and look at the network
settings. The `instance_ip_mode` field must be either not listed or
set to ``external``.

`gcloud app instances ssh` resolves the instance's IP address and
pre-populates the VM with a public key managed by gcloud. If the gcloud managed
key pair does not exist, it is generated the first time an SSH command is run,
which may prompt you for a passphrase for the private key encryption.
All SSH commands require the OpenSSH client suite to be installed on Linux and
Mac OS X. On Windows, the Google Cloud CLI comes with a bundled PuTTY suite
instead, so it has no external dependencies.

**EXAMPLES**

: To SSH into an App Engine Flexible instance, run:

```
gcloud app instances ssh --service=s1 --version=v1 i1
```

To SSH into the app container within an instance, run:

```
gcloud app instances ssh --service=s1 --version=v1 i1 --container=gaeapp
```

To SSH into the app container and run a remote command, run:

```
gcloud app instances ssh --service=s1 --version=v1 i1 --container=gaeapp -- echo hello
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
The instance ID.

**[-- `COMMAND` …]**:
Remote command to execute on the VM.
The '--' argument must be specified between gcloud specific args on the left and
COMMAND on the right.

**FLAGS**

: **--container**:
Name of the container within the VM to connect to.

**--service**:
The service ID.

**--tunnel-through-iap**:
Tunnel the ssh connection through Identity-Aware Proxy for TCP forwarding.
To learn more, see the [IAP for TCP
forwarding documentation](https://cloud.google.com/iap/docs/tcp-forwarding-overview).

**--version**:
The version ID.

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

: This variant is also available:

```
gcloud beta app instances ssh
```