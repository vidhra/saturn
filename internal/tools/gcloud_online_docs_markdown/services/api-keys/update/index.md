# gcloud services api-keys update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update)*

**NAME**

: **gcloud services api-keys update - update an API key's metadata**

**SYNOPSIS**

: **`gcloud services api-keys update` (`[KEY](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#KEY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--display-name)`=`DISPLAY_NAME`] [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--annotations)`=[`KEY`=`VALUE`,…]     | `[--clear-annotations](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--clear-annotations)`] [`[--clear-restrictions](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--clear-restrictions)`     | `[--api-target](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--api-target)`=`service`=`SERVICE`,[…] `[--allowed-application](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--allowed-application)`=[`sha1_fingerprint`=`SHA1_FINGERPRINT`,`package_name`=`PACKAGE_NAME`,…]     | `[--allowed-bundle-ids](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--allowed-bundle-ids)`=[`ALLOWED_BUNDLE_IDS`,…]     | `[--allowed-ips](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--allowed-ips)`=[`ALLOWED_IPS`,…]     | `[--allowed-referrers](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#--allowed-referrers)`=[`ALLOWED_REFERRERS`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/services/api-keys/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an API key's metadata.

**EXAMPLES**

: To remove all restrictions of the key:

```
gcloud services api-keys update projects/myproject/keys/my-key-id --clear-restrictions
```

To update display name and set allowed ips as server key restrictions:

```
gcloud services api-keys update projects/myproject/keys/my-key-id --display-name="test name" --allowed-ips=2620:15c:2c4:203:2776:1f90:6b3b:217,104.133.8.78
```

To update annotations:

```
gcloud services api-keys update projects/myproject/keys/my-key-id --annotations=foo=bar,abc=def
```

To update key's allowed referrers restriction:

```
gcloud services api-keys update projects/myproject/keys/my-key-id --allowed-referrers="https://www.example.com/*,http://sub.exampl\
e.com/*"
```

To update key's allowed ios app bundle ids:

```
gcloud services api-keys update projects/myproject/keys/my-key-id --allowed-bundle-ids=my.app
```

To update key's allowed android application:

```
gcloud services api-keys update projects/myproject/keys/my-key-id --allowed-application=sha1_fingerprint=foo1,package_name=bar1 --allowed-application=sha1_fingerprint=foo2,package_name=bar2
```

To update keys' allowed api target with multiple services:

```
gcloud services api-keys update projects/myproject/keys/my-key-id --api-target=service=bar.service.com --api-target=service=foo.service.com
```

To update keys' allowed api target with service and method:

```
gcloud services api-keys update projects/myproject/keys/my-key-id --flags-file=my-flags.yaml
```

```
The content of 'my-flags.yaml' is as following:
```

```
- --api-target:
      service: "foo.service.com"
  - --api-target:
      service: "bar.service.com"
      methods:
      - "foomethod"
      - "barmethod"
```

**POSITIONAL ARGUMENTS**

: **Key resource - The name of the key to update. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`KEY`**:
ID of the key or fully qualified identifier for the key.
To set the `key` attribute:

- provide the argument `key` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the key.
To set the `location` attribute:

- provide the argument `key` on the command line with a fully specified
name;
- provide the argument `--location` on the command line;
- location will default to global.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--display-name**:
Display name of the key to update.

**--annotations**

**--clear-restrictions**

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
gcloud alpha services api-keys update
```

```
gcloud beta services api-keys update
```