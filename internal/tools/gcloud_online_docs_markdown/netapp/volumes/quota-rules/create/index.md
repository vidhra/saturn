# gcloud netapp volumes quota-rules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create)*

**NAME**

: **gcloud netapp volumes quota-rules create - create a Cloud NetApp Volume Quota Rule**

**SYNOPSIS**

: **`gcloud netapp volumes quota-rules create` (`[QUOTA_RULE](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create#QUOTA_RULE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create#--location)`=`LOCATION`) `[--disk-limit-mib](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create#--disk-limit-mib)`=`DISK_LIMIT_MIB` `[--type](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create#--type)`=`TYPE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--target](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create#--target)`=`TARGET`] [`[--volume](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create#--volume)`=`VOLUME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/quota-rules/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud NetApp Volume Quota Rule.

**EXAMPLES**

: The following command creates a default `user` Quota Rule named NAME
using the required arguments:

```
gcloud netapp volumes quota-rules create NAME --location=us-central1 --volume=vol1 --type=DEFAULT_USER_QUOTA --disk-limit-mib=200
```

The following command creates a default `group` Quota Rule named NAME
using the required arguments:

```
gcloud netapp volumes quota-rules create NAME --location=us-central1 --volume=vol1 --type=DEFAULT_GROUP_QUOTA --disk-limit-mib=200
```

The following command creates an individual user Quota Rule named NAME for user
with UID '100' using the required arguments:

```
gcloud netapp volumes quota-rules create NAME --location=us-central1 --volume=vol1 --type=INDIVIDUAL_USER_QUOTA --target=100 --disk-limit-mib=200
```

The following command creates an individual group Quota Rule named NAME for
group with GID '1001' using the required arguments:

```
gcloud netapp volumes quota-rules create NAME --location=us-central1 --volume=vol1 --type=INDIVIDUAL_GROUP_QUOTA --target=1001 --disk-limit-mib=200
```

**POSITIONAL ARGUMENTS**

: **Quota rule resource - The Quota rule to create. The arguments in this group can
be used to specify the attributes of this resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `quota_rule` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `volume` attribute:

- provide the argument `quota_rule` on the command line with a fully
specified name;
- provide the argument `--volume` on the command line.

This must be specified.

**`QUOTA_RULE`**:
ID of the quota_rule or fully qualified identifier for the quota_rule.
To set the `quota_rule` attribute:

- provide the argument `quota_rule` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the quota_rule.
To set the `location` attribute:

- provide the argument `quota_rule` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

**REQUIRED FLAGS**

: **--disk-limit-mib**:
The disk limit in MiB for the quota rule.

**--type**:
String indicating the type of quota rule. The supported values are:
'DEFAULT_USER_QUOTA','DEFAULT_GROUP_QUOTA','INDIVIDUAL_USER_QUOTA','INDIVIDUAL_GROUP_QUOTA'

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A description of the Cloud NetApp Quota rule

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--target**:
The target of the quota rule. Identified by a Unix UID/GID, Windows SID, or null
for default.

**Volume resource - The volume for which quota rule applies. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.

**--volume**:
ID of the volume or fully qualified identifier for the volume.
To set the `volume` attribute:

- provide the argument `--volume` on the command line.**

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
gcloud beta netapp volumes quota-rules create
```