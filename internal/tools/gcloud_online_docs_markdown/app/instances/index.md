# gcloud app instances  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/instances](https://cloud.google.com/sdk/gcloud/reference/app/instances)*

**NAME**

: **gcloud app instances - view and manage your App Engine instances**

**SYNOPSIS**

: **`gcloud app instances` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/app/instances#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/instances#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This set of commands can be used to view and manage your existing App Engine
instances.
For more information on App Engine instances, see: [https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine](https://cloud.google.com/appengine/docs/python/an-overview-of-app-engine)

**EXAMPLES**

: To list your App Engine instances, run:

```
gcloud app instances list
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[delete](https://cloud.google.com/sdk/gcloud/reference/app/instances/delete)`**:
Delete a specified instance.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/app/instances/describe)`**:
Display all data about an existing instance.

**`[disable-debug](https://cloud.google.com/sdk/gcloud/reference/app/instances/disable-debug)`**:
Disable debug mode for an instance.

**`[enable-debug](https://cloud.google.com/sdk/gcloud/reference/app/instances/enable-debug)`**:
Enable debug mode for an instance (only works on the flexible environment).

**`[list](https://cloud.google.com/sdk/gcloud/reference/app/instances/list)`**:
List the instances affiliated with the current App Engine project.

**`[scp](https://cloud.google.com/sdk/gcloud/reference/app/instances/scp)`**:
SCP from or to the VM of an App Engine Flexible instance.

**`[ssh](https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh)`**:
SSH into the VM of an App Engine Flexible instance.

**NOTES**

: This variant is also available:

```
gcloud beta app instances
```