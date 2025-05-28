# gcloud services api-keys create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create)*

**NAME**

: **gcloud services api-keys create - create an API key**

**SYNOPSIS**

: **`gcloud services api-keys create` [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#--annotations)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#--display-name)`=`DISPLAY_NAME`] [`[--key-id](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#--key-id)`=`KEY_ID`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--api-target](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#--api-target)`=`service`=`SERVICE`,[…] `[--allowed-application](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#--allowed-application)`=[`sha1_fingerprint`=`SHA1_FINGERPRINT`,`package_name`=`PACKAGE_NAME`,…]     | `[--allowed-bundle-ids](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#--allowed-bundle-ids)`=[`ALLOWED_BUNDLE_IDS`,…]     | `[--allowed-ips](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#--allowed-ips)`=[`ALLOWED_IPS`,…]     | `[--allowed-referrers](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#--allowed-referrers)`=[`ALLOWED_REFERRERS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an API key.

**EXAMPLES**

: To create a key with display name and allowed IPs specified:

```
gcloud services api-keys create --display-name="test name" --allowed-ips=2620:15c:2c4:203:2776:1f90:6b3b:217,104.133.8.78
```

To create a key with annotations:

```
gcloud services api-keys create --annotations=foo=bar,abc=def
```

To create a key with user-specified key ID:

```
gcloud services api-keys create --key-id="my-key-id"
```

To create a key with allowed referrers restriction:

```
gcloud services api-keys create --allowed-referrers="https://www.example.com/*,http://sub.exampl\
e.com/*"
```

To create a key with allowed IOS app bundle IDs:

```
gcloud services api-keys create --allowed-bundle-ids=my.app
```

To create a key with allowed Android application:

```
gcloud services api-keys create --allowed-application=sha1_fingerprint=foo1,package_name=bar.foo --allowed-application=sha1_fingerprint=foo2,package_name=foo.bar
```

To create a key with allowed API targets (service name only):

```
gcloud services api-keys create --api-target=service=bar.service.com --api-target=service=foo.service.com
```

To create a key with service account:

```
gcloud services api-keys create --service-account=my-service-account
```

To create a key with allowed API targets (service and methods are specified):

```
gcloud services api-keys create --flags-file=my-flags.yaml
```

The content of 'my-flags.yaml' is as follows:

```
- --api-target:
    service: "foo.service.com"
- --api-target:
    service: "bar.service.com"
    methods:
      - "foomethod"
      - "barmethod"
```

**FLAGS**

: **--annotations**:
Annotations are key resource. Specify annotations as a key-value dictionary for
small amounts of arbitrary client data.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--display-name**:
Display name of the key to create.

**--key-id**:
User-specified ID of the key to create.

**--service-account**:
The email of the service account the key is bound to. If this field is
specified, the key is a service account bound key and auth enabled.

**--api-target**:
Repeatable. Specify service and optionally one or multiple specific methods.
Both fields are case insensitive. If you need to specify methods, it should be
specified with the `--flags-file`. See $ [gcloud topic flags-file](https://cloud.google.com/sdk/gcloud/reference/topic/flags-file) for
details. See the examples section for how to use `--api-target` in
`--flags-file`.

**--allowed-application**

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
gcloud alpha services api-keys create
```

```
gcloud beta services api-keys create
```