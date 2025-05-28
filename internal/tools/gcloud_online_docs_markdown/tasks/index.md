# gcloud tasks  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/tasks](https://cloud.google.com/sdk/gcloud/reference/tasks)*

**NAME**

: **gcloud tasks - manage Cloud Tasks queues and tasks**

**SYNOPSIS**

: **`gcloud tasks` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/tasks#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/tasks#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/tasks#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Cloud Tasks queues and tasks.

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[cmek-config](https://cloud.google.com/sdk/gcloud/reference/tasks/cmek-config)`**:
Get or change CMEK configuration for Cloud Tasks.

**`[locations](https://cloud.google.com/sdk/gcloud/reference/tasks/locations)`**:
Get information about Cloud Tasks locations.

**`[queues](https://cloud.google.com/sdk/gcloud/reference/tasks/queues)`**:
Manage Cloud Tasks queues.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[buffer](https://cloud.google.com/sdk/gcloud/reference/tasks/buffer)`**:
Buffers a task into a queue.

**`[create-app-engine-task](https://cloud.google.com/sdk/gcloud/reference/tasks/create-app-engine-task)`**:
Create and add a task that targets App Engine.

**`[create-http-task](https://cloud.google.com/sdk/gcloud/reference/tasks/create-http-task)`**:
Create and add a task that targets a HTTP endpoint.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/tasks/delete)`**:
Delete a task from a queue.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/tasks/describe)`**:
Show details about a task.

**`[list](https://cloud.google.com/sdk/gcloud/reference/tasks/list)`**:
List tasks.

**`[run](https://cloud.google.com/sdk/gcloud/reference/tasks/run)`**:
Force a task to run now.

**NOTES**

: These variants are also available:

```
gcloud alpha tasks
```

```
gcloud beta tasks
```